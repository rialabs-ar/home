#!/usr/bin/env python3
"""El eclipse cinemático del hero (2026-10-12, rama `eclipse-cinematico`): tres imágenes generadas con
google/nano-banana (Replicate) y procesadas en post para que la página las use como CAPAS.

  corona   la corona de la totalidad: streamers finos y asimétricos, protuberancias en el limbo, disco negro
           centrado, cielo negro puro. Se convierte a WebP CON ALFA desde la luminancia (negro → transparente),
           así se funde con el cielo de estrellas sin `mix-blend-mode` (que adentro del stacking context del
           hero taparía el cielo con un cuadrado negro) y sin recuadro en ningún tema.
  sol      la fotósfera en luz blanca: oscurecimiento al limbo, granulación, alguna mancha. Alfa = disco.
  luna     la luna llena, textura de mares y cráteres. Alfa = disco; se tiñe al dorado de la casa en post
           (la cara iluminada de la luna viajera se ve con la luz del sol de la página, que es dorada).

Uso:
  generar-eclipse.py corona [n=4] [variante=a|b]     genera variantes en _capturas/eclipse-cinematico/gen/
  generar-eclipse.py sol [n=2]
  generar-eclipse.py luna [n=2]
  generar-eclipse.py medir <png>                       centro y radio del disco negro/claro, para alinear
  generar-eclipse.py post-corona <png> [lado=1000] [radios=3.3]   → assets/eclipse-corona.webp (+ .jpg de respaldo en negro)
  generar-eclipse.py post-sol <png> [lado=720]         → assets/eclipse-sol.webp
  generar-eclipse.py post-luna <png> [lado=720]        → assets/eclipse-luna.webp
  generar-eclipse.py hoja <salida.png> <a.png> <b.png> [...]    hoja de contacto para elegir mirando

Precio leído de Replicate el 2026-10-11: nano-banana US$ 0,039 por imagen (salida 1024×1024). Las variantes
no se commitean; lo elegido se exporta a assets/. Token en ~/.credentials/replicate.env.

Lo que quedó hecho (2026-10-12, rama `eclipse-cinematico`; detalle en CONTENIDO.md §0.1 y §0.3):
  corona   4 × `corona-a` (astrofoto pura, blanca y fría) + 4 × `corona-b` (cine, blanco-dorado a ámbar). Elegida
           corona-b-4 → `post-corona corona-b-4.png 1000 3.3` → assets/eclipse-corona.webp (150 KB, r/lado = 0,1515)
           + eclipse-corona.jpg (37 KB, la toma sobre negro, de respaldo). nano-banana hizo el disco al 24 % del
           cuadro, no al 40 % pedido: el post lo mide y no depende de eso.
  sol      2 variantes; elegida sol-2 (más oscurecimiento al limbo) → assets/eclipse-sol.webp (20 KB, r/lado = 0,4873).
  luna     2 variantes; elegida luna-1 (mares más ricos) → assets/eclipse-luna.webp (22 KB, r/lado = 0,4873). El tinte
           (150,118,70)→(255,250,232) es el segundo: el primero, con mares marrones, daba una bola oliva sobre papel.
  costo    12 imágenes, US$ 0,47. Variantes y hojas de contacto en _capturas/eclipse-cinematico/gen/ (ignorado).
  página   v5/index.html: #sis-corona-img (177,6 % del wrap = 91,5/0,1515 unidades de 340), <image> del sol de 190,85
           unidades (93/0,4873) y de la luna viajera de 2,052 (1/0,4873). Si cambia el radio medido, cambian esos tres.
"""
import base64, json, os, sys, time, urllib.request, pathlib, concurrent.futures, subprocess

TOKEN = None
for line in open(os.path.expanduser("~/.credentials/replicate.env")):
    if line.startswith("REPLICATE_API_TOKEN="):
        TOKEN = line.split("=", 1)[1].strip()

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ASSETS = RAIZ / "assets"
# las variantes caen en el repo principal (ignorado), aunque el script corra desde un worktree
OUT = pathlib.Path("/Users/tano/dev/RIALabs/Proyectos/RIA/_capturas/eclipse-cinematico/gen")
OUT.mkdir(parents=True, exist_ok=True)
PRECIO = 0.039

# ── prompts ─────────────────────────────────────────────────────────────────────────────────────────
NEGATIVO = ("Pure black sky with no stars, no landscape, no clouds, no lens flare, no text, no watermark, "
            "no caption, no frame, no vignette.")

PROMPTS = {
    # a: astrofotografía pura, HDR compuesto (lo que se ve en una buena foto de totalidad)
    "corona-a": (
        "Astrophotography of a total solar eclipse at the exact moment of totality. The Moon is a perfectly round, "
        "perfectly black disc exactly centered in the square frame, its diameter about 40% of the frame width. "
        "Around it the real solar corona: fine, filamentous, asymmetric streamers — long helmet streamers tapering "
        "far out toward the solar equator on the left and right, short bristling polar plumes at the top and bottom — "
        "with delicate white-gold light that fades smoothly into pure black. Two or three tiny red-pink prominences "
        "on the lunar limb. High dynamic range composite shot through a long telephoto lens, razor sharp, cinematic, "
        "photorealistic. " + NEGATIVO),
    # b: la misma escena con la temperatura de la casa (dorado) y más dramatismo de cine
    "corona-b": (
        "Cinematic photograph of a total solar eclipse at totality, as seen through a long telephoto lens on a cinema "
        "camera. A perfectly black circular Moon disc sits exactly in the center of the square frame, about 40% of the "
        "frame width in diameter. The solar corona surrounds it: intricate, thread-like streamers radiating outward, "
        "longer and asymmetric along the horizontal axis, shorter feathery plumes near the poles, every filament "
        "resolved, warm golden-white light near the limb fading to amber and then to pure black far out. A few small "
        "red prominences glow on the edge of the disc. Deep contrast, true black background, no stars. Photorealistic, "
        "high dynamic range, no grain. " + NEGATIVO),
    "sol": (
        "The Sun photographed in white light through a solar telescope with a Herschel wedge: a perfectly round disc "
        "exactly centered, its diameter about 72% of the square frame. Pale golden-white photosphere with realistic "
        "limb darkening (noticeably darker and more orange toward the edge), fine granulation texture, two or three "
        "small sunspot groups with umbra and penumbra, a crisp sharp edge, on a pure black background. No glare, no "
        "corona, no rays, no stars, no text, no watermark. Photorealistic astrophotography."),
    "luna": (
        "The full Moon photographed through a telescope: a perfectly round disc exactly centered, its diameter about "
        "80% of the square frame. Sharp maria, craters and ray systems with realistic detail, neutral grey tones, "
        "evenly lit with no terminator and no shadow, crisp edge, on a pure black background. No stars, no text, no "
        "watermark, no glow. Photorealistic astrophotography."),
}

# ── Replicate ───────────────────────────────────────────────────────────────────────────────────────
def predecir(prompt, dest):
    assert TOKEN, "sin token"
    body = json.dumps({"input": {"prompt": prompt, "aspect_ratio": "1:1", "output_format": "png"}}).encode()
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
    json.dump({"prompt": prompt, "modelo": "google/nano-banana", "costo_usd": PRECIO,
               "predict_time": pred.get("metrics", {}).get("predict_time")},
              open(dest.with_suffix(".json"), "w"), indent=1, ensure_ascii=False)
    return f"{dest.name} ok ({pred.get('metrics', {}).get('predict_time')} s)"

def correr(clave, n, prefijo):
    prompt = PROMPTS[clave]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        futs = [ex.submit(predecir, prompt, OUT / f"{prefijo}-{i + 1}.png") for i in range(n)]
        for f in concurrent.futures.as_completed(futs):
            print(f.result(), flush=True)
    print(f"costo ≈ US$ {n * PRECIO:.2f}")

# ── post (PIL puro: en esta máquina no hay numpy, y el script tiene que correr donde corre la captura) ──
from PIL import Image, ImageChops, ImageDraw, ImageMath, ImageOps

def _max_canal(im):
    r, g, b = im.convert("RGB").split()
    return ImageChops.lighter(ImageChops.lighter(r, g), b)

def medir_disco(im, oscuro=True, umbral=14):
    """Centro y radio del disco (negro si oscuro=True, claro si no) que contiene el centro de la imagen.
    Flood fill desde el centro sobre la máscara umbralizada; el radio sale del área (robusto a bordes
    irregulares) y el centro del bbox (el disco es redondo). Si el relleno se escapa al cielo, avisa."""
    mx = _max_canal(im)
    m = mx.point(lambda v: 255 if ((v < umbral) if oscuro else (v >= umbral)) else 0)
    w, h = m.size
    if m.getpixel((w // 2, h // 2)) != 255:
        raise SystemExit("el centro de la imagen no cae en el disco")
    ImageDraw.floodfill(m, (w // 2, h // 2), 128)
    sel = m.point(lambda v: 255 if v == 128 else 0)
    x0, y0, x1, y1 = sel.getbbox()
    n = sel.histogram()[255]
    cx, cy, r = (x0 + x1 - 1) / 2, (y0 + y1 - 1) / 2, (n / 3.141592653589793) ** 0.5
    if r > 0.45 * min(w, h):
        raise SystemExit(f"el disco se escapa al cielo (r={r:.0f}): subir/bajar el umbral")
    return cx, cy, r

def _recentrar(im, cx, cy, lado):
    """Recorta un cuadrado de `lado` centrado en (cx, cy); lo que falta se rellena con negro."""
    out = Image.new("RGB", (lado, lado), (0, 0, 0))
    x0, y0 = round(cx - lado / 2), round(cy - lado / 2)
    out.paste(im.convert("RGB"), (-x0, -y0))
    return out

def _radial(lado):
    """Distancia al centro normalizada (1 = semilado), como imagen L en 0..181 (Image.radial_gradient
    devuelve dist·√2 sobre 256 px: 181 en el medio de un lado, 255 en la esquina)."""
    return Image.radial_gradient("L").resize((lado, lado), Image.BILINEAR)

def _disco_aa(lado, R):
    """Máscara de disco antialiasada (dibujada a 4× y reducida)."""
    m = Image.new("L", (lado * 4, lado * 4), 0)
    c = lado * 2
    ImageDraw.Draw(m).ellipse([c - R * 4, c - R * 4, c + R * 4, c + R * 4], fill=255)
    return m.resize((lado, lado), Image.BOX)

def _despremultiplicar(sq, alpha):
    """color = color·255/alfa donde alfa>0 (ImageMath divide enteros y da 0 si alfa=0)."""
    a = alpha.convert("I")
    bandas = []
    for c in sq.split():
        bandas.append(ImageMath.lambda_eval(lambda d: d["convert"](d["min"](d["c"] * 255 / d["a"], 255), "L"),
                                            c=c.convert("I"), a=a))
    return bandas

def _webp(rgba, dest, q=82, aq=90):
    tmp = OUT / ("_" + dest.stem + "-rgba.png")
    rgba.save(tmp)
    subprocess.run(["/opt/homebrew/bin/cwebp", "-quiet", "-q", str(q), "-alpha_q", str(aq), "-m", "6", str(tmp), "-o", str(dest)], check=True)
    return dest.stat().st_size // 1024

def post_corona(src, lado=1000, radios=3.3):
    """Corona → WebP con alfa. El disco negro queda centrado; la imagen se recorta a un cuadrado que
    incluye toda la corona que haya, y el alfa sale de la luminancia (canal máximo), des-premultiplicando
    el color para que compuesta en normal sobre negro dé exactamente la foto. Un feather radial lleva el
    alfa a cero antes del borde del cuadrado, así nunca se ve el recorte. Imprime el radio del disco
    relativo al lado, que es el número que la página necesita para escalarla."""
    im = Image.open(src).convert("RGB")
    cx, cy, r = medir_disco(im)
    w, h = im.size
    half = r * radios   # el cuadrado abarca `radios` radios de disco; lo que falte se rellena en negro
    sq = _recentrar(im, cx, cy, int(round(half * 2))).resize((lado, lado), Image.LANCZOS)
    rr = r / (half * 2) * lado
    # alfa = canal máximo, con el ruido del negro (≤ 2,5 %) a cero
    alpha = _max_canal(sq).point(lambda v: 0 if v <= 6 else min(255, round((v - 6) * 255 / 249)))
    # feather radial: de 0,86 a 1,0 del semilado el alfa baja a cero, suave (smoothstep)
    def fth(v):
        t = max(0.0, min(1.0, (1.0 - v / 181.02) / 0.14))
        return round(255 * t * t * (3 - 2 * t))
    alpha = ImageChops.multiply(alpha, _radial(lado).point(fth))
    # el disco de la luna también a cero (la página dibuja su propia luna encima)
    ImageDraw.Draw(alpha).ellipse([lado / 2 - rr * 0.985, lado / 2 - rr * 0.985, lado / 2 + rr * 0.985, lado / 2 + rr * 0.985], fill=0)
    rgba = Image.merge("RGBA", _despremultiplicar(sq, alpha) + [alpha])
    dest = ASSETS / "eclipse-corona.webp"
    kb = _webp(rgba, dest)
    jpg = ASSETS / "eclipse-corona.jpg"
    sq.save(jpg, "JPEG", quality=86, progressive=True, optimize=True)
    print(f"disco: centro ({cx:.1f},{cy:.1f}) r={r:.1f} px en el original; en el cuadrado de {lado}: r={rr:.1f} "
          f"→ r/lado = {rr / lado:.4f}")
    print(f"{dest} {kb} KB · {jpg} {jpg.stat().st_size // 1024} KB")
    return rr / lado

def _post_disco(src, dest, lado, tinte=None, margen=1.006):
    """Sol o luna → WebP con alfa = disco (medido), centrado, con el disco ocupando (casi) todo el lado:
    la página lo calza con un círculo de radio conocido. `tinte` = (oscuro, claro) para duotono."""
    im = Image.open(src).convert("RGB")
    cx, cy, r = medir_disco(im, oscuro=False, umbral=18)
    sq = _recentrar(im, cx, cy, int(round(r * 2 * margen * 1.02))).resize((lado, lado), Image.LANCZOS)
    if tinte:
        sq = ImageOps.colorize(ImageOps.grayscale(sq), black=tinte[0], white=tinte[1])
    R = lado / 2 / margen / 1.02
    alpha = _disco_aa(lado, R)
    rgba = Image.merge("RGBA", list(sq.split()) + [alpha])
    kb = _webp(rgba, dest, q=84, aq=95)
    print(f"disco r={r:.1f} px en el original; {dest} {kb} KB; el disco ocupa r/lado = {R / lado:.4f}")

def hoja(salida, rutas, lado=512):
    n = len(rutas); cols = min(n, 4); filas = (n + cols - 1) // cols
    H = Image.new("RGB", (cols * lado, filas * (lado + 22)), (0, 0, 0))
    dr = ImageDraw.Draw(H)
    for i, p in enumerate(rutas):
        im = Image.open(p).convert("RGB").resize((lado, lado), Image.LANCZOS)
        x, y = (i % cols) * lado, (i // cols) * (lado + 22)
        H.paste(im, (x, y + 22)); dr.text((x + 6, y + 4), pathlib.Path(p).stem, fill=(220, 200, 150))
    H.save(salida); print(salida)

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "corona":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 4
        v = sys.argv[3] if len(sys.argv) > 3 else "a"
        correr("corona-" + v, n, "corona-" + v)
    elif cmd in ("sol", "luna"):
        correr(cmd, int(sys.argv[2]) if len(sys.argv) > 2 else 2, cmd)
    elif cmd == "medir":
        im = Image.open(sys.argv[2]); print(im.size, "negro:", medir_disco(im))
    elif cmd == "post-corona":
        post_corona(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1000, float(sys.argv[4]) if len(sys.argv) > 4 else 3.3)
    elif cmd == "post-sol":
        _post_disco(sys.argv[2], ASSETS / "eclipse-sol.webp", int(sys.argv[3]) if len(sys.argv) > 3 else 720)
    elif cmd == "post-luna":
        _post_disco(sys.argv[2], ASSETS / "eclipse-luna.webp", int(sys.argv[3]) if len(sys.argv) > 3 else 720,
                    tinte=((150, 118, 70), (255, 250, 232)))   # cara luminosa: crema con mares tostados, legible sobre papel y sobre noche
    elif cmd == "hoja":
        hoja(sys.argv[2], sys.argv[3:])
    else:
        raise SystemExit(__doc__)
