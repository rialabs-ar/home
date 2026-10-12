#!/usr/bin/env python3
"""Retratos vivos (2026-10-11): los dos cofundadores quietos, esperando la foto, con la melena al viento
de un ventilador. Tres etapas, todas reproducibles desde acá (ver CONTENIDO.md §0.3):

  1. fondo      unifica el eclipse de los dos retratos fijos con google/nano-banana como editor: misma idea
                en los dos (chico, alto, centrado sobre la cabeza, lejos y apagado), sin tocar cara, pelo,
                ropa, pose ni luz. Parte de la familia con melena (`assets/retrato-*.jpg`); con `-sobrio`
                aplica lo mismo a la familia sobria.
  2. video      clip de 5 s por persona con el MISMO retrato como primer y último cuadro (el truco del loop):
                kwaivgi/kling-v2.5-turbo-pro (start_image = end_image) o bytedance/seedance-1-pro
                (image = last_frame_image, camera_fixed). Guarda el mp4 y un .json con métricas y costo.
  3. post       ffmpeg: costura del loop con fundido cruzado corto de la cola sobre la cabeza (nunca ping-pong),
                720×900, mp4 H.264 yuv420p sin audio + webm VP9, ≤ 2 MB cada uno.

Uso:
  generar-retratos-vivos.py fondo <sebastian|matias|sebastian-sobrio|matias-sobrio> [n=3]
  generar-retratos-vivos.py fondo-ref <persona> <referencia.jpg> [n]   # igualar el eclipse al de otra imagen
  generar-retratos-vivos.py video <kling|seedance> <sebastian|matias> [n=1] [imagen.jpg]
  generar-retratos-vivos.py tira <clip.mp4>                   # tira de cuadros + primer/último cuadro, para mirar
  generar-retratos-vivos.py medir <clip.mp4>                  # ¿pulsa el eclipse? ¿se mueve el fondo? ¿empalma el loop?
  generar-retratos-vivos.py post <persona> <clip.mp4> [clip2.mp4 ...]   # loop con el tramo móvil, ver abajo
  generar-retratos-vivos.py igualar-eclipse <origen> <ref> <salida> cx cy rcx rcy [cy_nuevo]   # post PIL, ver abajo
  generar-retratos-vivos.py exportar <origen> <destino>       # recorte 4:5 → 720×900 JPG progresivo q84
  generar-retratos-vivos.py ladoalado <salida.png> <a.jpg> <b.jpg> [...]
  generar-retratos-vivos.py costura <persona> [clip.mp4]   # ¿empalma el loop? ¿pestañea en el corte? ¿salta del póster?

Las variantes caen en `_capturas/retratos-vivos/` (ignorado); sólo lo elegido se exporta a `assets/`.
Token de Replicate en ~/.credentials/replicate.env. Precios leídos de Replicate el 2026-10-11:
nano-banana US$ 0,039/imagen · kling-v2.5-turbo-pro US$ 0,07/s (0,35 el clip) · seedance-1-pro US$ 0,03/0,06/0,15
por segundo a 480p/720p/1080p (0,30 el clip a 720p).

Lo que quedó hecho (2026-10-11, rama `retratos-vivos`; reconstruido de los .json y de los cuadros, ver CONTENIDO.md §0.3):
  fondo   14 ediciones nano-banana (US$ 0,55). matias ← fondo-matias-1 · sebastian ← fondo-sebastian-4 + igualar-eclipse con
          fondo-matias-1 de referencia · sobrios ← fondo-*-sobrio-2 + igualar-eclipse. Los cuatro pasaron por `exportar`.
  video   6 seedance (US$ 1,80) y 10 kling (US$ 3,50); los kling 4 y 5 de cada persona con VIENTO=fuerte. Se usaron los kling.
  post    matias ← kling-matias-2 (cuadros ~21–90) → kling-matias-4 (~15–90) → kling-matias-5 (~27–110): 246 cuadros, 10,25 s.
          sebastian ← kling-sebastian-1 (~16–100) → kling-sebastian-4 (~23–88) → kling-sebastian-5 (~25–88): 232 cuadros, 9,67 s.
          Las tres juntas de cada loop (dos adentro y la del cierre) caen bajo un pestañeo: el peso de la cara elige pares de
          cuadros con los ojos iguales, y los iguales son los cerrados. La costura del cierre mide menos que un paso entre
          cuadros consecutivos, y póster ↔ cuadro 0 también (`costura`): el arranque no salta, pestañea.
  costo   ≈ US$ 5,85 en total (sin contar generaciones fallidas, si las hubo; no quedaron registradas).
"""
import base64, json, os, subprocess, sys, time, urllib.request, pathlib, concurrent.futures

TOKEN = None
for line in open(os.path.expanduser("~/.credentials/replicate.env")):
    if line.startswith("REPLICATE_API_TOKEN="):
        TOKEN = line.split("=", 1)[1].strip()
assert TOKEN, "sin token"

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ASSETS = RAIZ / "assets"
OUT = RAIZ / "_capturas" / "retratos-vivos"
OUT.mkdir(parents=True, exist_ok=True)
FFMPEG = "/opt/homebrew/bin/ffmpeg"
FFPROBE = "/opt/homebrew/bin/ffprobe"

PRECIO = {"nano-banana": 0.039, "kling": 0.07 * 5, "seedance": {"480p": 0.03 * 5, "720p": 0.06 * 5, "1080p": 0.15 * 5}}

# ══════════════════════════════════════════════════════════════════════════════════════════════════
# 1. FONDO — la idea común del eclipse en los dos retratos
# ══════════════════════════════════════════════════════════════════════════════════════════════════
# Lo que pidió Matías: «los logos de RIA de fondo si están presentes está bien pero debe ser siguiendo una
# idea común en ambas imágenes y mucho más de fondo». La idea común, escrita una sola vez:
ECLIPSE_COMUN = (
    "Change ONLY the solar eclipse in the background, and make it the same in look, size and placement as described here: "
    "a SMALL total solar eclipse — a black disc with a thin golden corona ring — on the dark back wall, far behind him. "
    "Size: its diameter is about one fifth of the image width. Placement: horizontally centered on the vertical axis of his head, "
    "high in the frame, its center about 15 percent of the image height below the top edge, well above the top of his head, "
    "with empty dark wall between the eclipse and his hair. "
    "It is far away and out of focus (soft bokeh edges, consistent with the shallow depth of field of the portrait), and DIM: "
    "the corona glows at roughly a third of the brightness of the current one, with only a faint warm halo on the wall around it, "
    "so it reads as a quiet detail of the room, not as a halo around the person. "
    "Remove every trace of the current, larger eclipse. The eclipse is BEHIND everything: any strands of hair in front of it stay in front, sharp. "
    "Keep absolutely everything else pixel-identical: his face, expression, eyes, skin, hair (every strand, same shape and volume), "
    "beard, clothes, pose, framing, the lighting on him, the background screens and objects, the grain and the colors. Photorealistic. "
)
FONDO = {
    "sebastian": ("Edit this photograph. The man with glasses, grey-streaked beard, a navy jacket and a long blond mane flying in the wind "
                  "stays exactly as he is, and so do the video wall of street cameras on the left and the equipment rack with blue LEDs on the right. "
                  + ECLIPSE_COMUN),
    "matias":    ("Edit this photograph. The man with crossed arms, dark blazer, stubble beard and long blond hair streaming back to the left "
                  "stays exactly as he is, and so do the monitors with code and the blue wireframe city behind him. " + ECLIPSE_COMUN),
}
# Con la consigna común nano-banana le hizo a Sebastián un eclipse más chico y más alto que a Matías (≈7 % del ancho
# contra ≈12 %). Igualarlo pasándole el retrato de Matías como referencia NO sirve: la edición con dos imágenes le
# contagia el fondo (monitores, brazos cruzados) o mueve el encuadre (probado, 3 de 3). Sí sirve escribirle los
# números medidos del eclipse elegido de Matías (`fondo-matias-1`): diámetro ≈ 12 % del ancho, centro ≈ 14 % de alto.
FONDO["sebastian"] = FONDO["sebastian"].replace(
    "Size: its diameter is about one fifth of the image width.",
    "Size: its diameter is about 12 percent of the image width — a bit less than half the width of his face, clearly larger than a dot.") \
    .replace("its center about 15 percent of the image height below the top edge",
             "its center about 14 percent of the image height below the top edge")
FONDO["sebastian-sobrio"] = FONDO["sebastian"].replace("a long blond mane flying in the wind", "short hair")
FONDO["matias-sobrio"] = FONDO["matias"].replace("and long blond hair streaming back to the left", "and short dark hair")

# ══════════════════════════════════════════════════════════════════════════════════════════════════
# 2. VIDEO — quietos esperando la foto, pero vivos; la melena al viento de un ventilador
# ══════════════════════════════════════════════════════════════════════════════════════════════════
# Pedido textual: «segundos en los cuales pestañamos, nuestro pelo vuela suavemente con el viento, miramos a la
# cámara en posición estática como esperando la foto, pero se nota que estamos ahí» · «las melenas tienen que
# volar al movimiento de un ventilador, moverse en el aire como símbolo de potencia y visión».
VIVO_COMUN = (
    "Locked-off photographic portrait on a tripod: the camera does not move at all, the framing is identical from the first "
    "frame to the last. The man holds his pose completely still, looking straight into the lens, waiting for the photo to be "
    "taken, his expression unchanged. He is clearly alive: he blinks naturally twice, his chest rises and falls with slow quiet "
    "breathing, and his head has the tiniest natural micro-movements. {PELO} The wind is strong and sustained for the whole clip, "
    "never a timid breeze, and his face is never covered. {ROPA} The background stays perfectly still: {FONDO} and the small "
    "golden eclipse ring on the back wall do not move or flicker. Constant lighting throughout, the same warm amber key light and "
    "cool blue fill. Same face, same identity, {RASGOS} from start to finish. Photoreal, cinematic, 24 fps, no morphing. "
    "The last frame matches the first frame exactly so the clip loops seamlessly."
)
VIVO = {
    "sebastian": VIVO_COMUN.format(
        PELO=("His long blond mane is blown continuously by a powerful studio fan from the front: the hair streams open to both sides "
              "and upward, billowing and flowing in the air in long elegant waves, a symbol of power and vision, every strand in motion "
              "all the time."),
        ROPA="The collar of his navy jacket flutters very slightly in the wind.",
        FONDO="the video wall of street-camera feeds, the equipment rack with blue LEDs",
        RASGOS="same rectangular glasses, same grey-streaked beard, same calm half-smile"),
    "matias": VIVO_COMUN.format(
        PELO=("His long blond hair is blown continuously by a powerful studio fan from the front-right: the hair streams backward and to "
              "the left of the frame, flowing in the air in long elegant waves, a symbol of power and vision, every strand in motion "
              "all the time, his face fully visible."),
        ROPA="He keeps his arms crossed; the lapel of his dark blazer moves very slightly in the wind.",
        FONDO="the monitors with code, the blue wireframe city model",
        RASGOS="same stubble beard, same knowing half-smile, same crossed arms"),
}
# Ronda de reserva (VIENTO=fuerte): Kling dejó el pelo casi quieto en 4 de 6 clips de la primera ronda (diferencia media
# cuadro a cuadro en la zona de la melena < 1,5 sobre 255); se le pide amplitud explícita.
VIENTO_FUERTE = (" IMPORTANT: the wind is the strongest element of the shot. The fan blows hard and without pause: the hair "
                 "whips, lifts and billows with LARGE amplitude the whole five seconds, strands rising high, crossing and "
                 "streaming, constantly changing shape; at no moment does the hair hang still. The face, the body and the "
                 "background remain perfectly still.")
NEGATIVO = ("camera movement, zoom, pan, dolly, handheld shake, face change, identity change, different person, expression change, "
            "smile change, talking, mouth opening, head turning away, extra limbs, extra hands, text, watermark, flicker, lighting change, "
            "warping, morphing, blur, cartoon, hair covering the face, background movement")


# ── Replicate ─────────────────────────────────────────────────────────────────────────────────────
def data_uri(p):
    return "data:image/jpeg;base64," + base64.b64encode(open(p, "rb").read()).decode()

def replicate(modelo, entrada, timeout=900):
    body = json.dumps({"input": entrada}).encode()
    req = urllib.request.Request(f"https://api.replicate.com/v1/models/{modelo}/predictions", data=body, method="POST",
                                 headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json", "Prefer": "wait=60"})
    with urllib.request.urlopen(req, timeout=120) as r:
        pred = json.load(r)
    t0 = time.time()
    while pred.get("status") not in ("succeeded", "failed", "canceled"):
        if time.time() - t0 > timeout:
            raise TimeoutError(pred["id"])
        time.sleep(4)
        req = urllib.request.Request(f"https://api.replicate.com/v1/predictions/{pred['id']}", headers={"Authorization": f"Bearer {TOKEN}"})
        with urllib.request.urlopen(req, timeout=60) as r:
            pred = json.load(r)
    return pred

def bajar(pred, dest):
    url = pred["output"] if isinstance(pred["output"], str) else pred["output"][0]
    urllib.request.urlretrieve(url, dest)


# ── 1. fondo ──────────────────────────────────────────────────────────────────────────────────────
def fondo(persona, n=3, referencia=None):
    origen = ASSETS / f"retrato-{persona}.jpg"
    prompt = FONDO[persona]
    refs = [origen]
    if referencia:
        refs.append(pathlib.Path(referencia))
        prompt = ("Edit the FIRST image only. Replace its solar eclipse with one that matches the eclipse of the SECOND image EXACTLY "
                  "in size, position within the frame, dimness, softness and look, so that the two photographs read as the same photo "
                  "session. Use the second image ONLY for the eclipse. " + prompt.split("Edit this photograph. ", 1)[1])
    def uno(i):
        dest = OUT / f"fondo-{persona}{'-ref' if referencia else ''}-{i + 1}.jpg"
        pred = replicate("google/nano-banana", {"prompt": prompt, "image_input": [data_uri(r) for r in refs],
                                                "aspect_ratio": "4:5", "output_format": "jpg"})
        if pred["status"] != "succeeded":
            return f"{dest.name} FALLÓ: {pred.get('error')}"
        bajar(pred, dest)
        return f"{dest.name} ok ({pred.get('metrics', {}).get('predict_time')} s, US$ {PRECIO['nano-banana']:.3f})"
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for f in concurrent.futures.as_completed([ex.submit(uno, i) for i in range(n)]):
            print(f.result(), flush=True)


# ── 2. video ──────────────────────────────────────────────────────────────────────────────────────
def video(modelo, persona, n=1, imagen=None, resolucion="720p"):
    img = pathlib.Path(imagen) if imagen else ASSETS / f"retrato-{persona}.jpg"
    uri = data_uri(img)
    prompt = VIVO[persona] + (VIENTO_FUERTE if os.environ.get("VIENTO") == "fuerte" else "")
    if modelo == "kling":
        nombre, entrada = "kwaivgi/kling-v2.5-turbo-pro", {
            "prompt": prompt, "negative_prompt": NEGATIVO, "start_image": uri, "end_image": uri, "duration": 5}
        costo = PRECIO["kling"]
    elif modelo == "seedance":
        nombre, entrada = "bytedance/seedance-1-pro", {
            "prompt": prompt, "image": uri, "last_frame_image": uri, "duration": 5, "resolution": resolucion,
            "camera_fixed": True, "fps": 24}
        costo = PRECIO["seedance"][resolucion]
    else:
        raise SystemExit("modelo: kling | seedance")
    existentes = sorted(OUT.glob(f"{modelo}-{persona}-*.mp4"))
    base = len(existentes)
    def uno(i):
        k = base + i + 1
        dest = OUT / f"{modelo}-{persona}-{k}.mp4"
        e = dict(entrada)
        if modelo == "seedance":
            e["seed"] = 1000 + k
        t0 = time.time()
        pred = replicate(nombre, e)
        if pred["status"] != "succeeded":
            return f"{dest.name} FALLÓ: {pred.get('error')}"
        bajar(pred, dest)
        meta = {"modelo": nombre, "version": pred.get("version"), "id": pred["id"], "persona": persona, "imagen": str(img),
                "entrada": {k2: v for k2, v in e.items() if not str(v).startswith("data:")}, "metrics": pred.get("metrics"),
                "costo_usd": costo, "espera_s": round(time.time() - t0)}
        (OUT / f"{modelo}-{persona}-{k}.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False))
        return f"{dest.name} ok ({pred.get('metrics', {}).get('predict_time')} s de cómputo, {meta['espera_s']} s de espera, US$ {costo:.2f})"
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for f in concurrent.futures.as_completed([ex.submit(uno, i) for i in range(n)]):
            print(f.result(), flush=True)


# ── tira de cuadros, primer y último cuadro ────────────────────────────────────────────────────────
def tira(clip):
    clip = pathlib.Path(clip)
    base = clip.with_suffix("")
    sh = lambda *a: subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", *a], check=True)
    sh("-i", str(clip), "-vf", "fps=2,scale=240:-1,tile=10x1", "-frames:v", "1", f"{base}-tira.png")
    sh("-i", str(clip), "-vf", "scale=480:-1", "-frames:v", "1", f"{base}-primero.png")
    sh("-sseof", "-0.05", "-i", str(clip), "-update", "1", "-vf", "scale=480:-1", f"{base}-ultimo.png")
    print(f"{base}-tira.png  {base}-primero.png  {base}-ultimo.png")


# ── medir un clip: ¿el eclipse parpadea? ¿la cámara se mueve? ¿el último cuadro empalma con el primero? ──
def medir(clip, caja_eclipse=None, caja_fondo=None, fps=4):
    """Muestrea el clip a `fps` y mide, por cuadro: luminancia media en la caja del eclipse (si pulsa, se ve),
    diferencia media contra el primer cuadro en una caja de fondo quieto (si la cámara se mueve o la luz cambia, sube),
    y la diferencia del último cuadro contra el primero (la costura del loop). Cajas como fracciones x0,y0,x1,y1."""
    import tempfile, glob
    from PIL import Image, ImageChops, ImageStat
    clip = pathlib.Path(clip)
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-i", str(clip), "-vf", f"fps={fps},scale=360:-1", f"{td}/f%03d.png"], check=True)
        fr = [Image.open(f).convert("RGB") for f in sorted(glob.glob(f"{td}/f*.png"))]
    w, h = fr[0].size
    ce = caja_eclipse or (0.38, 0.03, 0.66, 0.22)
    cf = caja_fondo or (0.70, 0.55, 0.99, 0.75)
    box = lambda c: (int(c[0] * w), int(c[1] * h), int(c[2] * w), int(c[3] * h))
    lum = [ImageStat.Stat(f.crop(box(ce)).convert("L")).mean[0] for f in fr]
    dif = [sum(ImageStat.Stat(ImageChops.difference(fr[0].crop(box(cf)), f.crop(box(cf)))).mean) / 3 for f in fr]
    costura = sum(ImageStat.Stat(ImageChops.difference(fr[0], fr[-1])).mean) / 3
    print(f"{clip.name}: eclipse lum {min(lum):.1f}–{max(lum):.1f} (×{max(lum) / max(min(lum), 1):.2f}) · fondo dif máx {max(dif):.1f} · costura último↔primero {costura:.1f}")
    return lum, dif, costura

# ── 3. post: el loop se arma con el tramo en movimiento ───────────────────────────────────────────
# Con el mismo retrato como primer y último cuadro, los dos modelos dejan el pelo QUIETO ~0,5–1 s al principio y
# ~1 s al final (medido: diferencia cuadro a cuadro < 1/255 en la zona de la melena). Un loop del clip entero
# tendría ~2 s de pelo congelado por vuelta. Por eso el loop se construye con el tramo móvil de cada clip: se busca
# el par de cuadros (cola de uno, cabeza del siguiente —o del mismo, si es uno solo—) que más se parecen y se
# cortan ahí con un fundido cruzado corto (6 cuadros = 0,25 s). Nunca ping-pong: el pelo no vuelve para atrás.
ZONA_PELO = {"matias": (0.0, 0.1, 0.55, 0.55), "sebastian": (0.0, 0.0, 1.0, 0.45)}
# La cara pesa ×25 al elegir el par de cuadros del corte: el pestañeo de cada clip cae a ~1 s, justo donde arranca el
# pelo, y si el corte cae ahí el fundido mezcla un ojo cerrado con uno abierto (párpado fantasma). Con el peso, el
# corte se corre unos cuadros y las dos caras del fundido tienen los ojos igual.
ZONA_CARA = {"matias": (0.35, 0.30, 0.65, 0.60), "sebastian": (0.33, 0.28, 0.67, 0.60)}
PESO_CARA = 25
# La zona de los ojos sola, para `costura`: ahí se ven los pestañeos.
ZONA_OJOS = {"matias": (0.40, 0.40, 0.62, 0.50), "sebastian": (0.36, 0.36, 0.64, 0.46)}

def duracion(clip):
    out = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(clip)],
                         capture_output=True, text=True, check=True).stdout.strip()
    return float(out)

def _extraer(clip, td, nombre):
    subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-i", str(clip), "-vf",
                    "scale=720:900:force_original_aspect_ratio=increase:flags=lanczos,crop=720:900,setsar=1,fps=24",
                    f"{td}/{nombre}-%04d.png"], check=True)
    import glob
    return sorted(glob.glob(f"{td}/{nombre}-*.png"))

def _tramo_movil(chicos, zona):
    from PIL import ImageChops, ImageStat
    w, h = chicos[0].size
    b = (int(zona[0] * w), int(zona[1] * h), int(zona[2] * w), int(zona[3] * h))
    pel = [f.crop(b) for f in chicos]
    d = [ImageStat.Stat(ImageChops.difference(a, bb)).mean[0] for a, bb in zip(pel, pel[1:])]
    a = next((i for i in range(len(d) - 3) if all(x >= 1.0 for x in d[i:i + 3])), 0)
    z = next((i + 1 for i in range(len(d) - 1, 2, -1) if all(x >= 1.0 for x in d[i - 2:i + 1])), len(chicos) - 1)
    return a, z, d

def _dif(a, b, cara=None):
    from PIL import ImageChops, ImageStat
    d = ImageStat.Stat(ImageChops.difference(a, b)).mean[0]
    if cara:
        d += PESO_CARA * ImageStat.Stat(ImageChops.difference(a.crop(cara), b.crop(cara))).mean[0]
    return d

def post(persona, clips, fundido=6, ventana=30):
    """clips: uno o más mp4 de la misma persona (y del mismo modelo, para que no cambie el color). Salida:
    assets/retrato-<persona>.mp4 (H.264 yuv420p, sin audio, faststart) y .webm (VP9), 720×900, 24 fps."""
    import tempfile
    from PIL import Image
    F = int(fundido)
    with tempfile.TemporaryDirectory() as td:
        rutas = [_extraer(c, td, f"c{k}") for k, c in enumerate(clips)]
        chicos = [[Image.open(r).convert("L").resize((240, 300), Image.BILINEAR) for r in rs] for rs in rutas]
        tramos = []
        for k, ch in enumerate(chicos):
            a, z, _ = _tramo_movil(ch, ZONA_PELO[persona])
            tramos.append([a, z])
            print(f"  {pathlib.Path(clips[k]).name}: {len(ch)} cuadros, pelo en movimiento del {a} al {z} ({(z - a) / 24:.2f} s)")
        n = len(clips)
        w, h = chicos[0][0].size; zc = ZONA_CARA[persona]
        cara = (int(zc[0] * w), int(zc[1] * h), int(zc[2] * w), int(zc[3] * h))
        # un corte por junta k→k+1 (la última junta cierra el loop con el primero): el par (i, j) más parecido
        cortes = []
        for k in range(n):
            k2 = (k + 1) % n
            a, z = tramos[k]; a2, z2 = tramos[k2]
            mejor = None
            # la cola puede entrar unos cuadros en la zona quieta (el pelo frena, la cara vuelve a la pose) y la cabeza
            # arrancar unos cuadros antes del movimiento: ahí las dos caras del fundido son casi la misma foto
            for i in range(max(z - ventana, a + 24), min(z + 12, len(chicos[k]) - 1) + 1):
                for j in range(max(a2 - 8, 0), min(a2 + ventana, len(chicos[k2]) - 1) + 1):
                    if k == k2 and j + 24 > i: continue
                    v = _dif(chicos[k][i], chicos[k2][j], cara)
                    if mejor is None or v < mejor[0]: mejor = (v, i, j)
            cortes.append(mejor)
            print(f"  junta {k}→{k2}: cuadro {mejor[1]} → {mejor[2]} (dif ponderada {mejor[0]:.1f}, "
                  f"cara {_dif(chicos[k][mejor[1]].crop(cara), chicos[k2][mejor[2]].crop(cara)):.1f})")
        # cada tramo k va desde la cabeza que le dejó la junta k-1 hasta la cola que le pide la junta k
        salida = []
        for k in range(n):
            _, i_fin, _ = cortes[k]
            _, _, j_ini = cortes[(k - 1) % n]
            s0, e0 = j_ini - F // 2, i_fin + F // 2
            cuerpo = [Image.open(r).convert("RGB") for r in rutas[k][s0:e0 + 1]]
            salida.append(cuerpo)
        # fundidos: los últimos F cuadros de cada tramo se funden con los primeros F del siguiente. Los F primeros
        # cuadros de CADA tramo (también del 0) viven sólo dentro del fundido que los precede, que para el tramo 0
        # es el último del loop: así, al reiniciar, el cuadro que sigue al fundido final es cuerpo0[F], sin salto.
        final = []; centros = []
        for k in range(n):
            cuerpo = salida[k]; sig = salida[(k + 1) % n]
            final.extend(cuerpo[F:-F])
            centros.append(len(final) + F // 2)
            for t in range(F):
                al = (t + 1) / (F + 1)
                final.append(Image.blend(cuerpo[-F + t], sig[t], al))
        (OUT / "final").mkdir(exist_ok=True)
        for k, c in enumerate(centros):   # el cuadro del centro de cada fundido, para mirarlo
            final[c].save(OUT / "final" / f"{persona}-junta-{k + 1}.png")
        for q, im in enumerate(final):
            im.save(f"{td}/o-{q:04d}.png")
        print(f"  loop: {len(final)} cuadros = {len(final) / 24:.2f} s · centros de fundido en "
              + ", ".join(f"{c / 24:.2f} s" for c in centros) + f" (cuadros guardados en {OUT / 'final'})")
        dest = ASSETS / f"retrato-{persona}"
        ent = ["-hide_banner", "-loglevel", "error", "-y", "-framerate", "24", "-i", f"{td}/o-%04d.png", "-an"]
        subprocess.run([FFMPEG, *ent, "-c:v", "libx264", "-preset", "slow", "-crf", "24", "-pix_fmt", "yuv420p",
                        "-movflags", "+faststart", "-tune", "film", f"{dest}.mp4"], check=True)
        subprocess.run([FFMPEG, *ent, "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "34", "-row-mt", "1", "-deadline", "good",
                        "-cpu-used", "1", "-pix_fmt", "yuv420p", f"{dest}.webm"], check=True)
    for ext in ("mp4", "webm"):
        pth = pathlib.Path(f"{dest}.{ext}")
        print(f"{pth.name}: {pth.stat().st_size / 1024:.0f} KB, {duracion(pth):.2f} s")


# ── costura: ¿empalma el loop? ¿pestañea en el corte? ¿salta del póster al cuadro 0? ─────────────────
def costura(persona, clip=None):
    """Mide el clip final (o el que se pase) a 240×300 en gris: el paso medio entre cuadros consecutivos (total, zona del
    pelo, zona de la cara) y, contra eso, la diferencia último ↔ primero —si es menor o parecida, la costura no se ve—;
    los tramos con los ojos lejos de la mediana por píxel (los pestañeos marcados —los suaves, y los que caen bajo un
    fundido, no llegan al umbral: para esos, mirar la tira— y si uno cruza el corte); y la diferencia del
    póster (assets/retrato-<persona>.jpg) contra el cuadro 0 —si en el pelo es menor que el paso, el arranque no salta."""
    import tempfile, glob
    from PIL import Image, ImageChops, ImageStat
    clip = pathlib.Path(clip) if clip else ASSETS / f"retrato-{persona}.mp4"
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-i", str(clip), "-vf", "scale=240:300",
                        "-fps_mode", "passthrough", f"{td}/f%04d.png"], check=True)
        fr = [Image.open(f).convert("L") for f in sorted(glob.glob(f"{td}/f*.png"))]
    w, h = fr[0].size
    box = lambda z: (int(z[0] * w), int(z[1] * h), int(z[2] * w), int(z[3] * h))
    zp, zc, zo = box(ZONA_PELO[persona]), box(ZONA_CARA[persona]), box(ZONA_OJOS[persona])
    d = lambda a, b, z=None: ImageStat.Stat(ImageChops.difference(a.crop(z) if z else a, b.crop(z) if z else b)).mean[0]
    media = lambda xs: sum(xs) / len(xs)
    ct, cp, cc = ([d(a, b, z) for a, b in zip(fr, fr[1:])] for z in (None, zp, zc))
    print(f"{clip.name}: {len(fr)} cuadros = {len(fr) / 24:.2f} s")
    print(f"  paso entre cuadros consecutivos · total {media(ct):.2f} (máx {max(ct):.2f}) · pelo {media(cp):.2f} (máx {max(cp):.2f})"
          f" · cara {media(cc):.2f} (máx {max(cc):.2f})")
    print(f"  último ↔ primero                · total {d(fr[-1], fr[0]):.2f} · pelo {d(fr[-1], fr[0], zp):.2f} · cara {d(fr[-1], fr[0], zc):.2f}")
    ojos = [f.crop(zo) for f in fr]; px = [o.load() for o in ojos]; bw, bh = ojos[0].size
    ref = Image.new("L", (bw, bh)); rp = ref.load()      # mediana por píxel: los ojos están abiertos casi todo el tiempo
    for y in range(bh):
        for x in range(bw):
            v = sorted(p[x, y] for p in px); rp[x, y] = v[len(v) // 2]
    do = [d(o, ref) for o in ojos]; umbral = 2 * sorted(do)[len(do) // 2]
    tramos, cur = [], None
    for i, v in enumerate(do):
        if v > umbral: cur = [i, i] if cur is None else [cur[0], i]
        elif cur: tramos.append(tuple(cur)); cur = None
    if cur: tramos.append(tuple(cur))
    cruza = bool(tramos) and (tramos[0][0] == 0 or tramos[-1][1] == len(fr) - 1)
    print("  pestañeos (ojos lejos de la mediana): " + (", ".join(f"{a}–{b} ({a / 24:.2f} s)" for a, b in tramos) or "ninguno")
          + (" · uno cruza el corte" if cruza else ""))
    poster = ASSETS / f"retrato-{persona}.jpg"
    if poster.exists():
        p = Image.open(poster).convert("L").resize((w, h), Image.LANCZOS)
        print(f"  póster ↔ cuadro 0               · total {d(p, fr[0]):.2f} · pelo {d(p, fr[0], zp):.2f} · cara {d(p, fr[0], zc):.2f}")


# ── igualar el eclipse en post (PIL) ──────────────────────────────────────────────────────────────
# nano-banana no agranda el eclipse por texto (3 de 3 el 10/10, 7 de 7 hoy). Como alrededor del eclipse hay pared lisa,
# se puede escalar EN SU LUGAR el parche del eclipse de la variante elegida hasta el radio de corona medido en la
# imagen de referencia, con una máscara radial suave. Es una operación de post, no una generación.
def perfil_radial(im, cx, cy, rmax=150):
    L = im.convert("L").load()
    acc = [0.0] * rmax; cnt = [0] * rmax
    for y in range(cy - rmax, cy + rmax):
        for x in range(cx - rmax, cx + rmax):
            r = int(((x - cx) ** 2 + (y - cy) ** 2) ** 0.5)
            if r < rmax: acc[r] += L[x, y]; cnt[r] += 1
    return [a / c if c else 0 for a, c in zip(acc, cnt)]

def centro_corona(im, cx, cy, R=90):
    """Afina el centro con el centroide de los píxeles dorados en un radio R."""
    px = im.convert("RGB").load(); xs = []; ys = []
    for y in range(cy - R, cy + R):
        for x in range(cx - R, cx + R):
            r, g, b = px[x, y]
            if r > 90 and g > 55 and b < 80 and r - b > 60 and (x - cx) ** 2 + (y - cy) ** 2 < R * R: xs.append(x); ys.append(y)
    return round(sum(xs) / len(xs)), round(sum(ys) / len(ys))

def radio_corona(im, cx, cy):
    perf = perfil_radial(im, cx, cy)
    return max(range(6, len(perf)), key=lambda r: perf[r])

def igualar_eclipse(origen, referencia, salida, cx, cy, rcx, rcy, cy_nuevo=None):
    from PIL import Image, ImageDraw, ImageFilter
    im = Image.open(origen).convert("RGB"); ref = Image.open(referencia).convert("RGB")
    cx, cy = centro_corona(im, cx, cy); rcx, rcy = centro_corona(ref, rcx, rcy)
    r0, r1 = radio_corona(im, cx, cy), radio_corona(ref, rcx, rcy)
    f = r1 / r0
    print(f"origen: centro {(cx, cy)} radio corona {r0} px · referencia: centro {(rcx, rcy)} radio {r1} px · factor {f:.2f}")
    half = int(r0 * 2.6)                       # el parche incluye el halo
    parche = im.crop((cx - half, cy - half, cx + half, cy + half))
    nh = int(half * f)
    parche = parche.resize((2 * nh, 2 * nh), Image.LANCZOS)
    masc = Image.new("L", parche.size, 0)
    ImageDraw.Draw(masc).ellipse((nh * 0.12, nh * 0.12, 2 * nh - nh * 0.12, 2 * nh - nh * 0.12), fill=255)
    masc = masc.filter(ImageFilter.GaussianBlur(nh * 0.14))
    # primero se tapa el eclipse chico con pared limpia (un parche de pared de al lado), después se pega el grande
    pared = im.crop((cx - half - 2 * half, cy - half, cx - half, cy + half)).transpose(Image.FLIP_LEFT_RIGHT)
    mp = Image.new("L", pared.size, 0); ImageDraw.Draw(mp).ellipse((half * 0.1, half * 0.1, 2 * half - half * 0.1, 2 * half - half * 0.1), fill=255)
    mp = mp.filter(ImageFilter.GaussianBlur(half * 0.14))
    im.paste(pared, (cx - half, cy - half), mp)
    ncy = cy_nuevo if cy_nuevo is not None else cy
    im.paste(parche, (cx - nh, ncy - nh), masc)
    im.save(salida, "JPEG", quality=95)
    print(salida, "centro nuevo", (cx, ncy), "radio nuevo ≈", round(r0 * f))

# ── exportar / lado a lado ─────────────────────────────────────────────────────────────────────────
def exportar(origen, destino):
    from PIL import Image
    im = Image.open(origen).convert("RGB")
    w, h = im.size
    r = 4 / 5
    if w / h > r:
        nw = round(h * r); x0 = (w - nw) // 2; im = im.crop((x0, 0, x0 + nw, h))
    elif w / h < r:
        nh = round(w / r); y0 = (h - nh) // 2; im = im.crop((0, y0, w, y0 + nh))
    im.resize((720, 900), Image.LANCZOS).save(destino, "JPEG", quality=84, progressive=True, optimize=True)
    print(destino)

def ladoalado(salida, *imgs, alto=600):
    from PIL import Image
    ims = [Image.open(p).convert("RGB") for p in imgs]
    ims = [im.resize((round(im.width * alto / im.height), alto), Image.LANCZOS) for im in ims]
    lienzo = Image.new("RGB", (sum(im.width for im in ims) + 8 * (len(ims) - 1), alto), (20, 20, 20))
    x = 0
    for im in ims:
        lienzo.paste(im, (x, 0)); x += im.width + 8
    lienzo.save(salida)
    print(salida)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    if a[0] == "fondo":
        fondo(a[1], int(a[2]) if len(a) > 2 else 3)
    elif a[0] == "fondo-ref":
        fondo(a[1], int(a[3]) if len(a) > 3 else 3, referencia=a[2])
    elif a[0] == "video":
        video(a[1], a[2], int(a[3]) if len(a) > 3 else 1, a[4] if len(a) > 4 else None,
              os.environ.get("RESOLUCION", "720p"))
    elif a[0] == "medir":
        for c in a[1:]:
            medir(c)
    elif a[0] == "tira":
        for c in a[1:]:
            tira(c)
    elif a[0] == "post":   # post <persona> <clip.mp4> [clip2.mp4 ...]   (FUNDIDO=6 cuadros por defecto)
        post(a[1], a[2:], int(os.environ.get("FUNDIDO", 6)))
    elif a[0] == "costura":   # costura <persona> [clip.mp4]
        costura(a[1], a[2] if len(a) > 2 else None)
    elif a[0] == "igualar-eclipse":   # origen referencia salida cx cy rcx rcy [cy_nuevo]
        igualar_eclipse(a[1], a[2], a[3], *map(int, a[4:8]), cy_nuevo=int(a[8]) if len(a) > 8 else None)
    elif a[0] == "exportar":
        exportar(a[1], a[2])
    elif a[0] == "ladoalado":
        ladoalado(a[1], *a[2:])
    else:
        raise SystemExit(__doc__)
