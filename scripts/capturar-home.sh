#!/bin/zsh
# Fotografía la home v5 completa (desktop 1440 y móvil 390) con Chrome headless.
# Sirve la raíz del repo RIA en un puerto libre 8895-8899 y lo mata por PID al salir.
# QUERY=tema=dia fotografía el tema día (ver "DESENCLIPSAR" en v5/index.html); QUERY=ciclo=4200
# congela el ciclo del eclipse a los 4,2 s. NOMBRE=dia cambia el sufijo de los PNG (v5_dia_d.png).
set -e
RAIZ=${RAIZ:-/Users/tano/dev/RIALabs/Proyectos/RIA}   # con RAIZ=... se fotografía otro checkout (un worktree)
S=${CAPTURAS:-"$(dirname "$0")/capturas"}
VER=${1:-v5}
ALTO=${ALTO:-7800}
Q=${QUERY:+?$QUERY}
N=${VER}${NOMBRE:+_$NOMBRE}
mkdir -p "$S"
PUERTO=""
for pp in 8895 8896 8897 8898 8899; do nc -z 127.0.0.1 $pp >/dev/null 2>&1 || { PUERTO=$pp; break; }; done
[[ -z "$PUERTO" ]] && { echo "sin puerto"; exit 2; }
MIPID=""
limpiar(){ [[ -n "$MIPID" ]] && kill "$MIPID" 2>/dev/null || true; rm -f "$RAIZ/$VER/_preview.html" "$RAIZ/_mob.html"; }
trap limpiar EXIT INT TERM
# preview: hero con alto fijo (100vh en una ventana de 7800 px rompería la composición)
python3 - "$RAIZ/$VER" <<'PY'
import sys
d = sys.argv[1]
src = open(f"{d}/index.html").read()
inj = "<style>.hero{min-height:900px !important}html{scroll-behavior:auto}*,*::before,*::after{animation-delay:0s !important;animation-duration:0.01s !important;transition-duration:0s !important;transition-delay:0s !important}#sistema *,#equipo-orbit *,.df-vis *,.prod-vis *{animation-duration:revert !important}</style></head>"
open(f"{d}/_preview.html","w").write(src.replace("</head>", inj, 1))
PY
cat > "$RAIZ/_mob.html" <<HTML
<style>html,body{margin:0;background:#000}iframe{border:0;width:390px;height:${ALTO}px;display:block;margin:0 auto}</style>
<iframe src="/$VER/_preview.html$Q"></iframe>
HTML
(cd "$RAIZ" && python3 -m http.server $PUERTO --bind 127.0.0.1 >/dev/null 2>&1) &
MIPID=$!
for i in {1..10}; do nc -z 127.0.0.1 $PUERTO >/dev/null 2>&1 && break; sleep .3; done
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
LOG="$S/chrome.log"; : > "$LOG"
"$CH" --headless=new --disable-gpu --hide-scrollbars --window-size=1440,$ALTO \
  --enable-logging=stderr --v=0 --virtual-time-budget=6000 \
  --screenshot="$S/${N}_d.png" "http://127.0.0.1:$PUERTO/$VER/_preview.html$Q" >>"$LOG" 2>&1 || true
"$CH" --headless=new --disable-gpu --hide-scrollbars --window-size=500,$((ALTO+20)) \
  --enable-logging=stderr --v=0 --virtual-time-budget=6000 \
  --screenshot="$S/${N}_m.png" "http://127.0.0.1:$PUERTO/_mob.html" >>"$LOG" 2>&1 || true
if [[ -n "$OG" ]]; then
python3 - "$RAIZ/$VER" <<'PY'
import sys
d = sys.argv[1]
src = open(f"{d}/index.html").read()
inj = "<style>nav,.hero-eyebrow,.hero-ctas,.hero-origin,.hero-sub{display:none !important}.hero{min-height:630px !important;padding:0 24px !important;justify-content:center}#sistema-wrap{max-width:760px}.wordmark{margin-top:-14px}.ria{font-size:76px}.hero-headline{font-size:17px;margin:14px 0 0}*,*::before,*::after{animation-delay:0s !important;animation-duration:0.01s !important;transition-duration:0s !important}#sistema *{animation-duration:revert !important}#cielo{opacity:1}</style></head>"
open(f"{d}/_og.html","w").write(src.replace("</head>", inj, 1))
PY
"$CH" --headless=new --disable-gpu --hide-scrollbars --window-size=1200,630 \
  --enable-logging=stderr --v=0 --virtual-time-budget=6000 \
  --screenshot="$S/og-${VER}.png" "http://127.0.0.1:$PUERTO/$VER/_og.html" >>"$LOG" 2>&1 || true
rm -f "$RAIZ/$VER/_og.html"
fi
grep -i "uncaught\|error" "$LOG" | grep -v "DevTools\|GPU\|gpu\|dbus\|Fontconfig" | head -5 || true
ls -la "$S"/${N}_*.png
