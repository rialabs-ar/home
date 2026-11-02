# RIA Labs — Contenido del proyecto organizado por tipo de elemento

> Síntesis y categorización de todo el material institucional presente en la carpeta RIA
> (home web, prototipos v1–v4, assets, favicons y configuración).
> Fuente principal de contenido vigente: `v5/index.html` (el redirect de Netlify apunta ahí desde el 2026-10-10).
> Lo que sigue describe v4 y anteriores salvo donde se indica; **la v5 está resumida en §0**, al principio,
> porque es la que está publicada. Fecha de consolidación original: 2026-04-16.

---

## 0. v5 (vigente desde 2026-10-10) — tres verticales, el eclipse al centro, Dataflow como motor

> Prompts de giro, verbatim: `docs/prompts-usuario/2026-10-10-upgrade-home-tres-verticales.md` (la v5) y
> `docs/prompts-usuario/2026-10-10-sin-orbitas-verticales-tecnologicas.md` (el mismo día: fuera las órbitas
> del hero, los productos como verticales tecnológicas). Lo que sigue es lo curado. Mismo estilo que v4 (Saira + DM Mono, paleta medianoche + dorado, ruido, reveals), misma
> página única sin build; v4 queda como histórico en `v4/`.

### 0.1 Qué cambió y por qué

- **Productos: sin definición, en otro orden, Automotrices y las presentaciones a la vista (rama `productos`,
  2026-11-01).** Prompt de giro verbatim en `docs/prompts-usuario/2026-11-01-home-en-paginas-y-oficina-rosario.md`:
  *«sacar la definición etimologica de la palabra, eso no debe estar, y tambien cambiar el orden […] primero deberia estar
  SmartCity y luego Analítico, despues automocion, aunque Automocion no es un nombre que nos resuene mucho, probemos RIA
  Automotrices. En estas descripciones de productos tenemos que poner los links a las presentaciones»*, y del borrador:
  *«DAR más protagonismo a Brid Map»*. Corrección posterior de Matías: smartcity.rialabs.ar va (se olvidó de nombrarla),
  **Jockey no**. Esta entrada reemplaza, para la banda de productos, la tabla «Tres verticales, una palabra cada una» y la
  de satélites que siguen más abajo (quedan como historia).
  **Qué cambió.** (1) *Sin definición de diccionario*: fuera los tres `.prod-def` y su CSS. La intro dice ahora «Cada
  producto es una forma distinta del mismo motor, **Dataflow**: lee la realidad con las cámaras y los sensores que ya están,
  la comprende y actúa. **Cada uno con sus presentaciones, para verlo funcionar.**»; **«Un solo motor.»** del título y
  **«Dataflow»** enlazan a `/dataflow/` (el título con un filo dorado debajo, sin cambiar de color). (2) *Orden*: **01
  Smartcity** (astro a la izquierda) · **02 Analítico** (`.inv`, astro a la derecha) · **03 Automotrices** (izquierda). Los
  rótulos: «01 · Ciudad y espacios» (era «02 · Ciudad y predio»: sin Jockey no hay predio), «02 · Seguridad», «03 ·
  Concesionarias». (3) *RIA Automoción → **RIA Automotrices***: nombre, id **`#automotrices`** (la nav ya apuntaba ahí) con
  **`#automocion` como ancla vieja** (un `<span class="ancla-vieja">` absoluto al tope del bloque: cae en el mismo píxel,
  medido), aria-labels del astro y del satélite, `description`/`og:description`/`twitter:description` (que además van en el
  orden nuevo: «RIA Smartcity, RIA Analítico y RIA Automotrices»), la constelación de la máquina del hero en los encuadres
  1–3 (`PROD`: «AUTOMOTRICES» entra sin pisarse en 1440 y 390, capturado con `?hero=1`) y los comentarios. **Sale «antes RIA
  Drivecore»**: Drivecore sigue vivo como el nombre del sistema y de su presentación, y así aparece ahora en la lista
  («Drivecore — el sistema operativo de la concesionaria»); la línea contaba un nombre viejo del producto, y con el nombre
  nuevo confundía (¿cuál es cuál?). El «RIA Automoción» de Laboratorio no se tocó: lo mueve la rama de `/laboratorio/`.
  (4) *«en castellano» → «en tu idioma»*: Monitoreo («búsqueda forense en tu idioma») y Gerencia («conversá con tus números
  en tu idioma, sobre lo que pasó de verdad»); el «en español» estaba en la definición de Smartcity y se fue con ella. Queda
  un «en castellano» en Laboratorio, para esa rama. (5) *Las presentaciones*: bajo los sabores de cada producto, «Las
  presentaciones» — una fila por enlace con qué es, de qué se trata y su dirección con ↗ (todas `target="_blank"
  rel="noopener"`); el botón suelto `prod-link` de cada producto desaparece (su CSS también; la regla de transición de tema
  de la línea 116 cambia `.prod-link` por `.prod-pres a, .prod-dest`). Leídas el 01/11 a la noche, todas responden 200.
  **Corregido el 02/11 (Matías: «los links a las presentaciones no puede ser una lista diferente, los links tienen que
  estar en la misma lista en la que se listan los diferentes subproductos»):** la lista aparte se fue (`.prod-pres*`). Cada
  sabor que tiene presentación termina, en su mismo ítem, con su dirección y ↗ (`.pi-link`): Ciudad, Centros comerciales,
  Country, Reciclaje, Integradores y Monitoreo. La presentación de todo el producto (analitico.rialabs.ar,
  drivecore.rialabs.ar) volvió al pie como `prod-link`, al lado del estado; Bird Map sigue en su tarjeta destacada. 
  **Y el 02/11, más tarde:** Centros comerciales y Country dejaron de apuntar a Grit; ahora van a sus sitios nuevos,
  **https://shopping.rialabs.ar/** («RIA Shopping — Lo que el centro comercial sabe de sí mismo») y
  **https://country.rialabs.ar/** («RIA Country — Un día en el barrio»), en el ítem de la lista y en el satélite.
  **Y el 02/11 también:** se sumó **Estaciones de servicio**, con su sitio **https://station.rialabs.ar/** («RIA Station —
  Del surtidor a la caja, cada minuto cuenta»), como ítem de la lista de Smartcity después de Country, y en la línea de
  sabores del linaje de `/laboratorio/`. Satélite no tiene: el astro ya lleva seis y con siete las etiquetas se pisan. Los dos
  responden 200 desde el box (64.176.19.100); esa noche el DNS todavía se propagaba: algún resolver no encontraba
  `shopping` y otro todavía mandaba `country` al Netlify viejo (`country-rialabs`, una página del Jockey).
  **Y el 02/11 a la noche:** el ítem **Acceso** («control de ingreso de un mercado concentrador o de un barrio») pasó a
  ser **Checkpoint**, con su sitio **https://checkpoint.rialabs.ar/** (RIA Checkpoint, el control de acceso y aforo que
  se armó en `../ria-access` como «RIA Access» y Matías renombró ese día: `../ria-access/docs/prompts-usuario/2026-11-02-nombre-checkpoint.md`).
  Es el mismo producto con nombre propio, así que reemplaza a Acceso en su lugar en vez de sumarse al lado. El texto sale
  de su guion: «Quién entra. Quién está. Quién salió.» y «La cámara reconoce; la persona decide.»; nunca «no se
  identifica». También en el linaje de `/laboratorio/`. Sin satélite, por lo mismo que Station. La
  tabla de abajo queda como registro de qué dice cada página:

  | Producto | Rótulo en la home | Enlace | Qué dice la página (el 01/11) |
  |---|---|---|---|
  | Smartcity | **Bird Map** · fauna urbana (destacado) | birdmap.rialabs.ar | «RIA Bird Map — Sensores urbanos»: conteo de fauna urbana por visión sobre una cámara IP común, guarda números y nunca imágenes, serie por hora y por plaza; «un módulo más» de Smartcity |
  | Smartcity | **Ciudad** · las cámaras de una ciudad, convertidas en sensores | smartcity.rialabs.ar | «RIA Smartcity — Cinco verticales sobre las cámaras que ya están»: movilidad, seguridad vial, espacio público, estacionamiento y ambiente, en un equipo del tamaño de un módem; multilingüe |
  | Smartcity | **Centros comerciales** · un sábado medido, de la playa al tablero | grit.rialabs.ar/neander/ | Hoy «Grit IA · Neander — Un sábado en el centro comercial» (Villa Amelia): playa con patente sin barrera, tráfico y conversión por local, cruce entre locales, eventos, incidentes, tablero. Se transforma hoy en la de Centros comerciales: rotulada por lo que va a ser |
  | Smartcity | **Country** · un día en el barrio, sin una sala de monitoreo | grit.rialabs.ar/sapiens/ | Hoy «Grit IA · Sapiens — Un día en el barrio» (barrio cerrado, Álvarez): actas, la patente es la llave, patrulla virtual, avisos, perímetro. Se transforma hoy en Country |
  | Smartcity | **Eco Aceite** · reciclaje: la trazabilidad del aceite usado | ecoaceite.byt.ar | «Eco Aceite · Trazabilidad 360° — con tecnología RIA Labs»: cada litro de aceite vegetal usado del bidón al biodiésel, firma digital en el retiro, certificados verificables; cooperativa de Rosario, proyecto presentado al Programa Kit 4.0 |
  | Analítico | **Analítico** · un producto, dos brazos: la puerta a las dos películas | analitico.rialabs.ar | «Byte Analítico — monitoreo inteligente»: un concepto, dos brazos, con enlace a cada película |
  | Analítico | **Integradores** · de la cámara a la central | analitico.rialabs.ar/integradores | «Byte Analítico Integradores — de la cámara a la central»: cualquier cámara, cualquier evento, con evidencia |
  | Analítico | **Monitoreo** · ver ahora y volver atrás: la consola, vista por vista | analitico.rialabs.ar/monitoreo | «Byte Analítico Monitoreo — ver ahora, volver atrás»: la consola al lado de la central, vista por vista |
  | Automotrices | **Drivecore** · el sistema operativo de la concesionaria, área por área | drivecore.rialabs.ar | «RIA Drivecore · El sistema operativo de la concesionaria»: toda la concesionaria en un solo sistema vivo, en producción real |

  jockey.rialabs.ar también responde, pero **no está** (pedido de Matías). (6) ***Bird Map, protagonista***: dentro de
  Smartcity, entre el lead y los sabores, una **tarjeta-enlace propia** (`.prod-dest`): borde y fondo teñidos del color de
  Smartcity, un dibujo chico animado —tres aves que aletean, dos palomas en la plaza y las cajas de la detección que se
  encienden de a una, como contándolas; quieto con reduced-motion— y «Bird Map · fauna urbana / Una cámara que mira una
  plaza y cuenta las aves. / Analiza el video en el lugar y guarda números, nunca imágenes: la serie por hora y por plaza
  con la que una ciudad decide cuándo intervenir. / Ver la presentación · birdmap.rialabs.ar ↗». En el astro es **el
  satélite más grande** (radio 8,5, el de Drivecore), con la etiqueta siempre entera y un anillo tenue; y **es el que está
  delante cuando se llega a la sección** (los primeros 12 s de reloj). No se repite en la lista de abajo: la tarjeta es su
  enlace. La cifra «−40 %» de su presentación no se trajo a la home: no queda claro de qué medición sale. (7) *Smartcity, los
  sabores*: los ítems son **Entrypoint** (acortado a su primera frase, la del prompt del 26/10), **Ciudad** (con las cinco
  verticales de su presentación), **Centros comerciales**, **Country**, **Acceso** (igual que antes) y **Reciclaje** («cada
  litro de aceite usado, trazado del restaurante al biodiésel. Un caso particular, pero de ciudad: un proyecto en pleno
  desarrollo para empresas de Rosario» — las palabras de Matías). Salen **Predio** (era Jockey) y **Barrio y centro
  comercial** (se abrió en dos). El lead pierde «el club»: «La ciudad, el barrio o el centro comercial, medidos con las
  cámaras que ya tienen…». El estado: **«Midiendo 24/7 · municipio y mercado en Rosario»** (sin el club; se lee natural).
  **Satélites (seis)**: Ciudad · municipios → smartcity.rialabs.ar; **Bird Map · fauna urbana** → birdmap; **Centros
  comerciales · la playa y los locales** → grit/neander; **Country · barrios** → grit/sapiens; **Eco Aceite · reciclaje** →
  ecoaceite.byt.ar; Entrypoint · la puerta de entrada (mudo, sin web). **Acceso deja de ser satélite** (no tiene web y eran
  siete): sigue en la lista de sabores. Las órbitas se eligieron con una simulación de las etiquetas (misma matemática que el
  script, 300 s de reloj): con las dos de adelante a la vista, se pisan el **23 %** del tiempo contra el **35 %** de los cinco
  satélites de antes, y **nada en los primeros 15 s**. Además, la etiqueta de un satélite que pasa por detrás del astro baja
  a 0,28 de opacidad (vuelve al hover), y la etiqueta deja de ir de costado si se saldría más de 20 unidades del cuadro
  (centrada debajo): en 390, «CENTROS COMERCIALES» se cortaba contra el borde. (8) *El astro acompaña*: el texto de
  Smartcity mide unas tres veces el astro, así que en desktop (≥861) su viñeta arranca arriba y queda **sticky** a media
  pantalla mientras se lee (`.prod-larga`; `.prod` pasa de `overflow: hidden` a `clip`, que corta igual pero no crea
  contenedor de scroll; `hidden` queda de respaldo para navegadores viejos). Analítico y Automotrices no cambian de
  composición. (9) ***La nav***: medida por iframes del ancho exacto, antes los siete enlaces se partían en dos líneas y
  aplastaban logo y botón **por debajo de ~1045 px** (no sólo entre 861 y 1000). Cambios en el CSS «NAV», para que las
  páginas nuevas los copien: `.nav-links { gap: clamp(16px, 3.2vw - 14px, 32px) }` (era `32px`: 32 en 1440, 27 en 1280,
  18,8 en 1024), `white-space: nowrap` en `.nav-links a`, y un corte nuevo **`@media (min-width: 861px) and (max-width:
  1023px) { .nav-links { display: none } .nav-burger { display: block } .nav-menu { padding-left: 52px; padding-right:
  52px } }`**: entre 861 y 1023 va el MENÚ con «Conversemos» a la vista (≤860 sigue igual que siempre). Medido: una línea
  desde 1024, con 30 px libres a cada lado de los enlaces en 1024, 61 en 1100, 133 en 1280 y 198 en 1440.
  **Verificado:** los `<script>` pasan `node --check`; sin errores de JS (colector en iframe); `#automocion` y
  `#automotrices` a la misma altura (4156 px en 1440); capturas en `_capturas/productos/` (ignorado): los tres productos en
  1440×900 y 390×844, Smartcity entero en 1440×1500 y 390×2300, Smartcity de día y a t=15 s y 40 s, la nav en 861/1024/1280/
  1440 × 700 y la máquina del hero 1 en 1440 y 390. **Pendiente / para Matías:** (a) si Neander y Sapiens cambian de dirección
  al transformarse, hay que cambiarla en dos lugares cada una (satélite y fila); hoy los rótulos ya dicen Centros comerciales
  y Country aunque las páginas todavía digan Neander y Sapiens; (b) las presentaciones de Analítico se siguen llamando *Byte
  Analítico* y la de Automotrices *RIA Drivecore*; (c) Acceso dice «de un mercado concentrador o de un barrio» y el barrio
  ahora tiene Country: ¿Acceso queda sólo para el mercado?; (d) Eco Aceite vive en `byt.ar`, no en `rialabs.ar`; (e)
  Entrypoint sigue sin web: cuando la tenga, su satélite pasa de mudo a enlace.
- **El stand con la máquina abajo: quinto encuadre del hero, `?hero=5` (rama `hero-stand`, 2026-11-01).** Matías,
  verbatim: *«Probemos ahora una version donde la maquina pasa a estar abajo del nombre, como la teniamos antes. El eclipse
  como logo y el nombre de la empresa con las animaciones de los CEOs quedan como portada pero la maquina la pasamos
  abajo.»* (en `docs/prompts-usuario/REGISTRO-2026-11.md`). **Qué es.** La primera pantalla (`100svh`) es sólo la
  portada: el rótulo, **el eclipse solo como figura** (flama, estrella de luz, sin máquina adentro), **RIA / LABS** debajo,
  **los dos retratos vivos a los costados del eclipse** (Matías a la izquierda, Sebastián a la derecha, sólo el nombre,
  la misma máscara elíptica que el 4) y la línea **Smart City Expo · Barcelona · 3–5 de noviembre** al pie. Al hacer
  scroll, antes de `#productos`, **la máquina entera con su reactor propio en el centro**, como en main o en el encuadre
  1, con **«Tu infraestructura ya existe. / Nosotros la hacemos pensar.»** como su pie; su salida es **la red abierta** del
  4. Los encuadres 1–4 no cambian y el de por defecto sigue siendo el 2.
  **Las decisiones, medidas.** (1) *Los retratos se alinean con el eclipse*, no con el wordmark ni con el conjunto: las
  caras (el 44 % del alto de la foto, donde la viñeta de los clips centra la cara) van a la altura exacta del centro del
  disco —Matías, el eclipse y Sebastián en una misma línea, tres caras— y el nombre al pie de la parte visible de cada
  foto. Alinearlos con el wordmark (como en el 4) los dejaba al pie del eclipse, con los costados de arriba vacíos;
  con el conjunto, las caras caían ~22 px bajo el centro del disco sin ganar nada. (2) *El grupo escala como una sola
  pieza*: la foto mide 0,64 del eclipse (lo visible de la foto queda del tamaño del disco más la flama: el eclipse,
  con su aureola, sigue siendo la figura) y su centro va a 0,65 eclipses del centro de la pantalla, así lo visible de cada
  foto queda a ~0,1 eclipse de la flama. Centrarlas en el espacio libre de cada lado (la primera prueba) las dejaba como
  islas lejos del logo. (3) *El eclipse se sienta al pie de su fila* y RIA / LABS sube 7vh sobre su aureola (el 4 sube
  5vh): cuando el ancho lo limita (pantallas 4:3), el aire sobrante va arriba y no entre el disco y el nombre. Tope de
  ancho 46vw (42 dejaba 190 px de aire arriba en 1024×768). (4) *La frase va con la máquina*, abajo, como su pie: no
  encontré razón para dejarla en la portada —sin la máquina arriba, «la hacemos pensar» no tiene a qué referirse— y la
  portada respira mejor con un solo texto al pie, la expo, que queda **debajo de RIA / LABS**.
  **Cómo está hecho.** CSS: `html[data-hero="5"]` con la misma escala de espacios `--u`, los márgenes del nav y el mismo
  `--ria` que el 4. Cada `<figure class="stand">` cubre la fila del eclipse y es un **contenedor de tamaño**
  (`container-type: size`): `100cqh` es el alto de la fila, así `--e: min(100cqh, 46vw, 820px)` es exactamente lo que
  mide el eclipse (su misma fórmula) sin medir nada en JS; la foto y el nombre se posicionan con `--e`. Los retratos se
  estampan desde el mismo `<template id="stand-tpl">` con el mismo script (ahora con `data-hero` 4 o 5), y el del
  `<head>` acepta `[1-5]` y precarga los pósters en el 4 y el 5. La máquina sale del hero con un script de cinco líneas
  que sigue al `</header>`: sólo con `data-hero="5"`, durante el parseo, mueve `#maquina` y `#maq-pie` a un
  `<div class="maq-banda" id="banda-maquina">` (padding `9vh 52px 5vh`; 24 px en celular). La caja de la máquina tiene
  la proporción del dibujo horizontal (1116 × 320 unidades, centrada en el reactor: el reactor queda justo sobre la
  frase) con tope de escala 1,45; en celular, la del vertical con tope en `78svh`, así máquina y pie entran juntos en
  una pantalla. Script «LA MÁQUINA»: `ABIERTA = VAR === '4' || VAR === '5'`; en el 5 la red se arma con el reactor
  propio (`OJO` sigue siendo sólo 2 y 4); sus límites (`T.ext`) son el borde de la ventana a los costados, **el pliegue
  arriba** (el pie del hero) y **el contenido de `#productos` abajo**; `armarRedAbierta` cuenta desde el origen del
  viewBox (que en el 4 es 0,0: mismas cuentas) y en la banda su fade **nace 24 px bajo el pliegue y llega entero a los
  164** (nunca entra en la primera pantalla ni sobre la foto de Sebastián), se pierde 20 px antes de «Productos» y se
  aparta 70 px de las letras de la frase. La estrella no asoma del lado de Sebastián (`cos a > 0,3`, como el 3 del
  lado del logo): su rayo largo apunta siempre a la derecha y desde el limbo derecho llegaría a su foto.
  **Retratos:** igual que en el 4 —autoplay mudo, `DESFASE = 0,87` (se turnan la sonrisa), pausa fuera de pantalla (el
  observador mira `.hero-escena`: al bajar a la banda se pausan) y con la pestaña oculta, póster con reduced-motion o
  Save-Data (verificado por DOM: 0 `<video>`, 2 `<img>`), pósters precargados sólo en el 4 y el 5 (en 1–3 y por defecto
  no hay ni preload ni retratos en el DOM). De día, la misma máscara blanda del 4.
  **La red abierta en el 5:** sale de la brida del reactor en abanico hacia la derecha y sube hasta cerca del pliegue y
  baja más allá de la frase, perdiéndose antes de «Productos»; destellos de colores desde la química como en el 4 (la
  misma simulación, la misma semilla). En celular el abanico de 100° abre a los dos costados del reactor, hasta los
  bordes, y muere 80 px antes del pie de la caja, delante de la frase.
  **Celular (≤860 px):** primera pantalla con el eclipse arriba, grande (hasta el ancho de la pantalla: la caja es casi
  toda aureola), RIA / LABS subido `clamp(10px, 4vh, 36px)` sobre la aureola, **los dos retratos de a par** debajo
  (41vw de ancho con tope en 19svh: 160×200 a 390×844, 126×158 a 390×664), cada uno con su nombre centrado debajo, y la
  expo al pie; la foto va a escala 1,12 hacia la cara (1,3 en el 4). Abajo, la máquina vertical (estación arriba,
  reactor al medio, red abajo) con su pie. **Cómo se elige:** `?hero=5` (con `?tema=dia` para el día); sin parámetro
  sigue el 2. **Medidas de la primera pantalla** (`getBoundingClientRect` en Chrome headless por iframe del tamaño
  exacto, animaciones a cero, px; «rótulo→llama» = del pie del rótulo a la punta de la flama, 1,17 radios; «luna→RIA» =
  del pie del disco a la caja de RIA; «cara−luna» = línea de las caras menos centro del disco; «foto↔llama» = del borde
  interior de la caja de la foto a la flama, izquierda / derecha —la diferencia es la libración de la luna—, lo visible
  de la foto empieza ~20–30 px más adentro; «foto→nombre» negativo = el nombre se apoya sobre el pie fundido de la foto):

  | Pantalla | eclipse caja / disco | RIA / LABS | nav→rótulo | rótulo→llama | luna→RIA | LABS→expo | expo→borde | foto | cara−luna | foto↔borde | foto↔llama | foto→nombre | nombre→RIA |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | 1440×900 | 614 / 336 | 108 / 19,4 | 21,6 | 123 | 86,6 | 21,6 | 32,4 | 314×393 | −0,3 | 164 / 164 | 48 / 43 | −36 | 46 |
  | 1280×720 | 469 / 257 | 86,4 / 15,6 | 17,3 | 95 | 64,3 | 17,3 | 25,9 | 240×300 | −0,2 | 215 / 215 | 36 / 33 | −28 | 31 |
  | 1920×1080 | 769 / 421 | 128 / 23 | 24 | 154 | 110 | 24 | 36 | 394×492 | −0,3 | 263 / 263 | 60 / 54 | −45 | 66 |
  | 1024×768 | 471 / 258 | 92,2 / 16,6 | 18,4 | 133 | 62 | 18,4 | 27,6 | 241×302 | −0,2 | 85 / 85 | 37 / 33 | −28 | 29 |

  | Celular | eclipse caja / disco | RIA / LABS | nav→rótulo | rótulo→llama | luna→RIA | LABS→fotos | fotos | foto↔borde | entre fotos | nombre→expo | expo→borde |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | 390×844 | 390 / 213 | 56,6 / 10,2 | 20 | 92 | 64,4 | 10 | 160×200 | 29,5 / 29,6 | 11 | 18,7 | 30 |
  | 360×740 | 321 / 175 | 52,2 / 9,4 | 17,8 | 68 | 51,8 | 8,8 | 141×176 | 31,7 / 31,7 | 15 | 16,5 | 26,6 |
  | 390×664 | 285 / 156 | 49,1 / 8,8 | 15,9 | 61 | 45,9 | 8 | 126×158 | 46,4 / 46,4 | 45 | 14,6 | 23,9 |

  En las siete las fotos son simétricas respecto del centro (±0,1 px) y nada toca el nav (el rótulo queda a 2u de su
  borde; a 360 el rótulo va en dos líneas, igual que en el 4). **La banda** («g» = px por unidad de diseño; «pliegue→red»
  = del pie del hero al nodo visible más alto, opacidad ≥ 0,05; en celular la red vive al costado y debajo del reactor):

  | Pantalla | caja de la máquina | g | estación | pliegue→caja | caja→frase | pliegue→red | red→«Productos» | frase→«Productos» |
  |---|---|---|---|---|---|---|---|---|
  | 1440×900 | 1336×383 | 1,18 | 425×324 | 81 | 33 | 69 | 90 | 176 |
  | 1280×720 | 1176×337 | 1,03 | 373×285 | 65 | 33 | 67 | 96 | 168 |
  | 1920×1080 | 1816×464 | 1,45 | 524×400 | 97 | 33 | 57 | 84 | 186 |
  | 1024×768 | 920×264 | 0,80 | 290×221 | 69 | 33 | 68 | 85 | 170 |
  | 390×844 | 342×658 | 0,73 | 203×265 | 51 | 33 | 446 | 229 | 134 |
  | 360×740 | 312×577 | 0,64 | 178×233 | 44 | 33 | 387 | 241 | 130 |

  El centro del reactor coincide con el de la frase en los seis (±0,1 px). **Verificado:** capturas reales de la
  primera pantalla en los seis tamaños más 390×664 y 900×700, de la banda en los seis (`ANCLA=banda-maquina`), día,
  reduced-motion y la transición del pliegue a 1440×900 (`BAJAR=450`: la red empieza ~80 px bajo la línea de la expo);
  sin errores de JS (colector de `error`/`unhandledrejection`/`console.error` en el harness de medidas) y los `<script>`
  pasan `node --check`. **El 4 no cambió:** 30 cajas del hero (nav, rótulo, expo, escena, máquina, eclipse, wordmark,
  frase, fotos, nombres, fuentes, preload, alto de página) idénticas antes y después en sus seis tamaños y de día, y lo
  mismo para 1, 2, 3 y el de por defecto (sólo 0,1 px de ruido subpíxel en la frase del 3, que ninguna regla nueva
  toca); la red del 4 es la misma en la captura (0,36 % de píxeles distintos: engranajes, tokens y destellos en otro
  instante). Capturas en `_capturas/hero-5/` (ignorado; `antes/` y `despues/` del 4). **Gotchas:** con `aspect-ratio`
  y ancho `auto`, Chrome pasa el `max-height` al ancho y la caja se angosta y queda corrida a la izquierda (la máquina
  quedaba 100 px fuera del eje de la frase a 1920 y 58 en 390): por eso la banda lleva `width: 100%` explícito. Un
  `Range` sobre un bloque mide el bloque entero, no las letras: la caja de la frase se mide con un Range por párrafo. El
  modo `BAJAR=` del script de captura hace el scroll en el `onload` del iframe y, con tiempo virtual, a veces no llega a
  correr el IntersectionObserver que revela la máquina (la banda sale vacía en la foto aunque en el navegador se revela:
  verificado por DOM, `maq vis` tras bajar): para la banda usar `ANCLA=banda-maquina`. **Script de captura:** con
  `PANTALLA=1`, `BAJAR=<px>` o `ANCLA=<id>` fotografían la pantalla bajada, siempre por un iframe del tamaño de la
  pantalla (así el `100svh` del hero sigue siendo el de la pantalla); sin esas variables se comporta igual que antes.
- **La red abierta (encuadre 4, rama `red-abierta`, 2026-11-01).** Matías, verbatim, sobre la portada del stand: *«Por
  ultimo, la parte de la red a la derecha de la maquina (la salida del eclipse) quisiera que fuera una red abierta que no
  termine, que se difumine y pierda en el espacio para que parezca mas grande, y sacaria los nombres de los productos
  como items en la red, solo salen de la maquina quimica pulsos de energia que se distribuyen por la red, de diferentes
  colores.»* **Qué es.** Sólo en el stand (`?hero=4`; los encuadres 1–3 no cambian): la constelación cerrada de la
  salida —tres nodos con ANALÍTICO · SMARTCITY · AUTOMOCIÓN y quince menores con borde— deja lugar a una **red sin
  nombres** que sale de la brida en abanico y sigue hacia la derecha, arriba y abajo **hasta el borde de la ventana y más
  allá**: la sección deja de recortar en este encuadre, así las aristas cruzan el borde y no se le ve el final. Más
  nodos y más aristas cuanto más lejos, y más tenues y más finos, hasta quedar como estrellas entre las del cielo. Los
  productos ya están en el nav; de la red salen los tres **troncos** dorados de siempre (en el lugar de los tres
  productos, con sus conductos desde la brida y las dos aristas doradas que respiran) y de ahí la malla. **Los pulsos
  de energía salen de la química**: cada partícula de una estructura madura que cruza la brida lanza un destello **de
  su color** (azul de la cámara `--maq-p1` = `--c-ana`, violeta del registro `--maq-p2`, teal del sensor `--maq-p3` =
  `--c-esp`; las tres primeras de cada estructura) y la estructura entera, al terminar de cruzar, uno **dorado**
  (`--gold-hi` = `--c-aut`). Cada destello viaja por el conducto hasta un tronco (nunca el mismo dos veces seguidas),
  sigue de nodo en nodo siempre alejándose de la salida, prefiriendo la arista que mantiene el rumbo, se **bifurca** en
  algunos nodos (una rama más débil) y pierde energía en cada salto hasta apagarse a lo lejos; la arista por la que pasa
  y el nodo al que llega quedan brillando en su color (2,6 y 3,4 s). Cadencia medida con 192 s de reacción: una ráfaga
  cada 9–10 s (32,9 · 46,9 · 55,7 · 64,9 · 73,9 · 83,2 · 93,3 s…), de 3–4 destellos de colores distintos en ~2 s. Vivo
  pero sereno: la red está «respirando» la mitad del tiempo y quieta la otra mitad. **Cómo está hecho** (script «LA
  MÁQUINA», `ABIERTA = VAR === '4'`; `armarRedAbierta`, `lanzarChispa`/`ramificar`, `pintarRed`): la red se muestrea
  con un **Poisson de radio decreciente** (separación mínima 64 px cerca → 32 lejos; en vertical 46 → 24) con azar
  propio (`rndR`, semilla fija: la misma caja da siempre la misma red y la reacción no gasta su azar en armarla), en un
  abanico desde la brida (horizontal: |v| < 60 + 1,25·u desde u = 95; vertical: un sector de 100° desde u = −140, que
  alcanza los flancos de abajo del eclipse; nunca sobre la flama, a 1,3 R del centro). Aristas a los 2 vecinos más
  cercanos (3 a lo lejos) a menos de 2,4 radios, y siempre una hacia un nodo más cercano a la salida, para que un
  destello pueda llegarle; cada arista va del nodo de adentro al de afuera, y por ahí corren los destellos. **El
  fade** de cada punto: decae con la distancia a la brida (piso 0,08: una estrella), se apaga bajo el nav (48 → 148 px
  de ventana), bajo la caja se atenúa y alrededor de la **foto de Sebastián** —leída del DOM con
  `getBoundingClientRect`, así sigue al layout de la otra sesión— baja a 0,1 (la red pasa por detrás, muy tenue: la
  sección baja al z-index de los retratos, que vienen después en el DOM, y sigue encima del eclipse); en vertical muere
  80 px antes del pie de la caja, delante del wordmark y los retratos. El color va del gris violeta de la constelación
  (`--nodo`) al violeta de los nodos (`--maq-vio`) con **`color-mix()` por fade**, declarado por `style` con el gris
  antes en la misma cascada (un navegador sin color-mix ve la red gris); la opacidad baja con el fade; los nodos lejanos
  pierden el aro y quedan como puntos violeta tenues; cada tercero es violeta, como antes. Lo que no se ve no se dibuja
  (bajo 0,04). Unos 160 nodos y 300 aristas a 1440×900, 320 a 1920×1080, 75 a 390×844. **Los destellos** son estado
  de la simulación (`segs`: cada salto con su arista, su instante, su color y su energía, decididos al lanzarlo con
  `rndR`: pintar es sólo leer; `?t=` da siempre la misma foto), un pool de 28 (núcleo + cola) en el mismo rAF; los
  nodos cercanos titilan como antes. Los pulsos de la constelación siguen lanzándose invisibles, así **la reacción es
  idéntica en el 2 y en el 4** al mismo `?t=`. Con `prefers-reduced-motion`, un cuadro con cuatro destellos ya en camino,
  de los cuatro colores. **Rearmado sin perder los destellos:** los candidatos del Poisson se tiran en px sobre una caja
  canónica fija alrededor de la salida (u ∈ [−200, 1400], v ∈ [−1400, 1400]) y el radio decae en px, así un cambio
  chico de la caja (la fuente que carga y corre el logo unos px, un resize) da casi la misma red; cada nodo lleva una
  clave estable (su candidato; los troncos `T0..T2`) y `armar` re-mapea por clave los destellos en vuelo a la red nueva
  (verificado en el log: 63 → 58 → 52 recorridos a través de dos rearmados al cargar la fuente). **Accesibilidad:** el
  grupo de la red va `aria-hidden` y sin `pointer-events` (ya no tiene enlaces) y el `aria-label` del SVG en este
  encuadre describe los pulsos de colores en vez de «cada producto es un enlace». **CSS:** una sola regla, en el bloque
  de la máquina: `html[data-hero="4"] .hero .maq { overflow: visible; z-index: 2 }`. **Verificado en captura real**
  (`PANTALLA=1 … QUERY=hero=4`): 1440×900 (también `t=7500` con la ráfaga de los 46,9 s en vuelo, reduced-motion y
  `tema=dia`), 1280×720, 1920×1080, 390×844 y 360×740; sin `Uncaught`. Capturas en `_capturas/red-abierta/`
  (ignorado). Gotcha de captura: Chrome headless con `--virtual-time-budget` casi no corre cuadros de rAF (la
  simulación avanza apenas 0,1 s después del precalentamiento), así que para fotografiar una ráfaga hay que apuntar
  `?t=` 2–3 s después de una salida conocida (`t=7500` → 49,5 s de reacción: la de los 46,9 s), no esperar a que pase.
- **El stand: cuarto encuadre del hero, `?hero=4` (rama `hero-stand`, 2026-10-31).** Matías, verbatim: *«Probemos
  una version de portada con el logo de RIA Labs como esta ahora con el eclipse actual y la maquina dibujada pero que
  entre todo en una sola pagina de pantalla, y a cada costado del logo las imagenes de los ceos, Matias y Sebastian, en
  movimiento como posando esperando que le saquen la foto con el parpadeo de ojos y todo, pero sin pelo agregado. La
  idea es mostrar los CEOs que estan presentes en el stand como una primera vista cuando se visita la home de la
  empresa»*; y después, sobre una captura del encuadre 2: *«abajo de la maquina, del lado izquierdo, a la altura de
  RIA, pone la imagen viva de Matias desarrollador, y a la misma altura pero del lado derecho, abajo de la red de
  sistemas, pone la foto viva de Sebastian de Byte»* (los dos en `docs/prompts-usuario/2026-11-01-portada-ceos-en-el-stand.md`).
  Contexto: Smart City Expo World Congress, Barcelona, 3–5/11/2026; los dos están en el stand y la home es lo primero
  que ve quien los visita. **Qué es:** el encuadre 2 tal cual (el eclipse es el reactor, RIA / LABS debajo, la frase al
  pie) más **los dos retratos vivos en las esquinas de abajo, a la altura de RIA / LABS**: Matías a la izquierda, bajo
  la estación (engranajes y entradas); Sebastián a la derecha, bajo la red; del mismo tamaño, simétricos respecto del
  logo, con el rótulo **nombre · oficio** como en `#equipo` (Matías Gallego · Programador, Sebastián Acedo ·
  Integrador) a la altura de la frase. No es la sección de equipo subida: es la recepción. Ningún otro texto nuevo
  («desarrollador» y «de Byte» son cómo Matías identifica las fotos; Byte no vuelve a la página). Una línea opcional
  con la feria queda **apagada** detrás de la constante `EXPO` del script del stand (debajo del rótulo del hero, en
  gris; el texto sugerido está en el comentario). **Cómo está hecho:** la grilla es la misma del 2; los retratos son
  dos `<figure class="stand">` absolutas dentro de `.hero-escena` (no miden: no empujan ni la máquina ni el logo),
  cada una en la franja que va del borde a la mitad menos lo que reserva el wordmark (`--stand-centro`) y centrada en
  esa franja —que es justo donde caen la estación y la red, en todos los anchos—, con el pie del rótulo al ras del pie
  de la escena. Sin tarjeta ni marco: una **máscara radial** (`mask-image`, óvalo centrado en la cara) funde la foto
  con el cielo, con decisión porque los retratos traen su contexto (Matías con las pantallas de código y la maqueta,
  Sebastián con el muro de cámaras y el rack) y el fondo oscurecido hacia los bordes. Alto `clamp(140px, 27svh,
  290px)` (243 px a 1440×900, 194 a 1280×720, 290 a 1920×1080), 4:5; el eclipse sigue siendo la figura (disco de 299
  px a 1440×900). El marcado vive en `<template id="stand-tpl">` y un script lo estampa durante el parseo **sólo con
  `data-hero="4"`**: en los otros encuadres no existe en el DOM y no se descarga ni el póster (verificado por DOM). En
  el 4 el script del `<head>` pide los dos pósters con `<link rel=preload fetchpriority=high>`: son lo más grande que
  pinta la primera pantalla. Los clips van con `autoplay muted loop playsinline` sobre su póster; el script «EL
  STAND» arranca el segundo en otro punto del loop (`DESFASE` del largo: 0,42 al principio, 0,87 desde la tercera vuelta de los retratos, para que se turnen la sonrisa lenta; ver §0.3), los pausa
  fuera de pantalla y con la pestaña oculta (IntersectionObserver + visibilitychange) y los retoma al volver. Con
  `prefers-reduced-motion` o Save-Data el estampado cambia cada `<video>` por su póster (el `<img>` de adentro, con
  su `alt`). `alt` y `aria-label` describen a cada uno con su contexto, sin melena. La máquina y la estrella tratan
  al 4 como al 2 (`OJO` en «LA MÁQUINA»; la estrella no asoma sobre las bridas). De día (`?tema=dia&hero=4`) el
  retrato sigue siendo una foto nocturna sobre papel: el óvalo se funde más despacio para no quedar como un agujero
  con borde. **Celular (≤860 px):** los dos flanquean RIA / LABS, con el pie de la foto a la altura de LABS y el rótulo
  al lado del wordmark; la frase sigue debajo a lo ancho; la máquina vertical no cambia (los retratos no miden).
  Más chicos (`clamp(84px, 28vw, 112px)` de ancho: 109 a 390, 100 a 360) y acercados a la cara (escala 1,3 con origen
  en la cara) para que se lean en 100 px; el nombre a 11 px en una línea, el oficio a 8,5. En 390×844 y 360×740
  quedan por fuera de la constelación (sus vértices bajos están en x 140–250). **Verificado en captura real**
  (`PANTALLA=1 … QUERY=hero=4`): 1440×900, 1280×720, 1920×1080, 1024×768, 390×844 y 360×740, más `?tema=dia` y
  reduced-motion a 1440×900; en todos entra en la pantalla y no tapa nodos ni etiquetas. Capturas en
  `_capturas/hero-stand/` (ignorado). **Depende de los retratos reales** (`assets/retrato-stand-*`, §0.3, los produce
  otra sesión): el ajuste fino de la máscara, el `object-position` (hoy 50 % 30 %: con los provisorios Matías queda un
  poco más abajo que Sebastián porque su cabeza viene más baja en el cuadro) y el `DESFASE`, que hay que mirar con los
  pestañeos reales. Los encuadres 1–3 y el de por defecto (2) no cambian. **Los reales entraron el 01/11** (merge de
  `retratos-stand`, 480×600, sin el eclipse chico): en la captura a 1440×900 las dos cabezas quedan a la misma altura y la
  máscara funde bien con los stops de los provisorios, así que no se tocó nada; el `DESFASE` sigue sin mirarse en un
  navegador real.

  **Segunda vuelta, medida (01/11).** Matías, verbatim: *«Saca el nombre del oficio. Agrega la linea de "Smart City
  Expo · Barcelona · 3–5 de noviembre". Saca los pequeños eclipses sobre las cabezas de Matias y Sebastian y trata de
  redondear las imagenes de fondo de esas dos fotos. Los fondos de las fotos se tienen que difuminar con el fondo de la
  pagina. [...] Hagamos también que todo el titulo RIA Labs este mas grande y acomodemos bien los elementos en la
  portada, midamos para que todo quede bien armonico en el espacio entre ellos y con los margenes»* (en el mismo
  archivo de prompts; los eclipses chicos eran los pósters provisorios en caché: los reales no los traen). Lo que
  sigue **reemplaza** la mecánica descripta arriba:
  - **Sin oficio:** bajo cada retrato va sólo el nombre (Saira 500, `clamp(13px, 1.1vw, 16px)`, blanco).
  - **La expo, encendida:** `EXPO = 'Smart City Expo · Barcelona · 3–5 de noviembre'` en el script del stand; es una
    línea en el lenguaje del rótulo de arriba (mono, versalitas, 4 px de tracking) en `--gold-hi`, que **cierra la
    escena debajo de la frase**, centrada y a lo ancho (`.hero-expo`, fila 4 de la grilla). Se eligió abajo y no bajo
    el rótulo de arriba porque es lo que liga a los dos retratos —las dos personas, esta feria— y porque el rótulo de
    arriba sigue diciendo de dónde somos. Vaciar la constante la apaga.
  - **La escena pasa a tres columnas** (franja · centro · franja), sólo en el 4: el eclipse y la máquina cruzan las
    tres; el wordmark (fila 2) y la frase (fila 3) van en la del centro; **cada retrato es un ancla de alto cero en la
    fila del wordmark** (`.stand-ancla`, `align-self: center`: no mide, no empuja ni la máquina ni el logo; sube la
    mitad de lo que sube el wordmark sobre la aureola, así los centros coinciden) con la foto absoluta encima,
    centrada en la franja, y **su nombre es un ítem de la fila de la frase** (`align-self: end`): el pie del nombre y
    el de la frase son el mismo. El `<figure>` es `display: contents`. Las franjas miden lo mismo a los dos lados,
    así los retratos son simétricos respecto del wordmark; y en los seis tamaños caen bajo la estación y la red.
  - **RIA / LABS más grande:** `--ria: clamp(56px, min(10.5vw, 12svh), 128px)` (108 px a 1440×900, antes 76; 86 a
    1280×720; 128 a 1920×1080; 92 a 1024×768) y LABS en proporción (0,18 de RIA, margen 0,07): el wordmark entero
    crece junto. En celular `clamp(44px, min(14.5vw, 7.4svh), 68px)` (57 a 390, 52 a 360).
  - **Escala de espacios `--u` = 1,2 vh** (6–12 px; 5–10 en celular): 2u entre los grupos de texto (nav→rótulo —el
    padding de arriba pasa a `83px + 2u`, que es el alto del nav más 2u—, LABS→frase, frase→expo), 3u de margen
    inferior, 1u de gap de grilla. **Márgenes laterales = los del nav:** 52 px (24 en celular) en vez de los 24/16 del
    hero; la máquina se arma 5 % más chica y queda alineada con el logo y el botón del nav.
  - **Fundido redondo:** la máscara calca la viñeta horneada de los clips (elipse centrada al 44 % del alto, radios =
    el semiancho y la distancia del centro al borde de abajo; plena hasta 0,28 r, cielo puro `#0b0a14` desde 0,80 r)
    apenas más grande —`ellipse 52% 58% at 50% 44%`, plena al 30 %, 0,75 al 55 %, 0,25 al 82 %, cero al 100 %— para
    no recortar contexto, y el `<video>`/`<img>` de adentro lleva un degradé lineal que funde el borde de arriba
    (donde la elipse no llega a cero). Resultado: la cara entera, las pantallas y el muro se pierden en redondo, sin
    borde ni rectángulo. En celular, donde la foto va escalada 1,3 a la cara y la viñeta horneada ya no coincide con
    la caja, la máscara vuelve a la elipse que llega a cero en los cuatro bordes (`50% 46% at 50% 45%`); de día, lo
    mismo con stops más blandos. Fotos: `clamp(150px, 30svh, 330px)` de alto, 4:5, `object-position 50% 45%`.
  - **Celular (≤860 px):** la misma grilla con una fila más: fotos flanqueando RIA / LABS (centradas con el
    wordmark), **los nombres en su propia fila** debajo (la frase a lo ancho no entra al lado de un nombre en 390 px),
    después la frase y la expo (8,5 px / 1,6 de tracking, entra en una línea a 360). Cuesta ~24 px a la máquina.
  - **Las medidas** (`getBoundingClientRect` en Chrome headless por iframe del tamaño exacto, animaciones a cero; en
    px; «hueco» = tope de la foto menos pie de la estación/red, negativo = se montan en el borde transparente de
    arriba, que la máscara y la viñeta dejan en cielo puro; «foto↔RIA» izquierda / derecha):

    | Pantalla | RIA / LABS | nav→rótulo | rótulo→dibujo | luna→RIA | LABS→frase | frase→expo | expo→borde | foto | hueco | foto↔borde | foto↔RIA |
    |---|---|---|---|---|---|---|---|---|---|---|---|
    | 1440×900 | 108 / 19,4 | 21,6 | 141 | 86 | 21,6 | 21,6 | 32,4 | 216×270 | 28 | 222 | 181 / 170 |
    | 1280×720 | 86,4 / 15,6 | 17,3 | 84 | 61 | 17,2 | 17,3 | 25,9 | 173×216 | −11 | 208 | 179 / 170 |
    | 1920×1080 | 128 / 23,0 | 24 | 162 | 111 | 24 | 24 | 36 | 259×324 | 25 | 310 | 271 / 258 |
    | 1024×768 | 92,2 / 16,6 | 18,4 | 135 | 77 | 18,4 | 18,4 | 27,6 | 184×230 | 38 | 138 | 104 / 95 |
    | 390×844 | 56,6 / 10,2 | 20 | 21 | — | 44 (fila de nombres) | 20 | 30 | 109×136 | 0 (x aparte) | 26 | 7 / 2 |
    | 360×740 | 52,2 / 9,4 | 17,8 | 19 | — | 40 (ídem) | 18 | 27 | 101×126 | −1 (x aparte) | 25 | 6 / 1 |

    En los seis el **centro de la foto coincide con el centro del wordmark** (±0,1 px) y las dos fotos distan lo mismo
    del centro de la pantalla; en los cuatro de escritorio el **pie del nombre es el pie de la frase** (la misma
    coordenada); en celular los nombres van 10 px bajo el wordmark y la frase arranca 12 px bajo las fotos. El margen
    lateral del hero es el del logo y el botón del nav (52 / 24). «rótulo→dibujo» es del pie del rótulo al tope de la
    estación (la flama del eclipse empieza ~30 px más abajo que ella en 1440); «luna→RIA», del pie del disco negro al
    tope de RIA. Capturas de los seis más `?tema=dia` y reduced-motion en `_capturas/hero-stand/`.
  - Herramientas de la sesión (fuera del repo): `medir.sh` + `tabla.py` en el scratchpad; conviene traerlas a
    `scripts/` si se vuelve a medir.
- **RIA Smartcity (2026-10-29).** «Creo que tenemos que renombrar RIA Espacios a RIA Smartcity para poder abarcar
  esta expo Barcelona a la que estamos a punto de ir y nuestro nuevo producto RIA Smartcity Entrypoint. Sin perder el
  resto de las cosas que ya hicimos.» El producto 02 vuelve a llamarse **RIA Smartcity** (Smart City Expo World
  Congress, Barcelona, 3–5/11/2026): nav, menú, banda, astro, máquina del hero, Laboratorio y metadatos; el ancla pasa
  de `#espacio` a **`#smartcity`** (v5 no está publicada, no hay enlaces externos que romper). Bajo el nombre ya no va
  una entrada de la RAE (no tiene «smart city»): va una definición propia en el mismo formato, *smart city. Voz inglesa;
  en español, ciudad inteligente. 1. Ciudad que mide lo que pasa en sus calles y usa esa medición para decidir. 2. Por
  ext., todo lugar —un club, un barrio, un mercado— que hace lo mismo con su espacio.* (la segunda acepción conserva la
  idea de «Espacios»: el mismo producto reproducido en sabores). **Entrypoint** entra como sabor nuevo: primer ítem de la
  lista («el acceso instantáneo a la experiencia Smartcity: en un mes, con el parque de cámaras que ya tenés y sensores de
  bajo costo, sin licitar una cifra extraordinaria. Un chat guía arma tu Presente; las analíticas se suman por vertical o
  por paquete, y se pagan por mes», con las palabras del prompt fundacional del 26/10 en
  `ria-smartcity-machine/docs/prompts-usuario/2026-10-26-ria-smartcity-entrypoint.md`) y satélite nuevo del astro, sin
  enlace (todavía no tiene página pública), rotulado «la puerta de entrada». El satélite que decía «Smartcity · ciudad»
  pasa a **«Ciudad · municipios»** (mismo enlace a smartcity.rialabs.ar), para no repetir el nombre del producto. Todo
  lo demás de la banda quedó igual.
- **El hero, depurado (2026-10-14).** Matías: «Saquemos todo desde Metaestructura hasta los botones inclusive.
  Dejemos solo debajo del logo el dibujo de la máquina y la frase de siempre.» El hero queda: rótulo · eclipse
  (flama ecuánime + estrella de luz) · **RIA / LABS** · **la máquina** con su pie «Tu infraestructura ya existe. /
  Nosotros la hacemos pensar.». Salieron el titular «Metaestructura», la cita, el audio y su script «LA FRASE
  HABLADA», los botones «Ver los productos» / «Conocer el motor →» y la tipografía M PLUS Rounded 1c (no se usaba
  en otro lado). La máquina dejó de ser banda propia: vive dentro de `<header>` debajo del logo, sin fondo ni
  bordes (`.hero .maq`), con el mismo `id="maquina"` y el mismo script (el mismo día, más tarde, el hero pasó a
  medir una pantalla y el orden depende del encuadre: ver el bullet siguiente). `<title>` vuelve a «RIA Labs — Software e
  inteligencia artificial»; `og:title`/`twitter:title` y la description arrancan con la frase. La OG muestra eclipse
  + RIA LABS + la frase (el modo OG del script de captura esconde el dibujo y deja el pie). **El discurso quedó
  guardado como idea a futuro** en `docs/ideas/2026-10-13-discurso-metaestructura.md` (las dos versiones, cómo se
  podría producir y cómo no, y dónde está el código en git). Los bullets de «Superestructura/Metaestructura» que
  siguen más abajo son historia.
- **El hero entra en una pantalla: tres encuadres, `?hero=1|2|3` (rama `hero-pantalla`, 2026-10-14).** Matías,
  verbatim: *«ok bien, tratemos de que entre en la pantalla de presentacion de la web. Aunque el dibujo es hermoso
  verlo en grande, no se como se puede acomodar...hmm»*. Apilado, el hero medía ~1.300 px (eclipse ~400 · RIA / LABS
  ~150 · máquina ~355 · pie ~70) y una laptop muestra 720–900: la máquina y la frase quedaban bajo el pliegue. Ahora
  el hero mide **una pantalla** (`height: 100svh`, piso de 560 px) y adentro una grilla, `.hero-escena`, reparte el
  alto entre el eclipse, el logo, la máquina y su pie. El pie dejó de estar dentro de `#maquina`: es su hermano
  (`.maq-pie`), así cada encuadre lo pone al pie aunque entre la máquina y él vaya el logo. **La máquina ya no tiene
  tamaño propio**: el script «LA MÁQUINA» calcula el viewBox para la caja que la grilla le deja (una unidad de
  diseño —las de la original de 1200×380— mide g px y el dibujo queda centrado; las etiquetas de los productos no
  bajan de 8,5 px en pantalla y el radio de clic de cada producto, de 22 px) y se rearma sola cuando la caja cambia (ResizeObserver
  sobre la sección y, en el 2, sobre el eclipse; también al cargar la fuente), sin perder el estado de la reacción.
  La grilla tenue de la original se funde hacia los bordes (máscara radial) porque ya no hay banda que la corte. El
  encuadre lo decide un script en el `<head>` (`data-hero` en `<html>`, antes del primer cuadro); sin parámetro, o con
  uno inválido, es el 2.
  1. **Escalonado** (`?hero=1`). Todo apilado como antes, medido por el alto: eclipse `clamp(160px, 32svh, 400px)`
     (disco de 158 px a 1440×900, 126 a 1280×720), RIA a `9,2svh`, y la máquina horizontal y entera con todo el alto
     que sobra (1.054 px de ancho a 1440×900, 794 a 1280×720: g 0,94 y 0,71). El más conservador; en pantallas bajas
     la máquina queda chica.
  2. **El eclipse es el reactor** (`?hero=2`, **el de por defecto**). La máquina pasa *a través* del eclipse del hero:
     la estación manda su cañería a una brida en la punta de la flama (de la brida sale una boquilla fina que se
     apaga antes del limbo), el token cruza la corona y entra al disco, y **la química de partículas se pinta adentro
     del disco negro, sobre la luna** (recortada a 0,985 del radio de la luna: la flama queda libre); de la brida del
     otro lado salen los tres conductos a la constelación. El reactor chico, su aro y su manómetro no se dibujan. El
     script lee el centro y el radio del eclipse del DOM (`offsetLeft/Top/Width` de `#sistema-wrap`, que no ven el
     transform de la entrada; luna = 93/340 del ancho) y escala la estación y la constelación para que respiren
     alrededor. El eclipse es tan alto como su fila, con tope de 38vw (disco de 299 px a 1440×900, 251 a 1280×720,
     399 a 1920×1080) y la estación mide 361×282 px a 1440×900 —como la de la banda original—; RIA / LABS va debajo
     del conjunto, subido 5vh sobre la aureola de abajo (sólo aureola: la flama queda arriba), y la frase al pie. La
     estrella de luz no asoma sobre las bridas (±25° del eje de la cañería). De día (`?tema=dia`) el reactor es el sol
     encendido y la química se ve sobre la fotósfera. **Por qué es el de por defecto:** es el que mejor usa la
     pantalla —el eclipse deja de ser una figura aparte que se come 400 px de alto y pasa a ser el motor del dibujo,
     así el dibujo se ve del tamaño de la original y el eclipse, más grande que antes— y el que más sentido tiene: la
     química vuelve al centro del eclipse, donde nació en la primera v5, y la página dice en una sola imagen lo que
     dice la frase.
  3. **Lockup y escenario** (`?hero=3`). El eclipse chico (`clamp(120px, 23svh, 240px)`: disco de 113 px a
     1440×900) a la izquierda de RIA / LABS, a la altura de la R, como un logo horizontal arriba; la máquina, con su
     propio reactor, toma el escenario grande de abajo (1.350 px de ancho a 1440×900, g 1,22: un 30 % más grande que
     la banda original; 1.192 a 1280×720). El dibujo se ve más grande que en ningún otro; el eclipse pierde
     protagonismo. La estrella sólo asoma del lado de afuera (del lado del logo, los rayos cruzarían la R).

  **Móvil (≤860 px).** La máquina va vertical y compacta: la estación girada arriba, el reactor (o el eclipse) al
  medio, la constelación apretada a lo largo del flujo (0,6 en el 1 y el 3, 0,78 en el 2) y Analítico y Automoción
  rotulando hacia afuera, Espacios abajo (centradas bajo sus nodos se pisaban). En 390×844: el **1** muestra eclipse
  (disco de 107 px) · RIA / LABS · la máquina vertical de ~165 px de ancho (se reconoce, pero chica: g 0,43) · la
  frase; el **2**, la máquina vertical con el eclipse como reactor al medio (disco de 119 px, estación de 144×184),
  RIA / LABS y la frase; el **3**, el lockup arriba (disco de 64 px, RIA a 49 px) y la máquina vertical más grande de
  las tres (g 0,63), con la frase al pie. Las tres entran enteras; en 390×664 (Safari con sus barras: el `svh` real
  de un iPhone) también, con la máquina chica (g 0,29–0,45).

  Verificado en ventana real (sin el alto fijo que el script de captura le pone al hero): 1440×900, 1280×720,
  1920×1080, 1440×760 y 390×844 (y 390×664, 768×1024, 1024×768 y 900×600), en noche, `?tema=dia` y reduced-motion,
  sin errores de consola; en todos el pie termina dentro de la pantalla. Capturas en `_capturas/hero-pantalla/`
  (ignorado). `scripts/capturar-home.sh` suma `PANTALLA=1` (una pantalla real de `ANCHO`×`ALTO`), `RM=1`
  (reduced-motion) y un perro guardián para cuando Chrome headless se cuelga. Entre 861 y ~1.000 px de ancho la nav
  se parte en dos líneas: viene de antes y queda fuera de esta rama.
- **Los productos son la espina.** Se fueron las secciones *Servicios* (cuatro líneas de consultoría) y
  *Mercado* (radial de seis rubros): describían una consultora, no la empresa de producto que es hoy. Su
  mensaje útil («partimos de lo que ya tenés») pasó al hero, a la banda de Dataflow y al método.
- **Tres verticales, una palabra cada una, con su definición de diccionario** bajo el nombre (regla fijada
  por Matías con *Automoción*: una sola palabra en español con sentido profundo):

| # | Nombre | Definición mostrada (fuente: RAE) | Qué agrupa | Color | Sitio |
|---|---|---|---|---|---|
| 01 | **RIA Analítico** | *analítico, ca.* Perteneciente o relativo al análisis. Que procede descomponiendo, o que pasa del todo a las partes. | seguridad: los dos brazos **Integradores** y **Monitoreo** | `#4a8fd4` azul | analitico.rialabs.ar |
| 02 | **RIA Smartcity** (fue RIA Espacio y RIA Espacios del 10 al 29/10) | *espacio.* Extensión que contiene toda la materia existente. Parte de esa extensión que ocupa cada objeto sensible. Capacidad de un lugar. | los **sabores** de smartcity: Ciudad · Predio · Acceso · Barrio y centro comercial | `#2fd0c8` teal | smartcity.rialabs.ar |
| 03 | **RIA Automoción** | *automoción.* Facultad o condición de lo que se mueve por sí mismo. Estudio o descripción de las máquinas que se desplazan por la acción de un motor y particularmente de los automóviles. | la concesionaria (antes **RIA Drivecore**; la página lo dice debajo del nombre) | `#EF9F27` dorado | drivecore.rialabs.ar |

  Los nombres públicos de los sitios de destino todavía dicen *Byte Analítico* y *RIA Drivecore*: la home
  usa los nombres nuevos y enlaza a esos sitios tal como están. Renombrarlos es una pasada aparte.
- **El hero dice «Metaestructura» y abajo va una frase, no una explicación** (rama `hero-texto`, 2026-10-13;
  pedido verbatim de Matías en `docs/prompts-usuario/2026-10-13-metaestructura.md`: *«el texto "de ver a saber"
  y toda la explicacion de abajo me resulta muy ñoño. Prefiero expresar una idea con un titulo y una frase. El
  titulo es " super estructura" con una fuente destacable pero amable, mas cercana a la idea de la onda
  dataflow»*). El titular es **una sola palabra, «Metaestructura»**, como la usa la frase, en sentence case (en
  mayúsculas se volvía afiche: se probó), en **M PLUS Rounded 1c 800** —la misma redonda pesada que titula la onda
  en `dataflow.rialabs.ar` (sitios `lambda` y `ver-dataflow` de `dataflow-expresiones`, variable `--redonda`),
  así el parentesco con Dataflow es real y no un parecido—, tracking −0,018 em como allá, 56 px en desktop y 38 en
  un celular, siempre en una línea (`white-space: nowrap`; a 390 px mide 306 px). Se probaron en captura, sobre el
  hero real con el eclipse y RIA / LABS en Saira arriba, nueve variantes (M PLUS Rounded 1c en sentence case y en
  mayúsculas, Nunito 800, Fredoka 600, Zen Maru Gothic 700, Rubik 700, Red Hat Display 700, Baloo 2 800,
  Quicksand 700): Nunito es la misma idea con menos carácter y sin el vínculo; Baloo 2 tiene más personalidad
  pero tira a cómic; Fredoka es juguetería; Zen Maru es amable pero liviana, no destacable; Rubik y Red Hat
  Display son geométricas corporativas y pierden la onda; Quicksand es demasiado fina para un display. La fuente
  se carga con un `<link>` propio de Google Fonts con un solo peso (`wght@800`). **Cormorant Garamond se fue**
  con el titular y la prosa viejos: no quedaba en ningún otro lado.

  Debajo, en lugar de la prosa, **la frase de Matías tal cual**, en `<blockquote class="hero-cita">` con sus dos
  párrafos (las comillas internas de «Señor Presidente…» pasan a tipográficas ‘ ’; el bloque no lleva comillas
  propias, la comilla grande ya es la cita):

  > Miren, tenemos gente increíble trabajando en esto. Los mejores ingenieros, tipos verdaderamente brillantes, de
  > los que nadie había oído hablar antes, pero son genios absolutos. Y me dijeron: ‘Señor Presidente, tenemos algo
  > tan grande, tan revolucionario, que va a cambiar el juego para siempre’.
  >
  > Le llamamos Metaestructura. Suena bien, ¿verdad? Metaestructura. Suena fuerte. No es una de esas ideas débiles
  > y ridículas de la vieja política que cuestan trillones y no sirven para nada. Esto es real. Es hormigón, es
  > acero, es tecnología digital de última generación, y **está hecha en RIA Labs**.

  Es un parlamento, así que se lee como tal: columna de ~80 caracteres (620 px) **alineada a la izquierda** dentro
  del hero centrado, Saira 300 a 16 px con interlineado 1,72 (15 px / 1,7 en el celular), una **comilla de
  apertura grande** colgando a la izquierda del bloque (la “ de la misma M PLUS Rounded, 104 px, dorada al 42 %;
  en el celular va en una fila propia bajo el titular, a 68 px, porque colgando se montaba sobre la S) y la
  última cláusula en blanco como los `strong` del resto de la página. Medidas: el hero mide 1.214 px en 1440×900
  y 1.230 en 390×844 —lo mismo que antes: la frase más larga se absorbió con el cuerpo más chico y la columna más
  ancha—; sin scrollear se ven el eclipse, el wordmark, el titular y las primeras tres líneas de la cita (cinco en
  el celular); los CTAs siguen debajo del pliegue. Con el control de audio visible el hero crece 45 px.

  **La frase hablada.** Matías va a generar un audio de la frase (dicho por Donald Trump) y entregarlo después; el
  mecanismo ya está: **`assets/metaestructura.mp3`** (y, opcional además, `assets/metaestructura.ogg`) —ese
  nombre exacto, en esa carpeta, y se activa solo—. Al cargar, un `HEAD` al mp3 decide: si no existe, no se ve
  nada. Si existe, **al posar el mouse sobre la cita suena y al salir se pausa y rebobina**; como sin un clic
  previo en la página los navegadores rechazan `play()` (política de autoplay), el error se traga en silencio y
  queda un **botón chico en mono, «escuchar ▶»**, a la derecha del bloque, que alterna reproducir/pausar y sirve en
  touch; después de cualquier clic en la página el hover ya suena. Lo que arranca el botón no lo corta el mouse al
  salir (termina solo); mientras suena, la comilla grande se enciende. `preload="none"`: no descarga nada hasta
  que se pide. `prefers-reduced-motion` no cambia nada. Script: sección «LA FRASE HABLADA», al final del
  `<script>` principal.

  Los metadatos se alinearon con el titular: `<title>`, `og:title` y `twitter:title` dicen **«RIA Labs —
  Metaestructura»** y el «Un motor, tres productos, un laboratorio» de antes pasó a las descripciones (la `meta
  description` arranca con «Metaestructura: un motor, tres productos, un laboratorio…»). `og-image.png` queda por
  regenerar con el titular nuevo (§0.3; el modo OG del script ya esconde `.hero-cita`). El titular anterior («DE
  VER A SABER», del 10 al 13/10, en Cormorant Garamond) y su prosa quedan como históricos en §1.4.
- **El eclipse manda, solo, y es cinemático** (rama `eclipse-cinematico`, 2026-10-12; pedido verbatim de
  Matías en el registro de prompts: *«emular un eclipse en modo cinemático… emulando la inigualable naturaleza
  de los fenómenos del universo. El movimiento hacia la izquierda y la vuelta por la derecha se mantiene, pero
  la imagen también tendría que ser cinemática acorde»*). En el hero es la figura de portada: el eclipse total,
  sin nada alrededor. (La primera v5 lo rodeaba de un *sistema* de tres órbitas con un planeta por producto;
  Matías lo descartó el mismo día: «las órbitas no van, el eclipse es total y figura de la portada». Hasta el
  11/10 era vectorial: anillos de trazo, halos planos, una corona que respiraba y un enjambre de partículas
  adentro de la luna.) Ahora es **un eclipse solar total como lo muestra la naturaleza y lo filmaría una
  cámara**, armado en capas para que el ciclo del desenclipsar siga funcionando igual:
  - **La corona es una fotografía** (`assets/eclipse-corona.webp`): generada con `google/nano-banana` como
    astrofotografía de la totalidad (streamers finos y asimétricos, largos hacia el ecuador y cortos en los
    polos, protuberancias rojas en el limbo, luz blanco-dorada que se funde en ámbar y en negro) y pasada a
    **WebP con alfa desde la luminancia** (negro → transparente): así se funde con el cielo de estrellas sin
    `mix-blend-mode` —que adentro del stacking context del hero taparía el cielo con un cuadrado negro— y sin
    recuadro en ningún tema. Va en HTML debajo del SVG (`#sis-corona-img`), centrada en el sol, y su tamaño
    sale del disco medido en la imagen (r = 0,1515 del lado ↔ 91,5 unidades del viewBox de 340: la luna, de
    r 93, la cubre siempre). Dos copias: la de base respira (9 s); la otra, al 28 %, gira ±1,1° en 70 s —el
    shimmer de los filamentos—. Tres protuberancias en SVG, sobre las de la foto, parpadean a períodos
    distintos. Si la foto no carga (`onerror` → `.sin-corona`), vuelve el halo vectorial de antes.
  - **La luna es negra** (`#sis-moon`, gradiente casi negro con un hilo cálido en el limbo), centrada en el sol
    y librando apenas (1,2 unidades en 28 s, siempre adentro del disco negro de la foto). Ya no deja ver un filo
    de sol ni lleva el enjambre de partículas: en la totalidad la luna es negra. Al hover, un hilo de luz fuera
    del limbo (`#sis-anillo`), la pista de que se toca.
  - **La fotósfera es una foto del sol en luz blanca** (`assets/eclipse-sol.webp`: oscurecimiento al limbo,
    granulación, dos grupos de manchas), calzada sobre el disco r 93 que el ciclo mide, con el gradiente de
    antes debajo como fallback. Se enciende cuando la luna lo destapa, con un resplandor amplio sin festones
    (los arcos punteados de 150 de ancho que hacían la mancha festoneada del día se fueron), 18 rayos afilados
    de largo desparejo que giran en 540 s y un destello anamórfico horizontal.
  - **Perlas de Baily y anillo de diamante** en los contactos (`#sis-perlas`, `#sis-diamante`): las perlas a
    q = d/R ≈ 0,03–0,16, el diamante a q ≈ 0,1–0,3, los dos en el punto de contacto (el grupo de perlas se
    rota hacia él, el diamante se traslada). El diamante: núcleo blanco, su resplandor y un destello anamórfico
    horizontal largo, como lo da la lente.
  El SVG `#sistema` conserva el viewBox recortado al eclipse —`310 70 340 340` sobre el sistema de
  coordenadas original, el centro sigue en 480,240— y el tamaño lo da el CSS: `min(400px, 78vw, 44vh)` de
  ancho, o sea un disco de ~218 px de diámetro en desktop y ~166 en un celular (desde el 14/10 lo da cada
  encuadre del hero: ver «El hero entra en una pantalla»), con la corona desbordando
  (177,6 % del ancho; los streamers largos llegan a ~2,6 radios; en 390 px el borde del viewport los corta
  como el cuadro de una cámara). Pesa 248 KB en total (corona 150 + jpg de respaldo 37 + sol 20 + luna 22),
  sin dependencias ni rAF nuevo: el movimiento de la corona es CSS (compositor) y el de las protuberancias,
  SMIL; `prefers-reduced-motion` deja la foto quieta y una sola copia. Los gradientes `sp-*` siguen en sus
  `defs` porque los usa el diagrama de Dataflow. Vuelve en la banda de Dataflow como el motor, en el
  separador de Equipo (Byte y VRIO, heredado de v4) y en los dos retratos: esos siguen vectoriales. Cómo se
  generó, qué se eligió y qué costó: §0.3.
- **Pulido del hero** (rama `hero-pulido`, 2026-10-13; pedido verbatim de Matías en el registro de prompts: *«el
  juego del click y la orbita del ente eclipsante lo vamos a apagar por ahora… la flama en el aureola del eclipse es
  exagerada, prefiero que no haya flama o si la hay que sea ecuanime en todo el diametro de la circunferencia y muy
  sutil, y en movimiento… si cada tanto puede asomar una estrella de luz… la screen 2 es una idea que me gusta como
  logo»*; las tres capturas de referencia quedaron en `_capturas/referencias-eclipse/`, fuera de git). Cinco cosas:
  - **La corona es una flama ecuánime, procedural.** Fuera la foto con streamers (`assets/eclipse-corona.webp` queda
    en el repo, pero la página ya no la carga). En su lugar un `<canvas>` (`#sis-flama`, script «FLAMA») debajo del
    SVG, centrado en la luna y siguiéndola en su libración, así el aro queda parejo: para cada ángulo, un hilo de luz
    amarillo pálido pegado al limbo (una campana de 1,5 px a 0,9 px del borde negro, con el brillo modulado ±8 %) y una
    lengua corta —de 4,5 a 17 % del radio— que va del amarillo pálido al ámbar, al naranja y al rojo, cuyo largo sale
    de dos octavas de ruido periódico: 48 y 144 puntos de control alrededor del aro, cada uno pasando de un valor al
    azar al siguiente (smoothstep) en 1,4–3,2 s y en 0,5–1,2 s, y las dos octavas derivando despacio en sentidos
    opuestos (una vuelta en 240 s y en 150 s). Titila sin saltos y la turbulencia recorre el borde. Se pinta por píxel
    sobre una lista fija del anillo (distancia al limbo y ángulo de cada píxel, precalculada al medir: ~80 mil píxeles
    a 1440) con dos tablas de color, a 24 fps y sólo con el hero a la vista y la pestaña visible; DPR tope 2 y lado
    tope 640 px. Alrededor, `#sis-aureola`: un gradiente radial rojizo en CSS que respira en 7 s y de día se apaga.
    Las tres protuberancias rojas del SVG se fueron (la flama es pareja, sin accidentes). Sin canvas, vuelve el halo
    vectorial (`.sin-corona`). De lejos se lee como un aro de luz fino y vivo, no como fuego; de cerca, como la
    screen 3. Pesa cero: no hay imagen.
  - **La estrella de luz.** Cada tanto asoma en un punto del borde (`#sis-estrella`, script «ESTRELLA»): un núcleo
    blanco que crece en el primer tercio y se apaga en los dos restantes (3,2 s), seis rayos de lente finos con
    degradé a la punta (uno largo, de 150 unidades; el conjunto rota al azar ±45°) y un glare suave de 64 unidades.
    La primera a los 4,5 s de cargar; después a intervalos irregulares de 25 a 60 s, nunca dos seguidas a menos de 50°
    una de otra, sólo con el hero a la vista, la pestaña visible y en noche. `?estrella=<ms>` la fija en ese instante
    arriba a la derecha (1000 = el pico) para fotografiarla; `?estrella=no` la apaga. Con `prefers-reduced-motion`:
    sin estrella, flama quieta (un cuadro) y aureola sin respirar.
  - **El desenclipsar está apagado, no borrado.** `DESENCLIPSAR_ACTIVO = false` al principio de la IIFE: el ciclo
    entero sigue en el código, sin disparadores —ni clic en el eclipse, ni en el logo (que vuelve a ser sólo el enlace
    a `#inicio`), ni botón accesible, ni `aria-pressed`, ni cursor, ni la pista «tocá el eclipse»—. Los tres elementos
    del SVG (`#sis-anillo`, `#sis-hint`, `#sis-hit`) y el botón `.ecl-btn` salieron del DOM; un comentario en el hero
    los guarda textualmente y sus reglas CSS siguen. Los ganchos `?tema=dia` y `?ciclo=<ms>` andan para probarlo.
    Para reactivar: la constante en `true` y devolver esos cuatro elementos. Lo que no vuelve solo: el isotipo de la
    nav ya es el anillo y no tiene luna que acompañe el viaje (el ciclo lo tolera: `navLuna` queda en null). Las
    fotos del sol y de la luna viajera (`eclipse-sol.webp`, `eclipse-luna.webp`) ya no se descargan al cargar la
    página: van en `data-href` y el ciclo (o `?tema=dia`) las pide cuando las necesita.
  - **El logo es el anillo** (la screen 2; §9.3 y `logos/README.md`). En la página, con mesura: el isotipo de la nav
    (24 px, grosor 7,5 de 100 para que a ese tamaño siga siendo un aro), el pie (18 px, al 80 %), el `favicon.svg`
    (grosor 9) y el separador entre Equipo y Contacto (58 px). El hero sigue siendo el eclipse grande, no el logo.
  - **Fuera Byte × VRIO** (pedido de Matías del mismo día: *«vamos también a sacar las menciones a Byte y a VRIO de
    la página»*): la línea `.hero-origin` del hero («Byte × VRIO», con enlaces a compu-byte.com.ar y vrio.ar) se fue
    con su CSS; el pie dice «© 2026 RIA Labs · Rosario, Argentina»; el separador orbital de Equipo (los planetas Byte
    y VRIO alrededor del eclipse, heredado de v4, con sus gradientes `vrio-grad`/`byte-grad` y su script) es ahora
    el anillo solo (`#equipo-anillo`). Quedan para otra pasada la meta description («Nacidos de Byte y VRIO»), las
    bios de Equipo (la casa Byte de Sebastián, VRIO Estudio en la de Matías) y el Laboratorio («dos puertas en
    Rosario»).
- **Cada vertical es un astro vivo con sus sabores en órbita** (viñeta `.prod-vis` de cada banda, SVG propio de
  480×400, vanilla; la superficie la arma y la mueve el script, según `data-astro`). El astro lleva la tecnología
  de la vertical en su superficie, en línea técnica sobre la esfera, no como ícono, y **se mueve**: mirarlo es
  ver actividad, nunca algo central ni invasivo. Períodos largos y desfasados entre sí; nada acumula estado,
  todo es función del tiempo. (Rama `astros-vivos`, 2026-10-11, sobre el pedido de Matías: sin líneas de órbita,
  un ojo y no un lente de cámara, la red desde el centro hacia afuera, para Automoción lo más parecido a una
  máquina posible, y que las tres tengan movimiento.)
  - **Analítico es un ojo que lee.** Párpados en almendra con su pliegue, esclerótica clara, iris de dos capas
    de fibras (66 líneas que giran lentísimo en sentidos opuestos, 160 y 230 s por vuelta) con criptas oscuras,
    pupila que respira (9 y 23 s) con la corona dorada de la casa alrededor, 12 destellos que aparecen y se
    van. La mirada se corre apenas cada 2,6–7 s (una sacada de 220 ms; algunos tramos siguen algo que pasa) y
    parpadea cada 4,5–11 s (18 % dobles; cierre en 110 ms, apertura en 210; el párpado de arriba hace casi
    todo el cierre). La abertura respira en 41 s.
  - **Espacio es la ciudad que se enciende desde el centro.** Sobre la trama fija del globo, una malla de
    manzanas proyectada en la esfera (grilla de 12,5° rotada 28°, con manzanas vacías y aristas faltantes por
    azar determinista; queda sólo lo conexo al origen). Cada 9,5 s sale una onda del centro —apenas corrido
    hacia el sol, para que se vea— y llega a la periferia en 4,2 s: las aristas se dibujan y los nodos se
    encienden al pasar la onda, y después decaen a un fondo encendido. Siete pulsos recorren rutas que siempre
    se alejan del centro (6,5–13 s cada uno). La primera onda construye la red; las siguientes la reavivan.
  - **Automoción es una máquina en marcha.** Chapa remachada con costuras biseladas, un tren de tres
    engranajes engranados (24, 14 y 10 dientes, mismo módulo; A da una vuelta cada 44 s y mueve a B y C **al
    revés**, a 24/14 y 24/10 de su velocidad), biela y pistón sobre el eje de B, un volante con rayos movido
    por correa desde la polea de A (34,6 s por vuelta, la relación real de las poleas; la correa corre a la
    velocidad de la polea), una tubería con flujo, un manómetro cuya aguja oscila y tres testigos que titilan
    a períodos distintos. La luz del sol queda fija sobre los cantos.

  Un sol fuera de cuadro, arriba a la izquierda, ilumina los tres igual: terminador, filo de luz en el borde,
  y un halo tenue del color de la vertical. **La sombra que el astro proyecta no se dibuja**: en el espacio no
  hay sobre qué, y de día la cuña gris que tenía la primera versión cruzaba la viñeta como una mancha. Se ve
  sólo en lo que la atraviesa —los satélites, que se oscurecen al cruzarla—. El cuerpo del astro va en sus
  colores de noche en los dos temas (es oscuro siempre y lo ilumina su propio sol); los satélites, las
  etiquetas, la estela y el polvo sí siguen al tema. **Cada satélite es un sabor y un enlace** (`<a>` dentro
  del SVG, con `tabindex`, `aria-label`, halo al hover y al foco, y la estela se enciende) a la web de ese
  sabor:

| Vertical | Satélite (etiqueta visible) | Abre |
|---|---|---|
| Analítico | **Integradores** · cualquier cámara | analitico.rialabs.ar/integradores/ |
| Analítico | **Monitoreo** · la consola de la central | analitico.rialabs.ar/monitoreo/ |
| Espacio | **Smartcity** · ciudad | smartcity.rialabs.ar |
| Espacio | **Jockey** · predio | jockey.rialabs.ar |
| Espacio | **Grit** · barrio y centro comercial | grit.rialabs.ar |
| Espacio | **Acceso** · sin web pública | — (Rosental y Mercado Fisherton son instalaciones con login; el satélite existe, más chico y apagado, pero no enlaza) |
| Automoción | **Drivecore** · la concesionaria | drivecore.rialabs.ar |

  Profundidad: cada satélite recorre su propia órbita elíptica inclinada (la misma matemática que el
  separador de Equipo), pasa **por detrás y por delante** del astro con oclusión real (cambia de grupo en el
  DOM), crece hasta un 26 % al acercarse y se achica y se desenfoca al alejarse, se oscurece al cruzar la
  umbra, y la etiqueta se acomoda del lado de afuera (centrada debajo cerca de los bordes, para que en
  móvil no se corte). Detrás, 48 motas de polvo propias de cada viñeta con paralaje al scroll. **La órbita
  no se dibuja**: queda la estela del satélite, seis tramos cortos que se afinan y se apagan, cada uno delante
  o detrás del astro según le toque; al hover y al foco se alarga y se enciende. **Sumar un sabor es sumar
  un `<a class="sat">`** con su `data-orb` (`rx ry inclinación período fase sentido radio`): Estación de
  Servicio e Industria entrarán así en Espacio. Un solo `requestAnimationFrame` para las tres viñetas, que
  corre sólo mientras alguna está en pantalla (IntersectionObserver, 120 px de margen); `?t=<ms>` adelanta
  el reloj para fotografiar otro instante (`QUERY=t=5000` en `scripts/capturar-home.sh`; el reloj ya va por
  ~700 ms cuando Chrome fotografía, así que el primer parpadeo del ojo cae en `t≈9900`).
  `prefers-reduced-motion`: un cuadro compuesto y quieto (ojo abierto mirando apenas a la izquierda, red
  encendida entera, máquina detenida con un testigo prendido), sin transiciones.
- **El sentido del eclipse, dicho en la página.** Lo decía la banda Dataflow hasta el 12/10: *«Un eclipse es dos
  cosas que ya existían, alineadas por un instante. La luna es tu infraestructura. El sol es el motor. Lo que se ve es
  la corona: lo que la alineación deja pasar.»* Con la banda-onda la frase salió de la página (esa banda ya no
  explica); queda acá como texto de la casa por si vuelve en otro lugar.
- **El cielo.** Un `<canvas id="cielo">` fijo detrás de todo emula el espacio: ~360 estrellas a 1440×900
  (densidad por área), con profundidad —las cercanas son más grandes, más brillantes, se corren más con
  el scroll (paralaje) y con el mouse—, titilan con fase propia, derivan lentísimo, y cada 9–20 s cruza un
  meteoro. Colores: blanco cálido, algunas doradas, azules y teal. Las bandas de sección son translúcidas
  para que se vea a través. `prefers-reduced-motion`: cielo estático, sin meteoros, sin órbitas animadas.
- **Dataflow como onda** (rama `dataflow-onda`, 2026-10-12; reemplaza a la banda-historia del 10/10 —escenario
  sticky con el flujo en canvas y cuatro cuadros que pasaban con el scroll, ~3.700 px— que Matías descartó el 12/10:
  *«lo actual me parece grotesco y de mal gusto… prefiero que nos basemos en la idea y visual de dataflow.rialabs.ar,
  volver a la onda para explicar de qué se trata. Sin dar explicaciones sobre cómo… pero sí los números de las
  mediciones, que se eleven emulando el funcionamiento del motor»*). La banda `#dataflow` es ahora **una sola escena
  de ~775 px**: una ventana al universo Dataflow —la onda de la identidad, las tres cintas de `lambda`, cruzando la
  banda a sangre— y encima el tablero, seis contadores que **suben en vivo** proyectando lo medido en el tablero del
  motor. Palabras: *Dataflow · el motor* / **Todo sigue pasando** / *Lo que el motor lleva contado, ahora mismo.* y el
  enlace «Universo Dataflow ↗». Qué muestra, de dónde viene la onda, la tabla contador → base → tasa → fuente y cómo
  se fotografía: **§0.5**. Regla de marca intacta: un solo nombre público, *Dataflow*; la onda se muestra, no se
  nombra; *Datamotor* ya no aparece en la página. **Desde el 01/11 la banda ya no está en la home**: los contadores se
  mudaron a la página propia, `/dataflow/`, y la onda de colores se fue; en su lugar, el motor en pleno funcionamiento
  (§0.7).
- **La máquina** (rama `maquina`, 2026-10-13; pedido verbatim de Matías en el registro de prompts: *«mostrar una
  reproducción actualizada de la máquina de la página original de RIA Labs… haciéndola más mecánica y más química…
  esa química que existía en el centro del eclipse original de esta versión podría estar dentro de esta máquina»*).
  Banda propia `#maquina` a lo ancho, inmediatamente después del hero, **en el lugar de la barra de números**: la
  ilustración animada del hero de v4 (§9.4: infraestructura → eclipse → inteligencia; referencia en
  `_capturas/referencias-eclipse/screen4-maquina-v4.png`) reproducida en el lenguaje de los astros vivos (trazo fino,
  dorado, volumen sutil, piezas que se mueven de verdad). Fondo `--banda`, ~500 px en desktop; un SVG
  (`viewBox 0 0 1200 380`) que arma y mueve el script «LA MÁQUINA» (vanilla, sin dependencias); abajo, como pie de la
  imagen, los dos textos de la original: *Tu infraestructura ya existe.* (`--muted`) y **Nosotros la hacemos pensar.**
  (`--white`), con el mismo fade escalonado: la máquina aparece por partes al entrar en pantalla (estación 0,2 s ·
  primer texto 1 s · conducciones 1,5 s · reactor 2,1 s · constelación 2,8 s · segundo texto 3,4 s).
  - **Izquierda, la estación: lo que ya está, como piezas de una máquina.** Tres entradas reales —una **cámara** PTZ
    en su horquilla (panea ±20° en 26 s, el iris gira, el cono de visión respira, un testigo late), un **sensor**
    (plato, alimentador y mástil; emite tres anillos cada 5,5 s) y un **registro** (caja con dos carretes que giran y
    tres testigos)—, cada una con su cañería (sombra, cuerpo dorado y flujo punteado que corre) hasta un
    **distribuidor rotativo**: corona dentada de 21 dientes que da una vuelta cada 12 s, cuerpo fijo con tres puertas
    (215°, 180°, 145°) y un rotor de tres canales; un token pasa cuando un canal se alinea con su puerta (cada puerta,
    cada 4 s), va al centro y sigue por la cañería principal. La corona engrana un **tren de engranajes** del mismo
    módulo (A de 10 dientes a −45°, B de 8 sobre A, C de 10 a 110°; cada uno al revés del anterior, a la relación real
    de dientes): B lleva la **manivela** que mueve por biela la **bomba de pistón**, de pie sobre la cañería, y C mueve
    por correa un **volante** de cinco rayos (la correa corre a la velocidad de la polea). Sobre la cañería, una
    **compuerta** que levanta la hoja cuando un token se le acerca y la baja al pasar; antes del reactor, una
    **válvula** (cuerpo hexagonal, vástago y volante que gira una vuelta cada 40 s). Costuras con remaches y marcas de
    esquina, como la chapa del astro de Automoción. Los tokens llevan el color de su origen: cámara azul
    (`--maq-p1`), sensor teal (`--maq-p3`), registro violeta (`--maq-p2`).
  - **Centro, el reactor: el eclipse como cámara de reacción.** Aro de la totalidad (`--gold` + `--gold-hi`, r 100)
    con los halos de la casa afuera (`--h3…--h6`), el sol tapado como filo cálido (`--sol-tapado`) y la luna
    (`--luna`) como cámara: vectorial y de trazo, para dialogar con el eclipse fotográfico del hero sin competir.
    Bridas con bulones en la entrada y la salida, y un **manómetro** arriba a la derecha cuya aguja marca la presión
    real: la cantidad de enlaces formados adentro. **La química de tokens**, heredera del enjambre `sis-swarm` de la
    primera v5 y del acto 3 del manifiesto (se muestra, no se dice): una simulación de partículas a paso fijo (60
    pasos por segundo de reloj, semilla propia; determinista, así `?t=<ms>` da siempre la misma foto). Cada token que
    llega entra como partícula libre y deriva (paseo al azar, leve corriente hacia la salida, confinada al disco);
    dos libres que se acercan a menos de 11,5 unidades **se funden**: un destello blanco se expande, quedan unidas
    por un resorte a 13 unidades y, si una vecina está cerca, se cierra el **triángulo**; hasta 3 enlaces por
    partícula y 7 por estructura (triángulos, cadenas y mallas que se sostienen y vibran; las enlazadas llevan halo).
    Una estructura **madura** (≥4 nodos y 2,5 s sin enlaces nuevos, o un triángulo de más de 9 s) se enciende en
    blanco cálido, cruza hacia la brida de salida (una salida cada ≥9 s) y al atravesarla se vuelve **un pulso**.
    Población estable de 22–31 partículas; la banda arranca con 42 s de reacción ya andando (`PRE`), así la cámara
    está poblada al aparecer. Las partículas van en sus colores de noche en los dos temas: viven adentro de la
    cámara, que es oscura siempre.
  - **Derecha, la constelación: la inteligencia, resuelta en los tres productos.** Tres conductos dorados salen de la
    brida al **nodo mayor** de cada producto —**Analítico** (`--c-ana`), **Espacios** (`--c-esp`, al centro; el
    renombre a plural es del 13/10), **Automoción** (`--c-aut`)—, cada uno un `<a>` a su banda (`#analitico` ·
    `#espacio` · `#automocion`, con `aria-label`, halo al hover y al foco) y su nombre en mono. Quince nodos menores
    (cada tercero violeta) unidos por aristas dibujadas a mano, como en la original, más cuatro aristas doradas que
    respiran (6–11 s). El pulso viaja 1,7 s por su conducto (destino: nunca el mismo producto dos veces seguidas); al
    llegar, el nodo mayor late (el aro crece 4 unidades, un resplandor de 2,8 s) y manda dos o tres pulsos
    secundarios a sus menores, que se encienden y decaen en 5 s. De fondo, los menores titilan apenas, cada uno con su
    período, y la grilla tenue de la original cruza la banda.
  - **Técnica.** SVG inline; un solo `requestAnimationFrame` para todo (mecanismos, tokens, reacción, pulsos), que
    corre sólo con la banda a la vista (IntersectionObserver, 120 px de margen) y la pestaña visible; el tiempo real
    se vuelca en pasos fijos con tope de 100 ms por cuadro (una pausa no hace saltar nada). Todo color por variables de
    tema; las que no existían se definen en `.maq` con versión de día (`--maq-metal`, `--maq-osc` para rellenos
    oscuros, `--maq-tubo` para la sombra de la cañería —tostada de día, no marrón—, `--maq-vio`, `--maq-p1/2/3`,
    `--maq-flash`, `--maq-grilla`). **En ≤860 px la máquina gira a vertical**: la estación rota 90° (los dispositivos
    quedan en fila arriba), el reactor al medio y los productos en fila abajo (`viewBox 0 0 480 1040`, ~900 px de
    banda); el trazado se rearma al cruzar el breakpoint sin perder el estado de la reacción. (Desde el 14/10 el
    viewBox no es fijo: se calcula para la caja del hero, y la vertical es compacta; ver «El hero entra en una
    pantalla».) `prefers-reduced-motion`:
    un cuadro compuesto y quieto (la reacción a los 53 s, Analítico recién encendido), sin transiciones. `?t=<ms>`
    adelanta el reloj (`QUERY=t=20000 scripts/capturar-home.sh v5`). Gotcha: la regla de reduced-motion no puede
    declarar `transform: none` sobre los grupos del SVG, porque el CSS pisa el atributo `transform` que ubica la
    estación. Verificado el 13/10 en noche (t = 0 y t = 20 s), día, móvil y reduced-motion, sin `Uncaught`:
    `_capturas/maquina/` (ignorado). La dinámica se midió aparte con la simulación corrida en Node (300 s: máximo
    de estructura 7, un pulso cada ~10 s, presión 0,7–1,3).
  - **Qué pasó con la barra de números** (1 motor · 24 analíticas · 30 mil eventos por día · 1.100 vehículos activos;
    v4 traía cifras de mercado): se fue con esta banda. Repetía lo que la página ya cuenta: *un solo motor* lo dicen
    el título de Productos y la banda Dataflow; los eventos se cuentan en vivo en Dataflow (784.790 y subiendo, más
    fuerte que «30 mil por día»); los 1.100 vehículos activos siguen en el linaje del laboratorio (vía Automoción).
    **Las 24 analíticas y los 30 mil eventos por día en una instalación ya no se publican en la home** (siguen
    medidos; fuentes en §0.5). El count-up (`[data-countup]`) se fue con ella. Criterio intacto: si no está medido,
    no se dice.
- **La página del Laboratorio (rama `pagina-laboratorio`, 2026-11-01).** Matías, verbatim (en
  `docs/prompts-usuario/2026-11-01-home-en-paginas-y-oficina-rosario.md`): *«Todo lo que ea Laboratorio tiene que ir en
  su propia pagina, dedicada exclusivamente a laboratorio, y no en la pagina principal como hay ahora. Y hay que borrar
  los productos de laboratorio: RIA DIÁLOGO DEPORTES MAQUETA Y ESTACIÓN IA, que hoy no deberían estar allí. Aqui
  tambien cambiar el orden de "De aca salieron", poniendo: 1 SMARTCITY; 2 RIA analitico; 3 RIA Automotrices.»*
  **Qué es.** `laboratorio/index.html` se reescribió entero: la página de octubre (§5bis: cinco proyectos p01–p05, tres
  de los cuales ya eran producto, órbita, rail y «Seis reglas que no negociamos», con CSS propio) se fue, y en su lugar
  está la sección «nuestra casa» de la home (la entrada que sigue), con una página entera de aire. **La home ya no la
  tiene:** salieron `<section id="laboratorio">` con el divisor que la seguía (de la banda Dataflow se pasa al Método),
  el CSS «LABORATORIO · nuestra casa» y `#laboratorio video` del script de videos, que queda sólo para `#equipo`; la nav
  y el pie ya apuntaban a `/laboratorio/` desde 33563bb. **La base es la de la home, copiada tal cual** —fuentes, tokens
  de `:root`, el cielo, nav y menú móvil, botones, layout, reveal, el anillo con «Hablemos.» y el pie—, cada bloque con
  el comentario «copiado de v5/index.html (BLOQUE) el 01/11 — mantener igual». Nav con enlaces absolutos y
  `aria-current="page"` en Laboratorio (subrayado dorado; en el menú móvil, una rayita). Sólo noche. `<title>`
  «Laboratorio — RIA Labs»; description y og propios («Pasá, esta es nuestra casa: de dónde salió cada producto y qué
  estamos probando ahora, con los números medidos y los límites dichos por nosotros»); og:image, la de la home.
  **Secuencia:** `#casa` → `#puertas` → `#linaje` → `#expediciones` → `#metodo` → el anillo y «Hablemos.» (`#contacto`)
  → pie.
  - **La casa** (`#casa`): rótulo *Laboratorio*, **«Pasá, esta es nuestra casa»** a 96 px y el copete, que ahora dice
    «Todo lo que hoy es producto empezó acá…» y «Lo que funciona en la calle **se vuelve producto**, con cliente adentro»
    (en la home: «todo lo que está arriba», «se muda arriba»; acá no hay arriba). A la derecha, *La casa, por dentro*:
    el índice de las cuatro partes, cada una con su bajada.
  - **Las dos puertas** (`#puertas`, «La casa tiene dos puertas en Rosario»), cada una con un dibujo vivo. *La ochava*:
    «Donde la cámara de la esquina alimenta al motor las veinticuatro horas. Es la que le dio el verde al semáforo de la
    expedición 01 y la que, desde agosto de 2026, mide la esquina entera.» Dibujo: la esquina desde arriba —cuatro
    manzanas con su ochava, dos calles de una mano, sendas—, la cámara en la ochava con su cono, un semáforo que alterna
    (4 s de verde por mano, 0,6 de amarillo, 0,4 de todo rojo) y autos que frenan en la línea y guardan distancia; el que
    entra al cono queda en una caja verde. *El taller*: «Donde el motor se escribe: Dataflow (→ `/dataflow/`), el mismo
    debajo de los tres productos. Lo que la ochava ve, el taller lo vuelve pieza.» Dibujo: una ventana «dataflow · el
    motor» que se escribe sola, línea por línea, en los colores de los tres productos. Cierra a lo grande: «Y una sola
    regla de convivencia: **si no está medido, no se dice.**»
  - **De acá salieron** (`#linaje`): el orden pedido, **Smartcity · Analítico · Automotrices**; *RIA Automoción* pasa a
    **RIA Automotrices**; los planetas van a `/#smartcity`, `/#analitico` y `/#automotrices`; la búsqueda forense es
    «**en tu idioma**» (antes «en castellano»). El cierre de Smartcity decía «Ciudad · Predio · Acceso · Barrio y centro
    comercial»: **Predio salió** (era el Jockey, que sale de Smartcity; no se nombra) y la línea es la de los sabores de
    hoy, **«Ciudad · Centros comerciales · Country · Birdmap · EcoAceite. Midiendo 24/7 en Rosario.»** (Entrypoint y
    Acceso no tienen web y no se nombran).
  - **Expediciones en curso** (`#expediciones`): **fuera RIA Diálogo, Deportes, Maqueta navegable y Estación IA.**
    Quedan *Tránsito inteligente* (01, a lo ancho con el video de la ochava, igual que en la home) y *Fauna urbana* (la
    que se mudó). Para que la mesa siga armada con dos, Tránsito trae **su cuaderno**, rescatado del proyecto 04 de la
    página de octubre: *el mismo auto, dos sensores* (la espira contra la cámara, ahora **apilado**: un panel arriba del
    otro, así se lee en 390; escala 2,44 px/m, el borde izquierdo a 150 m de la línea de parada), *lo que midió* (−27 %
    de demora contra tiempo fijo · 15–18 ms de inferencia por cuadro, en la placa · 0 falsos positivos sobre asfalto
    mojado · 15 fps en el navegador, y las barras de anticipación 52 m / 150 m con la cita del manual de detectores de
    EE. UU.) y tres notas (*No se cambia el semáforo: se cambia el sensor* · *La zona de dilema, servida por ETA* · *El
    número espera a la muestra*). Fauna urbana: «la pregunta se mudó: hoy es Birdmap, en RIA Smartcity»; su puerta
    (*Hoy vive en* RIA Smartcity) va a `/#smartcity` y a **birdmap.rialabs.ar ↗** (en octubre no se enlazaba por no
    comercial; desde el 01/11 Birdmap es un sabor de Smartcity con su web).
  - **La puerta** (`#metodo`): «La puerta está abierta. Si tenés una pregunta que nadie midió todavía, contanos: así
    empezaron todos nuestros productos.» Botones **«Las seis reglas de la casa →»** (`/metodo/`; las reglas no se
    repiten acá) y «Ver los productos» (`/#productos`). Ya no está «Recorrer el laboratorio →»: es esta página.
  - **Enlaces viejos:** `/laboratorio/#metodo` cae en la puerta hacia `/metodo/`; `#p04` en Tránsito; `#p01`, `#p02` y
    `#p05` en las vías de Automotrices, Analítico y Smartcity; `#cierre` en «Hablemos.»; `#p03` (Comms) ya no existe y
    cae al principio. Fuera de la home sólo `v4/` (histórico) enlaza a `/laboratorio/#p0x`; en los otros proyectos de
    `Proyectos/` no hay enlaces a la página.
  - **Movimiento:** cada dibujo corre sólo a la vista y con la pestaña visible (`animar()` en el script); con
    `prefers-reduced-motion`, un cuadro quieto (el taller, escrito entero). El video de la ochava carga y arranca sólo a
    la vista. La lógica del semáforo se corrió diez minutos en Node: cero autos encimados.
  - **Qué no se trajo** de la página de octubre: lo que es producto (Drivecore, la analítica de video, Comms, Smartcity
    con sus capturas) vive en la home; el **video del tablero** (`traffic-dashboard.mp4`), porque su barra dice «Byte
    Analítico · cámara calle Byte» y el cuadro muestra −32,7 % (un instante; lo publicado es −27 %); y la «categoría ya
    validada» (−23 % de una empresa británica), que es argumento comercial. `laboratorio/media/` queda entera aunque
    `sc-*.jpg` y `traffic-dashboard.*` ya no los use ninguna página.
  - Capturas de la verificación (1440 y 390, reduced-motion, las anclas viejas): `_capturas/pagina-laboratorio/`
    (ignorado).
- **Laboratorio es la casa** (rama `laboratorio-casa`, 2026-10-10; pedido verbatim en el registro de prompts:
  «un laboratorio como un centro de experimentación y creación, más búsqueda y aventura, más imaginación y
  trabajo… más en nuestra cosa, nuestra casa»). *Fue sección de la home hasta el 01/11: desde entonces vive en
  `/laboratorio/` (la entrada anterior), con el linaje reordenado y sólo dos expediciones. Lo que sigue la describe
  tal como estaba en la home.* Antes era una grilla de seis fichas iguales con rótulo de
  estado («Lo que todavía es pregunta»), que presentaba el laboratorio como un backlog. Ahora la sección es
  **el origen**, en primera persona del plural y con los mismos números medidos, en tres partes:
  - **Titular:** *Pasá, esta es nuestra casa*. **Copete:** «Todo lo que está arriba empezó acá, con una
    pregunta que nadie había pedido medir. Acá se busca, se imagina y se trabaja: un cuaderno con patentes
    anotadas a birome, una cámara que mira la calle desde una ochava, un semáforo que se dejó manejar. **Lo
    que funciona en la calle se muda arriba, con cliente adentro. Lo demás se queda en casa, en prueba.**»
    Segundo párrafo: las dos puertas de la casa en Rosario, **Byte** (la cámara de la esquina alimenta al
    motor las veinticuatro horas) y **VRIO** (donde el motor se escribe), y la regla de convivencia, la misma
    de arriba: si no está medido, no se dice.
  - **De acá salieron** (el linaje): tres vías de cuatro hitos, una por producto y en su color, que se
    encienden de izquierda a derecha al entrar en pantalla (verticales en ≤860 px); el último hito es el
    planeta y enlaza a la banda del producto. Fuentes: `rialabs-manifiesto/docs/GUION.md` actos 0 y 1 (el
    cuaderno, la barrera, los seis pasos), `byt-edge` (LPR en producción desde 2026-03), `byt-fall`
    (local-first, primer recorrido completo 2026-05-15), `byt-analitico` (búsqueda forense, 2026-08),
    `byt-traffic-demo` (−27 %), `byt-smartcity` (la esquina 24/7 desde 2026-08), `byt-pajaritos` (demo 25/08).

| Vía | Hitos | Llega a |
|---|---|---|
| Automoción (`--c-aut`) | Un auto, una barrera, un cuaderno → La cámara leyó la patente → Se prototipó sobre el plano del taller | `#automocion` · 1.100 vehículos activos |
| Analítico (`--c-ana`) | La misma cámara del ingreso (procesada en un servidor remoto) → Todo en una PC, en el cliente → Buscar por lo que la cámara vio | `#analitico` · Integradores y Monitoreo |
| Espacio (`--c-esp`) | Un semáforo que ve → ¿Y si la esquina hiciera todo? → Las palomas de una plaza | `#espacio` · Ciudad · Predio · Acceso · Barrio y centro comercial |

  - **Expediciones en curso** (la bitácora): las seis exploraciones, cada una con **la pregunta que la
    abrió**, una cabecera mono con dónde se prueba y desde cuándo, **Hasta ahora** (lo medido) y **Todavía
    no sabemos** (el límite, dicho por nosotros). Grilla de dos columnas; Tránsito va a lo ancho con el
    **video real de la ochava** (`laboratorio/media/traffic-deteccion.mp4`, póster `.jpg`, `muted loop
    playsinline preload="none"`; arranca sólo a la vista y se pausa al salir; con `prefers-reduced-motion`
    queda el póster quieto). Fauna urbana cierra a lo ancho como **«la que se mudó»**, con la puerta a RIA
    Espacio («Hoy vive arriba»). Las fechas «desde…» salen del primer commit de cada repo; Tránsito dice
    «invierno de 2026» porque `byt-traffic-demo` no tiene git y el clip es de un día de lluvia de invierno.

| Expedición | Cabecera (dónde · desde) | Hasta ahora (el número) | Todavía no sabemos | Origen | Enlace |
|---|---|---|---|---|---|
| 01 Tránsito inteligente | la ochava de Byte, Rosario · invierno de 2026 | −27 % de demora contra tiempo fijo; 0 falsos positivos con lluvia | la ola verde (una sola cámara no la hace); calibración provisoria hasta medir con cinta | `byt-traffic-demo` | `/laboratorio/#p04` |
| 02 **RIA Diálogo** (antes RIA Comms) | una concesionaria de Rosario · desde mayo de 2026 | guardado, clasificado, ruteado y medido; audios transcriptos; lo usamos nosotros primero | cómo se llama (Diálogo es propuesta; la casa grande dice Comms) | `ria-comms` (Seprio sigue con el predecesor `seprio-comms`) | `/laboratorio/#p03` |
| 03 Deportes | una transmisión de tenis, en el estudio · desde septiembre de 2026 | la cancha se calibra sola, poco más de un píxel de error (mediana 1,34 px), recalibra tras cada corte; ve jugadora, jueza y recogepelotas, no la tribuna (`dataflow-deportes/docs/ESTADO.md`) | la pelota (~6 px a 720p); qué contar en los ~20 s entre puntos | `dataflow-deportes` | — |
| 04 Maqueta navegable | un barrio en Álvarez, un centro comercial en Rosario · desde septiembre de 2026 | 1.276 tramos del legajo real, 19 manzanas, el lago y el cerco; mouse, teclado, voz y gestos sobre un mismo vocabulario; repetido sobre el centro comercial sin tocar el motor | la primera cámara real; toda la actividad es simulada y la pantalla lo dice | `dataflow-smartcity-sapiens` / `-neander` | — |
| 05 Estación IA | un stand, una fiesta, una feria | selfie → personaje animado → QR; la gente ve al modelo trabajar en vivo | si es un juego o una pieza | `IA Fun Station` | — |
| La que se mudó · Fauna urbana | las palomas de una plaza · agosto de 2026 | conteo por punto en bandada densa; cada cifra medida o estimada; demo a la Municipalidad el 25/08 | qué fracción de la bandada ve la cámara en una plaza real | `byt-pajaritos` (birdmap.rialabs.ar es no comercial y no se linkea) | `#espacio` |

  - **La puerta:** «Recorrer el laboratorio →» (`/laboratorio/`), «Las seis reglas de la casa»
    (`/laboratorio/#metodo`) y una nota mono: «La puerta está abierta. Si tenés una pregunta que nadie
    midió todavía, contanos: así empezaron todas las de arriba» (→ `#contacto`).
  - **Estilo:** misma tipografía y paleta; la calidez viene del tono, de la composición y de la luz: un
    resplandor dorado (la lámpara de taller) detrás del título (`#laboratorio::before`, opacidad `--glow`,
    así se apaga de día como el del hero) y un filo del color de cada expedición arriba de su ficha. Todo
    color sale de las variables de tema; los acentos de las expediciones tienen versión de día (`--lab-c1…c6`,
    definidos en `#laboratorio`, no en `:root`). Sin dependencias; `color-mix` con fallback a `--border3`.
    Los pares de capturas noche/día de la verificación están en el scratchpad de la sesión, no en el repo.
  **Diálogo** es una propuesta de nombre por la regla de una palabra (RAE: *plática entre dos o más
  personas que alternativamente manifiestan sus ideas o afectos; discusión o trato en busca de
  avenencia*). Alternativa considerada: *Comunicación*. La página `/laboratorio/` todavía dice *RIA Comms*.
  Lo que quedó fuera a propósito: RIO (capa interna, sin posicionamiento público todavía), herramientas
  internas (faro, nx-server-monitor, meta-mcp, ria-wa-viewer, ria-quizz), presentaciones comerciales y
  trabajos para terceros (arg-tour-experience).
- **Método**: seis principios, tres heredados de v4 y tres traídos de las reglas del laboratorio
  (*Partimos de lo que ya tenés* · *Si no está medido, no se dice* · *Los límites los decimos nosotros* ·
  *Se instala, no se demuestra*).
- **Equipo**: retratos nuevos, verticales 4:5 de 210 px de ancho (en vez del círculo de 112 px), al lado
  del nombre; en móvil arriba. **Segunda pasada (rama `equipo`, 2026-10-10; pedido verbatim en el registro de
  prompts):** el título pasó de «Dos empresas consolidadas» a **«Dos oficios consolidados»**. VRIO no tiene
  producto ni cliente que mostrar y Matías no quiere llamarla empresa; *oficio* nombra lo que sí hay (el
  integrador con 25 años de campo, el programador desde 2001) sin repetir «trayectorias», que ya está en el
  copete. Descartadas: *ideas* (el ejemplo de Matías; una idea no se consolida, un oficio sí), *vocaciones*
  (suena a escuela o a sacerdocio y no dice que estén probadas), *talentos* (autoelogio), *trayectorias*
  (repite el copete), *caminos* (vago). El copete no cambió. Sebastián queda igual. **Matías se presenta por
  su carrera**, no por una empresa (bio en §7.1), y donde Sebastián tiene la casa (Byte · claim · sitio) Matías
  tiene el oficio: **Programador** · *Desde 2001 · Redeeem · Estados Unidos → Argentina*, sin enlace (la
  primera versión, «Programador desde 2001» en el slot grande, se partía en dos líneas a 1440). Retrato
  nuevo de Matías con otra actitud, y dos familias de retratos (con melena y sobria): §0.3.
  **Retratos vivos (rama `retratos-vivos`, 2026-10-11; pedido verbatim en el registro de prompts):** cada
  `.f-photo` es ahora un `<video>` en loop de ~10 s con el jpg de póster —quietos esperando la foto, pestañean,
  la melena vuela al viento de un ventilador, el eclipse chico y al fondo, el mismo en los dos— y el jpg adentro
  como fallback. Arranca solo a la vista, se pausa al salir, y con `prefers-reduced-motion` queda la foto. Cómo
  se hizo y qué se midió, en §0.3.
- **Nav** (el isotipo es el anillo desde el 13/10): Analítico · Espacio · Automoción (con el punto de color de cada uno) · Dataflow · Laboratorio ·
  Equipo · *Conversemos*. En ≤860 px hay botón MENÚ con panel desplegable (v4 escondía los enlaces).
- **Contacto**: el pre-título ahora es la pregunta del laboratorio («¿Tenés un problema que nadie resolvió?»)
  y vuelve el copete de cierre. Footer © 2026 (desde el 13/10, «© 2026 RIA Labs · Rosario, Argentina»: sin Byte × VRIO,
  y con el anillo delante del wordmark).
- **Desenclipsar: el eclipse se toca** — **apagado desde el 13/10** (`DESENCLIPSAR_ACTIVO = false`; ver el pulido
  del hero, arriba; lo que sigue describe el ciclo tal como queda en el código) (rama `desenclipsar`, 2026-10-10; pedido verbatim en el registro de
  prompts). Un clic en el centro del eclipse del hero, o en el isotipo + wordmark de la nav (que sigue
  llevando a `#inicio`), dispara **un ciclo completo, no un toggle**: la luna sale del disco hacia la
  izquierda en trayectoria elíptica —*destape*, ~2,5 s, en los que el sol se enciende (disco, resplandor,
  rayos sutiles) y la página se ilumina hasta el **tema día**—, sigue la elipse y cruza la pantalla entera
  iluminada del lado del sol (fase creciente a gibosa, lado oscuro que se funde con el fondo, borde definido)
  hasta salir por el borde izquierdo del viewport (~3,5 s); descansa en día (~8 s; un toque lo acorta);
  reaparece por el borde derecho, llega al sol (~3,5 s) y lo cubre (~3 s): anillo de diamante en el último
  filo, corona de totalidad, y la noche vuelve exactamente al estado inicial. Durante el viaje los
  disparadores no responden. Teclado y lectores de pantalla: un botón invisible calzado sobre el disco
  (`aria-pressed` = día, anillo de foco punteado) y un `aria-live` que anuncia «Tema día / Tema noche»;
  `prefers-reduced-motion`: sin viaje, fundido de tema con la luna desvaneciéndose en su lugar (~1,6 s).
  Una pista mono «tocá el eclipse» aparece una vez a los 3 s de cargar y se apaga sola. El isotipo de la
  nav acompaña el ciclo: su luna se corre y vuelve. Duraciones en `T` al principio del script `DESENCLIPSAR`.
  **Cinemático desde el 12/10** (misma línea de tiempo, otra imagen): la luna viajera lleva **textura lunar**
  en la cara iluminada (`assets/eclipse-luna.webp`, la luna llena generada y teñida al dorado del sol de la
  página; la fase la recorta como máscara con el terminador desenfocado y el limbo nítido, más una sombra
  suave hacia el terminador; el gradiente de antes queda debajo como fallback); la corona fotográfica y las
  protuberancias se apagan apenas asoma la fotósfera (con el sol a la vista la corona no se ve) y vuelven con
  la totalidad; en los dos contactos, perlas de Baily y anillo de diamante. Instantes para fotografiar con
  `?ciclo=<ms>`: 520 (perlas), 730 (diamante), 2600 (destape), 4200 (viaje, la luna a la izquierda), 16600
  (regreso por la derecha), 19700 (diamante y totalidad). El isotipo de la nav se rehízo para armonizar: una
  corona de luz con un streamer ecuatorial y la luna negra centrada (antes, anillos de trazo y la luna corrida).
- **Tema día.** `data-tema="dia"` en `<html>` conmuta las variables de `:root`: papel cálido `#f4efe4`,
  tinta `#1a1712`, el dorado sigue siendo el acento pero más oscuro (`#a66a06` / `#c47d0a`) para leerse
  sobre claro; azul, teal y dorado de producto oscurecidos; bandas, tarjetas y nav translúcidas en su
  equivalente claro (`--banda`, `--banda2`, `--tarjeta`, `--nav-bg`…); el eclipse en colores de tema
  (`--luna`, `--luna-cuerpo`, `--sol-tapado`; los halos `--h1…--h6` sólo sobreviven en el halo vectorial de
  respaldo del hero, el que se muestra si la foto de la corona no carga). El cambio es gradual y universal (`--t-tema`, que el ciclo ajusta a cada fase: 2,5 s al
  aclarar, 3 s al oscurecer con la totalidad); el cielo de estrellas se apaga en día. Decisiones: la elipse
  del viaje tiene su punto bajo en la luna del hero y sube hacia ambos bordes (ry = 16 % de rx); la
  geometría se lee del DOM en cada fotograma, nada de pantalla está hardcodeado; si el sol no está en
  pantalla (página scrolleada), la elipse se centra en el viewport y la viajera entra y sale con un
  fundido; desde el logo la luna sigue al sol aunque la página todavía esté scrolleando hacia él. Ganchos:
  `?tema=dia` carga en día con el sol encendido y la luna fuera (sin animar); `?ciclo=<ms>` congela el
  ciclo en ese instante. Dataflow y laboratorio se rehacen en ramas paralelas: toman el día de las
  variables de `:root`; sus colores fijos de `main` no se tocaron.

- **Sin Byte ni VRIO, y RIA Espacios (2026-10-13).** Matías pidió sacar de la página toda mención a Byte y a VRIO
  (ya no hay empresas que mostrar: los dos cofundadores cierran su ficha con su oficio). Se fueron: «Byte × VRIO» del
  hero y del pie, «Nacidos de Byte y VRIO» de la meta description, los planetas Byte/VRIO del separador de Equipo
  (hoy el anillo solo), el bloque de empresa de Sebastián (ahora **Integrador** · «Desde hace 25 años · seguridad
  electrónica · Rosario»; su bio dice «al frente de una empresa de seguridad electrónica e integración de sistemas»),
  «con VRIO Estudio entre sus emprendimientos» de la bio de Matías, y en el Laboratorio «la ochava de Byte» pasó a
  **«nuestra ochava»** y las dos puertas de la casa son «la ochava» y «el taller». Quedaban menciones en `/laboratorio/`:
  se fueron con la página nueva del 01/11. Y el producto **RIA Espacio pasó a llamarse RIA Espacios** («explica mejor la naturaleza de la
  versión reproducible en sabores»): nav, menú, banda, satélites, Laboratorio y metadatos; la entrada de diccionario
  sigue siendo *espacio.* en singular y el ancla `#espacio` no cambió para no romper enlaces.

- **«Metaestructura» (2026-10-13, más tarde).** Matías pidió cambiar «super estructura» por «meta estructura» donde se
  mencione. Se escribe en una palabra, como venía el titular: **Metaestructura**, en el `h1`, en la cita («Le llamamos
  Metaestructura. Suena bien, ¿verdad? Metaestructura.»), en `<title>` y metadatos, y el audio pasa a esperar
  **`assets/metaestructura.mp3`** (+ `.ogg`). La OG se regeneró. El prompt verbatim del 13/10 en `docs/prompts-usuario/`
  conserva la palabra vieja, porque el registro no se edita.

### 0.2 Secuencia de la página (anclas)

`#inicio` hero, una pantalla (eclipse · RIA LABS · `#maquina` · el pie «Tu infraestructura ya existe. / Nosotros la hacemos pensar.»;
en el encuadre por defecto, `?hero=2`, la máquina pasa a través del eclipse y RIA LABS va debajo; en el 4, `?hero=4`, el stand:
lo mismo más los retratos vivos de Matías y Sebastián en las esquinas de abajo, con nombre y oficio; en el 5, `?hero=5`, el
hero es sólo la portada —eclipse, RIA LABS, los dos retratos a los costados del eclipse y la expo— y `#maquina` con su pie
pasa a una banda propia, `#banda-maquina`, entre el hero y `#productos`) →
`#productos` (`#smartcity` · `#analitico` · `#automotrices`, con `#automocion` como ancla vieja) →
`#rosario` (antes `#equipo`, que queda como ancla vieja; §0.8. Dataflow, el Laboratorio y el Método se fueron a `/dataflow/`, `/laboratorio/` y `/metodo/` el 01/11, §0.7, §0.1 y §0.6) → `#contacto` (separador orbital) → contacto → footer.

Dataflow tiene página propia desde el 01/11: `/dataflow/` (§0.7); la banda `#dataflow` salió de la home.

### 0.3 Assets nuevos

| Ruta | Qué es |
|---|---|
| `v5/index.html` | la home vigente, autocontenida |
| `assets/retrato-sebastian.jpg` · `assets/retrato-matias.jpg` | **sin uso desde el 2026-11-01** (la sección Equipo pasó a ser `#rosario`, §0.8; quedan en el repo). Eran los retratos 720×900 (4:5) de la familia **con melena** (~120 KB y ~103 KB desde el 11/10, con el eclipse unificado): el **póster** de los retratos vivos y la foto que quedaba con `prefers-reduced-motion`. Los del stand de la portada son otros (`retrato-stand-*`) |
| `assets/retrato-sebastian.mp4` / `.webm` · `assets/retrato-matias.mp4` / `.webm` | **sin uso desde el 2026-11-01** (quedan en el repo, §0.8). Eran los **retratos vivos** de Equipo (2026-10-11): clips 720×900, 24 fps, en loop (9,67 s y 10,25 s), H.264 `yuv420p` sin audio + VP9. Sebastián 1,09 MB / 0,90 MB · Matías 0,83 MB / 0,65 MB |
| `assets/retrato-sebastian-sobrio.jpg` · `assets/retrato-matias-sobrio.jpg` | la familia **sobria**: los mismos retratos sin la melena (~82 KB y ~79 KB, con el mismo eclipse unificado). Para cambiar de familia alcanza con renombrar; la sobria no tiene clip |
| `assets/retrato-stand-matias.jpg` · `assets/retrato-stand-sebastian.jpg` | **retratos stand** (2026-10-31, segunda vuelta 01/11), el póster: 480×600 (4:5) JPG progresivo q84, 15 KB y 19 KB. Es **exactamente el cuadro 0** del loop de al lado, un momento neutro (ojos abiertos, boca en reposo). La familia sobria sin su eclipse chico, con el contexto de cada uno conservado y fundido **en redondo** hacia el cielo `#0b0a14` (viñeta elíptica centrada en la cara: cielo puro antes del borde, sin rectángulo), y una luz de borde dorada del lado que mira al centro de la portada: Matías va a la IZQUIERDA (borde a la derecha), Sebastián a la DERECHA (borde a la izquierda). Los usa el encuadre 4 de la portada (`?hero=4`, §0.1), que apunta a estos nombres. |
| `assets/retrato-stand-matias.mp4` / `.webm` · `assets/retrato-stand-sebastian.mp4` / `.webm` | los **retratos stand vivos**: posando, miran a cámara, **sonríen** (una sola sonrisa lenta por loop: se arma en ~2 s, se sostiene y se suelta en ~2,5 s) y pestañean; pelo inmóvil, contexto casi quieto. 480×600, 24 fps, loop de 18,04 s (Matías, 433 cuadros, sonrisa 0,8–8,8 s) y 17,92 s (Sebastián, 430, sonrisa 7,5–15,1 s), H.264 `yuv420p` sin audio + VP9, un solo keyframe. Matías 269 KB / 161 KB · Sebastián 331 KB / 205 KB (tercera vuelta, 01/11). |
| `scripts/generar-retratos-vivos.py` | cómo se hicieron el eclipse unificado y los retratos vivos (abajo): `fondo`, `video`, `post`, y `costura` para medir el loop; y la familia `stand` (`fondo-stand`, `medir-stand`, `vinetear`, `post <p>-stand`) |
| `assets/eclipse-corona.webp` · `.jpg` | **la corona fotográfica** (2026-10-12): WebP 1000×1000 con alfa desde la luminancia, 150 KB, el disco negro centrado a r = 0,1515 del lado. El jpg (37 KB) es la misma toma sobre negro. **Desde el 13/10 la página no carga ninguno de los dos** (la corona es la flama procedural); quedan en el repo por si el ciclo o la foto vuelven |
| `assets/eclipse-sol.webp` | la fotósfera en luz blanca, 720×720, alfa = disco (r = 0,4873 del lado), 20 KB. Desde el 13/10 va en `data-href`: se descarga sólo cuando el ciclo o `?tema=dia` la piden |
| `assets/eclipse-luna.webp` | la luna llena teñida al dorado, 720×720, alfa = disco, 22 KB: la cara iluminada de la luna viajera. Desde el 13/10, `data-href` como la del sol |
| `logos/ria-anillo-{color,blanco,negro,outline}.svg` · `logos/ria-anillo-lockup-horizontal-{color,blanco,negro,outline}.svg` | **el isotipo anillo** (2026-10-13, la screen 2 de Matías) y su lockup horizontal con el wordmark en Saira; §9.3 y `logos/README.md`. PNG de los cuatro isotipos a 256/512/1024/2048 en `logos/png/` (`bash logos/build-pngs.sh ria-anillo-color.svg …`, ahora con fallback a Chrome headless si no hay cairosvg). Los lockups no tienen PNG: sin Saira instalada saldrían con otra fuente |
| `favicon.svg` | el anillo (grosor 9 de 92, un poco más grueso que el de marca, para que a 16 px siga siendo un aro). Hasta el 13/10, el eclipse de halos de v4. `favicon.ico` y `ria-favicon/` siguen siendo los viejos |
| `scripts/generar-eclipse.py` | cómo se generaron y procesaron las tres (abajo): `corona`, `sol`, `luna`, `medir`, `post-*`, `hoja` |
| `og-image.png` | tarjeta 1200×630: el eclipse con la flama ecuánime + RIA Labs + «Metaestructura» en M PLUS Rounded (regenerada el 13/10 con `OG=1 scripts/capturar-home.sh v5`; el modo OG esconde la cita y el control de audio) |
| `scripts/generar-retratos.py` | cómo se hicieron los retratos (abajo) |
| `assets/oficina-rosario.jpg` · `.mp4` · `.webm` | **la oficina en video, de noche** (2026-11-02, rama `oficina-video`, §0.8): la esquina real de Donado y Chassaing llevada con IA (un piso más, paredes de vidrio con las cuatro salas encendidas y gente, carteles de RIA Labs) y animada. 1440×810, 24 fps, loop de 19,17 s (460 cuadros, dos clips Kling encadenados), viñeta hacia `#0b0a14` en el asset; H.264 `yuv420p` sin audio crf 22 `+faststart` + VP9 crf 32. 110 KB / 946 KB / 353 KB. El jpg es el cuadro 0 del loop (póster y lo que queda con reduced-motion o Save-Data). Es lo que muestra `#oficina` por defecto |
| `assets/oficina-rosario-dia.jpg` · `.mp4` · `.webm` | la misma oficina **de día** (`?oficina=dia`): la luz nublada de la foto. 1440×810, loop de 9,58 s (230 cuadros, un clip), 124 KB / 525 KB / 245 KB |
| `assets/oficina-rosario-concepto-noche.jpg` · `assets/oficina-rosario-concepto-dia.jpg` | **las imágenes concepto** de las que salen los dos videos, enteras y sin viñeta (1920×1072, 274 KB y 404 KB): la de noche cerrada y la de día. La página no las usa; quedan para que Matías elija la luz y para mostrar la oficina fuera de la home (son un concepto, no una foto: hay que decirlo donde se usen) |
| `scripts/generar-oficina-viva.py` | cómo se hizo la oficina en video (§0.8): `recorte`, `editar` (nano-banana / nano-banana-pro), `entrada`, `video` (Kling, `VIDEO=activo`), `post` (loop con fundidos, viñeta, exports, póster), `tira`, `vinetear`, `cuenta` y `recuperar` (cada predicción se anota con su id antes de esperarla: si la sesión se corta, se baja sin pagarla de nuevo). Importa los ayudantes de Replicate de `generar-retratos-vivos.py` |
| `scripts/capturar-home.sh` | fotografía la home completa con Chrome headless (desktop 1440 y móvil 390 por iframe; `OG=1` también la tarjeta, con el eclipse a 320 px; `QUERY=tema=dia`, `QUERY=ciclo=4200`, `QUERY=t=43200000` o `QUERY=estrella=1000` / `estrella=no` fotografía el día, un instante del ciclo del eclipse, la página con el reloj adelantado (astros y banda Dataflow) o la estrella de luz del hero fija en su pico / apagada (sin QUERY sale apagándose: la primera asoma a los 4,5 s y Chrome fotografía a los ~6); la QUERY aplica también a la tarjeta OG; `NOMBRE=dia` nombra los PNG; `ALTO=16000` para la página entera, que mide ~11.300 px en desktop desde el 13/10). Desde el 14/10: `PANTALLA=1` fotografía una sola pantalla real de `ANCHO`×`ALTO` sin fijarle el alto al hero (≤500 de ancho va por el iframe del celular y se recorta al cuadro), `RM=1` con reduced-motion, y el modo OG apila eclipse · RIA LABS · la frase en cualquier encuadre. Levanta su propio `http.server` en 8895–8899 y lo mata por PID (con `exec`, para que no quede suelto) |

**Retratos (2026-10-10).** Generados con `google/nano-banana` vía Replicate (token en
`~/.credentials/replicate.env`) a partir de las fotos reales de `~/dev/RIALabs/Fotos/` (`otra.jpeg` y
`1759492597591.jpeg` para Sebastián; `mati.jpeg` para Matías), con instrucción explícita de conservar
cara, edad, pelo, barba y anteojos. Los dos comparten la misma puesta: fotografía editorial, luz cálida
ámbar en la cara (la corona), relleno azul frío de pantallas, fondo negro, y **un eclipse total —disco
oscuro con corona dorada— flotando sobre la cabeza**. Cada uno en su terreno: Sebastián con un video wall
de cámaras de calle y un rack con LEDs azules; Matías con monitores de código y una maqueta 3D de ciudad.
Se generaron 3 variantes por persona (+3 de Sebastián con la composición unificada) y se eligieron
`matias-2` y `sebastian-b1`. Las variantes descartadas no se guardaron. Los retratos cuadrados de v4
(`equipo-*.jpg`) siguen en `assets/` porque v4 los usa.

**Retratos, segunda pasada (2026-10-10, rama `equipo`).** Matías pidió otro Matías: el de la mañana, frontal
y sereno, se veía frágil y «levemente afligido» al lado de un Sebastián sólido. Se generó de nuevo con
nano-banana desde la foto real (`mati.jpeg`), con la actitud escrita en el prompt —aventurero creador tech:
mirada directa, mentón firme, media sonrisa, hombros abiertos, torso girado 30° con los brazos cruzados, luz
ámbar lateral más dramática— y la identidad descripta con precisión (cara alargada, cejas marcadas, pelo corto
casi negro). Misma puesta que el par: estudio oscuro, monitores con código y maqueta de ciudad, el eclipse
sobre la cabeza. Lo aprendido, que `scripts/generar-retratos.py` documenta trabajo por trabajo: (1) pasar el
retrato anterior como referencia de puesta **ancla la pose** y devuelve el mismo Matías blando (4 de 4); va
solo la foto real. (2) El eclipse salía chico (≈16 % del ancho) y pedirlo más grande por texto no cambia nada
(3 de 3); sí funciona la **edición con dos imágenes** —la elegida más un retrato con el eclipse del tamaño del
par, «solo para el tamaño»—, que lo agranda sin tocar cara ni pose. Rondas: 6 (tres consignas) + 6 (dos
consignas) + 3 ediciones de eclipse fallidas + 2 con referencia; elegidos `m2-cruzado-2` → `m4-eclipse2-1`
(en el script, `matias` → `matias-eclipse`). Sebastián no se regeneró.

**La melena.** Pedido textual: «A Sebastián agregale una melena rubia contundente flameando en el viento, y a
Matías también pero como volando hacia atrás». Ediciones de nano-banana sobre el retrato terminado de cada
uno, con la consigna de conservar cara, anteojos, ropa, fondo y eclipse. Sebastián: 5 variantes, 3 le tapan la
cara y 1 es un copete eléctrico vertical; elegida `s-melena-1` (melena abierta a los lados y hacia arriba, cara
visible, el anillo detrás). Matías: 3 sobre la base provisoria y 3 sobre la final; en cada tanda 2 levantan el
pelo en vertical; elegida `m-melena-final-3` (pelo volando hacia atrás, hacia la izquierda del cuadro, el
eclipse grande visible). **Dos familias en `assets/`:** la **con melena**, vigente (`retrato-*.jpg`), y la
**sobria** al lado (`retrato-*-sobrio.jpg`: Sebastián el de la primera pasada, Matías el nuevo sin melena);
se cambia renombrando. Lectura de la sesión: la melena cambia el registro de editorial a épico con humor; a
210 px la de Sebastián tapa casi todo el eclipse y las dos fichas juntas se leen como afiche de banda; la
sobria es la que conversa con el resto de la página (números medidos, mono, contención). Las variantes
descartadas no se guardaron; `generar-retratos.py exportar <origen> <destino>` recorta al 4:5 y guarda
720×900 JPG progresivo q84.

**Retratos vivos (2026-10-11, rama `retratos-vivos`).** Pedido textual: «seriamos nosotros pero en vivo en lugar de en
foto.. segundos en los cuales pestañamos, nuestro pelo vuela suavemente con el viento, miramos a la camara en posicion
estatica como esperando la foto, pero se nota que estamos ahí» y «las melenas tienen que volar al movimiento de un
ventilador, moverse en el aire como simbolo de potencia y vision. Y los logos de RIA de fondo si estan presentes esta
bien pero debe ser siguiendo una idea comun en ambas imagenes y mucho mas de fondo». Tres etapas, las tres en
`scripts/generar-retratos-vivos.py`:

1. **El eclipse, una idea común.** Los cuatro jpg (melena y sobria) se reeditaron con nano-banana: eclipse chico (≈12 %
   del ancho), alto (centro a ≈14 % de la altura), centrado sobre la cabeza, lejos, desenfocado y apagado (un tercio del
   brillo), sin tocar cara, pelo, ropa ni luz. Por texto nano-banana no igualó el tamaño entre los dos (a Sebastián se lo
   hacía más chico) y pasarle el retrato de Matías como referencia le contagiaba el fondo (3 de 3); lo que sirvió fue
   escribirle los números medidos del de Matías y, donde faltaba, **igualar en post** (`igualar-eclipse`: escala el parche
   del eclipse en su lugar con máscara radial, sobre pared lisa). Elegidos: Matías `fondo-matias-1`; Sebastián
   `fondo-sebastian-4` igualado; sobrios `fondo-*-sobrio-2` igualados. 14 ediciones, US$ 0,55.
2. **El clip.** Imagen a video con el **mismo retrato como primer y último cuadro** (el truco del loop), 5 s, prompt común:
   cámara fija en trípode, pose quieta mirando a la lente esperando la foto, dos pestañeos, respiración, micro-movimientos;
   la melena al viento de un ventilador de estudio, fuerte y sostenido, sin taparle la cara; el fondo y el eclipse quietos,
   luz constante, misma identidad. Negativo: movimiento de cámara, cambio de cara o expresión, hablar, girar la cabeza,
   parpadeo de luz, pelo sobre la cara, fondo en movimiento. Se probaron **Seedance 1 pro** (`image` + `last_frame_image`,
   `camera_fixed`, 720p, US$ 0,30 el clip; 3 por persona) y **Kling v2.5 turbo pro** (`start_image` = `end_image`,
   US$ 0,35 el clip; 5 por persona). Los dos dejan el pelo quieto ~0,5–1 s al principio y ~1 s al final, y Kling en la
   primera ronda lo dejó casi quieto en 4 de 6; la segunda ronda (clips 4 y 5) lleva un párrafo de **viento fuerte**
   explícito («el viento es el elemento más fuerte del plano… en ningún momento el pelo cuelga quieto»). Se quedaron los
   Kling. 16 clips, US$ 5,30.
3. **El loop, en post.** Como un clip entero en loop tendría ~2 s de pelo congelado por vuelta, el loop se arma con el
   **tramo móvil de tres clips** por persona, cortados donde más se parecen (con la cara pesando ×25, para que las dos
   caras del fundido tengan los ojos igual) y fundidos en 6 cuadros (0,25 s). Nunca ping-pong. Matías: kling-2 → kling-4 →
   kling-5, 246 cuadros (10,25 s); Sebastián: kling-1 → kling-4 → kling-5, 232 cuadros (9,67 s). Efecto del peso de la
   cara: las tres juntas de cada loop (dos adentro y la del cierre) **caen bajo un pestañeo**, porque los pares de cuadros
   con los ojos iguales son los cerrados; el pestañeo esconde la costura, y en el cierre mide menos que un paso entre
   cuadros consecutivos (Matías 1,05 contra 1,06 de media; Sebastián 1,31 contra 1,92; `costura <persona>` lo imprime).
   H.264 `yuv420p` crf 24 `+faststart` + VP9 crf 34, 720×900, 24 fps.

**El póster es el jpg, y no salta.** Se midió si convenía que el póster fuera el primer cuadro del clip: no hace falta.
El cuadro 0 de cada loop está a un paso de la foto en la zona del pelo (Matías 2,5 contra 3,6 de paso medio entre
cuadros; Sebastián 3,4 contra 3,7); lo único que cambia al arrancar son los ojos, que se cierran: la foto pestañea y
queda viva. Y el jpg con los ojos abiertos es lo que ven `prefers-reduced-motion`, el headless y quien no llegue a cargar
el clip. El `<video>` va `muted loop playsinline preload="none"`, sin `autoplay`; la IIFE de videos de la página (la
misma de la ochava del laboratorio) lo carga y arranca al 25 % a la vista y lo pausa al salir; con reduced-motion no
observa nada. En headless el póster del tema día a veces no llega a cargar dentro del presupuesto de tiempo virtual y
queda el placeholder `SA`/`MG`: repetir la captura; no es la página.

Costo total de la pasada: ≈ US$ 5,85 (14 ediciones + 16 clips; si hubo generaciones fallidas no quedaron registradas).
Las variantes y los clips crudos quedaron en `_capturas/retratos-vivos/` (ignorado): `kling-*`, `seedance-*`, `fondo-*`,
tiras y primer/último cuadro de cada uno, y en `revision/` las piezas con que se verificó la costura final.

**El eclipse cinemático (2026-10-12, rama `eclipse-cinematico`).** Pedido textual de Matías: «De logo me parece mejor
intentar emular un eclipse en modo cinematico. Busquemos la mejor imagen de eclipse para esta version, cinemtica, emulando
la inigualable naturaleza de los fenomenos del universo. El movimiento hacia la izquierda y la vuelta por la derecha se
mantiene, pero la imagen tambien tendria que ser cinematica acorde». Técnica elegida: **capas, con la corona fotográfica
generada y el movimiento en CSS/SMIL encima**, no un video ni una corona procedural. Se descartó el loop de video (Kling)
porque en la realidad la corona está quieta durante la totalidad —lo que se mueve es la luna, y eso ya lo hace el ciclo—
y porque un mp4 no tiene alfa: para no tapar las estrellas habría que procesarlo cuadro a cuadro en canvas; el shimmer de
una segunda copia girando ±1,1° y el parpadeo de las protuberancias dan la vida que hace falta. La corona procedural en
canvas (ruido radial y streamers) se descartó por calidad: no llega a la foto. Generación, con `google/nano-banana`
(US$ 0,039 por imagen, salida 1024×1024, `scripts/generar-eclipse.py`):

1. **Corona.** Dos consignas, cuatro variantes cada una. `corona-a`: astrofotografía pura, compuesto HDR, streamers
   largos hacia el ecuador y plumas polares, protuberancias rosas, cielo negro sin estrellas. `corona-b`: la misma escena
   «a través de un teleobjetivo largo en una cámara de cine», con la luz blanco-dorada cerca del limbo fundiéndose en
   ámbar. Las A salieron más blancas y frías; las B tienen la temperatura de la casa. Elegida **`corona-b-4`**: corona
   interna densa y plumosa, dos streamers ecuatoriales largos, protuberancia roja a la izquierda y abajo a la izquierda,
   disco limpio. Segunda, `corona-b-3` (su banda derecha se lee como manchón). nano-banana hizo el disco al 24 % del cuadro
   y no al 40 % pedido; el post lo mide y no depende de eso.
2. **Sol** (2 variantes): la fotósfera en luz blanca con cuña de Herschel, limbo oscurecido, granulación, manchas con
   umbra y penumbra, sobre negro. Elegida `sol-2` (más oscurecimiento al limbo).
3. **Luna** (2 variantes): la luna llena por telescopio, mares y cráteres nítidos, gris neutro, sin terminador. Elegida
   `luna-1` (mares más ricos).

**El post, en PIL puro** (en la máquina no hay numpy; el script tiene que correr donde corre la captura): el disco se mide
con un flood fill desde el centro sobre la máscara umbralizada (radio desde el área, centro del bbox); la corona se
recentra, se recorta a 3,3 radios (826 px nativos → 1000) y el alfa sale del canal máximo con el ruido del negro (≤ 2,5 %)
a cero, des-premultiplicando el color (color·255/alfa) para que compuesta en normal sobre negro dé exactamente la foto;
un feather radial desde 0,86 del semilado lleva el alfa a cero antes del borde, y el disco de la luna también va a cero
(la página dibuja su luna encima). Sol y luna: alfa = disco antialiasado (dibujado a 4× y reducido); la luna se tiñe en
duotono (150,118,70) → (255,250,232). El primer tinte, con mares marrones (70,44,8) y la sombra del terminador al 82 %,
daba una bola oliva que de día se veía más oscura que su propia cara en sombra: la cara iluminada tiene que ser luminosa
sobre papel y sobre noche, y la sombra del terminador bajó al 42 %. **12 imágenes, US$ 0,47.** Las variantes, las hojas
de contacto y las capturas de verificación quedaron en `_capturas/eclipse-cinematico/` (ignorado).

Lo verificado en captura (desktop 1440, móvil 390, los dos temas, OG, y los instantes 520/730/2600/4200/16600/19700 del
ciclo, sin `Uncaught` en el log de Chrome): de noche la corona se funde con el cielo sin recuadro; de día queda el sol
con su resplandor sin mancha festoneada; la luna viajera cruza con su cara iluminada mirando al sol; las perlas y el
diamante aparecen en el punto de contacto; en 390 px el eclipse sigue dominando el hero y los streamers largos se cortan
en el borde del viewport como el cuadro de una cámara; con la foto rota vuelve el halo vectorial. Lo que queda dudoso:
en las capturas del ciclo el tema ya está en día desde el primer cuadro (el script congela las transiciones), así que el
diamante del destape (730 ms) se fotografía sobre papel aunque en el navegador ocurre todavía sobre noche; y el limbo de la
fotósfera de día es marrón, como lo trajo la foto, lo que se lee como oscurecimiento al limbo pero podría aclararse en post.

**La flama ecuánime, la estrella y el anillo (2026-10-13, rama `hero-pulido`).** Técnica y períodos en §0.1 (pulido del
hero). Se eligió el canvas procedural y no una imagen generada porque lo que Matías pidió es control —sutileza pareja y
movimiento sin saltos—, y una foto de nano-banana trae accidentes (lenguas largas, zonas más densas) que después hay que
disimular; además pesa cero y sigue a la luna. Lo verificado en captura (desktop 1440, móvil 390, noche con y sin
estrella, `?tema=dia`, `prefers-reduced-motion` forzado, OG y la página entera, sin `Uncaught` en el log de Chrome): de
noche el aro se lee fino, parejo y vivo, con el hilo pálido en el limbo y las lenguas cortas de ámbar a rojo; la estrella
asoma con su núcleo, sus seis rayos y el glare y se lee como la screen 1; de día queda el sol con su resplandor, la flama
y la aureola apagadas; con reduced-motion la flama es un cuadro quieto y no hay estrella; el anillo se ve en la nav, en el
pie, en el separador y en el favicon a 16/32/64 px sobre oscuro y sobre blanco; la página no descarga
`eclipse-corona.webp`, `eclipse-sol.webp` ni `eclipse-luna.webp` al cargar. Las capturas quedaron en
`_capturas/hero-pulido/` (ignorado). Lo que queda dudoso: la lengua más larga (17 % del radio) y el alfa del rojo se
calibraron mirando capturas fijas, no el movimiento; si en el navegador la flama se siente demasiado quieta o demasiado
viva, los diales son `LMIN`/`LMAX`, las duraciones de las dos octavas y la deriva (`omega`) al principio del script
«FLAMA».

**Retratos stand (2026-10-31, rama `retratos-stand`).** Pedido textual de Matías, el día antes de la Smart City Expo
Barcelona (3–5/11, los dos en el stand): «a cada costado del logo las imagenes de los ceos, Matias y Sebastian, en movimiento
como posando esperando que le saquen la foto con el parpadeo de ojos y todo, pero sin pelo agregado. La idea es mostrar los
CEOs que estan presentes en el stand como una primera vista cuando se visita la home de la empresa». Y al ver la portada:
«abajo de la maquina, del lado izquierdo, a la altura de RIA, pone la imagen viva de Matias desarrollador, y a la misma
altura pero del lado derecho, abajo de la red de sistemas, pone la foto viva de Sebastian de Byte». Tres etapas, las tres en
`scripts/generar-retratos-vivos.py` (familia `stand`); la portada que los usa es de la rama de la otra sesión.

1. **El fijo.** Parte de la familia sobria («sin pelo agregado»). Edición nano-banana con dos cambios y nada más: sacar el
   eclipse chico (en la portada hay un solo eclipse, el del hero) y agregar una luz de borde dorada, fina, del lado que mira al
   centro: derecha en Matías (va a la izquierda), izquierda en Sebastián (va a la derecha). El contexto que los identifica
   —«Matías desarrollador»: las pantallas de código y la maqueta; «Sebastián de Byte»: el muro de cámaras y el rack— se
   conserva. 3 variantes por persona, cara intacta en las seis (mirada cara a cara al 100 %); elegidas `fondo-stand-matias-1`
   (el borde más legible) y `fondo-stand-sebastian-3`. Antes de ese giro del brief se habían hecho 6 con **fondo liso** del
   color del cielo (`fondo-stand-plano-*`): salieron bien de parecido pero más gris-azules que `#0b0a14`; quedan en
   `_capturas/retratos-vivos/` como alternativa. 12 ediciones, US$ 0,47. Medido en los sobrios: la luz cálida de Matías entra
   por la izquierda del cuadro y la de Sebastián por la derecha, o sea que con los lados invertidos la clave de cada uno queda
   del lado de afuera y el borde dorado del lado del eclipse —dos luces, no una contradicción, pero queda anotado. **Nunca se
   espejó una cara.**
2. **El clip.** Kling v2.5 turbo pro, `start_image` = `end_image` (el truco del loop), 5 s, 1268×1632, 122 cuadros. Prompt:
   cámara fija, posando quieto mirando a la lente esperando la foto, dos o tres pestañeos, respiración, micro-ajustes de la
   sonrisa; **sin viento ni ventilador**, ni un pelo se mueve; el contexto en su lugar y casi quieto (a lo sumo un cursor, sin
   scroll ni cambios de contenido, porque la costura funde dos clips y un cambio de contenido se vería). 5 clips, US$ 1,75:
   Matías 1–3 y Sebastián 1–2. Pelo quieto en todos, fondo sin pulsos (cielo ×1,00–1,09, dif de fondo ≤ 1,6). Descartado
   `matias-1`: un pestañeo lento (0,4 s de ojos cerrados, se lee somnoliento) y una deriva de cabeza entre 1,3 y 2,5 s.
3. **El loop, en post.** A diferencia de la melena, los clips stand **no tienen cabeza ni cola congeladas** (contra el cuadro
   0 ya difieren 0,2 en el cuadro 2 y la diferencia crece suave): el tramo útil es el clip entero. Dos clips por persona
   (Sebastián 1 → 2, Matías 2 → 3), juntas elegidas por el par de cuadros más parecido con la cara pesando ×25 (empalman cuadros
   casi iguales: los dos clips salen de la misma foto), fundido de 6 cuadros. Como el cuadro 0 es el póster, el loop **se rota**
   al centro del segundo más quieto con los ojos abiertos (menor desviación máxima de los ojos contra su mediana en ±12
   cuadros): los fundidos quedan adentro y el cierre es un paso cualquiera. Después, la **viñeta** —rectángulo redondeado
   (norma 3), plena hasta 0,42 del semilado, a cero en 1,02, centro al 54 % de la altura— mezcla cada cuadro y el póster hacia
   `#0b0a14`, la misma en todos, para que la portada funda los bordes con el cielo con una máscara CSS. 480×600 porque van
   chicos (200–260 CSS px de alto) y en la primera pantalla. Sebastián 215 cuadros (8,96 s), Matías 229 (9,54 s).

**Lo medido.** A 192×240 (la escala de la portada) el cierre mide 0,55–0,71 contra un paso medio de 0,10–0,13: es **grano del
códec** (el I-frame contra el último P-frame; el mapa ×20 es ruido fino parejo, sin contorno), no un salto de imagen, y está
por debajo de 1/255. Póster ↔ cuadro 0: 0,67–0,76 (JPEG q84 contra H.264), ojos abiertos en los dos. La codificación salió de un
barrido sobre los PNG del loop de Sebastián: a crf 24 el mp4 pesa 135 KB pero cada cuadro queda a 0,90 del origen (ruido en la
viñeta); **crf 22 + `aq-mode=3`** (más bits a lo oscuro) baja a 0,79 por 216 KB, y crf 18 a 0,67 por 457 KB sin ganancia visible
a 240 px. VP9 crf 24 + `aq-mode 2`. **Un solo keyframe por loop** (`-g 999`): libvpx-vp9 metía uno en el cuadro 128, un «pop»
del mismo tipo que el cierre, adentro del loop. Si en el navegador el reinicio se nota, el dial es crf 18 (≈ el doble de peso).
Costo de la primera vuelta: ≈ US$ 2,22. Variantes, clips crudos, tiras, hojas de contacto y los PNG de los dos loops en
`_capturas/retratos-vivos/` (ignorado); `ladoalado-stand-final.png` y `hoja-final-stand.png` son las piezas con que se verificó.

**Segunda vuelta (2026-11-01): la sonrisa y el fundido redondo.** Matías, al ver la portada: «Saca los pequeños eclipses sobre
las cabezas de Matias y Sebastian y trata de redondear las imagenes de fondo de esas dos fotos. Los fondos de las fotos se
tienen que difuminar con el fondo de la pagina. Y recuerda hacer las fotos vivas, como dos personas que miran a la camara
sonrien y pestanean». Los eclipses ya no estaban en los clips (veía en caché los pósters provisorios y el server local no
servía `Range`, así que Safari no reproducía el video; lo arregló la madre). Lo que sí faltaba: la **sonrisa** de la primera
vuelta era mínima, con la boca cerrada —el prompt pedía «la media sonrisa se tensa y se relaja casi imperceptiblemente» y el
negativo llevaba «expression change, smile change, mouth opening»—, y la viñeta era un rectángulo redondeado que llegaba a
cero recién en el borde: sin máscara CSS se leía el rectángulo.

1. **Clips con la sonrisa como evento.** Mismo Kling, mismos fijos, prompt nuevo: posando, mirando a la lente, «rompe en una
   sonrisa cálida y franca: se arma en un segundo, los labios se abren y asoman los dientes, las mejillas suben y los ojos se
   arrugan; la sostiene un par de segundos y vuelve con suavidad a su media sonrisa serena al final» (el truco del loop exige
   volver a la foto). Negativo sin expresión ni boca; con «grimace, exaggerated smile, laughing». 4 clips, US$ 1,40 (Matías 4–5,
   Sebastián 3–4), **los cuatro sirven**: en todos la sonrisa aparece a ~1,1 s, abierta entre ~1,4 y ~3,3 s, de vuelta a ~3,6 s;
   pestañeos naturales, cabeza quieta, pelo inmóvil, fondo sin pulsos. Se lee «persona posando que sonríe a la cámara».
2. **El loop.** Dos clips por persona, dos sonrisas por loop (Matías 4 → 5: 227 cuadros, 9,46 s; Sebastián 3 → 4: 228, 9,50 s).
   Las juntas caen en tramos neutros (cola relajada ↔ cabeza antes de la sonrisa). El cuadro 0 (= póster) se elige ahora con
   **ojos y boca** en reposo (menor desviación contra la mediana por píxel de las dos zonas en ±12 cuadros): neutro, sin
   pestañeo ni sonrisa.
3. **Fundido redondo en el asset.** Viñeta **elíptica** centrada en la cara (centro al 44 % de la altura; plena hasta 0,28 del
   radio, `#0b0a14` puro desde 0,80; radios = semiancho y distancia del centro al borde de abajo): los cuatro bordes del cuadro
   miden (12, 10, 20) en el mp4, las pantallas de Matías y el muro de Sebastián se pierden en redondo, el torso se funde a la
   altura del pecho. Aunque no hubiera máscara CSS, no se lee ningún rectángulo. De paso, el cierre del loop a 192×240 bajó a
   0,35 (antes 0,55–0,71): la elipse deja más cielo puro y menos ruido de códec.

Costo de la segunda vuelta: ≈ US$ 1,40; la familia stand completa, ≈ US$ 3,62 (12 ediciones + 9 clips). Las tiras donde se ve
la sonrisa: `_capturas/retratos-vivos/retrato-stand-{matias,sebastian}-sonrisa.png` (los loops finales a 8 fps) y
`kling-*-stand-{3,4,5}-sonrisa.png` (los clips crudos); `hoja-final-stand-sonrisa.png` y `ladoalado-stand-sonrisa.png`, la verificación.

**Tercera vuelta (2026-11-01, más tarde): loops largos, una sonrisa lenta.** Matías, con la portada integrada: «Podemos hacer
que los videos de Sebastian y Matias sean más largos, y las sonrizas mas lentas? En loop, esos videos parece como que rien y
se ponen serios muy rapidos». Dos sonrisas de ~2 s cada 9,5 s se leían como reírse y ponerse serio.

1. **Clips de 10 s.** Kling acepta `duration` 10 con start = end (US$ 0,70 el clip). Prompt con la sonrisa repartida en el
   tiempo (`VIVO_STAND_LENTO`: ~2 s en reposo, ~3 en armarse «como un amanecer lento», ~3 sostenida, ~2 en volver) y negativo
   con «sudden expression change, fast smile, quick grin». Un clip por persona: `kling-matias-stand-6`, `kling-sebastian-stand-5`
   (US$ 1,40). Aun así Kling armó la sonrisa rápido: del 20 al 80 % del pico en 1,3 s (Matías) y 1,4 s (Sebastián).
2. **Plan B, `lento`.** Sólo el tramo de la sonrisa se estira con `minterpolate` (compensación de movimiento, no cuadros
   duplicados) y el resto queda a velocidad natural: `kling-*-lento.mp4`, 12,42 s y 12,12 s; la sonrisa sube en ~2,2 s.
3. **El loop de ~18 s** con `post`: el tramo de la sonrisa lenta más tramos neutros de la primera vuelta, y `SONRISA_EN` /
   `RECORTE` para ubicar la sonrisa y emparejar largos (subcomandos nuevos del script). Qué clips neutros y qué cortes exactos
   no quedó registrado: la sesión se cortó por cuota de Fable antes de anotarlo; los exports, las juntas
   (`_capturas/retratos-vivos/final/`) y el script son la fuente.

**Lo medido** por la madre sobre los exports (`costura`): Matías 433 cuadros = 18,04 s, sonrisa 0,8–8,8 s (sube en 1,6 s, baja en
2,3); Sebastián 430 = 17,92 s, sonrisa 7,5–15,1 s (sube en 2,4, baja en 2,5). Cierre último ↔ primero en la cara 1,61 y 1,96
contra un paso máximo entre cuadros consecutivos de 3,63 y 2,72: no salta. Revisado cuadro a cuadro a 1,5 fps y de cerca en el
tramo ralentizado: sin labio doble ni párpado fantasma. En la portada, el segundo retrato (Sebastián) arranca en `DESFASE =
0,87` de su loop (15,6 s): su sonrisa cae a los ~9,8 s de página, después de la de Matías (0,8–8,8), y termina ~1,4 s antes de
que Matías vuelva a sonreír. Los largos difieren 0,12 s, así que se corren ~1 s cada 8 vueltas (≈ 2,5 min): suficiente para una
visita. Costo de la tercera vuelta: US$ 1,40; la familia stand completa, ≈ US$ 5,02.

### 0.4 Pendientes que deja la v5

- ~~Renombrar *RIA Comms* → *RIA Diálogo* en `/laboratorio/`~~: sin objeto desde el 01/11 (Diálogo salió del
  laboratorio y la página nueva no lo nombra).
- Los sitios de producto siguen diciendo *Byte Analítico* y *RIA Drivecore*; la home ya dice *RIA
  Analítico* y *RIA Automoción*.
- ~~`/laboratorio/` presenta cinco proyectos de los cuales tres ya son producto~~ y ~~la referencia vieja al proyecto
  03~~: resueltos el 01/11, la página se reescribió (§0.1, «La página del Laboratorio»).
- `/laboratorio/` sin el video del tablero: si se quiere de vuelta, hay que regrabarlo sin la marca «Byte Analítico» de
  su barra. Y `laboratorio/media/sc-*.jpg` y `traffic-dashboard.*` quedaron sin uso: decidir si se borran.
- Las maquetas Sapiens y Neander están en vivo (`sapiens.dataflow.rialabs.ar`, `neander.dataflow.rialabs.ar`)
  como prototipos sin control de acceso y con la actividad marcada como simulada. La expedición que las contaba
  (Maqueta navegable) salió del laboratorio el 01/11; si vuelven, es como sabores de Smartcity (Country, Centros
  comerciales).
- **RIA Espacio pasa a llamarse RIA Espacios** (Matías, 13/10: el plural «explica mejor la naturaleza de la versión
  reproducible en sabores»). La máquina ya rotula *Espacios*; el resto de la página (nav, banda, laboratorio, metas) y
  el ancla `#espacio` siguen en singular: renombrar en una pasada aparte, después de integrar las ramas del 13/10.
- El satélite **Acceso** de RIA Espacio no enlaza a nada: Rosental y Mercado Fisherton son instalaciones con
  login. Cuando Acceso tenga página pública, es agregarle el `href`.
- El separador de Equipo es el anillo (el isotipo) desde el 13/10; el eclipse vectorial que tenía, y el de la banda
  Dataflow, ya no están en la página.
- `favicon.ico` y la carpeta `ria-favicon/` siguen siendo el eclipse de halos viejo; `favicon.svg` ya es el anillo.
  Regenerar el `.ico` (y los PNG de `ria-favicon/`) desde `favicon.svg`.
- Los lockups con el anillo (`logos/ria-anillo-lockup-horizontal-*.svg`) no tienen PNG: hace falta Saira instalada
  para que el wordmark salga fiel (`logos/build-pngs.sh`).
- Quedan menciones a Byte y VRIO fuera del hero, el pie y el separador: la meta description («Nacidos de Byte y
  VRIO»), las fichas de Equipo (la casa Byte de Sebastián, VRIO Estudio en la bio de Matías) y el Laboratorio («dos
  puertas en Rosario: Byte… y VRIO»). Es otra pasada. *(El Laboratorio quedó resuelto el 13/10 en la home y el 01/11 en
  `/laboratorio/`: la página nueva no nombra ni a Byte ni a VRIO.)*
- Si el desenclipsar vuelve (`DESENCLIPSAR_ACTIVO = true`), el isotipo de la nav —hoy el anillo— ya no tiene luna que
  acompañe el viaje; decidir si el anillo acompaña de otra forma o no acompaña.
- Los contadores de Dataflow (desde el 01/11 en `/dataflow/`, §0.7) proyectan la lectura del tablero del 10/10/2026
  (§0.5): cada tanto conviene cargar una lectura nueva (constantes al principio del script «EL MOTOR» de
  `dataflow/index.html` y la fecha en `.df-nota`), porque
  con los meses la proyección se aleja de lo medido. Y la curva horaria es plausible, no medida: cuando el tablero
  exponga la serie por hora, va la real.
- ~~El audio de la frase del hero~~: sin objeto desde el 14/10 (la frase salió del hero; ver la idea guardada en
  `docs/ideas/2026-10-13-discurso-metaestructura.md`).
- Las viñetas de las verticales son SVG dibujado, no imágenes generadas: se decidió así para que sobrevivan a
  un tema claro (colores por variables), pesen cero y puedan moverse. Si alguna vez se quiere un render
  fotorrealista, el camino es el de los retratos (`scripts/generar-retratos.py`).

### 0.5 La banda Dataflow como onda (2026-10-12)

> **Histórico desde el 01/11:** la banda salió de la home y la onda de colores se fue (§0.7). Los contadores siguen,
> **tal cual**, en `/dataflow/`: la sección «Los contadores, vivos» y la tabla contador → base → tasa → fuente de acá
> abajo valen para la página nueva; las constantes ahora están al principio del script «EL MOTOR» de
> `dataflow/index.html`.

> Prompt de Matías, verbatim (registro de prompts, 12/10): «La expresión del Dataflow no me gustó. No era la idea que
> tenía en mente. … lo actual me parece grotesco y de mal gusto.» Y la dirección: «En la parte del motor creo que
> prefiero que nos basemos en la idea y visual de dataflow.rialabs.ar, volver a la onda para explicar de que se trata.
> Sin dar explicaciones sobre como, sin ser tan informativo, siendo mas concreto y directo y sin tantas palabras pero
> si los numeros de las mediciones en que se eleven emulando el funcionamiento del motor, haciendo algun calculo de
> proyeccion coherente, para que de la sensacion de estar contando eventos en vivo de verdad.»

**Qué muestra.** `<section class="df" id="dataflow">`: un `<canvas class="df-cv">` a sangre detrás de un `.wrap` con tres
piezas apiladas: la cabecera (rótulo `Dataflow · el motor`, título **Todo sigue pasando**, la línea *Lo que el motor
lleva contado, **ahora mismo**.* y, a la derecha, el botón «Universo Dataflow ↗» a dataflow.rialabs.ar), una franja
vacía `.df-onda` (`clamp(240px, 34vh, 330px)`; 190–240 px en móvil) que el script mide para ubicar la onda, y el
tablero `.df-tab`: seis contadores —**eventos** grande (56 px), y **autos · personas · camiones · motos · patentes
leídas** (30 px)— con la nota mono *proyección sobre lo medido el 10 oct 2026 · 8 cámaras · un equipo en Rosario*.
Nada más: ni etapas, ni catálogo, ni diagrama, ni el eclipse. Una sola escena: **~775 px** de alto en 1440×900 y
~870 en 390 px (el tablero pasa a dos columnas con *eventos* a lo ancho). El título sale del propio sitio de Dataflow
(`lambda`: *«una foto dice que algo pasó; una onda dice que todo sigue pasando»*).

**De dónde viene la onda.** `dataflow.rialabs.ar` es *la onda* (README de `dataflow-expresiones`: todo lo demás son
magnitudes de `u(x,t) = A·sen(kx − ωt + φ)`; regla de marca: *la onda se muestra, no se nombra*). Hoy la raíz sirve
la portada conmutador (`sitios/dataflow/index.html`: tres hilos senoidales finos, frambuesa · naranja · lima sobre
`#0a0714`) y `/universo/` sirve «Universo Dataflow» (`sitios/ver-dataflow/`), cuyo sabor de base `rio` es la onda de
identidad de `sitios/lambda/index.html`: el puerto a canvas del generador del GIF original (`render.py`). De ahí se
trajeron, vanilla y sin dependencias, **las tres cintas** (`ONDAS`: color, altura, amplitud, frecuencia 1,8 / 2,3 /
2,7, perfil 0,42 / 0,34 / 0,30, grosor), **`perfil(u, p) = sign(sen u)·|sen u|^p`** (las crestas achatadas del GIF),
el movimiento `scroll` (`desp = t/freq`, ciclo de 11 s con fases múltiplos de 2π: el loop cierra), **los remolinos**
violeta del fondo (mismo generador congruencial, semilla 1337) y **los pulsos**: en lambda son «detecciones viajando
por la cinta», un punto blanco con halo que recorre la cinta en ~4 s. Lo que se adaptó: las cintas se ubican en la
franja medida del DOM y suben hacia la derecha (`TILT` = 5 % del ancho), con amplitud al 82 % en pantallas angostas;
**se apagan con un degradé vertical donde entran en zona de texto** (arriba la cabecera, abajo el tablero: la onda no
se corta, cede); la sombra difusa de lambda (`shadowBlur`, caro por cuadro) se reemplazó por la misma cinta corrida
hacia abajo en violeta hondo; no hay burbujas (el cielo ya pone puntos). Colores por variables de `.df`, con versión
de día: `--df-c1/2/3` (`#fa4560` · `#fb8c21` · `#dbd71f`, muestreados del GIF; la lima baja a `#b9b400` sobre papel),
`--df-pulso` (blanco; violeta de noche sobre papel), `--df-campo` (los remolinos, 34 % de noche y 10 % de día, así el
cielo se sigue viendo a través) y `--df-sombra`. Se releen 3,2 s después de cada cambio de `data-tema`.

**Los contadores, vivos.** Cada contador muestra al cargar **lo medido + su tasa × el tiempo transcurrido desde la
fecha base** (reloj del visitante) y desde ahí sube de a uno. La tasa de cada uno es **su propio total dividido por las
682 h de la ventana medida** (primer evento 2026-09-11 19:59, último 2026-10-10 05:59, hora de Rosario), modulada por
una **curva horaria** (hora local de Rosario, UTC−3 sin horario de verano) hecha de armónicos de 24 h —`CURVA =
[[0,62, 14,5 h, 1], [0,08, 10 h, 2]]`: amplitud, hora del pico, armónico— para que su promedio diario sea exactamente 1
y la tasa medida se conserve: mínimo 0,32 a las 3, máximo 1,58 a las 13:30, 1,1 a las 20. La proyección usa la
integral analítica de la curva (`curvaAcum`), no una suma; el valor nunca baja de la base (si el reloj del visitante
está atrasado, muestra lo medido). En vivo, el intervalo entre subidas es `1/tasa(ahora) × (0,45 … 1,55)` al azar
(media 1: el ritmo es el real, los incrementos no son mecánicos), con una corrección suave si el conteo al azar se
aleja más de 1,5 de la proyección (apura ×0,6 o afloja ×1,6). Cada subida programada es **un pulso que nace a la
izquierda 4,2 s antes y llega cuando el número cambia** (los de *eventos* en una cinta al azar y más grandes; los
demás en su cinta); al subir, el número destella a blanco 140 ms y vuelve al dorado en 0,5 s (`.tic`). Formato es-AR
(puntos de miles, `fmt`), cifras tabulares para que no baile. Si la banda estuvo más de 15 s fuera de vista o la
pestaña oculta, al volver se **resincroniza** con la proyección. Las constantes (`DESDE`, `HASTA`, `TOTALES`, `HUSO`,
`CURVA`, `VIAJE`, `PERIODO`) están al principio del script «DATAFLOW · la onda»: cargar una lectura nueva del tablero
es reemplazarlas y cambiar la fecha de `.df-nota`. Los números escritos en el HTML son la base medida (lo que se ve
sin JS). La curva horaria es **plausible, no medida**: cuando el tablero exponga la serie por hora, va la real.

| Contador | Base medida | Tasa | Sube cada (media) | Fuente |
|---|---|---|---|---|
| eventos | 784.790 | 1.150,7 / h | 3,1 s (2 s a las 14, 10 s a las 3) | tablero `/api/historico` → `eventos.total_historico` |
| autos | 330.163 | 484,1 / h | 7,4 s | ídem, `por_tipo` |
| personas | 172.162 | 252,4 / h | 14,3 s | ídem, `por_tipo` |
| camiones | 74.018 | 108,5 / h | 33,2 s | ídem, `por_tipo` |
| motos | 57.498 | 84,3 / h | 42,7 s | ídem, `por_tipo` |
| patentes leídas | 20.750 | 30,4 / h | 118 s | ídem, `por_analitica` → `lpr` |
| 8 cámaras (en la nota) | 8 | — | — | tablero `/api/estado` → `motor.camaras` |

El tablero (`datamotor.rialabs.ar`, credencial en `~/.credentials/datamotor-tablero.txt`) se leyó en **solo lectura**
el 2026-10-10 02:59 -03; el box corría el motor con contrato 1.104.0, 74 kinds, 4 sabores. Por sabor, del mismo
tablero (no está en la página): `byte` 632.004 · `analitico` 131.822 · `jockey-acceso` 20.254 · `rosental` 711. El
12/10 a las 2:30 la banda mostraba 838.4xx eventos; a las 14:30, 852.2xx.

**Movimiento.** Un solo `requestAnimationFrame` para onda y contadores, que corre sólo con la banda a la vista
(IntersectionObserver, 120 px de margen) y se detiene con la pestaña oculta. `prefers-reduced-motion`: la onda es un
cuadro quieto (t = 0,18, tres pulsos a mitad de camino) y los contadores muestran la proyección sin animar.
`?t=<ms>` adelanta el reloj —el de la onda y el de la proyección— para fotografiar otro instante:
`QUERY=t=43200000 NOMBRE=t12h scripts/capturar-home.sh v5` fotografía doce horas después (de madrugada a la tarde
de Rosario: los números suben ~13.800 eventos y hay pulsos en vuelo). En la captura de página entera la banda queda
en y ≈ 3.980–5.000 (desktop) y ≈ 5.580–6.450 (móvil). Reduced-motion se verificó con Chrome directo
(`--force-prefers-reduced-motion` sobre una copia de `index.html` con la inyección del script). Lo verificado el
12/10 (noche, día, móvil, t = 12 h, reduced-motion, sin `Uncaught`): `_capturas/dataflow-onda/` (ignorado).

**Lo que se fue con la banda-historia** (siguen medidos, ya no se publican; sus fuentes quedan acá por si vuelven):
3 formas de entrar (`dataflow-jockey-acceso/docs/ESTADO.md`, `dataflow-integradores/docs/ESTADO.md`) · 15 cuadros
por segundo por cámara (`ria-smartcity/docs/ESTADO.md:81`; tablero `fps_objetivo: 15`) · 0 cambios en la instalación
(principio del método, no medición) · 24 analíticas (`PROMPT-FUNDACIONAL-AUDITORIA-DATAMOTOR-2026-10-03.md:25`;
`esquemas.py` tiene 25 claves, `compuerta_movimiento` es un filtro previo; la barra del hero dijo 24 hasta el 13/10, cuando la
reemplazó la máquina) ·
veredictos normal · atención · alerta (777.630 / 179 / 6.982) · 4 sabores a la vez (`motor.sabores`) · 130.520 el
2 de octubre (`eventos.serie`, `bucket=dia`) · 23.377 bicicletas (`por_tipo`) · 49 W de placa de video
(`acumulados.potencia_w`, 529 h desde el 18/09) · −27 % de demora y 300 vehículos por hora en la ochava
(`byt-traffic-demo/README.md:94,169`; siguen en Laboratorio). Hasta el 13/10 seguían en la **barra de números del
hero** (reemplazada por la máquina, §0.1): 1.100 vehículos activos (`drivecore-web/index.html:1008`, heredado de v4;
siguen en el linaje del laboratorio) y 30 mil lecturas por día en una puerta (`dataflow-rosental/docs/ESTADO.md` en el
commit `13377c9`, línea 35; ya no se publican).

### 0.6 La página del Método (`/metodo/`, 2026-11-01)

> Prompt de giro, verbatim: `docs/prompts-usuario/2026-11-01-home-en-paginas-y-oficina-rosario.md` — *«La sección de El
> Metodo tiene que pasar a una página propia y estar expresada con mas espacio y acompañada de artefactos visuales en
> movimiento que expresen el mensaje de cada item.»* (rama `pagina-metodo`).

**Qué es.** `metodo/index.html`, autocontenida. La sección «Método» (`#metodologia`, la grilla de seis tarjetas) **salió
de la home** junto con su CSS (`PRINCIPLES`, `.princ-grid` en los dos media queries y `.pr` en la lista de transición del
tema); entre Laboratorio y Equipo queda un solo divisor. La nav y el pie de la home ya apuntaban a `/metodo/`.

**La base, copiada.** Fuentes, tokens de `:root`, la base (reset, ruido), EL CIELO (CSS, canvas y script), NAV, BUTTONS,
LAYOUT, CONTACT (el anillo y «Hablemos.»), FOOTER, REVEAL y las reglas de base del `@media(max-width:860px)`, copiados
tal cual de `v5/index.html` con el comentario «copiado de v5/index.html (BLOQUE) el 01/11 — mantener igual» arriba de
cada uno. Sólo noche (sin tema día ni desenclipsar). La nav lleva enlaces absolutos (`/#smartcity`, `/#analitico`,
`/#automotrices`, `/dataflow/`, `/laboratorio/`, `/metodo/` con `aria-current="page"` —subrayado dorado—, `/#rosario`),
el logo va a `/`; **«Conversemos» va a `#contacto` de la propia página** (tiene su «Hablemos.»). El pie: `/#productos`,
`/dataflow/`, `/laboratorio/`, `/metodo/`, `/#rosario`, `/#contacto`. `<title>` «Método — RIA Labs», description y og
propios (`og:url` `https://rialabs.ar/metodo/`, `og:image` la de la home), `canonical`.

**Secuencia.** Encabezado: «Método» · **La forma en que pensamos** (el título de la home, a 46–92 px) · *«No son valores
de folleto. Son seis reglas que deciden, en cada proyecto, qué se construye y qué se deja afuera.»* · un índice de las
seis (`#regla-1` … `#regla-6`). Después **una estación por regla** (`<section class="met-est">`, `min-height:
min(90vh, 880px)`, casi una pantalla en desktop): el número fantasma (el `.pr-ghost` de la home a escala de estación),
«Regla 0N», el título, **el texto de la home tal cual** y el artefacto con su epígrafe en DM Mono («FIG. 0N — …»); las
pares van con el artefacto a la izquierda. En celular: título · artefacto · texto. Cierre: «Las reglas, en uso» · **Se ven
mejor funcionando** · *«En el laboratorio, cada expedición con la pregunta que la abrió, lo que medimos y lo que todavía
no sabemos. En los productos, lo que ya se instala.»* · «Recorrer el laboratorio →» (`/laboratorio/`) y «Ver los
productos» (`/#productos`); después el anillo, «Hablemos.» y el pie.

**Los seis artefactos** (SVG que arma el script «EL MÉTODO»; la gramática de la máquina: línea fina dorada, plano técnico
—grilla tenue y las cuatro escuadras de la estación—, tokens de colores con halo, nodos de la red, rótulos en DM Mono):

1. *El problema primero, la tecnología después* — se dibuja el problema (una forma irregular con cinco particularidades
   de color) y se le toman las cotas; recién después llega la herramienta, **una pieza cuadrada de catálogo** que tapa
   una parte y deja otra afuera (las particularidades de afuera titilan), y **se deforma hasta tomar la forma del
   problema**; toca cada particularidad y empieza a andar (tres tokens la recorren). Ciclo 13 s.
2. *Partimos de lo que ya tenés* — el plano de un edificio con tres cámaras, un sensor en el portón, el gabinete y **el
   cableado ya dibujado desde el primer cuadro** (punteado gris). En la ficha «config» se prenden los interruptores uno
   por uno: cada dispositivo se enciende (cono de visión, ondas del sensor) y sus datos viajan **por los cables que ya
   estaban** hasta el motor (el aro del reactor, con su química). Ninguna línea nueva aparece. Ciclo 12,4 s.
3. *Si no está medido, no se dice* — un registrador: las muestras corren a la izquierda, con el promedio de las últimas
   diez y su banda (± 2 errores estándar). Mientras falta muestra, la lectura es una raya («falta muestra»); cuando la
   banda entra en la tolerancia (las marcas punteadas junto a la cabeza), **aparece la cifra**; el sensor se vuelve
   ruidoso (puntos violeta), la banda se abre y **la cifra se oculta** («no es confiable») hasta que la ventana vuelve a
   estar limpia. **La cifra es el promedio real de los puntos que se ven** (lo dice el epígrafe): muestras simuladas con
   semilla, no un dato de producto. Ciclo 14 s.
4. *Simplicidad como estándar de calidad* — una red enmarañada («todo lo posible») entre una entrada y una salida; el uso
   pasa por un solo camino, que se calienta en dorado; dos tokens grises exploran ramas muertas y se apagan; lo que nadie
   usa se apaga (queda un rastro al 20 %), **el camino se endereza en una línea** («lo que se usa») y por ella pasa cada
   vez más uso, de colores. Ciclo 14 s.
5. *Los límites los decimos nosotros* — la red de lo que el sistema hace; **una pluma dorada traza la frontera**, con las
   marcas de plano del lado de afuera; afuera se raya y quedan, punteadas, las capacidades que todavía no están. Rótulos
   «hace | todavía no» a los dos lados de la línea. Los datos circulan y, **cuando uno llega a la frontera, la toca (un
   anillo) y vuelve**. Después de trazarla no se reinicia: sigue andando (caminatas sembradas de 10 min).
6. *Se instala, no se demuestra* — sobre el banco, el prototipo en línea punteada (anda: su luz titila); **el manual
   tilda sus cinco pasos** y con cada paso se arma en línea firme lo instalado (poste, equipo, cable, gabinete, la luz de
   en marcha y el cono); llega el equipo del cliente (teal), **el de RIA se va**, y el sistema sigue latiendo solo (el
   trazo de abajo no se corta). Ciclo 15 s.

**Cómo está hecho.** Cada artefacto es una función pura del tiempo (`frame(t)` pone los atributos del cuadro *t*; azar
mulberry32 con semilla), así `?t=<s>` adelanta todos los relojes y cada foto es reproducible. Cada figura tiene su reloj:
arranca la primera vez que entra a la vista, corre sólo a la vista (IntersectionObserver) y con la pestaña visible, un
solo rAF para las seis. Con `prefers-reduced-motion`, un cuadro quieto por figura (`quieto`: el instante que mejor cuenta
la regla —el problema con la herramienta ajustada; todo encendido; la cifra con el bulto de ruido en la historia; la línea
con el rastro de la maraña; un toque en la frontera; lo instalado con el cliente—) y no hay bucle. viewBox 480 × 360; los
rótulos toman `--fs`, recalculado con el ancho para quedar entre 9 y 11,5 px en pantalla. Colores en hex (la página es
sólo noche). Sin librerías.

**Verificado:** `node --check` de los `<script>` de `metodo/index.html` y `v5/index.html`; sin errores de JS en Chrome
headless (colector de `error`, 1440 y celular); capturas de página completa a 1440 y 390 con `?t=2`, `3,4`, `6,2`, `9,5`
y `12,4`, reduced-motion (`PANTALLA=1 RM=1`) y la home donde estaba la sección. **Ojo con el script de captura:** sin
`QUERY=t=…` las figuras salen casi vacías (el reloj virtual de Chrome apenas avanza el rAF): usar `QUERY=t=9.5` o `RM=1`.
Capturas en `_capturas/pagina-metodo/` (ignorado; `hoja_*.png` junta las seis figuras de cada instante).

**Pendiente / para decidir:** el copete, el cierre («Se ven mejor funcionando») y los epígrafes son textos nuevos; el
título sigue siendo el de la home. El botón «Las seis reglas de la casa» de `#laboratorio` en la home todavía apunta a
`/laboratorio/#metodo` (lo repunta la rama `pagina-laboratorio`, que saca esa sección). `og:image` es la de la home:
una tarjeta propia de la página sería mejor. La página es sólo noche.

### 0.7 La página de Dataflow (`/dataflow/`, 2026-11-01)

> Matías, verbatim (prompt de giro del 01/11, `docs/prompts-usuario/2026-11-01-home-en-paginas-y-oficina-rosario.md`):
> «La sección "TODO SIEGUE PASANDO" tiene que ser en realidad una sección en su propia página, dedicada a Dataflow.
> Hay que mantener los datos que se muestran, que son excelentes, pero hay que cambiar ese banner de flujo de onda
> porque contradice mucho el diseño general de la pagina. No estaría mal buscar otra expresión de onda que sea acorde
> a la visual expresada en el sitio, y también sería bueno replicar la visual expresada en la pagina del Datamotor con
> entradas de sensores hacia el motor de dataflow y la salida en las analiticas y los datos, algo que resulta una muy
> buena expresión del Dataflow en pleno funcionamiento.»

**Qué cambió en la home.** La banda `#dataflow` salió entera: el `<section class="df">`, su CSS «DATAFLOW · la onda»
(con sus reglas en reduced-motion, ≤1020 y ≤860) y su script (LO MEDIDO, el tablero y la onda). Donde estaba no queda
nada: `#productos` termina y empieza `#laboratorio`. Ningún otro script de la home la leía; la nav y el pie ya
apuntaban a `/dataflow/` (commit `33563bb`).

**La página.** `dataflow/index.html`, autocontenida y sin librerías. La base es la de la home **copiada tal cual**
(fuentes, `:root`, la base, el cielo, la nav, los botones, el layout, el reveal, el contacto y el pie; cada bloque con su
comentario «copiado de v5/index.html (…) el 01/11 — mantener igual»); sólo noche, sin el tema día ni su transición. La
nav lleva los enlaces absolutos, el logo a `/` y `aria-current="page"` en Dataflow —lo único agregado: la página propia
va en blanco en la nav y en dorado en el menú—; «Conversemos» baja al `#contacto` de la propia página; el pie va a
`/#productos · /dataflow/ · /laboratorio/ · /metodo/ · /#rosario · /#contacto`. `<title>` *Dataflow — RIA Labs*;
description, og y twitter propios (*Dataflow — el motor de RIA Labs. Todo sigue pasando.*), og:image la de la home.

Secuencia: `#dataflow` (rótulo *Dataflow · el motor*, título **Todo sigue pasando**, la línea *El motor detrás de RIA
Smartcity, RIA Analítico y RIA Automotrices. Lee la realidad con las cámaras y los sensores que ya están, la comprende y
actúa. Esto es lo que lleva contado, **ahora mismo**.*, el botón «Universo Dataflow ↗» a dataflow.rialabs.ar y **el
motor**) → `#como` (*Cómo trabaja* / **Lee, comprende, actúa.** y tres pasos: *Lo que ya está* · *Un catálogo de
analíticas* · *Cada evento, a quien lo necesita*) → `#productos` (*Los productos* / **Tres formas del mismo motor.**:
Smartcity, Analítico y Automotrices, cada uno a su ancla de la home, con una línea tomada de su sección) → `#contacto`
(el anillo, «Hablemos.») → pie. Mide ~2.850 px en 1440 y ~4.570 en 390.

**El motor** (`<figure class="mot" id="motor">`, la pieza central, ~480 px de alto en 1440). La idea del tablero del
Datamotor (`datamotor.rialabs.ar`; su dibujo es `ria-datamotor/ria_datamotor/tablero/ui/flujo.js`) dicha con la
gramática de la máquina y su red abierta, no con la piel del tablero: línea fina de plano técnico sobre el cielo, el
dorado del eclipse en el núcleo y el color de cada producto en las salidas. Cuatro columnas:

- **Entradas** (dibujos SVG de línea fina, 40×26; de su borde sale el cable). Tipos de fuente que el motor lee hoy, cada
  uno anclado en un repo o en la home: *Tránsito · una esquina de Rosario* (la cámara de la ochava) · *Acceso · la
  barrera de un club* (`dataflow-jockey-acceso`, la cámara de la barrera) · *Predio · un mercado concentrador*
  (Smartcity, «Acceso»; «midiendo 24/7 · municipio, club y mercado») · *Concesionaria · el ingreso al taller* (la
  lectura de patentes del ingreso) · *Monitoreo · las cámaras de una central* (Analítico; el motor lee VMS, `tipo: nx`)
  · *Grabador · el video que ya se graba* (el «registro» de la máquina; fuentes `nx` y `archivo` de
  `ria_datamotor/ingesta/spec.py`). Ninguna es un sensor que no sea cámara: el sensor es la cámara («Convertimos las
  cámaras en sensores de ciudad», `GUION-SMARTCITY-PELICULA-2026-09-10.md`).
- **El motor**: el eclipse de la casa (halos `--h3…--h6`, aro dorado, sol tapado, luna), con un dial alrededor (el
  manómetro de la máquina) y las bridas de entrada y salida; por dentro gira el anillo de tres arcos del tablero, los
  cuadros entran por el aro, giran hacia la salida y se doran, y la corona respira con lo que entra. Debajo (al costado,
  en el flujo vertical) **el instrumento**: las tres cintas de la onda de la identidad —frecuencias 1,8 · 2,3 · 2,7 y
  el perfil de crestas achatadas de `sitios/lambda`— en hilo dorado, con la amplitud de la hora de Rosario (la curva
  horaria de los contadores).
- **Analíticas**: *vehículos · personas · patentes · zonas · merodeo · sabotaje · aforo · fauna*, cada una con el punto
  de color de los productos que la usan, según los textos de la home (Analítico: personas, vehículos, patentes, zonas,
  merodeo, sabotaje; Smartcity: movilidad, espacio público, aforo, fauna, patentes en el predio; Automotrices:
  patentes). Son analíticas del catálogo del motor (`ria_datamotor/esquemas.py`: `deteccion_objetos`,
  `conteo_personas`, `lpr`, `invasion_zona`/`cruce_linea`, `merodeo`, `sabotaje`, `ocupacion`/`permanencia`,
  `conteo_poblacional`).
- **Lo que lleva contado**: los seis contadores de la banda, **tal cual** —mismas constantes, misma proyección y curva
  horaria, la nota *proyección sobre lo medido el 10 oct 2026 · 8 cámaras · un equipo en Rosario*; la tabla de §0.5
  sigue valiendo—, con *eventos* grande arriba (50 px) y un renglón por conteo, la cifra a la derecha. Los números
  escritos en el HTML son la base medida: sin script se ven tal cual.

**La otra onda.** Por cada cable corre un pulso de luz dorada, u = A·sen(ks − ωt), con fase propia (un degradé a lo
largo del cable): la onda de Dataflow dicha como pulsos que viajan por el cableado, no como cintas de colores. Los
cuadros son puntos de blanco cálido que van de cada cámara al aro (2,7 s; uno cada 0,4–1,1 s por cámara: expresión,
no el fps medido). **Las chispas son los contadores**: cada subida programada sale del núcleo 2,6 s antes, llega a su
analítica —que se enciende y suelta un anillo en el color de la chispa—, corre por la línea punteada de la analítica y
por la barra de los datos y entra en la cifra justo cuando el número cambia. Color: uno de los productos que usan esa
analítica, al azar. De dónde sale: autos, camiones y motos, de *vehículos*; personas, de *personas*; patentes leídas,
de *patentes*; las de *eventos*, de cualquiera, en las proporciones de lo medido (vehículos 0,588 · personas 0,219 ·
patentes 0,026) y el resto (0,166: bicicletas y lo que el tablero no desglosa) en partes iguales entre las otras cinco
—**ese reparto no está medido**—. El pie del motor lo dice: los tres productos con su color, *el color de cada chispa es
el producto que la usa*, y la nota de la proyección.

**Cómo se arma.** El marcado (rótulos, nodos vacíos, contadores) es HTML y lo ordena la grilla; el script «EL MOTOR»
mide dónde quedó cada cosa y dibuja en dos canvas: el plano (cruces de grilla, marcas de esquina, cables, núcleo y
nodos; se traza al entrar, como un plotter, en 1,9 s, y se redibuja con ResizeObserver) y lo vivo (un solo
`requestAnimationFrame`, sólo con el motor a la vista —IntersectionObserver, 120 px de margen— y la pestaña visible;
una pausa corta congela el reloj, una de más de 15 s resincroniza con la proyección). Todo se fecha con su instante
programado, así la escena es la misma aunque el navegador dibuje pocos cuadros. ≤980 px el flujo va de arriba hacia
abajo: entradas y analíticas en dos filas trabadas (grillas de 7 y 9 columnas, así los cables de la primera fila pasan
entre las celdas de la segunda), el instrumento al costado del núcleo y, de la analítica a la cifra, la chispa vuela
sin cable. `prefers-reduced-motion`: un cuadro quieto compuesto (cuadros a mitad de camino, giros en el núcleo, cinco
chispas, una analítica encendida) y los contadores con la proyección, sin animar. `?t=<ms>` adelanta el reloj. Se
fotografía con `scripts/capturar-home.sh dataflow` (el argumento es la carpeta). Lo verificado el 01/11 (1440, 1100,
920, 390, reduced-motion, y la home sin la banda): `_capturas/pagina-dataflow/` (ignorado).

**Pendiente.**
- El reparto de las chispas de *eventos* entre zonas, merodeo, sabotaje, aforo y fauna es parejo, no medido: cuando el
  tablero desglose `por_analitica`, va el real (constante `PESOS` de «EL MOTOR»).
- Las entradas son tipos de fuente, no las ocho cámaras del tablero; si se quiere dibujar el parque real (cuántas
  cámaras y de qué sabor), sale de `/api/estado` del tablero.
- La nav compartida (siete enlaces y «Conversemos») no entra entre 861 y ~1.100 px: «RIA Labs» y los enlaces se parten
  en dos renglones, en la home y en esta página por igual. Arreglarlo en la home y recopiar.
- La salida a productos cita la home del 01/11; si `#productos` cambia sus textos, actualizar acá.

### 0.8 Rosario: la oficina dibujada (`#rosario`, rama `oficina-rosario`, 2026-11-01)

> Prompt de giro, verbatim, en `docs/prompts-usuario/2026-11-01-home-en-paginas-y-oficina-rosario.md`: «Por ultimo, y
> esto si queda en la pagina principal, lo que hoy dice "El Equipo", ya no tiene que mostrar los personajes con su
> historia, sino que tiene que transformarse en una idea dibujada. Una animación visual creada para representar nuestras
> oficinas en Rosario. Hay que hablar de que salimos de la ciudad de Rosario, de la provincia de Santa Fe, de Argentina.
> De nuestra idiosincracia y cultura. Nuestra oficina esta compuesta por espacios para programadores, laboratorio,
> showrroom para el público y una sala de reuniones. Seria bueno representarlo con un edificio sin pared que muestra el
> interior donde estan los espacios con gente trabajando, presentando, probando, mirando, etc.» La guía
> (`2026-11-01-guia-oficina-rosario.jpg`: el edificio sin pared en realidad aumentada sobre una esquina de casas bajas)
> se tomó como idea, no como modelo: el dibujo es propio, en el lenguaje de la máquina.

**Qué es.** La sección que era «El equipo» (`#equipo`, los dos fundadores con su retrato vivo y su historia) es ahora
`<section id="rosario">`, en el mismo lugar: al final de la home, antes del separador del anillo y de «Hablemos.».
Queda un `<span id="equipo">` arriba de la sección para los enlaces viejos. La nav y el pie ya apuntaban a `#rosario`.

**El texto** (el tono de la casa; nada inventado: ni dirección, ni cuánta gente, ni metros, ni clientes):

- Etiqueta: **Rosario** · Título: **De dónde salimos**
- «**De Rosario, provincia de Santa Fe, Argentina.** Una ciudad puerto sobre el Paraná, de ingenieros y de
  programadores. De acá traemos la costumbre de trabajar con lo que ya está —la cámara que ya cuelga en la esquina, el
  sensor que ya mide, el cuaderno que alguien ya llena a birome— y la de decir lo que todavía no sabemos. Trabajamos en
  Fisherton, al oeste de la ciudad, en la esquina de Donado y Chassaing.» (la última oración, desde el 02/11, §0.8.1)
- «Esta es nuestra esquina como la imaginamos: la foto real del edificio, con un piso más y las paredes de vidrio para
  ver adentro. Arriba, **los programadores**, donde el motor se escribe, y **la sala de
  reuniones**, donde un cliente ve sus propios números. Abajo, **el laboratorio**, donde se prueba lo que todavía es
  pregunta, y **el showroom**, abierto a la vereda. En la ochava, una cámara mira la calle las veinticuatro horas. La
  regla es la misma en las cuatro salas: si no está medido, no se dice.»
- Pie del dibujo (mono): *corte de la oficina · una esquina de Rosario*.

  De dónde sale cada cosa: «trabajar con lo que ya está» es la idea de la casa («Tu infraestructura ya existe»); el
  cuaderno a birome, la ochava con su cámara de 24 horas, «donde el motor se escribe» (el taller) y «si no está medido,
  no se dice» vienen del texto del Laboratorio de la home; «decir lo que todavía no sabemos» es el «Todavía no sabemos»
  de las expediciones. Lo de Rosario es dato general: ciudad puerto sobre el Paraná, tradición de ingenieros y
  programadores de la región. Se dejó afuera, a propósito, lo de postal (la bandera, el asado) y las coordenadas.

**Qué muestra el dibujo.** Un **corte fugado** del edificio de dos pisos en su **ochava**, sin la pared del frente,
visto desde la vereda de enfrente con el ojo a la altura de la terraza (se ven los pisos, no los techos). Línea fina de
plano en el dorado de la casa; muros y losas cortados con rayado; las luces de cada sala en los colores por producto.

- **Sala de programadores** (arriba, izquierda; luz teal): dos escritorios con dos pantallas cada uno —en una el código
  se escribe línea a línea con su cursor, en la otra corre un log—, la gente de espaldas tipeando (cada tanto mira la
  otra pantalla o se echa atrás), un mate en la punta de un escritorio, una ventana al fondo con la ciudad de noche
  (alguna ventana lejana se prende o se apaga) y, en ancho, alguien que dibuja en la pizarra el recorrido de la casa
  (cámara → motor → tablero), lo anota, se corre para seguir, y después lo borra.
- **Sala de reuniones** (arriba, derecha; luz dorada): alguien presenta parado junto a la pantalla y señala el gráfico
  mientras crece (barras de a una, después la línea); los clientes a la mesa siguen el gráfico con la cabeza; mientras
  presenta baja la luz del techo y sube la de la pantalla. Una planta en el rincón (en ancho).
- **Laboratorio** (abajo, izquierda; luz ámbar): un brazo robótico que lleva una pieza de un lado al otro de la mesada y
  la vuelve a traer; alguien prueba una cámara en un trípode (la cámara panea con su campo de visión) con una tablet en la
  otra mano; un osciloscopio con una onda que corre; un sensor en la pared que emite; estantes con cajas; en ancho,
  alguien sentado a la mesada.
- **Showroom** (abajo, derecha; luz azul): la pantalla grande muestra **lo que ve la cámara de la ochava** (la calle en
  perspectiva, autos y personas con sus cajas de detección); dos personas la miran y una la señala; quien explica, de
  perfil (en ancho); pedestales con una cámara domo y un sensor, bajo un riel de luces. **Quien llega por la vereda entra
  por la puerta de la ochava** y aparece adentro, camina hasta los pedestales y se queda mirando.
- **Afuera:** el pretil con el cartel (el anillo y RIA LABS, con su resplandor), el tanque de agua en la terraza, un
  balcón en la ochava, la casa baja de al lado (cornisa, balaustrada, reja, una ventana encendida), un árbol de vereda que
  se mece, la farola de la esquina. **La cámara de la ochava** (rotulada «cámara de la ochava · mira la calle 24 h» en
  ancho) marca lo que pasa por su campo con cajas teal y su etiqueta: **persona** (quien entra; en ancho, alguien que
  baja por la vereda de la otra calle, asoma desde atrás de la esquina, dobla y sigue), **auto** y **bici**, que cruzan
  por la calle de enfrente.
- **Decisión:** nadie camina por la vereda por delante de las salas de abajo (con el ojo en la vereda de enfrente, un
  peatón tapaba medio laboratorio y se leía como si estuviera adentro): el que entra viene desde la esquina de enfrente y
  el que pasa baja por la otra calle. El auto y la bici sí cruzan por delante, rápido.
- **Celular (≤860 px):** el mismo edificio con salas más angostas (86 unidades en vez de 150) y menos gente (sin pizarra,
  sin quien explica en el showroom, sin el técnico sentado, sin la cabecera de la mesa ni la planta), el campo de la
  cámara hacia la esquina y sin el rótulo de la cámara; los rótulos cortos (Programadores, Reuniones). La gente mide
  ~59 px a 390 de ancho.

**Cómo está hecho.** HTML: la sección con `.ros-txt` (dos columnas; una en celular) y `<figure id="oficina">` con un
`<svg id="ros-svg" role="img">` vacío y su `aria-label` (describe el dibujo entero). CSS: bloque «ROSARIO · la oficina
dibujada» (donde estaba «EQUIPO»): los tonos del dibujo son variables de la sección (`--ros-int`, `--ros-fondo`,
`--ros-poche`, `--ros-gente`, `--ros-cuerpo`, `--ros-vidrio`, …) con su versión de día; lo que pasa adentro de las
pantallas va en sus colores de noche siempre. El dibujo va más ancho que el texto (hasta 1480 px), con los costados
fundidos al cielo por máscara (sin máscara en celular). JS: un `<script>` propio al final de la página, «ROSARIO · la
oficina dibujada», sin librerías. Todo en **unidades** (20 = 1 m; una persona mide 34) con una **proyección de un punto
de fuga** `P(x, y, z)` (z = profundidad desde el plano del corte; F = 800, el ojo en y = −170, la terraza): las cajas
(escritorios, mesas, mesada, pedestales) se proyectan cara por cara y la gente y los aparatos son figuras planas paradas a
su profundidad. La gente es figura de arquitecto en trazo (relleno opaco y contorno crema; brazos y piernas con doble
trazo, con codos por cinemática inversa para que una mano llegue a un punto: la pizarra, el gráfico, la cámara). Se arma
una vez por trazado (y se rearma si cambia el trazado o el tamaño de los rótulos); cada cuadro sólo mueve geometría y
opacidades, nunca colores, así la transición del tema no se entera. **Movimiento:** un `requestAnimationFrame` a ~30
cuadros por segundo, sólo con el dibujo a la vista (IntersectionObserver) y la pestaña visible; el reloj arranca en
`T_PRE = 18 s` (nada empieza vacío) y `?t=<ms>` lo adelanta (la misma foto siempre). **prefers-reduced-motion:** un
cuadro quieto elegido, `T_QUIETO = 24,8 s` (el gráfico armado, la pizarra escrita, el auto en la esquina y quien entra,
los dos con su caja). **Día** (`?tema=dia`): papel, tinta y las mismas luces; la ventana del fondo pasa a cielo claro y
las luces de la ciudad casi se apagan. Rótulos en DM Mono, nunca menos de 8,5 px (10 px en ancho, 9 en celular), con
halo del color del fondo. **Peso:** 848 nodos SVG en ancho, 623 en celular; pintar un cuadro cuesta ~0,07 ms de JS.

**Verificado (2026-11-01):** los cinco `<script>` pasan `node --check`; una copia con prueba pintó ~1.000 instantes de
0 a 300 s en 1440 y en 390 sin errores y sin ningún `NaN`/`Infinity` en el SVG; sin `Uncaught` en las capturas. Capturas
(Chrome headless, `scripts/capturar-home.sh` con `PANTALLA=1`): la sección (`ANCLA=rosario`) y el dibujo
(`ANCLA=oficina`) a 1440×900 y 390×844, 1024×768, día a 1440 y a 390, reduced-motion y el auto en la esquina
(`QUERY=t=6800`), en `_capturas/oficina-rosario/` (ignorado). Ojo: en la captura el reloj casi no avanza (tiempo
virtual), así que la foto es el cuadro de `T_PRE`; para otro instante, `QUERY=t=<ms>`.

**Lo que salió:** las dos fichas de fundadores (retrato vivo, bio, oficio) y su CSS (`.team-grid`, `.founder`,
`.f-photo`, …). Los retratos del stand siguen en la portada. `assets/retrato-sebastian.*` y `assets/retrato-matias.*`
quedan en el repo **sin uso** (§0.3); la historia de los dos sigue en §7.

**Pendiente / para decidir:**

- Que Matías confirme los detalles «de casa»: el mate en el escritorio, el balcón de la ochava, el tanque de agua, que
  el showroom esté «abierto a la vereda» con la puerta en la ochava, y que la oficina sea de verdad esa esquina con la
  cámara (la home ya hablaba de «nuestra ochava»). Todo se cambia en el script sin tocar el resto.
- Si la historia de los fundadores tiene que vivir en algún lado (¿una página propia, o alcanza con los retratos del
  stand en la portada?).
- En la integración: §0.2 todavía dice `#equipo` en la secuencia de anclas (va `#rosario`); quedaron dos referencias
  muertas fuera de la región de esta rama, para no chocar con las otras: `.team-grid` en la regla
  `.princ-grid,.team-grid{…}` del `@media (max-width:860px)` y `#equipo video` en el selector del script «LABORATORIO Y
  EQUIPO · videos» (ya no encuentran nada; no rompen).
- Ideas que no entraron: la vereda de enfrente de la otra calle con sus casas bajas fugando a la derecha (en ancho), un
  colectivo que pase cada tanto, y en celular un recorrido lento sala por sala en vez del edificio entero.

#### 0.8.1 El mapa de Rosario con la esquina (`#mapa-rosario`, rama `rosario-mapa`, 2026-11-02)

> Prompt verbatim en `docs/prompts-usuario/2026-11-02-oficina-real-mapa-y-video.md`: «Aca tengo una foto real de nuestro
> edificio en Rosario, en la esquina de Donado y Chassaing. En la sección de Equipo (donde hicimos el dibujo animado) me
> gustaria que, primero, podamos agregar un dibujo no tan grande del mapa de rosario en la ubicación donde se encuentra el
> edificio.» (La segunda parte del pedido, el video hecho con IA desde la foto, es otra rama: `oficina-video`.)

**Qué es.** Un plano chico de Rosario dibujado en el lenguaje de la casa (línea fina dorada sobre el cielo, como un plano
técnico), al lado del texto de «De dónde salimos»: el contorno del municipio con un fondo apenas dorado; el **Paraná**
con su agua rayada (rayas horizontales finas, como en un plano) y las dos orillas en `--gold-hi`; las **avenidas** en
trazo tenue (las primarias y las secundarias, más tenues) y la **Circunvalación** y los accesos un poco más marcados; un
punto en el **Monumento a la Bandera** rotulado *centro*; el **pin** en la esquina, con el anillo de la casa (el
degradé del eclipse) y un pulso suave de `--gold-hi`; el norte y una escala de 2 km arriba a la derecha (sobre las islas,
donde no hay nada); esquinas de marco de plano. Rótulos en DM Mono: **ROSARIO**, **RÍO PARANÁ** (paralelo al canal, del
lado de las islas), *CENTRO*. Abajo a la izquierda (afuera del municipio, donde el plano está vacío), un **recuadro de
detalle** unido al pin por las dos líneas de una lupa: las calles reales alrededor de la esquina (±115 m) dibujadas como
en un plano de manzanas —17,3 m entre líneas de edificación, las 20 varas de Rosario— con **todas las ochavas** (sólo
entre dos calles que existen: el lado liso de una T no se ochava), **la ochava de la oficina** resaltada en `--gold-hi`
con un anillo chico que late, y los nombres DONADO y CHASSAING sobre sus calles. Debajo del recuadro: **DONADO Y
CHASSAING** y **FISHERTON**. Sin coordenadas en pantalla (como en el texto de §0.8). Pie, afuera del SVG: *abrir en el
mapa ↗* (izquierda) y *© OpenStreetMap* (derecha, con enlace a openstreetmap.org/copyright).

**Dónde va.** Dentro de `.ros-txt` (que pasa a `.ros-txt ros-txt-mapa`): el texto en dos columnas pasa a **texto +
mapa**; los dos párrafos quedan apilados a la izquierda (la grilla los ubica, no se tocaron sus líneas) y el mapa a la
derecha, ancho `clamp(280px, 33vw, 400px)` —400 px a 1440, 338 a 1024—, alineado con el primer párrafo. En celular
(≤860 px), abajo del texto, a lo ancho (342 px a 390; tope de 440 en tablets), y con los rótulos chicos un punto más
grandes (≥ 8,2 px en pantalla; los nombres de calle del recuadro quedan en ~7,3 px). `scroll-margin-top` para que
`#mapa-rosario` no quede bajo la nav.

**El texto.** Al final del primer párrafo se sumó: «Trabajamos en Fisherton, al oeste de la ciudad, en la esquina de
Donado y Chassaing.» (la cita del primer párrafo, arriba en §0.8, todavía no la tiene: se dejó así para no chocar con la
rama del video, que toca el segundo párrafo; al integrar va ahí). El segundo párrafo («Esta es la oficina, sin la pared
del frente…») no se tocó.

**La esquina, verificada con OpenStreetMap (Overpass, 02/11):**

- El cruce: el **nodo 1732157336**, que comparten las vías *José Agustín Donado* y *Chassaing*: **−32,9286995,
  −60,7274409**. Cae dentro de *Municipio de Rosario* (relación 3368048, admin_level 7), *Rosario* (8), *Distrito
  Noroeste* (9) y el barrio **Fisherton** (10; más fino, OSM lo pone en *Nueva Fisherton*, admin_level 11). No es Funes.
- La **ochava de la oficina**: **−32,928577, −60,727406**, la medida de Matías que usa la Machine
  (`ria-smartcity-machine/datos/ubicaciones.json`, «Esquina Donado y Chassaing», 26/10): 13,6 m al norte y 3,3 m al este
  del cruce de los ejes → la esquina **noreste** (Donado al oeste, Chassaing al sur de la manzana). Un indicio a favor,
  no una prueba: en la Machine, la cámara de esa ochava tiene su zona de espera de Donado «a la izquierda»
  (`espera-donado-izq`), que es como se ve Donado desde la ochava noreste mirando al cruce. Es la que se resalta en el
  recuadro y la que abre el enlace. **A confirmar por Matías** (ver pendientes).
- Control de lugar: del pin al Monumento a la Bandera (relación 6804977) hay 9,04 km al oeste y 2,10 km al norte, y en el
  plano el Monumento cae sobre la costa; Fisherton queda al oeste, pegado a la Circunvalación por fuera.

**El enlace.** Todo el mapa es un enlace a Google Maps con la ochava (`https://www.google.com/maps/search/?api=1&query=
-32.928577,-60.727406`, `target="_blank" rel="noopener"`): en el celular abre la app y sirve para llegar, que es lo que
quiere quien va a ver la oficina. El `aria-label` del enlace describe el mapa (el SVG va `aria-hidden`). El crédito de
OSM es un enlace aparte, en el pie (no se anidan enlaces).

**Cómo está hecho.** Los datos se bajaron **una vez** de OpenStreetMap con `scripts/generar-mapa-rosario.py`
(Overpass, User-Agent `rialabs-home/1.0 (hola@rialabs.ar)`, un pedido cada 2 s, reintentos ante 502/504): el contorno
del municipio (relación 3368048), el agua del Paraná (el multipolígono 67124: la cadena de orilla se cierra afuera del
encuadre y las islas quedan como huecos), las vías `motorway`/`trunk`/`primary` y `secondary` dentro del municipio (sin
las colectoras de la Circunvalación; las dos manos de los bulevares se funden en una raya), el Monumento y las calles a
260 m de la esquina. El script los proyecta (equirectangular, 1 unidad ≈ 53 m, viewBox 400 × 386,4), los simplifica
(Douglas-Peucker, 0,3–0,45 u), los recorta al encuadre y hornea un **SVG inline de 16,5 KB y 67 nodos** entre las marcas
`<!-- MAPA-ROSARIO:inicio -->` y `<!-- MAPA-ROSARIO:fin -->` de `v5/index.html` (no se edita a mano). El SVG no trae
colores: todo va por clase con las variables de la página (`--gold`, `--gold-hi`, `--bg`, `--muted`), así que el
**tema día** (`?tema=dia`) lo sigue solo; el anillo del pin usa el degradé del eclipse en los dos temas. CSS: bloque
propio «ROSARIO · el mapa» (arriba de las reglas de `.ros-txt`, que no se tocaron). JS: un `<script>` chico pegado al
mapa, «ROSARIO · el mapa».

**Movimiento.** Al entrar en pantalla, el río ya está; se **trazan** las orillas y el contorno del municipio (2,2 s,
`stroke-dasharray` con `pathLength=1`, cada orilla un path propio), después aparecen la ciudad (el fondo y las avenidas)
y al final el pin, la lupa y el recuadro. El pin (y el anillo del recuadro, desfasado) **late sólo mientras el mapa se
ve** (IntersectionObserver pone y saca `.rm-vivo`). Sin JS, sin IntersectionObserver o con **prefers-reduced-motion**:
el mapa queda dibujado y quieto.

**Cómo se regenera.** Desde la raíz del repo: `python3 scripts/generar-mapa-rosario.py` (usa la caché de
`scripts/_osm-rosario/`, ignorada por git; si no está, baja los 7 pedidos). `--bajar` vuelve a bajar todo; `--svg
x.svg` escribe además el SVG suelto; `--no-html` no toca la página. En cada corrida verifica que la esquina siga
estando dentro del Municipio de Rosario (si no, para sin tocar nada) y avisa si el nodo de OSM cambió. Lo que se ajusta a
mano está arriba en el script: el encuadre (`SUR`, `NORTE`, `OESTE`, `ESTE`), la ochava (`OCHAVA`), el recuadro
(`DET_X`, `DET_Y`, `DET_L`, `DET_R`), el ancho de calle (`CALLE_M`) y el corte de la ochava (`OCHAVA_M`).

**Verificado (02/11):** los seis `<script>` de la página pasan `node --check`; capturas (`scripts/capturar-home.sh`,
`PANTALLA=1`) a 1440×900 (`ANCLA=rosario`), 1024×768, 390×844 (`ANCLA=rosario` y `ANCLA=mapa-rosario`), día a 1440 y a
390, y reduced-motion, en `_capturas/rosario-mapa/` (ignorado); el estado a mitad del trazado se miró aparte (en la
captura las transiciones van a cero). En la página, con el mapa a la vista queda `rm-vivo` y sin `rm-espera`; fuera de
pantalla, al revés.

**Pendiente / para decidir:**

- Que Matías confirme que la oficina es la esquina **noreste** del cruce (la manzana de Donado al oeste y Chassaing al
  sur). Si fuera otra, alcanza con cambiar `OCHAVA` en el script y regenerar: el lado del cruce que se resalta, el
  anillo del recuadro, los nombres de calle (se corren a las otras manzanas) y el enlace salen de esa medida (el enlace
  está escrito en el HTML: cambiar también la `query` del `href`).
- Google Maps u OpenStreetMap para el enlace (hoy Google, por la app en el celular).
- Si el punto *centro* (el Monumento) suma o sobra, y si el barrio va como *Fisherton* (hoy) o *Nueva Fisherton*.
- Los nombres de calle del recuadro quedan chicos en celular (~7,3 px): si molesta, se sacan en celular y queda sólo
  el rótulo DONADO Y CHASSAING de abajo.
- Al integrar con la rama del video: si el video muestra la ochava desde otro lado, que el recuadro y el video cuenten
  la misma esquina.

#### 0.8.2 La oficina en video (`#oficina`, rama `oficina-video`, 2026-11-02)

> Prompt de giro, verbatim, en `docs/prompts-usuario/2026-11-02-oficina-real-mapa-y-video.md`, con la foto real al lado
> (`2026-11-02-edificio-donado-y-chassaing.jpg`): «El dibujo que hiciste no me parece mal, pero me gustaría que probemos
> algo con video realista hecho con IA, partiendo desde la foto del edificio original, pero transformandolo para poder
> mostrar los distintos espacios que propuse.. le podemos agregar otro piso al edificio, le podemos sacar los carteles
> que dicen "Byte" y poner carteles de RIA Labs, queremos ver solo la esquina con el edificio y no las calles.. estaria
> bueno que este animado, que se vea la gente adentro, como si las paredes exteriores fueran vidriadas.» (El mapa de
> Rosario del mismo prompt es de otra rama, `rosario-mapa`.)

**Qué es.** La figura `#oficina` muestra por defecto un **video en loop** de la esquina real de Donado y Chassaing
transformada con IA: la misma ochava con la puerta y el cartel chico encima, los pilares grises y los árboles de la
vereda, con **un piso más**, **paredes de vidrio** y las **cuatro salas encendidas con gente**: arriba, programadores
frente a sus pantallas y una reunión donde alguien presenta un gráfico de barras; abajo, el laboratorio (un brazo
robótico amarillo, un técnico con su laptop, un banco de herramientas) y el showroom (cámaras sobre pedestales, dos
pantallas grandes con una ciudad, visitantes que miran y señalan). Los carteles de Byte y los vinilos de la vidriera
(«25 años», «Security 24») no están: en su lugar, el anillo y «RIA LABS · SOFTWARE E INTELIGENCIA ARTIFICIAL» arriba,
coronando el piso nuevo, y uno más chico sobre la puerta. Sólo la esquina: una viñeta funde las calles, las casas
vecinas y el cielo en el fondo de la página. **De noche** por defecto (el edificio oscuro, adentro más luz que afuera:
la gente se lee tras el vidrio y la página es nocturna); `?oficina=dia` muestra la versión de día y `?oficina=dibujo`
vuelve al corte dibujado de arriba, que **no se borró**.

- Encima, los **rótulos de las salas** como enlaces (DM Mono, chip oscuro con un punto del color de la sala, flecha al
  pasar): **Sala de programadores** → `/dataflow/` (donde el motor se escribe), **Sala de reuniones** → `#contacto`,
  **Laboratorio** → `/laboratorio/`, **Showroom** → `#productos`. Ubicados en % sobre el techo de cada sala, arriba de la
  gente. En celular, cortos (Programadores, Reuniones).
- Pie (mono): *nuestra esquina de Rosario, imaginada con IA desde su foto*. Es un concepto, no una foto de la oficina
  como está hoy: el pie lo dice. Con `?oficina=dibujo`, el pie de antes.

**Cómo se hizo** (`scripts/generar-oficina-viva.py`, que importa los ayudantes de Replicate de los retratos vivos):

1. **La imagen concepto.** Entrada: la foto recortada a 16:9 sobre el edificio y un cartel de referencia dibujado con
   el anillo de `logos/ria-anillo-color.svg` y el wordmark. Una sola consigna con los cuatro cambios (piso, carteles,
   vidrio con las salas y su gente, sólo la esquina), pidiendo conservar la ochava, las proporciones, los pilares y los
   árboles; gente genérica, inventada, vista de lejos, **nunca el parecido de una persona real**. `google/nano-banana`
   (US$ 0,039) cambió el encuadre y escribió la bajada del cartel ilegible; **`google/nano-banana-pro`** (US$ 0,15 a
   1K/2K, 0,30 a 4K; salida 2752×1536) escribió el cartel bien y armó las cuatro salas legibles. No hizo falta ir por
   pasos. Elegido `concepto-nbp-2` = **el de día**. De ahí, con «cambiá sólo la hora», la hora azul (cielo lavanda,
   poco contraste con el edificio) y, sobre ésa, la **noche cerrada** (`noche-cerrada-nbp-1`) = **el de noche**: mismas
   salas, misma gente en la misma pose, el anillo con su degradé, la bajada legible. 7 ediciones (2 nano-banana y 5 pro), US$ 0,83.
2. **El video.** `kwaivgi/kling-v2.5-turbo-pro` con la imagen (16:9, 1920×1080) como **primer y último cuadro** (el
   truco del loop de los retratos), cámara fija. La primera consigna (5 s, «movimientos chicos») dejó casi una foto: la
   gente se movía lo que el ruido del códec. La que quedó (`CONSIGNA_VIDEO_ACTIVA`, 10 s) pide acciones que se lean
   desde la vereda de enfrente y que vuelvan a su lugar: en el showroom un visitante camina hacia la pantalla, la señala
   y vuelve; en reuniones el que presenta barre las barras con la mano y la mesa lo sigue con la cabeza; un programador
   gira la silla hacia el de al lado y vuelve; el brazo robótico gira y vuelve; las hojas apenas. Negativo: movimiento
   de cámara, edificio que se deforma, gente que se transforma, carteles que cambian. 4 clips, US$ 2,45. Revisados
   cuadro a cuadro por sala (tiras a 1 fps al 100 %): edificio, carteles y letras quietos; nadie cambia de cara, cuerpo
   ni ropa. El brazo, al girar sobre su base, se ve de canto unos segundos (fino y oscuro): es una pose, no se deforma.
3. **El loop, en post.** Noche: `kling-noche-activo-2` → `kling-noche-activo-1` (los dos parten y terminan en la misma
   imagen), juntas fundidas en 12 cuadros (0,5 s), nunca ping-pong: 19,17 s. Día: un clip, 9,58 s. Cada cuadro a
   1440×810 y viñeteado hacia `#0b0a14` con una elipse «súper» (norma 2,6; plena hasta 0,70 del semieje, cielo en 1,04).
   Cierre medido sobre el edificio: 0,54 en los PNG (paso medio 0,09, y el fundido arrastra un resto del gesto del que
   presenta), 1,26 en el mp4 y 0,60 en el webm: lo que suma el mp4 es grano del I-frame contra el último P-frame, parejo
   en toda la imagen y sin cambio de brillo (bajar el crf a 18 sólo lo lleva a 1,07 y duplica el peso). El póster es el
   cuadro 0 del loop.

**En la página.** HTML: dentro de `<figure id="oficina">`, `.ros-vid` › `.ros-vid-lienzo` (16:9) con la foto
(`<img loading="lazy">`, con el `alt` que describe la escena), el `<video muted loop playsinline preload="none">`
(`aria-hidden`: es la misma imagen animada) y los cuatro `<a class="ros-sala">` con su `--x`/`--y`; después, el `<svg>`
del dibujo; el `figcaption` lleva los dos pies. CSS (bloque «ROSARIO», después de `.ros-pie`): `data-oficina` en la figura
elige qué se ve; la máscara CSS termina de fundir la viñeta del asset (en el tema día cierra antes, sobre el papel); en
celular (≤860 px) la caja pasa a 3:2 y el lienzo se agranda a 118,5 % del ancho, recortando los costados, que son viñeta,
sin mover los rótulos de su sala; `scroll-margin-top` para que `#oficina` no quede bajo la nav. JS: un bloque nuevo al
principio del script «ROSARIO · la oficina dibujada»: lee `?oficina=`, cambia las fuentes a `-dia` si hace falta, y con
dos IntersectionObserver **empieza a bajar el clip a 400 px de la vista** y **lo corre con la figura a la vista y la
pestaña visible** (lo pausa si no); el clip aparece sobre la foto recién cuando corre. Con **prefers-reduced-motion o
Save-Data no se pide el clip**: queda la foto. El dibujo se arma sólo con `?oficina=dibujo` (antes de eso no hace nada).

**Verificado (2026-11-02):** los cinco `<script>` pasan `node --check`. Capturas (`scripts/capturar-home.sh`, `PANTALLA=1
ANCLA=oficina`) a 1440×900 y 390×844, de noche, de día (`?oficina=dia`), con el tema día, con reduced-motion y con el
dibujo, en `_capturas/oficina-video/` (ignorado), sin `Uncaught`. En headless el clip corre (la captura con el tema día
agarró un cuadro con el brazo girado).

**Costo de Replicate:** US$ 3,28 de un tope de 8 (7 ediciones + 4 clips, 11 predicciones, ninguna fallida; el libro con los ids queda en
`_capturas/oficina-video/costos.jsonl`).

**Pendiente / para decidir (Matías):**

- **¿Video o dibujo?** Por defecto queda el video; el dibujo sigue entero en `?oficina=dibujo`.
- **¿Noche o día?** Por defecto, noche. Las dos imágenes concepto enteras están en `assets/oficina-rosario-concepto-{noche,dia}.jpg`.
- **¿Los rótulos como enlaces?** Están; si distraen, se dejan como texto quitando los `href`.
- ~~**El segundo párrafo de la sección** habla todavía del dibujo («Esta es la oficina, sin la pared del frente… En la ochava,
  una cámara mira la calle»): el video no tiene la cámara de la ochava. El texto nuevo lo aplica la madre (no es de esta
  rama, que no toca `.ros-txt`).~~ **Resuelto al integrar (02/11):** «Esta es nuestra esquina como la imaginamos…».
- Si se quiere que el tema día muestre el video de día solo (hoy el tema y la luz del video son independientes).
- Lo que el concepto inventa y habría que confirmar: el piso de arriba con las paredes de vidrio, el showroom en la planta
  baja hacia la ochava, el brazo robótico.


### 0.9 Móviles (02/11, rama `moviles-0211`)

> Pedido de Matías antes de la Smart City Expo (muestra el sitio desde el teléfono y la tablet), verbatim en
> `docs/prompts-usuario/2026-11-02-moviles-en-todo-el-sitio.md`. Sin textos nuevos: sólo media queries de pantalla táctil
> (`(hover: none), (pointer: coarse)`), angosta (≤860 / ≤480) o de **teléfono en horizontal** (`(orientation: landscape)
> and (max-height: 500px)`), y la lógica de entrada. **El escritorio no cambia**: la caja de cada elemento HTML de las
> cuatro páginas es la misma en 1440×900 (y la home también en 1024×768, 1280×720 y 1920×1080), medida contra `main`.

- **Nav (bloque NAV, idéntico en las cuatro páginas).** En táctil, logo, enlaces, MENÚ y Conversemos tocan a ~44 px sin
  cambiar el dibujo (padding con margen negativo o un `::before` invisible). El menú tiene `max-height` de la pantalla y se
  desplaza: en horizontal (390 px de alto) «Rosario» y «Conversemos» quedaban afuera y no se podían tocar. Con el teléfono
  en horizontal la nav pierde el aire de arriba aunque pase de 860 px (Android 915×412).
- **Home · la portada en horizontal.** El piso de 560 px estiraba el hero a pantalla y media y los dos retratos (debajo de
  RIA / LABS) quedaban fuera de la primera pantalla. Ahora el hero mide la pantalla y en el 5 los retratos vuelven a los
  costados del eclipse con las proporciones de desktop (0,64 y 0,65 del eclipse), en 844×390, 915×412 y 932×430.
- **Home · la máquina en horizontal** va horizontal, a lo ancho: el script «LA MÁQUINA» usa la vertical sólo con la
  pantalla angosta parada (`(max-width: 860px) and (orientation: portrait), (max-width: 860px) and (min-height: 501px)`).
- **Home · los astros.** En táctil el círculo que se toca de cada satélite es 22 unidades más grande que el cuerpo (era 12:
  ~25 px en un teléfono, ahora ~40). En ≤860 las etiquetas pasan de 9 a 13 unidades (6 px → 10 px en un teléfono) y sin
  el subtítulo, que está en la lista; en ≤480 la viñeta sangra 16 px a cada lado. El script mide el ancho de la etiqueta con
  la letra que de verdad tiene y no la deja salirse de la pantalla (en desktop sobra margen y queda igual que antes).
- **Home · toques y letra.** `.pi-link`, el correo y los rótulos de la oficina tocan a ~40–48 px (eran 17–21). La línea de
  arriba y la de la feria pasan de 9 / 8,5 px a 10 px (con `text-wrap: balance`), los rótulos de las salas de 9 a 10 px y
  la bajada de Bird Map de 13,5 a 14 px. En las cuatro páginas, el pie de la tablet acostada (enlaces de 12 px) toca a ~45 px. El anillo del separador (540 px) se recorta en su caja; la red abierta de la
  máquina, en su banda (`overflow-x: clip`): en iOS el `overflow-x` del body no siempre impide arrastrar de costado.
- **Home · la oficina en horizontal**: el video vuelve a 16:9 sin recortar los costados y se achica al alto de la
  pantalla (en 3:2 medía casi pantalla y media). Los retratos del stand se clonan de un `<template>`: ahora se les pone
  `muted` como propiedad además del atributo (sin eso iOS puede no arrancarlos solos).
- **/dataflow/**: las entradas del motor vertical de 9 a 10 px; la leyenda del pie toca a ~41 px.
- **/laboratorio/**: los rótulos mono de las fichas de 9 / 9,5 a 10 px; los dos enlaces de la mudanza tocan a ~32 px cada uno (eran 13; van a 8 px uno del otro y se reparten el espacio); en
  horizontal las dos puertas van de a par y el video de la ochava entra en el alto de la pantalla.
- **/metodo/**: los epígrafes de las figuras no bajan de 11 px; en horizontal cada estación va como en desktop (texto y
  artefacto lado a lado) y el artefacto entra en el alto de la pantalla.

**Cómo se verificó.** El banco común de las seis sesiones (Chrome headless con touch real y UA de iPhone/iPad/Android) en
375×667, 390×844, 412×915, 844×390, 820×1180, 1180×820 y 1440×900, más 915×412 y 932×430; toques reales
(`touchscreen.tap`) sobre los satélites con el dedo corrido 14 px del centro, sobre los enlaces 9 px por encima del texto y
sobre el menú desplazado; la altura que de verdad responde al toque medida con `elementFromPoint`. **Pendiente / para
Fable:** el astro en celular sigue siendo chico para seis sabores con nombre (las etiquetas se pisan a ratos); la portada
en la tablet parada (820×1180) usa la composición de celular (retratos debajo de RIA / LABS), que entra pero queda
despareja; el resto de las etiquetas mono decorativas siguen en 10 px.

---

## 1. Identidad de marca

### 1.1 Nombre y denominación

- **Nombre comercial:** RIA Labs
- **Dominio vigente:** rialabs.ar
- **Dominio previo (v1):** rialabs.ai (queda rastro en el email `hola@rialabs.ai` del prototipo v1)
- **Lectura del nombre a lo largo de las versiones:**
  - v1 → "RIA Labs. — Inteligencia Artificial Enriquecida"
  - v2 → "RIA Labs — Software e Inteligencia Artificial"
  - v3 → "RIA Labs" (tagline: "Inteligencia artificial aplicada")
  - v4 → "RIA Labs — Software e Inteligencia Artificial" (denominación actual)

### 1.2 Taglines / descripciones (evolución)

| Versión | Tagline / descripción |
|--------|-----------------------|
| v1 | "Entendemos tu negocio. Creamos el software que lo transforma." — "Consultora de software e inteligencia artificial. Entendemos tu negocio, creamos la solución. Rápido, simple, con impacto real." |
| v2 | "Transformamos los procesos de tu empresa con inteligencia artificial y software a medida. Nacidos de Byte y VRIO. Rosario, Argentina." |
| v3 | "Inteligencia artificial aplicada" — "Software a medida · Consultoría en IA — Rosario, Argentina." |
| v4 (actual) | "Transformamos los procesos de tu empresa con inteligencia artificial y software a medida. Nacidos de Byte y VRIO. Rosario, Argentina." |

### 1.3 Metáfora visual central

El **eclipse solar total** (anillos cálidos naranjas/dorados con disco lunar oscuro) funciona como símbolo de RIA: infraestructura + IA en el momento exacto de convergencia. Se usa en el hero de todas las versiones y como icono del sistema (`assets/ria-labs-eclipse-icon.svg`, favicons).

### 1.4 Frase filosófica / corazón narrativo

> "Tu infraestructura ya existe. Nosotros la hacemos pensar."
>
> (Vigente de nuevo desde el 2026-10-14: es el pie de la máquina, debajo del logo en el hero. El hero no tiene
> titular.)

> **Metaestructura**
>
> (Histórica: titular del hero del 13 al 14 de octubre de 2026, en M PLUS Rounded 1c 800, con la frase de Matías
> como cita debajo; antes, unas horas, «Superestructura». Guardada como idea en
> `docs/ideas/2026-10-13-discurso-metaestructura.md`.)

Históricas:

> **DE VER A SABER**
>
> (Titular del hero de v5 del 10 al 13 de octubre de 2026: sin punto, en mayúsculas, en Cormorant Garamond. Debajo
> iba esta prosa, que incluía sin atribución la frase *el verdadero signo de la inteligencia no es el conocimiento
> sino la imaginación* —circula atribuida a Einstein y se publicó sin nombrarlo, por decisión de Matías—:
> «El conocimiento ya lo tienen las máquinas: cada cámara, cada sensor, cada registro, acumulado sin cansancio. Pero
> el verdadero signo de la inteligencia no es el conocimiento sino la imaginación, y esa parte sigue siendo humana:
> una máquina puede saberlo todo de una esquina y no imaginar jamás un semáforo distinto. Nosotros ponemos la
> imaginación; el motor, la memoria y la atención que no duermen. Cuando las dos se alinean, como el sol y la luna
> por un instante, aparece algo que antes no estaba: una infraestructura que piensa.» Matías lo descartó el 13/10:
> «muy ñoño».)

> "Tu infraestructura ya existe. Nosotros la hacemos pensar."
>
> (v2 → primera v5. Texto incrustado en la ilustración animada del hero en v4 y titular del hero en la primera v5; versión v2 usaba "Tu infraestructura visual ya existe. Nosotros la hacemos pensar." Sobrevivió hasta el 13/10 como cierre de la prosa del hero: «una infraestructura que piensa».)

Declaración complementaria (sección Mercado, hover del nodo central en v4):
> "Lo que transforma a una empresa no es la tecnología que adopta — es el momento en que decide, por primera vez, mirarse de verdad."

---

## 2. Propuesta de valor y posicionamiento

### 2.1 Qué dice la empresa que hace

- Transforma procesos de empresas con IA y software a medida.
- Parte de la infraestructura que la empresa **ya tiene** — no reemplaza, potencia.
- "Diseñamos y construimos la solución exacta — con el stack más simple, rápido y efectivo posible."

### 2.2 Diferencial declarado

- No adapta plataformas genéricas: construye arquitectura propia desde cero.
- "La combinación de **acceso directo a clientes con infraestructura instalada** y **capacidad de desarrollo propio de soluciones de IA** — en el mismo equipo — no existe en el mercado argentino." (v2)
- Velocidad con método: del diagnóstico al primer sistema en producción en **5 semanas**.

### 2.3 Números clave (stat bar de v4)

- **70%** de las empresas argentinas sin estrategia de IA.
- **100%** de los procesos operativos de una empresa con potencial de IA sin explotar.
- **25+** años de experiencia en infraestructura y operaciones reales (aportados por Byte).
- **5 sem** del diagnóstico al primer sistema funcionando en producción.

> Nota: v2 usaba "70% de las pymes argentinas sin estrategia de IA" y "~100% de las cámaras instaladas sin generar valor de negocio" — en v4 el discurso se amplió de CCTV a procesos en general.

---

## 3. Servicios

Cuatro líneas de servicio, con evolución del enfoque entre versiones.

### 3.1 Versión actual (v4)

| # | Categoría | Título | Descripción |
|---|-----------|--------|-------------|
| 01 | Consultoría estratégica | Diagnóstico y estrategia IA | Auditamos tu infraestructura y tus procesos, identificamos dónde la IA genera el mayor impacto y diseñamos el camino más corto para llegar ahí. |
| 02 | IA generativa | Lenguaje, documentos y conocimiento | Asistentes internos, procesamiento automático de documentos, extracción de información y consultas en lenguaje natural sobre los datos del negocio. Sin reemplazar los sistemas que ya usás. |
| 03 | Desarrollo a medida | Software propio desde cero | Construimos la arquitectura que tu problema requiere. Sin soluciones genéricas. El cliente sabe en todo momento qué se está construyendo. Los primeros resultados pueden estar aplicados en semanas. |
| 04 | SaaS y escalabilidad | Sistemas que crecen con el negocio | Monitoreo y actualización continua hasta que la arquitectura queda consolidada. El sistema crece a la par que escala la operación. Cuanto más opera, más inteligente se vuelve. |

### 3.2 Evolución entre versiones

- **v1** tenía Consultoría / Desarrollo / Automatización / Integración (más genérico).
- **v2** hacía foco en visión artificial y OCR (01 OCR e inteligencia visual).
- **v4** reemplaza "OCR e inteligencia visual" por **"Lenguaje, documentos y conocimiento" (IA generativa)** — cambio de foco estratégico: de visión artificial como protagonista a IA generativa.

---

## 4. Metodología y principios

> Desde el 2026-11-01 los seis principios vigentes (los de la v5, no los de abajo) viven en su propia página,
> `/metodo/`, cada uno con su artefacto animado: §0.6.

### 4.1 Seis principios (idénticos en v2 y v4 — núcleo filosófico estable)

1. **El problema primero, la tecnología después.** No llegamos con una solución buscando un problema. La IA es el medio, no el fin. Si la mejor solución es simple, así la hacemos.
2. **Velocidad sin improvisación.** Construimos rápido porque tenemos un proceso claro. La velocidad viene de la experiencia acumulada en dos empresas con años de trabajo real en campo.
3. **Simplicidad como estándar de calidad.** Un sistema que nadie usa no sirve. Diseñamos para que el equipo del cliente adopte naturalmente. La complejidad no es señal de calidad — la adopción sí.
4. **Resultados medibles desde el día uno.** Definimos métricas de éxito antes de escribir la primera línea de código. Al final de cada ciclo, hay números concretos. No trabajamos en la oscuridad.
5. **Ingeniería creativa con rigor técnico.** VRIO aporta los nuevos paradigmas y la artesanía de sistemas. Byte aporta la solidez operativa de 25 años en el terreno. Los dos son necesarios.
6. **Transferencia real de conocimiento.** El objetivo no es que nos necesites para siempre. Documentamos, capacitamos y aseguramos la autonomía total del equipo del cliente.

### 4.2 Proceso de trabajo (v2, eliminado en v4 como sección explícita)

1. Diagnóstico gratuito — auditoría sin costo ni compromiso.
2. Diseño de la solución — arquitectura simple, métricas antes de construir.
3. Activación e integración — setup sobre infraestructura existente, resultados antes del primer mes.
4. MVP funcional en 5 semanas — operativo, con capacitación.
5. Evolución continua — monitoreo permanente, el sistema aprende con el uso.

### 4.3 Métricas del método (v1/v2)

- **5 semanas** del diagnóstico al primer sistema en producción.
- **1** interlocutor técnico dedicado por proyecto.
- **100%** software propio (nunca adaptaciones sobre terceros).

---

## 5. Casos en producción — ⚠️ REMOVIDOS DE v4 (2026-08-06)

> **Cambio de arquitectura de contenido.** Los dos bloques de "Caso en producción" (`#caso` Byte Analítico y `#caso-comms` RIA Comms) **ya no existen en el home**. En su lugar hay una **introducción al Laboratorio** (§5bis.0) que lleva a la página `/laboratorio/`, donde los mismos proyectos —y tres más— se presentan con más profundidad y sus números medidos.
>
> El material de 5.1 y 5.2 se conserva acá como **archivo institucional**: sigue vivo en los prototipos v1–v3 y sirve como fuente de copy reusable. No describe el sitio vigente.
>
> Con los bloques se removió también su CSS, que quedó sin uso: `.case-grid` · `.case-pill` · `.case-name` · `.case-b` · `.case-res` · `.c-r*` · `.client-logo-wrap` · `.client-cname` · `.fiat-*` · toda la familia `.term*`/`.t-*`/`.b-*` (terminal) y `.chat*` (mockup de WhatsApp). `.case-wrap` **sí sobrevive**: lo reusa la sección de Laboratorio.

### 5.1 Byte Analítico — Seprio (concesionaria oficial Fiat, Rosario) · *archivo*

**Descripción vigente (v4):**
> Construimos para Seprio — concesionaria oficial Fiat en Rosario — el sistema nervioso de toda su operación vehicular. Cada unidad que entra al predio queda identificada, trazada y gestionada en tiempo real hasta que el cliente se la lleva. Un nuevo sistema cambió la forma de trabajar, organizó la información y dotó al proceso de memoria y conocimiento.

**Descripción original (v1/v2):**
> Una concesionaria oficial de autos no sabía dónde estaba cada vehículo dentro de su predio. El stock se gestionaba a mano. Las búsquedas consumían tiempo. Los errores eran frecuentes y costosos. Instalamos una cámara estratégica y construimos un sistema de reconocimiento de patentes por OCR enriquecido con IA.

**Métricas publicadas (v1 y v2):**
- 100% trazabilidad vehicular en tiempo real.
- 0 registros manuales de movimientos.
- −60% tiempo de búsqueda de vehículos en planta.
- 1 cámara — todo lo que necesitó el sistema.

**Dato operativo mostrado en v4:** 1.100 vehículos activos · OCR + IA · tiempo real.

**Link externo:** https://byte-analitico-v2.netlify.app (v3).

### 5.2 RIA Comms — Primeros usuarios: Byte + VRIO (operación comercial sobre WhatsApp) · *archivo*

**Descripción vigente (v4):**
> Construimos una capa de comunicación inteligente sobre WhatsApp. Cada lead que entra es clasificado, ruteado al responsable adecuado y acompañado por bots de management que dan visibilidad en tiempo real. Un nuevo sistema pasa la operación comercial de ser una bandeja de mensajes a un proceso medido, con memoria y reportes. Byte y VRIO fueron los primeros equipos en usarlo en producción sobre sus propias operaciones.

**Posicionamiento:** dogfooding — RIA Labs construyó el sistema y lo usó internamente (Byte para inbound de infraestructura/seguridad, VRIO para inbound de software) antes de ofrecerlo a clientes externos.

**Mockup mostrado (terminal `ria_comms · whatsapp_thread`):**
- Lead entrante consultando por un sistema de cámaras para una oficina.
- Clasificación automática + auto-asignación a Sebastián (Byte).
- Respuesta coordinando relevamiento.
- Bot de management resumiendo `/leads · 9 activos · 3 nuevos hoy · 0 sin asignar`.

**Dato operativo (footer del mockup):** Lead intake · auto-ruteo · audit log · tiempo real.

**Marca / atribución mostrada:** badge "BYTE · VRIO" (BYTE en azul `--blue`, VRIO en dorado `--gold-hi`), respetando la paleta de los dos planetas del orbit animado del cierre del sitio.

**Anchor:** `#caso-comms` (el bloque comparte estilos `.case-wrap` con el de Byte Analítico y aparece inmediatamente debajo).

---

## 5bis.0 Laboratorio en el home (sección `#laboratorio`, v4 vigente)

Ocupa el lugar que tenían los dos casos, con el mismo tratamiento visual (`.case-wrap`: banda `--bg3` con bordes arriba y abajo), de modo que el ritmo de la página no cambia.

- **Label:** "Laboratorio" · **Título:** "Lo que estamos construyendo"
- **Copete:** "Trabajamos como un laboratorio de investigación y creación permanente: buscamos problemas reales, viejos y caros, y probamos si la inteligencia artificial los rompe. **Un experimento vale cuando produce un número** — no una maqueta, no una promesa de roadmap. Lo que sobrevive a esa prueba se vuelve producto, con cliente adentro."
- **Grilla de dos columnas** (`.lab-grid` / `.lab-card`): cuatro tarjetas más una **de ancho completo** (`.lab-card.wide`, el proyecto 05) — con cinco tarjetas en dos columnas, la alternativa era dejar la última sola al lado de un hueco. Cada tarjeta es un link a su ancla en la página del Laboratorio, con barra de acento que crece en hover y "Ver el proyecto →" que aparece (siempre visible ≤860 px, porque en touch no hay hover). En una columna (≤860 px) la tarjeta ancha vuelve a `grid-column:auto`: si siguiera pidiendo dos, la grilla inventaría una columna implícita.

| Tarjeta | Estado | Destino | Prueba que aporta |
|---|---|---|---|
| RIA Drivecore | En producción · Seprio, Rosario | `/laboratorio/#p01` | 1.100 vehículos activos, todos los días |
| Analítica de video · seguridad | v1 cerrada · instalable | `/laboratorio/#p02` | "Una pantalla nueva no se programa: se configura" |
| RIA Comms | En producción · Byte + VRIO | `/laboratorio/#p03` | Byte y VRIO lo usan sobre su propia operación |
| Tránsito inteligente | Prototipo · medido en calle | `/laboratorio/#p04` | −27 % de demora contra tiempo fijo |
| Sensores urbanos para la ciudad (ancho completo) | Midiendo 24/7 · piloto propio en Rosario | `/laboratorio/#p05` | Cuatro verticales sobre una sola cámara, sin nube y sin obra |

- **CTA:** botón dorado "Entrar al laboratorio →" hacia `/laboratorio/`.

> Esta sección es la que ahora carga la **prueba de producción** que antes daban los bloques de caso: por eso las tarjetas de Drivecore y Comms nombran explícitamente al cliente y el uso real.

---

## 5bis. Página Laboratorio (`/laboratorio/`)

> **Reemplazada el 2026-11-01** por la página nueva (§0.1, «La página del Laboratorio»): la casa, las dos puertas, el
> linaje y dos expediciones. Lo que sigue describe la página de agosto–octubre, como archivo.

> Página propia (no una sección del home). Agregada el 2026-08-06. Misma identidad visual que v4
> (Saira + DM Mono, fondo `#0b0a14`, dorado, ruido, reveals por IntersectionObserver), con un color
> de acento por proyecto.

### 5bis.1 Posicionamiento

Presenta la **modalidad de trabajo** de RIA Labs como laboratorio de investigación y creación permanente, y los cinco proyectos en curso con su estado declarado y sus números medidos. Desde el 2026-08-06 es **el único lugar del sitio donde se muestran los proyectos**: el home sólo tiene la introducción que lleva acá.

- **Título:** "Laboratorio"
- **Eyebrow:** "RIA Labs · investigación y construcción"
- **Copete:** "Trabajamos como un laboratorio: una pregunta, un prototipo que corre sobre datos reales, y una medición que decide si sigue. Esto es lo que hay hoy sobre la mesa."
- **Frase del manifiesto:** "No investigamos para publicar. Investigamos para que algo *funcione en la calle*."
- **Cierre:** "¿Tenés un problema que nadie resolvió?"

### 5bis.2 Los cinco proyectos

> **El orden es de producto, no cronológico** (fijado el 2026-08-14): Drivecore · Analítica de
> video como **vertical de seguridad** · Comms · Tránsito · Sensores urbanos. Los `id` de sección
> son POSICIONALES (`#p01`…`#p05`), así que reordenar mueve las anclas: al intercambiar Comms y
> Tránsito hubo que repuntar las tarjetas del home. La banda alterna (`.proj-alt`) también va por
> posición: pares con fondo `--bg3`, impares lisos.
>
> **Frontera 02 ↔ 05 (explícita en la página):** la seguridad vive en el 02 y la calle en el 05.
> El 02 la nombra ("este es el lugar de la seguridad… separado a propósito del proyecto 05") y el
> 05 la excluye con dirección ("fuera de este producto — vive en el 02", y lo mismo en la ficha
> de contexto). Es el mismo argumento comercial de los dos lados: un municipio puede comprar
> medición sin abrir el debate de la vigilancia.

| # | Proyecto | Bajada | Estado declarado | Acento |
|---|----------|--------|------------------|--------|
| 01 | **RIA Drivecore** | El sistema operativo de una concesionaria | En producción · Seprio, Rosario | `#EF9F27` dorado |
| 02 | **Analítica de video** | La vertical de seguridad · plataforma de monitoreo con motor propio | v1 cerrada · instalable | `#4a8fd4` azul |
| 03 | **RIA Comms** | La conversación con el cliente, como infraestructura | En producción · Byte + VRIO | `#7F77DD` violeta |
| 04 | **Tránsito inteligente** | Semáforos que ven, en vez de adivinar | Prototipo · medido en calle | `#4fd48f` verde |
| 05 | **RIA Smartcity** | La ciudad medida con las cámaras que ya tiene | Midiendo 24/7 · piloto propio en Rosario | `#2fd0c8` teal |

**Enlaces a sitios propios:** tres de los cinco proyectos tienen hoy su propia presentación
publicada, enlazada desde la página Laboratorio con el componente `.sitio` / `.sitio-a`, que
toma el acento de la sección (`--acc`) y por eso sirve igual en cualquiera de los cinco. El
enlace va siempre después del último `proj-lead`, antes del primer artefacto:

| # | Destino | Rótulo publicado |
|---|---------|------------------|
| 01 | `https://drivecore.rialabs.ar` | RIA Drivecore · toda la concesionaria, un solo sistema vivo ↗ |
| 02 | `https://analitico.rialabs.ar` | Byte Analítico · un producto, dos brazos: Integradores y Monitoreo ↗ |
| 05 | `https://smartcity.rialabs.ar` | RIA Smartcity · cinco verticales sobre las cámaras que ya están ↗ |

Los proyectos **03** (RIA Comms) y **04** (Tránsito inteligente) todavía no tienen sitio propio:
cuando lo tengan, se agregan con el mismo componente, sin CSS nuevo.

**Números publicados por proyecto:**

- 01 — 1.100 vehículos activos · 7 secciones del circuito · 100 % de unidades por control de calidad · 5 semanas al primer módulo.
- 02 — 1 fila de configuración separa una pantalla de otra · 5 pasos del asistente · 145 verificaciones de aislamiento · 390 px de ancho mínimo usable.
- 03 — 3 reintentos exponenciales · ~0,5 s de lectura de conversaciones · 1 motor para todas las empresas · 0 líneas de un cliente dentro de la plataforma.
- 04 — **−27 %** de demora contra tiempo fijo · 15-18 ms de inferencia por cuadro · 0 falsos positivos sobre asfalto mojado · 15 fps sin cuadros perdidos. Referencia externa citada sin nombrar la empresa: −23 % en tiempos de viaje, 15 cruces, 4 años.
- 05 — 4 verticales sobre una sola cámara · 24/7 midiendo una esquina real de Rosario · 0,01 ms por cuadro cuesta buscar cuasi-accidentes · **−61 %** de los conflictos de la primera corrida eran artefactos (descartados mirando la imagen, uno por uno).

**El 05 declara sus límites en la propia página**: es una cámara en una esquina y no un municipio instalado; el semáforo corre contra su controlador sombra y no contra un cruce conectado; la calibración de esa ochava es provisoria hasta medir dos distancias con cinta. También declara lo que queda **fuera del producto a propósito**: la vertical de seguridad ciudadana (aparece en la tira de verticales atenuada, con el motivo escrito).

> **Nota de nomenclatura:** en el proyecto Seprio conviven "RIA Track" (presentación v2, `track.rialabs.ar`) y "RIA Drivecore" (presentaciones v3/v4, más recientes). La página Laboratorio usa **RIA Drivecore**.

> **Menciones deliberadamente indirectas:** la plataforma de gestión de video de referencia y la compañía británica de control de tránsito se describen por su categoría, sin nombrarlas.

### 5bis.3 Artefactos animados

| Sección | Artefacto | Técnica |
|---|---|---|
| Hero | Campo orbital: núcleo de eclipse con enjambre de partículas y cinco planetas con estela, uno por proyecto. Hover ilumina órbita + tarjeta de leyenda; clic navega al proyecto. | SVG + `requestAnimationFrame` (misma matemática elíptica que el orbit de Equipo en v4) |
| 01 | Circuito de la unidad: token de vehículo recorriendo 7 estaciones (Recepción → Lavado → Taller → Prueba → Calidad → Terminado → Retirado), sellando filas en un ledger de auditoría en vivo. | SVG + rAF + DOM |
| 02 | Pantalla de monitoreo configurable: 3 presets (peatonal facial · vehicular patente+aforo · perímetro cruce de línea) que reconfiguran 4 viewports de cámara, la fila de definición de evento y los chips de veredicto. Rota sola hasta que el usuario elige. | SVG generado por JS |
| 03 | Recorrido de un mensaje: tres empresas → compuertas RLS → motor → cuatro salidas (ruteo, webhook firmado, primitivas de IA, registro y costo). | SVG + SMIL `animateMotion` |
| 04 | Espira vs cámara: el mismo auto sobre dos sensores; la espira emite un bit (con traza de onda cuadrada), la cámara emite distancia, velocidad, clase y ETA. Más barras de anticipación 52 m vs 150 m. | SVG + rAF |
| 05 | **Capturas del sistema corriendo** (no diagramas): el portal de la ciudad a lo ancho, y un selector de cuatro pestañas (Movilidad · Espacio público · Estacionamiento · Ambiente) que cambia la captura **y su pie**, porque el pie es lo que dice qué mirar en cada pantalla. Reusa `.sw-tabs`/`.sw-tab` del artefacto 02: la pestaña activa toma el acento de su proyecto (`var(--acc)`), no un azul fijo. | `<img>` + JS mínimo |
| 05 | Bloque de **contexto teórico** (`.teo`): seis fichas sobre qué es y qué no es una smart city — la definición, la capa que falta, la crítica seria, sensor vs. cámara, el argumento económico y la portabilidad del dato. 3 columnas → 2 (≤980 px) → 1 (≤860 px). | CSS grid |

Los tres diagramas anchos (`#circ-svg`, `#vs-svg`, `#comms-svg`) se recorren en horizontal en pantallas ≤860 px en vez de encogerse hasta ser ilegibles.

### 5bis.4 Videos y capturas

Extractos de una corrida real del prototipo de tránsito, sin acelerar ni editar, sobre la cámara de calle:

| Archivo | Contenido | Peso |
|---|---|---|
| `laboratorio/media/traffic-dashboard.mp4` (+ `.jpg` poster) | Pantalla completa del controlador: video con detecciones, fase del semáforo, métricas medidas/calculadas y comparador contra tiempo fijo | ~1,7 MB · 26 s |
| `laboratorio/media/traffic-deteccion.mp4` (+ `.jpg` poster) | Primer plano de la detección: cajas con clase, velocidad y ETA | ~1,0 MB · 18 s |

Ambos son `muted loop playsinline preload="none"`; cargan y arrancan sólo al entrar en viewport y se pausan al salir. Se respeta `prefers-reduced-motion`.

Capturas del proyecto 05, tomadas del sistema corriendo el 2026-08-14 sobre la cámara de la ochava (`loading="lazy"`, ~1,3 MB en total):

| Archivo | Contenido |
|---|---|
| `laboratorio/media/sc-portal.jpg` | Portal de la ciudad: mapa con los sensores como pines, el pulso del día redactado y las alertas recientes |
| `laboratorio/media/sc-movilidad.jpg` | Conteos por línea, giros O/D, histórico por hora, estudio de velocidades, casco en moto y panel de near-miss |
| `laboratorio/media/sc-esppub.jpg` | Peatones y bicis, permanencia, y las desire lines acumuladas |
| `laboratorio/media/sc-estac.jpg` | Ocupación del cordón con rotación y estadía + grilla horaria de doble fila |
| `laboratorio/media/sc-ambiente.jpg` | CO₂ estimado, chequeos de escena por modelo de visión y desglose por línea × clase |

> Las capturas se dejan **como salieron**, con las filas en cero incluidas: donde no hubo velocidad medida el sistema no estima emisiones y lo aclara. El pie del artefacto señala eso explícitamente en vez de esconderlo — es el mismo criterio que hace que el comparador del semáforo se quede mudo sin muestra suficiente.

### 5bis.5 Las seis reglas del laboratorio

1. **La pregunta antes que el producto** — si la pregunta no tiene respuesta medible, es una idea, no un proyecto.
2. **El prototipo es la tesis** — corre sobre datos reales o no probó nada.
3. **Si no está medido, no se dice** — y si el número todavía no es confiable, se oculta.
4. **Los límites los decimos nosotros** — cada proyecto publica lo que todavía no hace.
5. **Lo que aprendemos se vuelve pieza** — el mismo detector cuenta autos, lee patentes y dispara el ingreso.
6. **Se instala, no se demuestra** — sin procedimiento de instalación, sigue siendo un experimento.

---

## 6. Mercado / Verticales objetivo

### 6.1 Versión actual (v4) — 6 rubros

| Rubro | Título | Descripción |
|-------|--------|-------------|
| Concesionarias | Gestión y trazabilidad | Automatización del registro de stock, movimientos y atención al cliente. Procesos hoy manuales, operando solos. |
| Seguridad | Monitoreo automatizado e inteligente | Infraestructura de seguridad existente que deja de ser pasiva: detección automática de eventos, alertas inteligentes y reportes continuos. |
| Logística | Operaciones e inteligencia | Visibilidad en tiempo real sobre movimientos, stock y tiempos de entrega. Decisiones operativas con datos. |
| Retail | Inteligencia comercial | Análisis de comportamiento, optimización de operaciones y detección de oportunidades a partir de lo que ya pasa en el negocio. |
| Industria | Eficiencia operativa | Control de producción, cumplimiento de protocolos y auditoría continua de procesos. Menos fricción, más output. |
| Servicios | Flujos y atención | Automatización de operaciones, registros y reportes de gestión. Asistentes internos para equipos de atención. |

### 6.2 Diferencia con v2

v2 incluía **Countries** (propiedades y accesos) en lugar de **Seguridad** como rubro explícito, y el tono estaba más orientado a CCTV/visión artificial. En v4 el mercado se generalizó y entró Seguridad como categoría propia.

---

## 7. Equipo / Origen

> **Desde el 2026-11-01 la home ya no tiene sección de equipo:** «El equipo» pasó a ser `#rosario`, la oficina dibujada
> (§0.8). Lo que sigue queda como archivo de las fichas (bios, oficios, retratos); los retratos del stand siguen en la portada.

### 7.1 Co-fundadores

> **Retratos (2026-08-14):** las fichas de los dos co-fundadores llevan **foto redonda de 112 px a la izquierda del nombre y el rol**, alineada a su altura (`.f-head`, flex con `align-items:center`), en el lugar que antes ocupaba el círculo con las iniciales. Las iniciales siguen en el DOM **debajo** de la imagen (`.f-init` dentro de `.f-photo`): si la foto no carga, el círculo sigue diciendo quién es. Archivos en `assets/equipo-<nombre>.jpg` (360×360, recorte cuadrado amplio —la cara no toca los bordes, que en máscara redonda se nota—, ~52 KB cada uno), servidos con ruta absoluta y `loading="lazy"`. Cada foto tiene al de la casa en su propio terreno: Sebastián en un centro de monitoreo, Matías entre pantallas de código.

**Sebastián Acedo**
- Rol: Co-fundador · Infraestructura & Seguridad
- Empresa: **Byte** (Compu-Byte) — compu-byte.com.ar
- Bio: Más de 25 años al frente de Byte, diseñando e implementando infraestructuras tecnológicas para empresas e instituciones de la región. Especialista en integración de sistemas, operaciones físicas y redes de alta complejidad. Aporta el acceso directo a clientes con infraestructura instalada, la solidez operativa y el conocimiento profundo de los entornos reales.
- Claim de Byte: "Seguridad electrónica e integración de sistemas"

**Matías Gallego**
- Rol: Co-fundador · Software & Estrategia
- **Bio (v5, segunda pasada, 2026-10-10):** Programador desde 2001, hizo carrera en empresas de software y en grandes compañías de Estados Unidos, donde también tuvo su éxito emprendedor: Redeeem. Impulsor de startups del ecosistema joven, mentor de proyectos y emprendedor constante, con VRIO Estudio entre sus emprendimientos. Hoy abre el juego a la creación de software de impacto en Argentina.
- **Cierre de ficha (v5)**, en el lugar del bloque de empresa y con su misma forma: **Programador** · Desde 2001 · Redeeem · Estados Unidos → Argentina. Sin enlace. La flecha es una lectura de los elementos que dio Matías (carrera en Estados Unidos, «abriendo el juego … en Argentina»); si no le gusta, «Estados Unidos · Argentina» es la versión sin interpretación.
- Regla de la bio: construida **solo** con los elementos que dio Matías (programador desde 2001; carrera en empresas de software; impulsor de startups del ecosistema joven; mentor de proyectos; éxito emprendedor en Estados Unidos, Redeeem; carrera en empresas grandes de Estados Unidos; emprendedor constante; abriendo el juego a la creación de software de impacto en Argentina). VRIO aparece como un emprendimiento más de la trayectoria, nunca como empresa ni con su claim.
- *Histórico (v4 y primera v5):* Empresa: **VRIO Estudio** — vrio.ar · Bio: «Al frente de VRIO Estudio, dedicado al desarrollo de software disruptivo y la creación de soluciones tecnológicas de alta complejidad. Nuevos paradigmas, ingeniería creativa y estrategia aplicados a problemas reales. Aporta la arquitectura del motor y de los productos, la visión de producto y la filosofía de innovación que define el alma de RIA Labs.» · Claim: "Software as an art form". Matías lo retiró el 2026-10-10: VRIO «no tiene ningún producto ni cliente para mostrar. Por tanto no podemos llamarla Empresa».

**Título de la sección:** v5 segunda pasada **«Dos oficios consolidados»** (antes «Dos empresas consolidadas»; alternativas y por qué no, en §0).

### 7.2 Narrativa de origen ("Nacidos de Byte y VRIO")

RIA Labs nace de la convergencia de dos trayectorias complementarias:
- **Byte** → 25+ años en seguridad, infraestructura y operaciones reales en campo. Solidez operativa, acceso directo a clientes con infraestructura instalada.
- **VRIO** → Software disruptivo, IA aplicada, nuevos paradigmas, arquitectura de sistemas, filosofía de innovación. "Alma" de RIA Labs.

Frase central (v2, resumen de la ventaja competitiva):
> "La combinación de acceso directo a clientes con infraestructura de CCTV instalada y capacidad de desarrollo propio de soluciones de IA — en el mismo equipo — no existe en el mercado argentino. Esa es la ventaja que no se puede replicar."

### 7.3 Tags asociados (v1)

- Byte → Cámaras y visión · Hardware industrial · Procesos físicos · Confiabilidad operativa.
- VRIO → Desarrollo a medida · Arquitectura de software · IA aplicada · Diseño de producto.

---

## 8. Contacto y ubicación

- **Email vigente:** hola@rialabs.ar
- **Email previo (v1):** hola@rialabs.ai
- **Ubicación:** Rosario, Santa Fe · Argentina. Desde el 2026-11-01 tiene sección propia en la home, `#rosario` («De dónde
  salimos», con la oficina dibujada en corte; §0.8).
- **Copy de cierre:** "¿Listo para empezar? Hablemos. Contanos el problema en una primera conversación y te mostramos qué puede ver tu negocio que hoy no está viendo."

---

## 9. Identidad visual / Sistema de diseño

### 9.1 Paleta de colores (v4)

| Variable | Valor | Uso |
|----------|-------|-----|
| `--bg`   | `#0b0a14` | Fondo principal (negro-violáceo) |
| `--bg2`  | `#100f1e` | Fondo secundario |
| `--bg3`  | `#0d0c1a` | Fondo terciario |
| `--gold` | `#c8860a` | Dorado base |
| `--gold-hi` | `#EF9F27` | Dorado highlight (CTAs, acentos) |
| `--gold-lo` | `#7a5008` | Dorado profundo |
| `--blue` | `#4a8fd4` | Azul Byte (enlaces a compu-byte) |
| `--blue-lo` | `#1e4a78` | Azul profundo |
| `--white` | `#f0ece0` | Texto principal (blanco cálido) |
| `--muted` | `#8a8478` | Texto secundario |
| `--border`  | `rgba(200,134,10,0.14)` | Bordes dorados sutiles |
| `--border2` | `rgba(255,255,255,0.055)` | Bordes neutros |
| `theme-color` | `#07060f` | Barra de navegador móvil |

### 9.2 Tipografías

- **v4 / actual:** Saira (200, 300, 400, 500, 600) + DM Mono (300) — Google Fonts.
- **v5 desde 2026-10-13:** además **M PLUS Rounded 1c 800**, sólo para el titular del hero («Metaestructura») y la
  comilla grande de la cita: la redonda que titula la onda de Dataflow. Del 10 al 13/10 el titular iba en Cormorant
  Garamond (600 + cursiva 500); se quitó, no quedaba en otro lado.
- **v1 / v2:** Bebas Neue + DM Sans + DM Mono (según README).
- Uso: Saira para titulares y UI; DM Mono para numeraciones, labels y detalles tipo "terminal".

### 9.3 Logo / icono principal

- `assets/ria-labs-eclipse-icon.svg` — Eclipse con halos cálidos y disco interior oscuro (el de v4; sigue siendo el favicon-SVG de referencia).
- Dos variantes en el sitio: eclipse estático (versión pequeña de nav) y eclipse animado con disco lunar orbitando (hero en v3/v4).
- **v5 desde 2026-10-12:** el hero es un eclipse cinemático en capas (foto de la corona con alfa + fotósfera + luna negra,
  §0.1), y el isotipo de la nav, inline en `v5/index.html`, es una corona de luz con un streamer ecuatorial y la luna
  negra centrada (24 px). Dataflow y Equipo conservan el eclipse vectorial.
- **El anillo (2026-10-13, rama `hero-pulido`) — el isotipo nuevo.** Sale de una referencia que Matías trajo («la
  screen 2 es una idea que me gusta como logo»): una circunferencia limpia de grosor uniforme, sin relleno, con
  degradé lineal vertical amarillo → naranja → rojo. Medido en la referencia: grosor 6,3 % del diámetro exterior, el
  amarillo se sostiene en el 10 % de arriba y pasa rápido al naranja hacia el 30 %, después baja despacio al rojo.
  Construcción (`logos/ria-anillo-color.svg`, viewBox 100): círculo r 43, trazo 6 (exterior 46, interior 40), gradiente
  `#f8df6a` (0) → `#e4753d` (0,3) → `#d35745` (0,62) → `#c54a45` (1). Variantes `blanco`, `negro`, `outline` (los dos
  bordes en `currentColor`) y lockup horizontal con el wordmark RIA Labs en Saira
  (`ria-anillo-lockup-horizontal-*.svg`, misma caja de 640×180 que el lockup vigente). Convención y usos en
  `logos/README.md`. En la página: isotipo de la nav (24 px, trazo 7,5), pie (18 px, al 80 %), `favicon.svg` (trazo 9)
  y el separador entre Equipo y Contacto (`#equipo-anillo`). El hero sigue siendo el eclipse —la flama ecuánime sobre
  la luna negra— y no el logo; el anillo es la versión gráfica, plana, de esa misma figura. Los isotipos `ria-isotipo-*`
  (el eclipse de halos de v4) siguen en la carpeta como histórico.

### 9.4 Lenguaje visual

- Estética **oscura**, cálida (negro-violáceo + dorado).
- Abundantes **ilustraciones SVG animadas** que narran la propuesta: cámara/infraestructura → líneas de datos → eclipse/portal → constelación/mente.
- Diagramas radiales con nodos sectoriales (Mercado).
- "Terminal" estilizado con filas en vivo (Byte Analítico) — **sólo en v1–v3**; se removió de v4 junto con los bloques de caso. El recurso equivalente en `/laboratorio/` es el ledger de auditoría del circuito de Drivecore.
- Animación orbital con dos planetas (Byte azul + VRIO dorado) rotando sobre un eclipse — separador de Equipo → Contacto.

---

## 10. Assets gráficos presentes

### 10.1 Imágenes

| Ruta | Peso | Rol probable |
|------|------|--------------|
| `assets/image.png` | 761 KB | Referencia/mockup |
| `assets/image2.png` | 454 KB | Referencia/mockup |
| `assets/image3.png` | 355 KB | Referencia/mockup |
| `assets/image4.png` | 1.1 MB | Referencia/mockup |
| `assets/equipo-sebastian.jpg` | 52 KB | Retrato de Sebastián Acedo · 360×360, sección Equipo del home |
| `assets/equipo-matias.jpg` | 50 KB | Retrato de Matías Gallego · 360×360, sección Equipo del home |
| `assets/ria-labs-eclipse-icon.svg` | 645 B | Icono del eclipse (vector) |
| `og-image.png` (raíz) | ~600 KB desde v5 (cielo con ruido) | Open Graph 1200×630 para WhatsApp / Twitter Card |

### 10.2 Favicon system (`ria-favicon/`)

- `favicon.ico` · `favicon.svg` (origen)
- `favicon-16x16.png`, `favicon-32x32.png`, `favicon-48x48.png`, `favicon-64x64.png`
- `favicon-180x180.png` (Apple Touch Icon)
- `preview.png` — preview del set
- `favicon-snippet.html` — snippet HTML listo para pegar en `<head>` de cualquier versión (incluye `theme-color` `#0A0A12`)

Nota: los favicons "vigentes" están duplicados en la raíz (`/favicon.ico`, `/favicon.svg`) para que los referencie v4.

---

## 11. Estructura técnica y deployment

### 11.1 Árbol de carpetas

```
RIA/
├── README.md                    (descripción breve del repo)
├── .gitignore                   (solo excluye .DS_Store)
├── netlify.toml                 (redirect / → /v4/index.html)
├── favicon.ico · favicon.svg    (favicon activo en raíz)
├── og-image.png                 (tarjeta social)
├── assets/                      (imágenes y logo SVG)
├── ria-favicon/                 (set completo de favicons + snippet)
├── v1/index.html                (1.310 líneas · prototipo 1)
├── v2/index.html                (670 líneas · prototipo 2)
├── v3/index.html                (1.009 líneas · prototipo 3)
├── v4/index.html                (versión vigente del home)
└── laboratorio/
    ├── index.html               (página Laboratorio)
    └── media/                   (clips MP4 + posters del prototipo de tránsito
                                  + capturas JPG del sistema de sensores urbanos)
```

### 11.2 Deploy

- **Netlify.** `netlify.toml` define un redirect permanente de `/` a `/v4/index.html` (status 200 — rewrite, no 301), manteniendo las v1–v3 accesibles para comparar.
- Cada versión anterior (v1, v3) incluye un selector flotante en la esquina superior izquierda para saltar entre prototipos (V1/V2/V3).
- **`/laboratorio/`** no necesita regla en `netlify.toml`: el redirect sólo aplica a `/`, así que Netlify sirve `laboratorio/index.html` como índice del directorio.

### 11.3 Stack

- HTML + CSS vanilla (sin bundler, sin framework).
- JavaScript en línea para animaciones, IntersectionObserver (reveals), count-up de stats y tooltip interactivo del diagrama de mercado.
- SVG animado (SMIL + `requestAnimationFrame`) como recurso expresivo central.
- En `/laboratorio/`, además: video MP4 propio con carga diferida por viewport y respeto de `prefers-reduced-motion`.

---

## 12. Navegación y arquitectura de información

### 12.1 Anchors del sitio vigente (v4)

- `#servicios` — "Lo que hacemos"
- `#laboratorio` — "Lo que estamos construyendo" (intro al Laboratorio; ocupa el lugar de los ex `#caso` / `#caso-comms`)
- `#metodologia` — "La forma en que pensamos"
- `#mercado` — "Dónde opera lo que construimos"
- `#equipo` — "Dos empresas consolidadas"
- `#contacto` — "Hablemos."

> **Anclas retiradas el 2026-08-06:** `#caso`, `#caso-comms` y el efímero `#laboratorio-teaser`. Si aparece un link externo viejo a `rialabs.ar/#caso`, cae al tope del home sin romper nada — pero conviene repuntarlo a `/laboratorio/`.

### 12.2 Nav bar (v4)

Logo + enlaces a Servicios · **Laboratorio** (`/laboratorio/`, página propia) · Metodología · Mercado · Equipo · CTA "Conversemos".

El CTA secundario del hero dice **"Ver el laboratorio →"** y baja a `#laboratorio` (no salta de página); el salto a `/laboratorio/` lo hace el botón del final de esa sección.

### 12.3 Footer (v4)

"© 2025 RIA Labs — Byte × VRIO · Rosario, Argentina" + Servicios · Método · **Laboratorio** · Equipo · Contacto.

### 12.4 Páginas del sitio

| Ruta | Contenido | Fuente |
|---|---|---|
| `/` | Home institucional (rewrite a `/v4/index.html`) | `v4/index.html` |
| `/dataflow/` | Dataflow — el motor en pleno funcionamiento, lo que lleva contado, cómo trabaja y la salida a los productos (desde el 01/11; §0.7) | `dataflow/index.html` |
| `/laboratorio/` | Laboratorio — la casa, las dos puertas, de dónde salió cada producto y las expediciones en curso (desde el 01/11; §0.1) | `laboratorio/index.html` |
| `/metodo/` | Método — las seis reglas, una estación con su artefacto animado por regla (2026-11-01, §0.6) | `metodo/index.html` |
| `/v1/`, `/v2/`, `/v3/` | Prototipos históricos | — |

### 12.5 Anchors de `/laboratorio/`

Desde el 2026-11-01: `#casa` · `#puertas` · `#linaje` (las vías llevan los ids viejos: `#p05` Smartcity, `#p02`
Analítico, `#p01` Automotrices) · `#expediciones` (`#p04` Tránsito inteligente) · `#metodo` (la puerta hacia `/metodo/`)
· `#contacto` / `#cierre` («Hablemos.»). `#p03` (RIA Comms) ya no existe. La nav es la de la home con enlaces absolutos y
Laboratorio marcado con `aria-current`.

> Hasta el 01/11: `#p01` RIA Drivecore · `#p02` Analítica de video · `#p03` RIA Comms · `#p04` Tránsito inteligente ·
> `#p05` RIA Smartcity · `#metodo` «Seis reglas que no negociamos» · `#cierre`; con un rail vertical fijo (≥1340 px).

---

## 13. Comparativa rápida de versiones

| Dimensión | v1 | v2 | v3 | v4 (vigente) |
|-----------|----|----|----|--------------|
| Título | "Inteligencia Artificial Enriquecida" | "Software e IA" | "IA aplicada" | "Software e IA" |
| Tipografías | Bebas Neue + DM Sans + DM Mono | DM Sans + DM Mono | Saira + DM Mono | Saira + DM Mono |
| Foco de servicios | Consultoría genérica | OCR / visión artificial | 4 bloques narrativos | IA generativa + desarrollo |
| Sección Metodología | 5 pasos + 6 principios | 5 pasos + 6 principios | Ausente | 6 principios |
| Mercado | Solo en narrativa | 6 rubros (Countries incluido) | Ausente | 6 rubros (Seguridad incluido) |
| Dominio email | `.ai` | `.ar` | `.ar` | `.ar` |
| Stats destacadas | 2–4 sem · 1 interlocutor · 100% propio | 70% · ~100% cámaras · 25+ · 5 sem | — | 70% · 100% procesos · 25+ · 5 sem |
| Longitud (líneas) | 1.310 | 670 | 1.009 | 1.325 |

---

## 14. Elementos institucionales útiles para reuso

- **Elevator pitch (1 línea):** "Transformamos los procesos de tu empresa con inteligencia artificial y software a medida. Nacidos de Byte y VRIO."
- **Tagline poético:** "Metaestructura" (desde el 2026-10-13: el titular del hero, una palabra, con la frase que cierra en «está hecha en RIA Labs» debajo). Históricos: "De ver a saber" (v5, del 10 al 13/10/2026) y "Tu infraestructura ya existe. Nosotros la hacemos pensar."
- **Misión implícita:** Hacer que la IA produzca valor real sobre la infraestructura que las empresas argentinas ya tienen instalada.
- **Visión implícita:** Ocupar el nicho donde infraestructura operativa y software de IA se encuentran — un espacio hoy vacío en el mercado argentino.
- **Valores operativos:** Simplicidad · Velocidad · Resultados medibles · Autonomía del cliente · Ingeniería creativa con rigor.
- **Origen:** Byte (25+ años, Sebastián Acedo) + VRIO (software as an art form, Matías Gallego) = RIA Labs.
- **Primer caso emblemático:** Byte Analítico para Seprio (Fiat Rosario) — 1.100 vehículos, 1 cámara, 100% trazabilidad.

---

*Documento generado a partir de `README.md`, `netlify.toml`, `v1–v4/index.html`, `assets/` y `ria-favicon/` — carpeta RIA.*
