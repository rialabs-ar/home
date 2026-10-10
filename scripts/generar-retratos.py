#!/usr/bin/env python3
"""Genera retratos realistas de los dos cofundadores en contexto, con google/nano-banana
(Replicate) a partir de sus fotos reales. Uso: generar.py <quien> <n_variantes>"""
import base64, json, os, sys, time, urllib.request, pathlib

TOKEN = None
for line in open(os.path.expanduser("~/.credentials/replicate.env")):
    if line.startswith("REPLICATE_API_TOKEN="):
        TOKEN = line.split("=", 1)[1].strip()
assert TOKEN, "sin token"

OUT = pathlib.Path(__file__).parent
FOTOS = pathlib.Path("/Users/tano/dev/RIALabs/Fotos")

ESTILO = ("Photorealistic editorial portrait, natural skin texture, no retouching look, "
          "shot on a full-frame camera with an 85mm lens at f/2, shallow depth of field, "
          "cinematic lighting: warm amber key light on the face (like the corona of a solar eclipse), "
          "cool deep-blue fill from screens, very dark background with a faint golden ring glow behind the head. "
          "Head-and-shoulders framing, subject centered, face well inside the frame (not touching edges), "
          "looking at camera with a calm confident expression, slight natural smile. "
          "Keep the exact face, age, hair, beard and glasses of the person in the reference photo; this is the same real person. "
          "No text, no logos, no watermarks.")

PERSONAS = {
    "sebastian": {
        "refs": ["otra.jpeg", "1759492597591.jpeg"],
        "prompt": ("Create a new photograph of the man in the reference photos (he must be instantly recognizable: same face, "
                   "same rectangular glasses, same grey-streaked short beard, same age). "
                   "Context: a modern security operations and video-monitoring center at night. Behind him, slightly out of focus, "
                   "a large video wall with a grid of live street-camera feeds and a city map, and a rack of network equipment with small blue status LEDs. "
                   "He wears a dark navy field jacket over a light shirt. " + ESTILO),
    },
    "matias": {
        "refs": ["mati.jpeg"],
        "prompt": ("Create a new photograph of the man in the reference photo (he must be instantly recognizable: same face, "
                   "same short dark hair, same light stubble beard, same age, no glasses). "
                   "Context: a dark software and AI studio at night. Behind him, out of focus, two or three large monitors glowing with code and "
                   "a wireframe 3D model of a city block, and a thin golden ring of light on the wall like a solar eclipse. "
                   "He wears a dark charcoal crew-neck sweater or a dark blazer over a white shirt. " + ESTILO),
    },
}

def data_uri(p):
    mime = "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()

def run(quien, n):
    per = PERSONAS[quien]
    refs = [data_uri(FOTOS / r) for r in per["refs"]]
    for i in range(n):
        body = json.dumps({"input": {
            "prompt": per["prompt"],
            "image_input": refs,
            "aspect_ratio": "4:5",
            "output_format": "jpg",
        }}).encode()
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
            print(quien, i, "FALLÓ:", pred.get("error"), file=sys.stderr); continue
        url = pred["output"] if isinstance(pred["output"], str) else pred["output"][0]
        dest = OUT / f"{quien}-{i+1}.jpg"
        urllib.request.urlretrieve(url, dest)
        print(quien, i + 1, "->", dest, pred.get("metrics", {}).get("predict_time"))

if __name__ == "__main__":
    run(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 3)
