#!/usr/bin/env bash
# build-pngs.sh
# Renderiza SVG de esta carpeta a PNG en png/ a 256/512/1024/2048 px de ancho, con fondo transparente.
#
# Uso:
#   bash logos/build-pngs.sh                       todos los ria-*.svg
#   bash logos/build-pngs.sh ria-anillo-color.svg  sólo esos (rutas relativas a esta carpeta)
#
# Motor: cairosvg si está instalado (pip install cairosvg); si no, Google Chrome headless (macOS), que
# respeta gradientes y currentColor. En los dos casos la tipografía del wordmark y de los lockups sale fiel
# sólo con la fuente Saira instalada (https://fonts.google.com/specimen/Saira); sin ella se usa la primera
# fallback y conviene no commitear esos PNG. Los isotipos (sin texto) son pixel-perfect siempre.
#
# Salida: png/ria-{variante}-{color}-{tamaño}.png

set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT="${DIR}/png"
mkdir -p "${OUT}"
SIZES=(256 512 1024 2048)
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

if [[ $# -gt 0 ]]; then
  SVGS=(); for f in "$@"; do SVGS+=("${DIR}/$(basename "$f")"); done
else
  SVGS=("${DIR}"/ria-*.svg)
fi

if python3 -c "import cairosvg" 2>/dev/null; then
  MOTOR=cairosvg
elif [[ -x "$CHROME" ]]; then
  MOTOR=chrome
else
  echo "Falta cairosvg (pip install cairosvg) o Google Chrome." >&2; exit 1
fi

render_chrome() {   # svg ancho salida — el alto sale del viewBox
  local svg="$1" w="$2" out="$3"
  local vb; vb=$(grep -o 'viewBox="[^"]*"' "$svg" | head -1 | sed 's/viewBox="//;s/"//')
  local vw vh; vw=$(echo "$vb" | awk '{print $3}'); vh=$(echo "$vb" | awk '{print $4}')
  local h; h=$(python3 -c "print(round($w*$vh/$vw))")
  local tmp; tmp=$(mktemp -d)
  cp "$svg" "$tmp/l.svg"
  printf '<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:transparent}img{display:block;width:%spx;height:%spx}</style></head><body><img src="l.svg"></body></html>' "$w" "$h" > "$tmp/l.html"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --default-background-color=00000000 \
    --window-size="$w,$h" --screenshot="$out" "file://$tmp/l.html" >/dev/null 2>&1
  rm -rf "$tmp"
}

for svg in "${SVGS[@]}"; do
  base="$(basename "${svg}" .svg)"
  for s in "${SIZES[@]}"; do
    out="${OUT}/${base}-${s}.png"
    if [[ $MOTOR == cairosvg ]]; then
      python3 -c "import cairosvg; cairosvg.svg2png(url='${svg}', write_to='${out}', output_width=${s})"
    else
      render_chrome "$svg" "$s" "$out"
    fi
    echo "  ✓ ${base}-${s}.png"
  done
done

echo "Listo (${MOTOR}). ${#SIZES[@]} tamaños × ${#SVGS[@]} SVG en ${OUT}/"
