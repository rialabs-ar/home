#!/usr/bin/env bash
# build-pngs.sh
# Renders every ria-*.svg in this folder to PNGs at 256/512/1024/2048 px.
#
# Requisitos:
#   - Python 3 con cairosvg (pip install cairosvg)
#   - Fuente Saira instalada en el sistema (https://fonts.google.com/specimen/Saira).
#     Si Saira no está instalada, cairosvg usará la primera fallback disponible
#     (Helvetica Neue / Arial / sans-serif). Los isotipos no dependen de la fuente.
#
# Uso:
#   bash logos/build-pngs.sh
#
# Salida: archivos png/ria-{variante}-{color}-{size}.png

set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT="${DIR}/png"
mkdir -p "${OUT}"

SIZES=(256 512 1024 2048)

for svg in "${DIR}"/ria-*.svg; do
  base="$(basename "${svg}" .svg)"
  for s in "${SIZES[@]}"; do
    out="${OUT}/${base}-${s}.png"
    python3 -c "import cairosvg; cairosvg.svg2png(url='${svg}', write_to='${out}', output_width=${s})"
    echo "  ✓ ${base}-${s}.png"
  done
done

echo "Listo. ${#SIZES[@]} tamaños × $(ls "${DIR}"/ria-*.svg | wc -l | tr -d ' ') SVGs generados en ${OUT}/"
