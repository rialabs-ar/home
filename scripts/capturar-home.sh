#!/bin/zsh
# Fotografía la home v5 completa (desktop 1440 y móvil 390) con Chrome headless.
# Sirve la raíz del repo RIA en un puerto libre 8895-8899 y lo mata por PID al salir.
# QUERY=tema=dia fotografía el tema día (ver "DESENCLIPSAR" en v5/index.html); QUERY=ciclo=4200
# congela el ciclo del eclipse a los 4,2 s; QUERY=estrella=1000 fija la estrella de luz del hero en su pico y
# QUERY=estrella=no la apaga (sin QUERY, Chrome fotografía a los ~6 s virtuales y la primera estrella, que sale a
# los 4,5 s, aparece apagándose). La QUERY también aplica a la tarjeta OG. NOMBRE=dia cambia el sufijo (v5_dia_d.png).
# El modo OG (OG=1) esconde la máquina y apila eclipse · RIA LABS · la frase, en cualquier encuadre del hero (?hero=).
# PANTALLA=1 fotografía UNA pantalla real, sin inyectar el alto fijo del hero: ANCHO×ALTO (ANCHO=1440 por defecto).
# Con ANCHO≤500 va por el iframe del celular (del ancho y el alto pedidos) y recorta la captura a ese cuadro.
# Sale una sola captura, ${N}_p<ancho>x<alto>.png: sirve para ver qué entra sin scrollear.
set -e
RAIZ=${RAIZ:-/Users/tano/dev/RIALabs/Proyectos/RIA}   # con RAIZ=... se fotografía otro checkout (un worktree)
S=${CAPTURAS:-"$(dirname "$0")/capturas"}
VER=${1:-v5}
ALTO=${ALTO:-11600}   # la página mide ~11.100 px en desktop desde el 13/10 (Dataflow como onda); móvil necesita más: pasar ALTO=16000
Q=${QUERY:+?$QUERY}
N=${VER}${NOMBRE:+_$NOMBRE}
mkdir -p "$S"
PUERTO=""
for pp in 8895 8896 8897 8898 8899; do nc -z 127.0.0.1 $pp >/dev/null 2>&1 || { PUERTO=$pp; break; }; done
[[ -z "$PUERTO" ]] && { echo "sin puerto"; exit 2; }
MIPID=""
limpiar(){ [[ -n "$MIPID" ]] && kill "$MIPID" 2>/dev/null || true; rm -f "$RAIZ/$VER/_preview.html" "$RAIZ/_mob.html"; }
trap limpiar EXIT INT TERM
# preview: hero con alto fijo (100svh en una ventana de 11.600 px rompería la composición; con PANTALLA=1, no)
python3 - "$RAIZ/$VER" <<'PY'
import sys
d = sys.argv[1]
src = open(f"{d}/index.html").read()
import os
alto = "" if os.environ.get("PANTALLA") else ".hero{min-height:900px !important;height:900px !important}"
inj = "<style>" + alto + "html{scroll-behavior:auto}*,*::before,*::after{animation-delay:0s !important;animation-duration:0.01s !important;transition-duration:0s !important;transition-delay:0s !important}#sistema *,#equipo-orbit *,.df-vis *,.prod-vis *{animation-duration:revert !important}</style></head>"
open(f"{d}/_preview.html","w").write(src.replace("</head>", inj, 1))
PY
ANCHO=${ANCHO:-1440}
MW=390; [[ -n "$PANTALLA" && $ANCHO -le 500 ]] && MW=$ANCHO
cat > "$RAIZ/_mob.html" <<HTML
<style>html,body{margin:0;background:#000;overflow:hidden}iframe{border:0;width:${MW}px;height:${ALTO}px;display:block;margin:0 auto}</style>
<iframe src="/$VER/_preview.html$Q"></iframe>
HTML
(cd "$RAIZ" && exec python3 -m http.server $PUERTO --bind 127.0.0.1 >/dev/null 2>&1) &   # exec: el PID es el del servidor, y limpiar() lo mata
MIPID=$!
for i in {1..10}; do nc -z 127.0.0.1 $PUERTO >/dev/null 2>&1 && break; sleep .3; done
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
LOG="$S/chrome.log"; : > "$LOG"
if [[ -n "$PANTALLA" ]]; then
  OUT="$S/${N}_p${ANCHO}x${ALTO}.png"
  # Chrome headless a veces se cuelga esperando (sin CPU): un perro guardián lo mata a los 45 s
  # RM=1 fotografía con prefers-reduced-motion
  foto(){ "$CH" --headless=new --disable-gpu --hide-scrollbars --window-size=$1 --enable-logging=stderr --v=0 ${RM:+--force-prefers-reduced-motion} \
      --virtual-time-budget=${VT:-6000} --screenshot="$OUT" "$2" >>"$LOG" 2>&1 &
    local cp=$! n=0; while kill -0 $cp 2>/dev/null && (( n < 90 )); do sleep 0.5; n=$((n+1)); done
    kill -0 $cp 2>/dev/null && { kill $cp 2>/dev/null; echo "Chrome colgado: reintentar"; } || true; }
  rm -f "$OUT"
  if [[ $ANCHO -le 500 ]]; then
    foto 500,$ALTO "http://127.0.0.1:$PUERTO/_mob.html"
    [[ -f "$OUT" ]] && python3 -c 'import sys; from PIL import Image; f,w,h=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]); im=Image.open(f); x=(im.size[0]-w)//2; im.crop((x,0,x+w,h)).save(f)' "$OUT" $ANCHO $ALTO
  else
    foto $ANCHO,$ALTO "http://127.0.0.1:$PUERTO/$VER/_preview.html$Q"
  fi
  grep -i "uncaught\|error" "$LOG" | grep -v "DevTools\|GPU\|gpu\|dbus\|Fontconfig" | head -5 || true
  ls -la "$OUT" 2>/dev/null || true
  exit 0
fi
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
inj = "<style>nav,.hero-eyebrow,.hero-ctas,.hero-origin,.hero-sub,.hero-cita,#sis-hint,#maquina{display:none !important}.maq-pie{margin-top:18px !important}.maq-t1,.maq-t2{opacity:1 !important;transform:none !important;font-size:20px !important}.hero{height:630px !important;min-height:630px !important;padding:0 24px !important;justify-content:center !important}.hero-escena{display:flex !important;flex:0 0 auto !important;flex-direction:column;align-items:center;margin:0 !important}#sistema-wrap{width:320px !important;height:auto !important;margin:0 !important;top:0 !important}.wordmark{margin-top:16px !important}.ria{font-size:76px !important}.labs{font-size:17px !important}*,*::before,*::after{animation-delay:0s !important;animation-duration:0.01s !important;transition-duration:0s !important}#sistema *{animation-duration:revert !important}#cielo{opacity:1}</style></head>"
open(f"{d}/_og.html","w").write(src.replace("</head>", inj, 1))
PY
"$CH" --headless=new --disable-gpu --hide-scrollbars --window-size=1200,630 \
  --enable-logging=stderr --v=0 --virtual-time-budget=6000 \
  --screenshot="$S/og-${VER}.png" "http://127.0.0.1:$PUERTO/$VER/_og.html$Q" >>"$LOG" 2>&1 || true
rm -f "$RAIZ/$VER/_og.html"
fi
grep -i "uncaught\|error" "$LOG" | grep -v "DevTools\|GPU\|gpu\|dbus\|Fontconfig" | head -5 || true
ls -la "$S"/${N}_*.png
