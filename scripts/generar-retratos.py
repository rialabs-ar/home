#!/usr/bin/env python3
"""Genera los retratos de los dos cofundadores con google/nano-banana (Replicate) a partir de sus
fotos reales, y las ediciones que salen de ellos (eclipse, melena).

Uso: generar-retratos.py <trabajo> [n_variantes]      (las variantes caen al lado del script, no se commitean)

Trabajos y el orden en que se usaron (2026-10-10, ver CONTENIDO.md §0.3):
  sebastian          retrato de Sebastián desde sus fotos reales (el vigente salió de acá, `sebastian-b1`)
  matias-v1          el primer Matías (2026-10-10 a la mañana): frontal, sereno. Quedó corto de actitud.
  matias             el Matías nuevo: aventurero creador tech, giro de 30°, brazos cruzados, mentón firme,
                     media sonrisa, luz ámbar lateral. SOLO con la foto real: pasar el retrato anterior como
                     referencia de puesta ancla la pose y devuelve el mismo Matías blando (probado, 4 de 4).
  matias-eclipse     el eclipse salía chico (≈16 % del ancho) y pedirlo "más grande" por texto no lo cambia
                     (probado, 3 de 3). Sí funciona la edición con DOS imágenes: la elegida + un retrato con el
                     eclipse del tamaño del par, como referencia de tamaño únicamente. Elegido: `matias-eclipse-1`.
  sebastian-melena   edición sobre el retrato vigente: melena rubia abundante flameando en el viento
  matias-melena      edición sobre el Matías elegido: melena rubia volando hacia atrás, como contra el viento

Exportación: `exportar(origen, destino)` recorta al 4:5 centrado y guarda 720×900 JPG progresivo q84, que es lo
que la página sirve (`assets/retrato-*.jpg`; las dos familias, con melena y `-sobrio`).
"""
import base64, json, os, sys, time, urllib.request, pathlib, concurrent.futures

TOKEN = None
for line in open(os.path.expanduser("~/.credentials/replicate.env")):
    if line.startswith("REPLICATE_API_TOKEN="):
        TOKEN = line.split("=", 1)[1].strip()
assert TOKEN, "sin token"

OUT = pathlib.Path(__file__).parent
ASSETS = OUT.parent / "assets"
FOTOS = pathlib.Path("/Users/tano/dev/RIALabs/Fotos")

# ── la puesta común del par ────────────────────────────────────────────────────────────────
ESTILO = ("Photorealistic editorial portrait, natural skin texture, no retouching look, "
          "shot on a full-frame camera with an 85mm lens at f/2, shallow depth of field, "
          "cinematic lighting: warm amber key light on the face (like the corona of a solar eclipse), "
          "cool deep-blue fill from screens, very dark background with a faint golden ring glow behind the head. "
          "Head-and-shoulders framing, subject centered, face well inside the frame (not touching edges), "
          "looking at camera with a calm confident expression, slight natural smile. "
          "Keep the exact face, age, hair, beard and glasses of the person in the reference photo; this is the same real person. "
          "No text, no logos, no watermarks.")

PUESTA_MATIAS = ("Setting: a dark software and AI studio at night. Behind him, out of focus, two large monitors glowing "
                 "with code and a blue wireframe 3D model of a city block. ")

# ── el Matías nuevo: identidad, actitud, eclipse y luz, por separado para poder ajustar uno sin tocar el resto ──
IDENTIDAD_MATIAS = (
    "He must be instantly recognizable as the same real person as the reference photo: the same long oval face, "
    "strong brow ridge, deep-set brown eyes, the same nose and mouth, same age (early forties). "
    "Hair: very dark brown, almost black, SHORT, cropped close at the sides with a little texture on top, the same "
    "hairline as the reference — not longer, not wavy, not lighter. Light salt-and-pepper stubble beard. No glasses. ")
ACTITUD = (
    "His attitude is the point of this photograph: he is a confident tech founder and adventurer, "
    "a builder who knows exactly what he is doing. Direct, steady gaze straight into the lens; firm chin, "
    "slightly raised; a knowing half-smile (closed lips, one corner up); open shoulders, chest forward; "
    "energetic posture. More dramatic and contrasty light than a standard headshot: the amber key comes from "
    "the side and sculpts the face, with deep shadows on the far side. ")
ECLIPSE = (
    "A LARGE total solar eclipse — a pitch-black disc with a thin, bright, evenly glowing golden corona ring, no rays — "
    "floats in the air above his head: its diameter is about one third of the frame width and its lower edge sits "
    "just above his hair, in the upper third of the frame. ")
LUZ = (
    "Lighting: a strong warm amber key light from camera-left that sculpts the face with deep shadows on the far side, "
    "and a cool deep-blue fill from the monitors on the shadow side. Deep black background. ")

TRABAJOS = {
    "sebastian": {
        "refs": [FOTOS / "otra.jpeg", FOTOS / "1759492597591.jpeg"],
        "prompt": ("Create a new photograph of the man in the reference photos (he must be instantly recognizable: same face, "
                   "same rectangular glasses, same grey-streaked short beard, same age). "
                   "Context: a modern security operations and video-monitoring center at night. Behind him, slightly out of focus, "
                   "a large video wall with a grid of live street-camera feeds and a city map, and a rack of network equipment with small blue status LEDs. "
                   "He wears a dark navy field jacket over a light shirt. " + ESTILO),
    },
    "matias-v1": {
        "refs": [FOTOS / "mati.jpeg"],
        "prompt": ("Create a new photograph of the man in the reference photo (he must be instantly recognizable: same face, "
                   "same short dark hair, same light stubble beard, same age, no glasses). "
                   "Context: a dark software and AI studio at night. Behind him, out of focus, two or three large monitors glowing with code and "
                   "a wireframe 3D model of a city block, and a thin golden ring of light on the wall like a solar eclipse. "
                   "He wears a dark charcoal crew-neck sweater or a dark blazer over a white shirt. " + ESTILO),
    },
    "matias": {
        "refs": [FOTOS / "mati.jpeg"],
        "prompt": ("Create a new photograph of the man in the reference photo. " + IDENTIDAD_MATIAS + ACTITUD +
                   "Pose: body turned about 30 degrees from the camera, arms crossed, leaning slightly toward the lens, head turned "
                   "back to look straight into the camera. Framing: from mid-chest up, subject centered, his face large in the "
                   "middle of the frame. He wears a dark charcoal blazer over a black crew-neck t-shirt. "
                   + PUESTA_MATIAS + ECLIPSE + LUZ +
                   "Photorealistic editorial portrait, natural skin texture, 85mm lens at f/2, shallow depth of field. No text, no logos."),
    },
    # edición: la variante elegida de `matias` + un retrato con el eclipse del tamaño del par (sólo como referencia de tamaño)
    "matias-eclipse": {
        # retrato-matias-v1.jpg = el Matías de la primera pasada (git show 388714d:assets/retrato-matias.jpg); vale
        # cualquier retrato del par con el eclipse del tamaño correcto, p. ej. assets/retrato-sebastian-sobrio.jpg
        "refs": [OUT / "matias-2.jpg", OUT / "retrato-matias-v1.jpg"],
        "prompt": ("Edit the FIRST image only. Replace the small solar eclipse above his head with an eclipse the SIZE of the one "
                   "in the SECOND image: a large pitch-black disc with a thin bright golden corona ring, about a quarter of the "
                   "image width in diameter, centered above his head with its lower edge just above his hair. Use the second image "
                   "ONLY for the size and look of the eclipse: do not change the man, his pose, his crossed arms, his expression, "
                   "his clothes, the monitors, the lighting or the framing of the first image. Photorealistic, same grain and colors."),
    },
    # ediciones de melena: la imagen de entrada es el retrato terminado de cada uno
    "sebastian-melena": {
        "refs": [ASSETS / "retrato-sebastian-sobrio.jpg"],
        "prompt": ("Edit this photograph. Give the man a thick, abundant mane of blond hair: long, well past the shoulders, "
                   "voluminous, flapping dramatically in a strong wind, with strands flying sideways and across the frame. "
                   "Keep absolutely everything else identical: his face and expression, his rectangular glasses, his grey-streaked "
                   "beard, his navy jacket and light shirt, the video wall of street-camera feeds, the equipment rack with blue LEDs, "
                   "the golden eclipse ring above his head, the lighting, the framing, the grain and the colors. Photorealistic."),
    },
    "matias-melena": {
        "refs": [ASSETS / "retrato-matias-sobrio.jpg"],
        "prompt": ("Edit this photograph. Give the man a thick, abundant mane of long blond hair streaming straight BACK behind his "
                   "head, as if he were facing into a strong headwind coming from the camera: strands trailing backward and away "
                   "from his face, which must remain completely visible. Keep absolutely everything else identical: his face and "
                   "expression, his stubble beard, his pose with crossed arms, the dark blazer and black t-shirt, the monitors with "
                   "code and the blue wireframe city, the golden eclipse above his head, the amber and blue lighting, the framing, "
                   "the grain and the colors. Photorealistic."),
    },
}

def data_uri(p):
    return "data:image/jpeg;base64," + base64.b64encode(open(p, "rb").read()).decode()

def predecir(prompt, refs, dest):
    body = json.dumps({"input": {"prompt": prompt, "image_input": [data_uri(r) for r in refs],
                                 "aspect_ratio": "4:5", "output_format": "jpg"}}).encode()
    req = urllib.request.Request("https://api.replicate.com/v1/models/google/nano-banana/predictions",
                                 data=body, method="POST",
                                 headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json",
                                          "Prefer": "wait=60"})
    with urllib.request.urlopen(req, timeout=120) as r:
        pred = json.load(r)
    pid = pred["id"]
    while pred.get("status") not in ("succeeded", "failed", "canceled"):
        time.sleep(3)
        req = urllib.request.Request(f"https://api.replicate.com/v1/predictions/{pid}",
                                     headers={"Authorization": f"Bearer {TOKEN}"})
        with urllib.request.urlopen(req, timeout=60) as r:
            pred = json.load(r)
    if pred["status"] != "succeeded":
        return f"{dest.name} FALLÓ: {pred.get('error')}"
    url = pred["output"] if isinstance(pred["output"], str) else pred["output"][0]
    urllib.request.urlretrieve(url, dest)
    return f"{dest.name} ok ({pred.get('metrics', {}).get('predict_time')} s)"

def correr(trabajo, n):
    t = TRABAJOS[trabajo]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        futs = [ex.submit(predecir, t["prompt"], t["refs"], OUT / f"{trabajo}-{i + 1}.jpg") for i in range(n)]
        for f in concurrent.futures.as_completed(futs):
            print(f.result(), flush=True)

def exportar(origen, destino):
    """Recorta al 4:5 centrado y guarda 720×900 JPG progresivo q84 (lo que sirve la página)."""
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

if __name__ == "__main__":
    if sys.argv[1] == "exportar":
        exportar(sys.argv[2], sys.argv[3])
    else:
        correr(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 3)
