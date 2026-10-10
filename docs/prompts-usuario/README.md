# Prompts de Matías — RIA Labs (home)

Material primordial de este proyecto: las palabras con las que Matías lo pensó y lo pidió, verbatim.
Sirven para configurar las expresiones de comunicación de la home de RIA Labs y son referencia obligada de las
sesiones de marketing y de producto. Regla completa en
`~/dev/RIALabs/Proyectos/.claude/rules/prompts-usuario.md`.

- `REGISTRO-YYYY-MM.md`: todos los prompts, en orden, escritos por el hook
  `~/.claude/hooks/guardar-prompt-usuario.sh` en cada envío. Append-only, no se edita a mano.
- `YYYY-MM-DD-<titulo>.md`: copia con título de los prompts fundacionales o de giro, para
  encontrarlos sin recorrer el registro.

Esta carpeta es el interruptor del hook: si existe, guarda; si no, no toca el proyecto.
