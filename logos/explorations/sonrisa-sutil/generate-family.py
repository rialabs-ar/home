#!/usr/bin/env python3
"""
Genera la familia completa de logos 'sonrisa sutil' para RIA Labs.

3 niveles de sonrisa (10%, 15%, 20%)
× 3 tipologías (isotipo, lockup horizontal, lockup vertical)
× 4 flavors (color, blanco, negro, outline)
= 36 SVGs.

Todas las variantes preservan el centroide óptico del isotipo
(la luna se corre hacia arriba y la corona hacia abajo por mitades iguales).

Reference geometry (viewBox 120×120):
  - centro: (60, 60)
  - corona: 6 anillos concéntricos r=52..44 · stroke-widths 22..1.2
  - luna:   disco r=38
  - Δ por nivel: 10%→4px, 15%→6px, 20%→8px (como % del radio de la luna)

Para canvas 100×100 (isotipo oficial): scale = 100/120
Para lockup horizontal (640×180): eclipse en (100, 90), escala manual
Para lockup vertical (320×440): eclipse en (160, 140), escala manual
"""
import os
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "family"
OUT.mkdir(exist_ok=True)

# Δ en escala 120 (radio luna=38)
LEVELS = {
    10: 4,
    15: 6,
    20: 8,
}

# ==============================================================
# COLOR palette · eclipse cálido sobre fondo oscuro
# ==============================================================
COLOR_RINGS = [
    # (r, stroke, stroke-width, opacity)
    (52, "#1a0900", 22,   0.55),
    (50, "#2a1200", 14,   0.42),
    (48, "#3d1c00",  9,   0.32),
    (46, "#633806",  5,   0.24),
    (45, "#854F0B",  2.5, 0.18),
    (44, "#BA7517",  1.2, 0.13),
]
COLOR_INNER_DISC = ("#1c1810", 38)   # warm inner base
COLOR_MOON = ("#0b0a14", 38)
COLOR_RIA  = "#f0ece0"
COLOR_LABS = "#EF9F27"

# ==============================================================
# BLANCO · para uso sobre fondo oscuro (asume bg ~ #0a0814)
# ==============================================================
BLANCO_RINGS = [
    (50, "#ffffff",  6, 0.08),   # atmósfera difusa
    (46, "#ffffff",  3, 0.18),   # halo medio
    (44, "#ffffff", 4.5, 0.95),  # anillo principal
    (40, "#ffffff", 0.6, 0.5),   # pista interna
]
BLANCO_MOON = ("#0a0814", 38)   # dark bg color to cut the ring (smile visible)
BLANCO_RIA  = "#f0ece0"
BLANCO_LABS = "#f0ece0"

# ==============================================================
# NEGRO · para uso sobre fondo claro (asume bg ~ #ffffff)
# ==============================================================
NEGRO_RINGS = [
    (50, "#000000",  6, 0.08),
    (46, "#000000",  3, 0.18),
    (44, "#000000", 4.5, 0.95),
    (40, "#000000", 0.6, 0.5),
]
NEGRO_MOON = ("#ffffff", 38)
NEGRO_RIA  = "#000000"
NEGRO_LABS = "#000000"

# ==============================================================
# OUTLINE · line-art monocromático (currentColor)
# ==============================================================
OUTLINE_RINGS = [
    (44, "currentColor", 1.5, 1.0),
]
OUTLINE_MOON = ("none", 38)   # fill="none", stroke currentColor
OUTLINE_RIA  = "currentColor"
OUTLINE_LABS = "currentColor"


FLAVORS = {
    "color":   {"rings": COLOR_RINGS,   "inner": COLOR_INNER_DISC, "moon": COLOR_MOON,   "ria": COLOR_RIA,   "labs": COLOR_LABS,   "ria_weight": 500, "labs_weight": 300},
    "blanco":  {"rings": BLANCO_RINGS,  "inner": None,             "moon": BLANCO_MOON,  "ria": BLANCO_RIA,  "labs": BLANCO_LABS,  "ria_weight": 500, "labs_weight": 300},
    "negro":   {"rings": NEGRO_RINGS,   "inner": None,             "moon": NEGRO_MOON,   "ria": NEGRO_RIA,   "labs": NEGRO_LABS,   "ria_weight": 500, "labs_weight": 300},
    "outline": {"rings": OUTLINE_RINGS, "inner": None,             "moon": OUTLINE_MOON, "ria": OUTLINE_RIA, "labs": OUTLINE_LABS, "ria_weight": 500, "labs_weight": 300, "outline": True},
}


def scale_rings(rings, s):
    """Escala radios y anchos por factor s (manteniendo colores y opacidades)."""
    return [(r * s, c, w * s, o) for (r, c, w, o) in rings]


def eclipse_svg(cx, cy, delta, flavor, scale=1.0):
    """
    Devuelve el SVG del eclipse (sin wrapper) centrado en (cx, cy).
    delta: valor de Δ en unidades originales (escala 120).
    scale: factor de escala sobre la geometría base (r y sw).
    """
    flavor_cfg = FLAVORS[flavor]
    rings = scale_rings(flavor_cfg["rings"], scale)
    corona_cy = cy + (delta * scale) / 2
    moon_cy   = cy - (delta * scale) / 2

    parts = []
    for (r, stroke, sw, op) in rings:
        parts.append(
            f'<circle cx="{cx}" cy="{corona_cy:g}" r="{r:g}" fill="none" '
            f'stroke="{stroke}" stroke-width="{sw:g}" opacity="{op:g}"/>'
        )

    # inner disc (solo color)
    if flavor_cfg["inner"]:
        inner_color, inner_r = flavor_cfg["inner"]
        parts.append(
            f'<circle cx="{cx}" cy="{corona_cy:g}" r="{inner_r * scale:g}" fill="{inner_color}"/>'
        )

    # moon
    moon_fill, moon_r = flavor_cfg["moon"]
    if flavor == "outline":
        # luna como outline, no fill
        parts.append(
            f'<circle cx="{cx}" cy="{moon_cy:g}" r="{moon_r * scale:g}" fill="none" '
            f'stroke="currentColor" stroke-width="{1.5 * scale:g}"/>'
        )
    else:
        parts.append(
            f'<circle cx="{cx}" cy="{moon_cy:g}" r="{moon_r * scale:g}" fill="{moon_fill}"/>'
        )

    return "\n  ".join(parts)


# ==============================================================
# ISOTIPO · viewBox 120×120 (espejo del canvas de exploración)
# ==============================================================
def isotipo(level_pct, flavor):
    delta = LEVELS[level_pct]
    eclipse = eclipse_svg(cx=60, cy=60, delta=delta, flavor=flavor, scale=1.0)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <!-- RIA Labs · isotipo · sonrisa {level_pct}% · {flavor} · Δ={delta} · centroide (60,60) -->
  {eclipse}
</svg>
'''


# ==============================================================
# LOCKUP HORIZONTAL · viewBox 640×180 · eclipse izquierda + wordmark derecha
# ==============================================================
def lockup_horizontal(level_pct, flavor):
    delta = LEVELS[level_pct]
    # eclipse escalado a ~r_outer=68 → scale = 68/52 ≈ 1.31
    # pero queremos mantener la proporción del isotipo 120; escalamos a r=52*scale=~68
    scale = 68 / 52
    cx = 100
    cy = 90
    eclipse = eclipse_svg(cx=cx, cy=cy, delta=delta, flavor=flavor, scale=scale)

    cfg = FLAVORS[flavor]
    ria_fill  = cfg["ria"]
    labs_fill = cfg["labs"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 180" width="640" height="180">
  <defs>
    <style>
      .ria-h  {{ font-family: 'Saira', 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 118px; letter-spacing: 9px; fill: {ria_fill}; }}
      .labs-h {{ font-family: 'Saira', 'Helvetica Neue', Arial, sans-serif; font-weight: 300; font-size: 50px;  letter-spacing: 4px; fill: {labs_fill}; }}
    </style>
  </defs>

  <!-- Eclipse · sonrisa {level_pct}% · {flavor} · Δ={delta} -->
  {eclipse}

  <!-- Wordmark -->
  <text class="ria-h"  x="200" y="128">RIA</text>
  <text class="labs-h" x="478" y="92">Labs</text>
</svg>
'''


# ==============================================================
# LOCKUP VERTICAL · viewBox 320×440 · eclipse arriba, wordmark abajo
# ==============================================================
def lockup_vertical(level_pct, flavor):
    delta = LEVELS[level_pct]
    # eclipse escalado a ~r_outer=72 → scale = 72/52 ≈ 1.385
    scale = 72 / 52
    cx = 160
    cy = 140
    eclipse = eclipse_svg(cx=cx, cy=cy, delta=delta, flavor=flavor, scale=scale)

    cfg = FLAVORS[flavor]
    ria_fill  = cfg["ria"]
    labs_fill = cfg["labs"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 440" width="320" height="440">
  <defs>
    <style>
      .ria-v  {{ font-family: 'Saira', 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 128px; letter-spacing: 10px; fill: {ria_fill}; }}
      .labs-v {{ font-family: 'Saira', 'Helvetica Neue', Arial, sans-serif; font-weight: 300; font-size: 54px;  letter-spacing: 5px;  fill: {labs_fill}; }}
    </style>
  </defs>

  <!-- Eclipse · sonrisa {level_pct}% · {flavor} · Δ={delta} -->
  {eclipse}

  <!-- Wordmark -->
  <text class="ria-v"  x="160" y="316" text-anchor="middle">RIA</text>
  <text class="labs-v" x="160" y="386" text-anchor="middle">Labs</text>
</svg>
'''


# ==============================================================
# Generación
# ==============================================================
def main():
    count = 0
    for level_pct in LEVELS.keys():
        for flavor in FLAVORS.keys():
            # Isotipo
            path = OUT / f"iso-sonrisa-{level_pct}-{flavor}.svg"
            path.write_text(isotipo(level_pct, flavor))
            print(f"  ✓ {path.name}")
            count += 1

            # Lockup horizontal
            path = OUT / f"lockup-h-sonrisa-{level_pct}-{flavor}.svg"
            path.write_text(lockup_horizontal(level_pct, flavor))
            print(f"  ✓ {path.name}")
            count += 1

            # Lockup vertical
            path = OUT / f"lockup-v-sonrisa-{level_pct}-{flavor}.svg"
            path.write_text(lockup_vertical(level_pct, flavor))
            print(f"  ✓ {path.name}")
            count += 1

    print(f"\nListo. {count} SVGs generados en {OUT}/")


if __name__ == "__main__":
    main()
