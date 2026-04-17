# RIA Labs — Carpeta de logos

Todos los logos de la marca conviven en esta carpeta. La organización se hace por **convención de nombres**, no por subcarpetas, para que sea fácil agregar nuevas variantes en el futuro sin reordenar.

---

## Convención de nombres

```
ria-{variante}-{color}[-{tamaño}].{ext}
```

| Segmento | Valores actuales | Significado |
|----------|------------------|-------------|
| `variante` | `isotipo`, `wordmark`, `lockup-vertical`, `lockup-horizontal` | Tipo de construcción |
| `color` | `color`, `blanco`, `negro`, `outline` | Versión cromática |
| `tamaño` | `256`, `512`, `1024`, `2048` | Solo PNG — ancho en px |
| `ext` | `svg`, `png` | Formato |

Ejemplos válidos:

- `ria-isotipo-color.svg` — el eclipse full color en vector
- `ria-isotipo-blanco-512.png` — el eclipse en blanco, 512 px
- `ria-lockup-horizontal-negro.svg` — lockup horizontal en negro, vector
- `ria-wordmark-outline-2048.png` — wordmark solo contornos, 2048 px

---

## Variantes

### 1. Isotipo (`isotipo`)
El símbolo del eclipse aislado, sin tipografía. Usar para:
- Favicon / app icons
- Avatar de redes sociales
- Marca de agua o sello pequeño
- Cualquier contexto donde ya se identifica la marca textualmente

### 2. Wordmark (`wordmark`)
Solo la tipografía "RIA Labs", sin el símbolo. Usar para:
- Headers en documentos donde el eclipse distrae
- Firmas de email
- Contextos muy horizontales y ajustados

### 3. Lockup vertical (`lockup-vertical`)
Eclipse arriba + RIA + Labs abajo — el bloque tal como aparece en el hero del sitio. Usar para:
- Hero de landings, portadas de presentaciones
- Stickers, merchandising
- Cuando hay espacio vertical disponible

### 4. Lockup horizontal (`lockup-horizontal`)
Eclipse a la izquierda + "RIA Labs" a la derecha. Usar para:
- Navbars, headers de documento
- Firmas de email y membretes
- Cualquier barra horizontal

---

## Versiones de color

| Versión | Uso |
|---------|-----|
| `color` | Versión principal de marca: dorado (#EF9F27 / #c8860a) sobre fondo oscuro o transparente |
| `blanco` | Monocromo blanco — para fondos oscuros cuando no puede ir dorado (videos, fotos de fondo) |
| `negro` | Monocromo negro — para fondos claros, impresión, membretes, documentos formales |
| `outline` | Solo contornos — para marcas de agua, grabados, bordados, impresión monocromática mínima |

---

## Paleta oficial (referencia rápida)

| Nombre | Hex | Uso |
|--------|-----|-----|
| Gold highlight | `#EF9F27` | Acento principal del eclipse, CTAs |
| Gold base | `#c8860a` | Anillo del eclipse, líneas de marca |
| Gold deep | `#7a5008` | Halos profundos del eclipse |
| Moon dark | `#07060f` | Disco lunar, fondo oscuro principal |
| Blanco cálido | `#f0ece0` | Texto sobre fondo oscuro |
| Negro puro | `#000000` | Versión negra del logo |

---

## Ampliar en el futuro

Para agregar nuevas categorías sin romper la convención, simplemente se extiende el diccionario de segmentos. Ideas futuras:

- Nuevas variantes: `tagline` (lockup + "Software e IA"), `badge` (eclipse en círculo), `animated` (versiones con animación SVG).
- Nuevos colores: `dorado-sobre-blanco`, `azul` (color Byte), `gris`, `duotono`.
- Nuevos formatos: `.pdf`, `.eps`, `.ai`.
- Nuevos tamaños PNG: `128`, `4096`.

Ejemplo de extensión:
```
ria-tagline-color.svg
ria-badge-outline-1024.png
ria-lockup-horizontal-azul.svg
```

---

## Fuente de generación

Los SVGs fueron creados a partir de:
- El eclipse base del sitio (`/favicon.svg` y `/assets/ria-labs-eclipse-icon.svg`)
- La tipografía **Saira** (Google Fonts, pesos 300/500) usada en el hero del sitio vigente (v4)

Los PNGs se renderizan desde los SVG con `cairosvg`. Regenerar con el script `build-pngs.sh` incluido en esta carpeta:

```bash
pip install cairosvg
bash logos/build-pngs.sh
```

### ⚠ Nota sobre la tipografía en los PNG actuales

Los PNG que están hoy en `logos/png/` fueron generados en un entorno sin la fuente **Saira** instalada, por lo que usaron la primera fallback disponible (Liberation Sans / DejaVu Sans). La forma geométrica del eclipse es idéntica, pero la tipografía del wordmark y los lockups difiere ligeramente de Saira.

**Para PNG con fidelidad de marca total:** instalar Saira desde https://fonts.google.com/specimen/Saira en el sistema y volver a ejecutar `build-pngs.sh`. Los SVG ya referencian `'Saira'` como primera opción, así que una vez instalada la fuente los render son fieles al diseño.

Los isotipos (`ria-isotipo-*.png`) no tienen texto, así que son pixel-perfect siempre.

---

## Estructura final

```
logos/
├── README.md                       ← este archivo
├── build-pngs.sh                   ← script para regenerar los PNG
├── ria-isotipo-color.svg
├── ria-isotipo-blanco.svg
├── ria-isotipo-negro.svg
├── ria-isotipo-outline.svg
├── ria-wordmark-color.svg
├── ria-wordmark-blanco.svg
├── ria-wordmark-negro.svg
├── ria-wordmark-outline.svg
├── ria-lockup-vertical-color.svg
├── ria-lockup-vertical-blanco.svg
├── ria-lockup-vertical-negro.svg
├── ria-lockup-vertical-outline.svg
├── ria-lockup-horizontal-color.svg
├── ria-lockup-horizontal-blanco.svg
├── ria-lockup-horizontal-negro.svg
├── ria-lockup-horizontal-outline.svg
└── png/                            ← PNG renderizados (4 tamaños × 16 SVG = 64 archivos)
    ├── ria-isotipo-color-256.png
    ├── ria-isotipo-color-512.png
    ├── ria-isotipo-color-1024.png
    ├── ria-isotipo-color-2048.png
    └── ... (todas las combinaciones)
```

**Totales:** 16 SVG + 64 PNG = 80 archivos de logo.
