#!/usr/bin/env python3
"""El mapa de Rosario de la sección «De dónde salimos» (#rosario) de la home v5.

Baja de OpenStreetMap (Overpass) una sola vez —y lo guarda en una caché local, ignorada por git— el contorno del
Municipio de Rosario, el agua del Paraná, las avenidas y la Circunvalación, el Monumento a la Bandera y las calles de
alrededor de la esquina de Donado y Chassaing; los simplifica (Douglas-Peucker), los proyecta a un plano chico y los
hornea como un <svg> inline adentro de v5/index.html, entre las marcas

    <!-- MAPA-ROSARIO:inicio -->  …  <!-- MAPA-ROSARIO:fin -->

El SVG no lleva colores propios: usa las variables de la página (--gold, --gold-hi, --bg…) por clase, así el tema día
(?tema=dia) le cambia la tinta sin tocar nada. Los estilos y el pulso del pin viven en el bloque CSS «ROSARIO · el mapa»
y en el script «ROSARIO · el mapa» de la página: este script sólo genera el dibujo.

Uso (desde la raíz del repo):
    python3 scripts/generar-mapa-rosario.py              # usa la caché si está; si no, baja (≈6 pedidos, 1 cada 2 s)
    python3 scripts/generar-mapa-rosario.py --bajar      # vuelve a bajar todo de Overpass
    python3 scripts/generar-mapa-rosario.py --svg x.svg  # además escribe el SVG suelto (para mirarlo aparte)

Política de uso de Overpass/Nominatim: User-Agent propio y pedidos espaciados. Los datos son © OpenStreetMap (ODbL):
el mapa lleva el crédito.
"""
import argparse
import json
import math
import os
import re
import sys
import time
import urllib.parse
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(RAIZ, 'scripts', '_osm-rosario')
HTML = os.path.join(RAIZ, 'v5', 'index.html')
UA = 'rialabs-home/1.0 (hola@rialabs.ar)'
OVERPASS = 'https://overpass-api.de/api/interpreter'
OVERPASS_2 = 'https://overpass.kumi.systems/api/interpreter'   # espejo, sólo si la principal falla tres veces

MUNICIPIO = 3368048          # relation «Municipio de Rosario» (admin_level 7)
AREA = 3600000000 + MUNICIPIO
RIO = 67124                  # multipolygon water=river: el agua del Paraná frente a Rosario (y río arriba / abajo)
# encuadre del mapa (lat/lon): el municipio entero y el río con el borde de las islas
SUR, NORTE, OESTE, ESTE = -33.046, -32.862, -60.805, -60.578
# la esquina: el nodo de OSM que comparten Donado y Chassaing (verificado: se recalcula y se compara en cada corrida)
ESQ_NODO = 1732157336
# la ochava de la oficina, medida por Matías (ria-smartcity-machine/datos/ubicaciones.json, «Esquina Donado y Chassaing»,
# 26/10): ~14 m al norte y ~3 m al este del cruce de los ejes → la esquina NORESTE del cruce.
OCHAVA = (-32.928577, -60.727406)

CONSULTAS = {
    'esquina': f'''[out:json][timeout:60];
area({AREA})->.r;
way(area.r)["highway"]["name"="Chassaing"]->.c;
way(area.r)["highway"]["name"~"Donado$"]->.d;
node(w.c)->.cn; node(w.d)->.dn;
node.cn.dn; out;
is_in; area._["boundary"="administrative"]; out tags;''',
    'municipio': f'[out:json][timeout:120];rel({MUNICIPIO});out geom;',
    'rio': f'[out:json][timeout:120];rel({RIO});way(r)({SUR - 0.03},{OESTE - 0.03},{NORTE + 0.03},{ESTE + 0.03});out geom;',
    'avenidas': f'''[out:json][timeout:120];
area({AREA})->.r;
way(area.r)["highway"~"^(motorway|trunk|primary)$"];
out geom;''',
    'secundarias': f'''[out:json][timeout:120];
area({AREA})->.r;
way(area.r)["highway"="secondary"];
out geom;''',
    'centro': f'''[out:json][timeout:60];
area({AREA})->.r;
nwr(area.r)["historic"="monument"]["name"~"Monumento.*a la Bandera"];
out center tags;''',
    'detalle': '''[out:json][timeout:60];
way(around:260,-32.9287,-60.7274)["highway"~"^(primary|secondary|tertiary|residential|unclassified|living_street)$"];
out geom;''',
}


def bajar(nombre, forzar=False):
    os.makedirs(CACHE, exist_ok=True)
    ruta = os.path.join(CACHE, nombre + '.json')
    if os.path.exists(ruta) and not forzar:
        return json.load(open(ruta))
    datos = urllib.parse.urlencode({'data': CONSULTAS[nombre]}).encode()
    for intento in range(4):                         # Overpass a veces devuelve 502/504: se espera y se reintenta
        url = OVERPASS if intento < 3 else OVERPASS_2
        print(f'  overpass: {nombre} ({url.split("/")[2]})…', file=sys.stderr)
        try:
            req = urllib.request.Request(url, data=datos, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=180) as r:
                crudo = r.read()
            json.loads(crudo)
            break
        except Exception as e:                      # noqa: BLE001
            print(f'    falló: {e}', file=sys.stderr)
            if intento == 3:
                raise
            time.sleep(10 * (intento + 1))
    open(ruta, 'wb').write(crudo)
    time.sleep(2)                                   # un pedido cada dos segundos, como mucho
    return json.loads(crudo)


# ── geometría ─────────────────────────────────────────────────────────────
LAT0 = (SUR + NORTE) / 2
KX = math.cos(math.radians(LAT0))
W = 400.0                                           # ancho del viewBox
ESCALA = W / ((ESTE - OESTE) * KX)                  # unidades por grado de latitud
H = round((NORTE - SUR) * ESCALA, 1)
M_POR_U = (NORTE - SUR) * 111_195 / H               # metros por unidad (≈ 56)


def proy(lat, lon):
    return ((lon - OESTE) * KX * ESCALA, (NORTE - lat) * ESCALA)


def dp(pts, tol):
    """Douglas-Peucker iterativo."""
    if len(pts) < 3:
        return pts[:]
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    pila = [(0, len(pts) - 1)]
    while pila:
        a, b = pila.pop()
        ax, ay = pts[a]; bx, by = pts[b]
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy) or 1e-9
        mx, mi = -1.0, -1
        for i in range(a + 1, b):
            px, py = pts[i]
            d = abs(dy * (px - ax) - dx * (py - ay)) / L if (dx or dy) else math.hypot(px - ax, py - ay)
            if d > mx:
                mx, mi = d, i
        if mx > tol:
            keep[mi] = True
            pila += [(a, mi), (mi, b)]
    return [p for p, k in zip(pts, keep) if k]


def recortar_poligono(pts, x0, y0, x1, y1):
    """Sutherland-Hodgman contra un rectángulo (el polígono puede ser cóncavo; el recorte es convexo)."""
    def corta(pts, dentro, inter):
        out = []
        for i in range(len(pts)):
            p, q = pts[i - 1], pts[i]
            if dentro(q):
                if not dentro(p):
                    out.append(inter(p, q))
                out.append(q)
            elif dentro(p):
                out.append(inter(p, q))
        return out

    def ix(x):
        return lambda p, q: (x, p[1] + (q[1] - p[1]) * (x - p[0]) / (q[0] - p[0]))

    def iy(y):
        return lambda p, q: (p[0] + (q[0] - p[0]) * (y - p[1]) / (q[1] - p[1]), y)
    for dentro, inter in ((lambda p: p[0] >= x0, ix(x0)), (lambda p: p[0] <= x1, ix(x1)),
                          (lambda p: p[1] >= y0, iy(y0)), (lambda p: p[1] <= y1, iy(y1))):
        if not pts:
            break
        pts = corta(pts, dentro, inter)
    return pts


def recortar_linea(pts, x0, y0, x1, y1):
    """Parte una polilínea en los tramos que caen dentro del rectángulo (con un punto de más a cada lado)."""
    tramos, cur = [], []
    def dentro(p):
        return x0 <= p[0] <= x1 and y0 <= p[1] <= y1
    for i, p in enumerate(pts):
        if dentro(p):
            if not cur and i > 0:
                cur.append(pts[i - 1])
            cur.append(p)
        elif cur:
            cur.append(p)
            tramos.append(cur)
            cur = []
    if cur:
        tramos.append(cur)
    return [t for t in tramos if len(t) > 1]


def unir_anillos(ways):
    """Arma anillos cerrados con los tramos (listas de (lat, lon)) de un multipolígono de OSM."""
    tramos = [list(w) for w in ways if len(w) > 1]
    anillos = []
    while tramos:
        a = tramos.pop()
        cambio = True
        while a[0] != a[-1] and cambio:
            cambio = False
            for i, t in enumerate(tramos):
                if t[0] == a[-1]:
                    a += t[1:]
                elif t[-1] == a[-1]:
                    a += t[-2::-1]
                elif t[-1] == a[0]:
                    a = t[:-1] + a
                elif t[0] == a[0]:
                    a = t[:0:-1] + a
                else:
                    continue
                tramos.pop(i)
                cambio = True
                break
        anillos.append(a)
    return anillos


def f(v):
    s = f'{v:.1f}'.rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def camino(pts, cerrar=False):
    """Path SVG compacto: M absoluto y después l relativos, con un decimal."""
    if not pts:
        return ''
    q = [(round(x, 1), round(y, 1)) for x, y in pts]
    s = [f'M{f(q[0][0])} {f(q[0][1])}']
    rel = []
    for (ax, ay), (bx, by) in zip(q, q[1:]):
        dx, dy = round(bx - ax, 1), round(by - ay, 1)
        if dx == 0 and dy == 0:
            continue
        rel.append(f'{f(dx)}' + ('' if dy < 0 else ' ') + f'{f(dy)}')
    if rel:
        s.append('l' + ' '.join(rel).replace(' -', '-'))
    if cerrar:
        s.append('z')
    return ''.join(s)


def puntos(el):
    return [(p['lat'], p['lon']) for p in el['geometry']]


def unir_lineas(ways):
    """Encadena tramos que comparten extremo (sin cerrar); devuelve polilíneas."""
    return unir_anillos(ways)


def sin_duplicadas(lineas, celda=1.1, umbral=0.8):
    """Saca las calzadas paralelas de las avenidas de doble mano: una línea cuyos puntos (cada ~1 u) caen casi todos
    en celdas que ya pintó otra línea, se descarta. A 53 m por unidad, las dos manos de un bulevar son una sola raya."""
    ocupado, quedan = set(), []
    for pts in sorted(lineas, key=lambda p: -sum(math.dist(a, b) for a, b in zip(p, p[1:]))):
        muestras = []
        for a, b in zip(pts, pts[1:]):
            n = max(1, int(math.dist(a, b) / 0.8))
            muestras += [(a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n) for i in range(n)]
        celdas = [(int(x // celda), int(y // celda)) for x, y in muestras]
        cerca = sum(1 for cx, cy in celdas if any((cx + i, cy + j) in ocupado for i in (-1, 0, 1) for j in (-1, 0, 1)))
        if muestras and cerca / len(muestras) > umbral:
            continue
        quedan.append(pts)
        ocupado.update(celdas)
    return quedan


def centro_canal(agua, y):
    """El tramo de agua más ancho que corta la horizontal y (para poner el rótulo del río en el medio del canal)."""
    xs = []
    for anillo in agua:
        for (ax, ay), (bx, by) in zip(anillo, anillo[1:] + anillo[:1]):
            if (ay - y) * (by - y) < 0:
                xs.append(ax + (bx - ax) * (y - ay) / (by - ay))
    xs.sort()
    tramos = [(xs[i], xs[i + 1]) for i in range(0, len(xs) - 1, 2)]
    if not tramos:
        return None
    a, b = max(tramos, key=lambda t: t[1] - t[0])
    return (a + b) / 2, b - a


def generar(forzar=False):
    datos = {n: bajar(n, forzar)['elements'] for n in CONSULTAS}

    # ── la esquina: el nodo compartido, y en qué municipio y barrio cae ──
    nodo = [e for e in datos['esquina'] if e['type'] == 'node']
    areas = {int(e['tags'].get('admin_level', 0)): e['tags']['name'] for e in datos['esquina'] if e['type'] == 'area'}
    if not nodo or areas.get(7) != 'Municipio de Rosario':
        sys.exit(f'la esquina de Donado y Chassaing no aparece dentro del Municipio de Rosario: {nodo} {areas}')
    nodo = nodo[0]
    if nodo['id'] != ESQ_NODO:
        print(f'  ojo: el nodo de la esquina cambió en OSM ({ESQ_NODO} → {nodo["id"]})', file=sys.stderr)
    ESQ = (nodo['lat'], nodo['lon'])
    barrio = areas.get(10)
    print(f'  esquina: {ESQ[0]:.7f}, {ESQ[1]:.7f} · {areas.get(9)} · barrio {barrio} ({areas.get(11)})', file=sys.stderr)

    X0, Y0, X1, Y1 = -6, -6, W + 6, H + 6            # el recorte, un poco más allá del marco (lo demás lo tapa el clip)

    # ── agua: la cadena abierta del multipolígono del Paraná se cierra afuera del encuadre; las islas, adentro ──
    cadenas = unir_anillos([puntos(e) for e in datos['rio']])
    agua, costas = [], []
    for c in cadenas:
        pts = [proy(*p) for p in c]
        costas += [dp(t, 0.3) for t in recortar_linea(pts, X0, Y0, X1, Y1)]
        anillo = recortar_poligono(pts[:-1] if c[0] == c[-1] else pts, X0, Y0, X1, Y1)
        if len(anillo) > 2:
            agua.append(dp(anillo + anillo[:1], 0.3)[:-1])
    d_agua = ''.join(camino(a, True) for a in agua)
    # cada tramo de costa es un path propio con pathLength=1: el trazo que se dibuja al entrar recorre cada orilla
    # entera (dentro de un mismo path, el guionado vuelve a empezar en cada subtramo y los cortos aparecían de golpe)
    d_costa = [camino(t) for t in costas if len(t) > 1]

    # ── el municipio ──
    muni = [puntos(x) for x in datos['municipio'][0]['members'] if x['type'] == 'way' and x.get('role') == 'outer']
    d_muni = ''.join(camino(dp([proy(*p) for p in a], 0.3), True) for a in unir_anillos(muni))

    # ── avenidas (primary) y autopistas (la Circunvalación, los accesos: motorway / trunk) ──
    clases = {'sec': [], 'av': [], 'auto': []}
    for e in datos['avenidas']:
        clases['auto' if e['tags']['highway'] in ('motorway', 'trunk') else 'av'].append(puntos(e))
    for e in datos['secundarias']:
        if not e['tags'].get('name', '').startswith('Colectora'):   # las colectoras repiten la Circunvalación
            clases['sec'].append(puntos(e))
    d_vias = {}
    for k, ways in clases.items():
        lineas = []
        for l in unir_lineas(ways):
            for t in recortar_linea([proy(*p) for p in l], X0, Y0, X1, Y1):
                lineas.append(dp(t, 0.45))
        lineas = sin_duplicadas(lineas)
        d_vias[k] = ''.join(camino(l) for l in lineas if len(l) > 1)

    # ── puntos ──
    ex, ey = proy(*ESQ)
    mon = datos['centro'][0]['center']
    mx, my = proy(mon['lat'], mon['lon'])

    # ── el rótulo del río: en el medio del canal, con la inclinación del canal ──
    ya, yb = 96, 170
    (xa, wa), (xb, wb) = centro_canal(agua, ya), centro_canal(agua, yb)
    dx, dy = xb - xa, yb - ya
    ang = math.degrees(math.atan2(dy, dx))
    nx, ny = dy / math.hypot(dx, dy), -dx / math.hypot(dx, dy)       # la normal hacia el noreste (las islas)
    off = (wa + wb) / 4 + 9
    rx, ry = (xa + xb) / 2 + nx * off, (ya + yb) / 2 + ny * off

    # ── el detalle: las calles de alrededor, en metros desde la esquina ──
    det = detalle(datos['detalle'], ESQ)

    svg = armar_svg(d_agua, d_costa, d_muni, d_vias, (ex, ey), (mx, my), (rx, ry, ang), det, barrio)
    return svg, ESQ, areas


# ── el recuadro de detalle ────────────────────────────────────────────────
DET_X, DET_Y, DET_L = 6, 240, 112                   # dónde va (unidades del mapa) y su lado
DET_R = 115                                          # metros desde la esquina hasta el borde del recuadro
DET_K = DET_L / (2 * DET_R)                          # unidades por metro
CALLE_M = 17.3                                       # ancho entre líneas de edificación (las 20 varas de Rosario)
OCHAVA_M = 4.5                                       # cateto del corte de la ochava


def detalle(ways, ESQ):
    la0, lo0 = ESQ
    kx = 111_195 * math.cos(math.radians(la0))
    cx, cy = DET_X + DET_L / 2, DET_Y + DET_L / 2

    def pm(p):                                       # (lat, lon) → unidades del recuadro
        return (cx + (p[1] - lo0) * kx * DET_K, cy - (p[0] - la0) * 111_195 * DET_K)
    m = 4
    caja = (DET_X - m, DET_Y - m, DET_X + DET_L + m, DET_Y + DET_L + m)
    por_nombre = {}
    for e in ways:
        por_nombre.setdefault(e['tags'].get('name', '?'), []).append(puntos(e))
    calles = []
    for nombre, ws in por_nombre.items():
        for l in unir_lineas(ws):
            for t in recortar_linea([pm(p) for p in l], *caja):
                calles.append(dp(t, 0.2))
    # los cruces: nodos que comparten calles de distinto nombre, con el ángulo de la cuadrícula ahí
    usos = {}
    for e in ways:
        g = puntos(e)
        for i, p in enumerate(g):
            vecinos = [g[j] for j in (i - 1, i + 1) if 0 <= j < len(g)]
            usos.setdefault(p, []).extend((e['tags'].get('name'), pm(q)) for q in vecinos)
    cruces = []
    for p, us in usos.items():
        if len({u[0] for u in us}) < 2:
            continue
        x, y = pm(p)
        if not (caja[0] < x < caja[2] and caja[1] < y < caja[3]):
            continue
        dirs = [math.atan2(q[1] - y, q[0] - x) for _, q in us]
        g = (dirs[0] + math.pi / 4) % (math.pi / 2) - math.pi / 4
        brazos = {round((d - g) / (math.pi / 2)) % 4 for d in dirs}   # 0 este · 1 sur · 2 oeste · 3 norte (pantalla)
        cruces.append((x, y, g, brazos, p == ESQ))
    # de qué lado del cruce está la oficina: lo dice la ochava medida (+x este, −y norte, en pantalla)
    cuadrante = (1 if OCHAVA[1] >= lo0 else -1, -1 if OCHAVA[0] >= la0 else 1)
    return calles, cruces, (cx, cy), cuadrante


def rot(x, y, a, cx=0.0, cy=0.0):
    c, s = math.cos(a), math.sin(a)
    return (cx + x * c - y * s, cy + x * s + y * c)


def armar_svg(d_agua, d_costa, d_muni, d_vias, esq, mon, rio, det, barrio):
    ex, ey = esq
    mx, my = mon
    rx, ry, rang = rio
    calles, cruces, (dcx, dcy), (sx, sy) = det
    h = CALLE_M / 2 * DET_K                          # media calle entre líneas de edificación
    a = OCHAVA_M * DET_K                             # cateto de la ochava
    lw = 0.7                                         # el trazo de las líneas de edificación
    R = 2 * h + a                                    # el rombo que corta las cuatro esquinas de cada cruce
    rombos_borde, rombos = [], []
    oficina = None
    E = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for x, y, ang, brazos, es_esq in cruces:
        for k in range(4):                           # una ochava por esquina, sólo entre dos brazos que existen
            if k in brazos and (k + 1) % 4 in brazos:
                for rr, lista in ((R + lw * math.sqrt(2), rombos_borde), (R, rombos)):
                    v = ((0, 0), (E[k][0] * rr, E[k][1] * rr), (E[(k + 1) % 4][0] * rr, E[(k + 1) % 4][1] * rr))
                    lista.append(camino([rot(*q, ang, x, y) for q in v], True))
        if es_esq:
            # la ochava de la oficina (la del cuadrante sx, sy; hoy el noreste: +x, −y), sobre el medio del trazo del
            # corte, entre las dos líneas de edificación
            ext = R + lw / math.sqrt(2)
            p1 = rot(sx * (h + lw / 2), sy * (ext - h - lw / 2), ang, x, y)
            p2 = rot(sx * (ext - h - lw / 2), sy * (h + lw / 2), ang, x, y)
            dentro = ext / 2 + 3.4                   # el anillo, apenas adentro de la manzana: la ochava queda a la vista
            oficina = (p1, p2, rot(sx * dentro, sy * dentro, ang, x, y), ang)
    d_calles = ''.join(camino(c) for c in calles if len(c) > 1)
    (o1, o2, opin, oang) = oficina
    # los rótulos de las calles del detalle, del otro lado de Donado que la oficina: DONADO en la manzana opuesta a
    # la oficina (se lee de abajo hacia arriba, con las letras del lado de afuera de la calle) y CHASSAING del mismo
    # lado de Chassaing que la oficina (hoy: DONADO en la suroeste, CHASSAING en la noroeste)
    don = rot(-(h + 3.2) if sx > 0 else h + 9.5, h + 40 if sy < 0 else -(h + 5), oang, dcx, dcy)
    cha = rot(-(h + 2.5) if sx > 0 else h + 2.5, -(h + 3) if sy < 0 else h + 9.3, oang, dcx, dcy)
    cha_anc = 'end' if sx > 0 else 'start'
    gdeg = math.degrees(oang)
    if gdeg > 45:
        gdeg -= 90
    L = DET_L
    # el cono de la lupa: del borde del anillo a las dos esquinas de arriba del recuadro
    def borde(px, py, r=6.5):
        d = math.hypot(px - ex, py - ey)
        return (ex + (px - ex) * r / d, ey + (py - ey) * r / d)
    c1, c2 = borde(DET_X, DET_Y), borde(DET_X + L, DET_Y)
    escala = 2000 / M_POR_U                          # 2 km en unidades
    n = lambda v: f(v)
    partes = [
        f'<svg class="rm-svg" viewBox="0 0 {n(W)} {n(H)}" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">',
        '<defs>',
        f'<path id="rm-agua-d" fill-rule="evenodd" d="{d_agua}"/>',
        f'<path id="rm-muni-d" pathLength="1" d="{d_muni}"/>',
        f'<path id="rm-calles-d" d="{d_calles}"/>',
        f'<clipPath id="rm-marco"><rect width="{n(W)}" height="{n(H)}"/></clipPath>',
        f'<clipPath id="rm-det-clip"><rect x="{n(DET_X)}" y="{n(DET_Y)}" width="{n(L)}" height="{n(L)}"/></clipPath>',
        f'<mask id="rm-tierra" maskUnits="userSpaceOnUse" x="-10" y="-10" width="{n(W + 20)}" height="{n(H + 20)}">'
        f'<rect x="-10" y="-10" width="{n(W + 20)}" height="{n(H + 20)}" fill="#fff"/><use href="#rm-agua-d" fill="#000"/></mask>',
        '<pattern id="rm-rayas" width="8" height="2.4" patternUnits="userSpaceOnUse"><path class="rm-raya" d="M0 1.2H8"/></pattern>',
        '<linearGradient id="rm-anillo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f8df6a"/>'
        '<stop offset=".3" stop-color="#e4753d"/><stop offset=".62" stop-color="#d35745"/><stop offset="1" stop-color="#c54a45"/></linearGradient>',
        '<radialGradient id="rm-halo"><stop offset="0" class="rm-halo-0"/><stop offset="1" class="rm-halo-1"/></radialGradient>',
        '</defs>',
        # el plano
        '<g clip-path="url(#rm-marco)">',
        '<use href="#rm-agua-d" class="rm-agua"/>',
        '<use href="#rm-agua-d" class="rm-agua-rayas" fill="url(#rm-rayas)"/>',
        '<g mask="url(#rm-tierra)">',
        '<use href="#rm-muni-d" class="rm-muni-fondo"/>',
        f'<path class="rm-sec rm-via" d="{d_vias["sec"]}"/>',
        f'<path class="rm-av rm-via" d="{d_vias["av"]}"/>',
        f'<path class="rm-auto rm-via" d="{d_vias["auto"]}"/>',
        '<use href="#rm-muni-d" class="rm-muni rm-trazo"/>',
        '</g>',
        *[f'<path class="rm-costa rm-trazo" pathLength="1" d="{d}"/>' for d in d_costa],
        '</g>',
        # rótulos del plano
        f'<text class="rm-ciudad" x="{n(ex + 118)}" y="{n(ey + 116)}" text-anchor="middle">ROSARIO</text>',
        f'<text class="rm-rio" transform="translate({n(rx)} {n(ry)}) rotate({n(rang)})" text-anchor="middle" dy="3">RÍO PARANÁ</text>',
        f'<circle class="rm-centro" cx="{n(mx)}" cy="{n(my)}" r="1.7"/>',
        f'<text class="rm-chico" x="{n(mx - 5)}" y="{n(my + 3)}" text-anchor="end">CENTRO</text>',
        # el norte y la escala
        '<g class="rm-carto">',
        f'<path d="M{n(W - 14)} 32V16M{n(W - 17)} 21l3-5.5 3 5.5"/>',
        f'<path d="M{n(W - 26 - escala)} 30v-3.5h{n(escala)}v3.5M{n(W - 26 - escala / 2)} 30v-2"/>',
        '</g>',
        f'<text class="rm-chico" x="{n(W - 14)}" y="12" text-anchor="middle">N</text>',
        f'<text class="rm-chico" x="{n(W - 26 - escala / 2)}" y="21" text-anchor="middle">2 KM</text>',
        # las esquinas del marco
        f'<path class="rm-marco" d="M.5 10.5v-10h10M{n(W - 10.5)} .5h10v10M{n(W - .5)} {n(H - 10.5)}v10h-10M10.5 {n(H - .5)}h-10v-10"/>',
        # la lupa: del pin al recuadro
        f'<path class="rm-lupa" d="M{n(c1[0])} {n(c1[1])}L{n(DET_X)} {n(DET_Y)}M{n(c2[0])} {n(c2[1])}L{n(DET_X + L)} {n(DET_Y)}"/>',
        # el pin en la esquina
        f'<g class="rm-pin" transform="translate({n(ex)} {n(ey)})">',
        '<circle class="rm-halo" r="14" fill="url(#rm-halo)"/>',
        '<circle class="rm-pulso" r="4.2"/>',
        '<circle r="4.2" fill="none" stroke="url(#rm-anillo)" stroke-width="1.6"/>',
        '<circle class="rm-punto" r="1.1"/>',
        '</g>',
        # el recuadro de detalle
        '<g class="rm-det">',
        f'<rect class="rm-det-fondo" x="{n(DET_X)}" y="{n(DET_Y)}" width="{n(L)}" height="{n(L)}"/>',
        '<g clip-path="url(#rm-det-clip)">',
        f'<use href="#rm-calles-d" class="rm-calle-borde" style="stroke-width:{n(2 * h + 2 * lw)}px"/>',
        f'<path class="rm-ochava-borde" d="{"".join(rombos_borde)}"/>',
        f'<use href="#rm-calles-d" class="rm-calle" style="stroke-width:{n(2 * h)}px"/>',
        f'<path class="rm-ochava" d="{"".join(rombos)}"/>',
        f'<path class="rm-oficina" d="M{n(o1[0])} {n(o1[1])}L{n(o2[0])} {n(o2[1])}"/>',
        f'<text class="rm-calle-n" transform="translate({n(don[0])} {n(don[1])}) rotate({n(gdeg - 90)})">DONADO</text>',
        f'<text class="rm-calle-n" x="{n(cha[0])}" y="{n(cha[1])}" text-anchor="{cha_anc}" transform="rotate({n(gdeg)} {n(cha[0])} {n(cha[1])})">CHASSAING</text>',
        f'<g class="rm-pin rm-pin-det" transform="translate({n(opin[0])} {n(opin[1])})">',
        '<circle class="rm-pulso" r="2.5"/>',
        '<circle r="2.5" fill="none" stroke="url(#rm-anillo)" stroke-width="1.2"/>',
        '</g>',
        '</g>',
        f'<rect class="rm-det-marco" x="{n(DET_X)}" y="{n(DET_Y)}" width="{n(L)}" height="{n(L)}"/>',
        '</g>',
        f'<text class="rm-esq" x="{n(DET_X)}" y="{n(DET_Y + L + 14)}">DONADO Y CHASSAING</text>',
    ]
    if barrio:
        partes.append(f'<text class="rm-barrio" x="{n(DET_X)}" y="{n(DET_Y + L + 26)}">{barrio.upper()}</text>')
    partes.append('</svg>')
    return '\n'.join(partes)


MARCA_A, MARCA_B = '<!-- MAPA-ROSARIO:inicio -->', '<!-- MAPA-ROSARIO:fin -->'


def inyectar(svg):
    html = open(HTML, encoding='utf-8').read()
    i, j = html.find(MARCA_A), html.find(MARCA_B)
    if i < 0 or j < i:
        sys.exit(f'no encuentro las marcas {MARCA_A} … {MARCA_B} en {HTML}')
    nuevo = html[:i + len(MARCA_A)] + '\n' + svg + '\n' + html[j:]
    if nuevo != html:
        open(HTML, 'w', encoding='utf-8').write(nuevo)
    return len(svg.encode())


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--bajar', action='store_true', help='volver a bajar todo de Overpass')
    ap.add_argument('--svg', help='además, escribir el SVG suelto en esta ruta')
    ap.add_argument('--no-html', action='store_true', help='no tocar v5/index.html')
    args = ap.parse_args()
    svg, esq, areas = generar(args.bajar)
    if args.svg:
        open(args.svg, 'w', encoding='utf-8').write(svg)
    if not args.no_html:
        kb = inyectar(svg) / 1024
        print(f'  v5/index.html: mapa de {kb:.1f} KB entre las marcas', file=sys.stderr)
    else:
        print(f'  mapa de {len(svg.encode()) / 1024:.1f} KB', file=sys.stderr)


if __name__ == '__main__':
    main()
