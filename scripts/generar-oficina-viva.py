#!/usr/bin/env python3
"""La oficina viva (2026-11-02, rama `oficina-video`): el edificio real de Donado y Chassaing (Rosario) llevado con IA
hacia la oficina de RIA Labs que se propuso el 01/11, y animado. Ver CONTENIDO.md §0.8 («La oficina en video») y §0.3.

Pedido de Matías (docs/prompts-usuario/2026-11-02-oficina-real-mapa-y-video.md): «probemos algo con video realista
hecho con IA, partiendo desde la foto del edificio original, pero transformandolo para poder mostrar los distintos
espacios que propuse.. le podemos agregar otro piso al edificio, le podemos sacar los carteles que dicen "Byte" y poner
carteles de RIA Labs, queremos ver solo la esquina con el edificio y no las calles.. estaria bueno que este animado, que
se vea la gente adentro, como si las paredes exteriores fueran vidriadas.»

Etapas (todo cae en `_capturas/oficina-video/`, ignorado; sólo lo elegido se exporta a `assets/`):
  editar   edición de imagen con google/nano-banana (US$ 0,039) o google/nano-banana-pro (US$ 0,15 a 1K/2K, 0,30 a 4K):
           la foto real → el concepto (un piso más, carteles de RIA Labs, paredes vidriadas con las cuatro salas, sólo la
           esquina); de ahí, la versión de noche.
  video    kwaivgi/kling-v2.5-turbo-pro (US$ 0,07 por segundo) con el concepto como primer Y último cuadro (el truco del
           loop de los retratos vivos), cámara quieta.
  post     ffmpeg: costura del loop, viñeta hacia el cielo de la página (#0b0a14), webm VP9 + mp4 H.264 + póster jpg.

Uso:
  generar-oficina-viva.py recorte                              # la foto real recortada a 16:9 sobre el edificio
  generar-oficina-viva.py editar <nb|nbp> <consigna> <imagen> [n=1] [ref.jpg ...]   # consigna = clave de CONSIGNA
  generar-oficina-viva.py entrada <fijo.jpg> <salida.jpg>      # 16:9 exacto, 1920×1080, para Kling
  generar-oficina-viva.py video <imagen> <nombre> [n=1] [segundos=5]    # CONSIGNA_VIDEO (VIDEO=activo: CONSIGNA_VIDEO_ACTIVA); start = end
  generar-oficina-viva.py recuperar                            # baja lo que haya quedado sin bajar (por id, sin pagar de nuevo)
  generar-oficina-viva.py cuenta                               # lo gastado, contra el tope
  generar-oficina-viva.py tira <clip.mp4> [fps=2]              # tira de cuadros para mirar (deformaciones, carteles, caras)
  generar-oficina-viva.py post <salida-base> <clip.mp4> [clip2 ...]   # loop con fundidos + viñeta + exports + póster
  generar-oficina-viva.py vinetear <origen> <destino> [ancho]  # la viñeta sobre un fijo, para mirar

Cuenta de Replicate: cada predicción se anota en `_capturas/oficina-video/costos.jsonl` APENAS se crea (id, modelo, costo),
antes de esperar el resultado: si la sesión se corta, `recuperar` la baja por su id y nada se paga dos veces. Tope: US$ 8.
Ayudantes comunes (token, User-Agent, data_uri, bajar, ffmpeg) importados de `generar-retratos-vivos.py`.
Precios leídos de Replicate el 2026-11-02: nano-banana US$ 0,039 · nano-banana-pro US$ 0,15 (1K/2K), 0,30 (4K) ·
kling-v2.5-turbo-pro US$ 0,07 por segundo.

Lo que quedó hecho (2026-11-02; ver CONTENIDO.md §0.8 y §0.3):
  recorte  la foto real (1600×738) a 16:9 sobre el edificio (`foto-16x9.jpg`, 1312×738) + un cartel de referencia dibujado
           con PIL (`ref-cartel-ria.jpg`: el anillo con el degradé de logos/ria-anillo-color.svg y «RIA LABS · SOFTWARE E
           INTELIGENCIA ARTIFICIAL»), las dos como entrada de la edición.
  editar   `concepto` de una sola vez (piso, carteles, vidrio con las cuatro salas, sólo la esquina): 2 nano-banana
           (cambian el encuadre, se pierden los árboles y la bajada del cartel sale ilegible) y 2 nano-banana-pro (texto
           correcto, salas legibles). Elegido `concepto-nbp-2` (la ochava en el medio con la puerta y el cartel chico, los
           pilares grises, los árboles a los costados) = el de DÍA. De ahí `noche` (hora azul, 2 nbp: cielo lavanda, poco
           contraste) y de `noche-nbp-2` la `noche-cerrada` (1 nbp) = el de NOCHE: edificio oscuro, salas encendidas, el
           anillo con su degradé. 7 ediciones, US$ 0,83.
  video    `kling-dia-1` (5 s, consigna quieta): casi una foto, la gente se mueve lo que el ruido del códec. Con
           VIDEO=activo y 10 s: `kling-dia-activo-1`, `kling-noche-activo-1` y `-2` — se leen las acciones (el visitante
           camina y señala, el que presenta barre el gráfico, el brazo gira y vuelve, alguien gira la silla); edificio,
           carteles y letras quietos; ninguna cara ni cuerpo que se transforme. 4 clips, US$ 2,45.
  post     noche ← noche-activo-2 → noche-activo-1 (dos juntas de 12 cuadros): 460 cuadros, 19,17 s; día ← dia-activo-1:
           230 cuadros, 9,58 s. 1440×810, viñeta VINETA, mp4 crf 22 / webm crf 32: noche 110 KB / 946 KB / 353 KB, día
           124 KB / 525 KB / 245 KB (jpg / mp4 / webm). Cierre medido sobre el edificio a 480 px: PNG 0,54 (paso medio
           0,09), mp4 1,26 (grano del I-frame contra el último P-frame; bajar el crf a 18 sólo lo lleva a 1,07), webm 0,60.
  costo    US$ 3,28 de 8 (11 predicciones, ninguna fallida; el libro está en `_capturas/oficina-video/costos.jsonl`).
"""
import importlib.util, json, os, pathlib, subprocess, sys, time, urllib.request, concurrent.futures
sys.dont_write_bytecode = True   # importar el script de los retratos no deja __pycache__ en scripts/

RAIZ = pathlib.Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("retratos_vivos", RAIZ / "scripts" / "generar-retratos-vivos.py")
rv = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(rv)   # token, User-Agent, data_uri, bajar, FFMPEG

OUT = RAIZ / "_capturas" / "oficina-video"
OUT.mkdir(parents=True, exist_ok=True)
LIBRO = OUT / "costos.jsonl"
TOPE = 8.0
FOTO = RAIZ / "docs" / "prompts-usuario" / "2026-11-02-edificio-donado-y-chassaing.jpg"
CIELO = (11, 10, 20)   # #0b0a14
PRECIO = {"nb": 0.039, "nbp": 0.15, "kling-s": rv.PRECIO["kling-s"]}
MODELO = {"nb": "google/nano-banana", "nbp": "google/nano-banana-pro"}

# ══════════════════════════════════════════════════════════════════════════════════════════════════
# Las consignas
# ══════════════════════════════════════════════════════════════════════════════════════════════════
GENTE = ("All people are generic, invented, anonymous people seen at a distance — never the likeness of any real person. ")
SALAS = (
    "Through the glass you clearly see FOUR spaces, each with a few people, at realistic scale:\n"
    "- TOP FLOOR, LEFT part: the developers' room — rows of desks with two computer monitors each showing dark code editors, "
    "four or five people sitting and typing, one standing at a whiteboard.\n"
    "- TOP FLOOR, RIGHT part: the meeting room — a long table with three or four people seated, and one person standing next "
    "to a large wall screen that shows a rising bar chart, pointing at it.\n"
    "- GROUND FLOOR, LEFT part: the lab — workbenches with electronics and tools, a small yellow robotic arm on a bench, "
    "one person testing a security camera mounted on a tripod, another one at a bench with a laptop.\n"
    "- GROUND FLOOR, at the chamfered corner and to the RIGHT: the showroom, open to the public — a big display screen on the "
    "back wall showing a city camera view, white pedestals with security cameras and sensors on them, and three or four "
    "visitors standing and looking at the screen.\n"
    "Modern, tidy, real offices: light wood, white walls, black furniture, ceiling lights. " + GENTE)
CONSIGNA = {
    # todo de una: piso, carteles, vidrio con las salas, encuadre
    "concepto": (
        "Edit this photograph of a real corner building in Rosario, Argentina. Turn it into a realistic architectural "
        "photograph of the finished RIA Labs office, keeping it clearly recognisable as the SAME corner: the same chamfered "
        "corner (ochava) with the entrance door on it, the same footprint, proportions and rhythm of the two facades, the white "
        "render and the grey vertical pilasters, the same leafy street trees on the sidewalk in front of it, the same viewpoint "
        "from across the street, the same lens and the same soft overcast daylight.\n"
        "Make ALL these changes:\n"
        "1. ONE MORE FLOOR. Build a second storey on top of the existing building, over the same footprint and following the "
        "same chamfered corner, so the building is two storeys tall. Same architecture: white render, the grey pilasters continue "
        "up, a white parapet on top.\n"
        "2. SIGNAGE. Remove EVERY trace of the current orange-and-white 'Byte' sign band — its logos and all its texts — and "
        "the window vinyls ('25 años', 'Security 24', 'Tecnología para construir…'). Replace them with clean RIA Labs signage "
        "copied from the SECOND image: on the white parapet crowning the new top floor, centred on the chamfered corner, the "
        "RIA Labs logo — a thin ring with a gold-to-red gradient followed by 'RIA LABS' in dark letters with 'SOFTWARE E "
        "INTELIGENCIA ARTIFICIAL' in small letters underneath — and a second, smaller identical sign above the entrance door. "
        "No other text, logo or brand anywhere.\n"
        "3. GLASS WALLS. The exterior walls of both floors become floor-to-ceiling clear glass curtain walls with thin dark "
        "mullions, set between the white pilasters and the floor slabs, so the interior is fully visible from the street, "
        "brightly lit inside. " + SALAS + "\n"
        "4. ONLY THE CORNER. Show only the building, its corner sidewalk and its street trees. Remove the parked cars, the "
        "traffic sign pole, the overhead cables, the neighbouring houses and the buildings behind; there is only open sky and "
        "soft distant foliage around the building. Keep just a thin strip of street in the foreground.\n"
        "Photorealistic, natural colours, sharp, high detail, like a real photograph of the built office. Wide 16:9 frame with "
        "the building centred and fully visible, with some margin around it."),
    # de día → hora azul, nada más
    "noche": (
        "Edit this photograph. Keep EVERYTHING exactly as it is — the building, its two floors, the glass walls, every room, "
        "every person and their pose, the furniture, the screens, the RIA Labs signs, the trees, the framing and the viewpoint. "
        "Change ONLY the time of day: it is now blue hour, a few minutes after sunset. The sky is a deep blue-violet that darkens "
        "to almost black at the top; the outside is dim; the street trees are dark silhouettes with a little light on the leaves "
        "nearest to the glass. The interiors are brightly lit from inside — warm white ceiling lights, the cool glow of the "
        "monitors and the big screens — so the people inside read clearly through the glass, much brighter than the street. The "
        "two RIA Labs signs are softly backlit and the gold-to-red ring glows gently. The sidewalk catches the warm light that "
        "spills out of the windows. Photorealistic, natural, no lens flares."),
    # la hora azul → noche cerrada (para que la página, que es nocturna, y el edificio se fundan; adentro, más luz que afuera)
    "noche-cerrada": (
        "Edit this photograph. Keep EVERYTHING exactly as it is — the building, its two floors, the glass walls, every room, "
        "every person and their exact pose, the furniture, the screens and what they show, the RIA Labs signs and their exact "
        "letters, the trees, the framing and the viewpoint. Change ONLY the light: it is now full night. The sky is a very dark "
        "navy, almost black. The outside of the building — the facade, the pilasters, the parapet, the sidewalk, the street and "
        "the trees — is dark, lit only by the warm light spilling out of the glass and by the backlit signs. The interiors stay "
        "brightly lit, exactly as they are now, so the rooms and the people glow inside a dark building. On both signs the ring "
        "keeps its gold-to-red gradient, softly glowing, and the letters stay sharp and readable. Photorealistic, natural night "
        "photography, no lens flares, no stars."),
}

# ══════════════════════════════════════════════════════════════════════════════════════════════════
# Replicate, con el libro de cuentas
# ══════════════════════════════════════════════════════════════════════════════════════════════════
def libro():
    return [json.loads(l) for l in LIBRO.read_text().splitlines() if l.strip()] if LIBRO.exists() else []

def gastado():
    return sum(e["costo"] for e in libro() if e.get("estado") != "fallida-sin-cobro")

def _anotar(e):
    with open(LIBRO, "a") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")

def _get(pid):
    req = urllib.request.Request(f"https://api.replicate.com/v1/predictions/{pid}", headers={"Authorization": f"Bearer {rv.TOKEN}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def lanzar(clave, entrada, destino, costo, extra=None, timeout=1200):
    """Crea la predicción, la anota en el libro con su id ANTES de esperar, espera y baja la salida a `destino`."""
    if gastado() + costo > TOPE + 1e-9:
        raise SystemExit(f"tope: gastado US$ {gastado():.3f} + {costo:.3f} > {TOPE}")
    body = json.dumps({"input": entrada}).encode()
    req = urllib.request.Request(f"https://api.replicate.com/v1/models/{clave}/predictions", data=body, method="POST",
                                 headers={"Authorization": f"Bearer {rv.TOKEN}", "Content-Type": "application/json"})
    for intento in range(6):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                pred = json.load(r)
            break
        except urllib.error.HTTPError as e:
            if e.code != 429 or intento == 5: raise
            time.sleep(8 * (intento + 1))
    _anotar({"id": pred["id"], "modelo": clave, "destino": str(destino.relative_to(RAIZ)), "costo": costo,
             "creada": time.strftime("%Y-%m-%d %H:%M:%S")})
    meta = {"modelo": clave, "id": pred["id"], "costo_usd": costo,
            "entrada": {k: v for k, v in entrada.items() if not (isinstance(v, str) and v.startswith("data:"))
                        and not (isinstance(v, list) and v and str(v[0]).startswith("data:"))}}
    meta.update(extra or {})
    destino.with_suffix(".json").write_text(json.dumps(meta, indent=1, ensure_ascii=False))
    t0 = time.time()
    while pred.get("status") not in ("succeeded", "failed", "canceled"):
        if time.time() - t0 > timeout:
            return f"{destino.name}: sigue corriendo ({pred['id']}); `recuperar` la baja después"
        time.sleep(5)
        pred = _get(pred["id"])
    if pred["status"] != "succeeded":
        return f"{destino.name} FALLÓ ({pred['id']}): {pred.get('error')}"
    rv.bajar(pred, destino)
    meta["metrics"] = pred.get("metrics"); meta["espera_s"] = round(time.time() - t0)
    destino.with_suffix(".json").write_text(json.dumps(meta, indent=1, ensure_ascii=False))
    return f"{destino.name} ok ({meta['espera_s']} s, US$ {costo:.3f}; llevamos US$ {gastado():.3f} de {TOPE})"

def recuperar():
    for e in libro():
        dest = RAIZ / e["destino"]
        if dest.exists():
            continue
        pred = _get(e["id"])
        print(e["destino"], pred["status"], end=" ")
        if pred["status"] == "succeeded":
            rv.bajar(pred, dest); print("→ bajada")
        else:
            print(pred.get("error") or "")

def _siguiente(prefijo, ext):
    nums = [int(p.stem.rsplit("-", 1)[1]) for p in OUT.glob(f"{prefijo}-*{ext}") if p.stem.rsplit("-", 1)[1].isdigit()]
    return (max(nums) if nums else 0) + 1

def _uri(p):
    p = pathlib.Path(p)
    if p.suffix.lower() == ".png":
        import base64
        return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode()
    return rv.data_uri(p)

# ── editar ────────────────────────────────────────────────────────────────────────────────────────
def editar(modelo, consigna, imagen, n=1, refs=()):
    prompt = CONSIGNA[consigna]
    entrada = {"prompt": prompt, "image_input": [_uri(imagen)] + [_uri(r) for r in refs], "aspect_ratio": "16:9",
               "output_format": "jpg"}
    if modelo == "nbp":
        entrada["resolution"] = "2K"
    pref = f"{consigna}-{modelo}"
    base = _siguiente(pref, ".jpg") - 1
    def uno(i):
        dest = OUT / f"{pref}-{base + i + 1}.jpg"
        return lanzar(MODELO[modelo], entrada, dest, PRECIO[modelo],
                      {"consigna": consigna, "imagen": str(imagen), "refs": [str(r) for r in refs]})
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for f in concurrent.futures.as_completed([ex.submit(uno, i) for i in range(n)]):
            print(f.result(), flush=True)

# ── video ─────────────────────────────────────────────────────────────────────────────────────────
CONSIGNA_VIDEO = (
    "A locked-off architectural shot of a two-storey corner office building with glass walls, filmed from across the street "
    "on a tripod. The camera does not move at all: no pan, no zoom, no dolly, no shake. The building, its glass, its frame, "
    "its signs and the trees stay exactly in place. Life happens quietly inside, through the glass: upstairs on the left, "
    "developers type at their desks and one leans back for a moment; upstairs on the right, the presenter gestures toward "
    "the chart on the big screen and the people at the table nod; downstairs on the left, a technician slowly adjusts the "
    "camera on the tripod and the small robotic arm moves gently; downstairs on the right, in the showroom, a visitor walks "
    "a few slow steps and another points at the big screen. Screens flicker softly with content. The leaves of the street "
    "trees sway very slightly in a light breeze. Small, natural, slow movements; everybody keeps the same body, face and "
    "clothes; the light stays constant. Photorealistic.")
# Con la consigna de arriba (5 s, `kling-dia-1`) Kling dejó casi una foto: la gente se mueve lo que el ruido del códec
# (diferencia media ≈ 1,2/255 por sala contra el cuadro 0). La de 10 s pide acciones que se lean desde la vereda de
# enfrente y que vuelvan a su lugar (el loop exige terminar en la misma foto). VIDEO=activo la elige.
CONSIGNA_VIDEO_ACTIVA = (
    "A locked-off architectural shot of a two-storey corner office building with glass walls, filmed from across the street "
    "on a tripod. The camera never moves: no pan, no zoom, no dolly, no shake. The building, the glass, the frame, the signs "
    "and their letters stay exactly in place the whole time. Through the glass, the people inside move clearly and naturally, "
    "readable from across the street, and by the end everybody is back in their starting pose:\n"
    "- Ground floor right, the showroom: a visitor walks slowly from the door toward the big screen, stops, points at the "
    "screen and turns to the person next to him, then walks back to where he started; another visitor leans in to look at a "
    "camera on a pedestal.\n"
    "- Top floor right, the meeting room: the presenter turns to the chart on the big screen, sweeps his hand along the rising "
    "bars, turns back to the table and gestures while talking; the people at the table turn their heads to follow him.\n"
    "- Top floor left, the developers: they type at their keyboards; one turns his chair toward his neighbour, says something, "
    "and turns back to his screen.\n"
    "- Ground floor left, the lab: the yellow robotic arm slowly swings to one side and comes back; the technician with the "
    "laptop looks up at the arm and back down.\n"
    "Monitors and screens stay lit. The leaves of the street trees sway gently in a light breeze. Slow, calm, natural "
    "movements; everybody keeps the same body, face and clothes; the light stays constant. Photorealistic.")
NEGATIVO_VIDEO = (
    "camera movement, zoom, pan, dolly, tilt, handheld shake, building deformation, melting, warping walls, morphing, "
    "people morphing, faces changing, extra limbs, people appearing or disappearing, flicker, light change, day-night change, "
    "text changing, sign changing, fast motion, cars, crowds, birds")

def video(imagen, nombre, n=1, segundos=5):
    uri = _uri(imagen)
    consigna = CONSIGNA_VIDEO_ACTIVA if os.environ.get("VIDEO") == "activo" else CONSIGNA_VIDEO
    entrada = {"prompt": consigna, "negative_prompt": NEGATIVO_VIDEO, "start_image": uri, "end_image": uri,
               "duration": int(segundos)}
    base = _siguiente(f"kling-{nombre}", ".mp4") - 1
    def uno(i):
        dest = OUT / f"kling-{nombre}-{base + i + 1}.mp4"
        return lanzar("kwaivgi/kling-v2.5-turbo-pro", entrada, dest, PRECIO["kling-s"] * int(segundos), {"imagen": str(imagen)})
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for f in concurrent.futures.as_completed([ex.submit(uno, i) for i in range(n)]):
            print(f.result(), flush=True)

# ── mirar ─────────────────────────────────────────────────────────────────────────────────────────
def sh(*a):
    subprocess.run([rv.FFMPEG, "-hide_banner", "-loglevel", "error", "-y", *a], check=True)

def tira(clip, fps=2):
    clip = pathlib.Path(clip); base = OUT / clip.stem
    sh("-i", str(clip), "-vf", f"fps={fps},scale=480:-1,tile=4x3", "-frames:v", "1", f"{base}-tira.png")
    sh("-i", str(clip), "-frames:v", "1", f"{base}-primero.png")
    sh("-sseof", "-0.05", "-i", str(clip), "-update", "1", f"{base}-ultimo.png")
    print(f"{base}-tira.png")

def recorte():
    from PIL import Image
    im = Image.open(FOTO)   # 1600×738: el edificio va de x≈330 a x≈1100, centro ≈ 715
    w = round(im.height * 16 / 9); x0 = 715 - w // 2
    im.crop((x0, 0, x0 + w, im.height)).save(OUT / "foto-16x9.jpg", quality=95)
    print(OUT / "foto-16x9.jpg", w, im.height)

# ── la viñeta: el edificio se funde con el cielo de la página, como los retratos del stand ─────────────
VINETA = {"CX": 0.5, "CY": 0.50, "R0": 0.70, "R1": 1.04, "P": 2.6}   # elipse «súper» (norma P): plena hasta R0, cielo en R1
def mascara(w, h, v=None):
    from PIL import Image
    v = dict(VINETA, **(v or {}))
    m = Image.new("L", (w, h))
    px = m.load()
    for y in range(h):
        dy = abs((y / h - v["CY"]) / 0.5)
        for x in range(w):
            dx = abs((x / w - v["CX"]) / 0.5)
            r = (dx ** v["P"] + dy ** v["P"]) ** (1 / v["P"])
            t = min(1, max(0, (r - v["R0"]) / (v["R1"] - v["R0"])))
            px[x, y] = round(255 * (1 - t * t * (3 - 2 * t)))
    return m

def vinetear(origen, destino, ancho=None):
    from PIL import Image
    im = Image.open(origen).convert("RGB")
    if ancho:
        im = im.resize((int(ancho), round(im.height * int(ancho) / im.width)), Image.LANCZOS)
    m = mascara(*im.size)
    Image.composite(im, Image.new("RGB", im.size, CIELO), m).save(destino, quality=88, progressive=True, optimize=True)
    print(destino)

# ── post: el loop, la viñeta y los exports ─────────────────────────────────────────────────────────
def post(clips, salida, ancho=1440, fundido=12, crf_mp4=None, crf_webm=None):
    """Loop sin costura con uno o varios clips (todos empiezan y terminan en la misma foto). Kling vuelve a la foto pero no
    idéntica (cierre ≈ 1,5 contra un paso medio de 0,5–1,6), así que en cada junta la cola de un clip se funde sobre la
    cabeza del siguiente (y la del último sobre la del primero) en `fundido` cuadros (0,5 s a 24 fps; nunca ping-pong):
    loop = Σ clip_i[F:N_i-F] + mezcla(clip_i[N_i-F:], clip_{i+1}[:F]). Cada cuadro se escala a `ancho` (16:9) y se viñetea
    hacia #0b0a14 con la misma máscara. Exporta <salida>.mp4 (H.264 yuv420p, +faststart, sin audio), <salida>.webm (VP9)
    y <salida>.jpg (el cuadro 0 del loop, así el póster no salta cuando el clip arranca). GUARDAR_CUADROS=1 deja los PNG."""
    import shutil, tempfile
    from PIL import Image
    if isinstance(clips, (str, pathlib.Path)):
        clips = [clips]
    crf_mp4 = int(crf_mp4 or os.environ.get("CRF_MP4", 22)); crf_webm = int(crf_webm or os.environ.get("CRF_WEBM", 32))
    W = int(ancho); H = round(W * 9 / 16) // 2 * 2
    td = pathlib.Path(tempfile.mkdtemp(dir=OUT, prefix="post-"))
    cuadros = []
    for i, clip in enumerate(clips):
        sh("-i", str(clip), "-vf", f"scale={W}:{H}:flags=lanczos", str(td / f"c{i}-%04d.png"))
        cuadros.append(sorted(td.glob(f"c{i}-*.png")))
    F = int(fundido)
    m = mascara(W, H); cielo = Image.new("RGB", (W, H), CIELO)
    orden = []
    for i, cs in enumerate(cuadros):
        sig = cuadros[(i + 1) % len(cuadros)]; N = len(cs)
        orden += [(cs[k], None, 0) for k in range(F, N - F)] + [(cs[N - F + j], sig[j], (j + 1) / (F + 1)) for j in range(F)]
    for k, (a, b, t) in enumerate(orden):
        im = Image.open(a).convert("RGB")
        if b is not None:
            im = Image.blend(im, Image.open(b).convert("RGB"), t)
        Image.composite(im, cielo, m).save(td / f"l{k:04d}.png")
    n = len(orden)
    salida = pathlib.Path(salida)
    Image.open(td / "l0000.png").save(salida.with_suffix(".jpg"), quality=82, progressive=True, optimize=True)
    sh("-framerate", "24", "-i", str(td / "l%04d.png"), "-c:v", "libx264", "-preset", "slow", "-crf", str(crf_mp4),
       "-pix_fmt", "yuv420p", "-profile:v", "high", "-g", str(n), "-movflags", "+faststart", "-an", str(salida.with_suffix(".mp4")))
    sh("-framerate", "24", "-i", str(td / "l%04d.png"), "-c:v", "libvpx-vp9", "-crf", str(crf_webm), "-b:v", "0",
       "-row-mt", "1", "-deadline", "good", "-cpu-used", "2", "-g", str(n), "-pix_fmt", "yuv420p", "-an",
       str(salida.with_suffix(".webm")))
    if os.environ.get("GUARDAR_CUADROS") != "1":
        shutil.rmtree(td)
    pesos = {e: salida.with_suffix(e).stat().st_size for e in (".jpg", ".mp4", ".webm")}
    print(f"{salida}: {n} cuadros = {n / 24:.2f} s, {W}×{H}; " + " · ".join(f"{e[1:]} {v / 1024:.0f} KB" for e, v in pesos.items()))

def entrada(origen, destino):
    """El fijo elegido, recortado a 16:9 exacto y a 1920×1080: lo que recibe Kling como primer y último cuadro."""
    from PIL import Image
    im = Image.open(origen).convert("RGB"); w, h = im.size
    W = min(w, round(h * 16 / 9)); H = round(W * 9 / 16); x0 = (w - W) // 2; y0 = (h - H) // 2
    im.crop((x0, y0, x0 + W, y0 + H)).resize((1920, 1080), Image.LANCZOS).save(destino, quality=93)
    print(destino)

def cuenta():
    for e in libro():
        print(f"  {e['creada']}  {e['modelo']:32s} US$ {e['costo']:.3f}  {e['destino']}  {e['id']}")
    print(f"gastado US$ {gastado():.3f} de {TOPE}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    if a[0] == "recorte":
        recorte()
    elif a[0] == "editar":   # editar <nb|nbp> <consigna> <imagen> [n] [refs...]
        editar(a[1], a[2], a[3], int(a[4]) if len(a) > 4 else 1, a[5:])
    elif a[0] == "video":
        video(a[1], a[2], int(a[3]) if len(a) > 3 else 1, int(a[4]) if len(a) > 4 else 5)
    elif a[0] == "recuperar":
        recuperar()
    elif a[0] == "cuenta":
        cuenta()
    elif a[0] == "tira":
        tira(a[1], float(a[2]) if len(a) > 2 else 2)
    elif a[0] == "post":   # post <salida-base> <clip.mp4> [clip2.mp4 ...]   (ANCHO=1440, FUNDIDO=12, CRF_MP4=22, CRF_WEBM=32)
        post(a[2:], a[1], int(os.environ.get("ANCHO", 1440)), int(os.environ.get("FUNDIDO", 12)))
    elif a[0] == "entrada":   # entrada <fijo.jpg> <salida.jpg>
        entrada(a[1], a[2])
    elif a[0] == "vinetear":
        vinetear(a[1], a[2], a[3] if len(a) > 3 else None)
    else:
        raise SystemExit(__doc__)
