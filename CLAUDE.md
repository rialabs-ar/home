# Instrucciones del proyecto RIA Labs

## Mantenimiento de `CONTENIDO.md`

`CONTENIDO.md` es la **síntesis viva** del contenido institucional del proyecto
(identidad de marca, textos del sitio, assets, estructura de prototipos v1–v4, etc.).

**Regla:** cada vez que cambies algo que impacte en ese inventario, actualizá `CONTENIDO.md`
en el mismo commit o en un commit inmediatamente posterior. No lo dejes desincronizado.

Cambios que **sí** requieren actualizar `CONTENIDO.md`:

- Textos visibles del sitio (headings, copy, taglines, secciones, CTAs).
- Datos de contacto, dominios, emails, redes sociales.
- Metadata / SEO (title, description, Open Graph, Twitter Card).
- Estructura de navegación o aparición/desaparición de secciones.
- Alta, baja o renombre de assets de marca (logos, favicons, imágenes OG).
- Cambio de versión vigente del sitio (ej: si el redirect deja de apuntar a `v4/`).
- Nuevos prototipos (v5, v6…) o deprecación de versiones previas.

Cambios que **no** requieren tocarlo:

- Refactors de CSS/JS sin impacto en contenido visible.
- Ajustes de animación, tipografía o estilo sin cambiar texto.
- Arreglos técnicos (build, deploy, dependencias).

Si no estás seguro de si un cambio aplica, preguntá antes de omitir la actualización.

## Fuente vigente

El contenido visible actual está en [v4/index.html](v4/index.html).
El `_redirects` de Netlify apunta a esa versión; v1–v3 quedan como histórico.
