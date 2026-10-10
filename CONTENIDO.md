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

- **Los productos son la espina.** Se fueron las secciones *Servicios* (cuatro líneas de consultoría) y
  *Mercado* (radial de seis rubros): describían una consultora, no la empresa de producto que es hoy. Su
  mensaje útil («partimos de lo que ya tenés») pasó al hero, a la banda de Dataflow y al método.
- **Tres verticales, una palabra cada una, con su definición de diccionario** bajo el nombre (regla fijada
  por Matías con *Automoción*: una sola palabra en español con sentido profundo):

| # | Nombre | Definición mostrada (fuente: RAE) | Qué agrupa | Color | Sitio |
|---|---|---|---|---|---|
| 01 | **RIA Analítico** | *analítico, ca.* Perteneciente o relativo al análisis. Que procede descomponiendo, o que pasa del todo a las partes. | seguridad: los dos brazos **Integradores** y **Monitoreo** | `#4a8fd4` azul | analitico.rialabs.ar |
| 02 | **RIA Espacio** | *espacio.* Extensión que contiene toda la materia existente. Parte de esa extensión que ocupa cada objeto sensible. Capacidad de un lugar. | los **sabores** de smartcity: Ciudad · Predio · Acceso · Barrio y centro comercial | `#2fd0c8` teal | smartcity.rialabs.ar |
| 03 | **RIA Automoción** | *automoción.* Facultad o condición de lo que se mueve por sí mismo. Estudio o descripción de las máquinas que se desplazan por la acción de un motor y particularmente de los automóviles. | la concesionaria (antes **RIA Drivecore**; la página lo dice debajo del nombre) | `#EF9F27` dorado | drivecore.rialabs.ar |

  Los nombres públicos de los sitios de destino todavía dicen *Byte Analítico* y *RIA Drivecore*: la home
  usa los nombres nuevos y enlaza a esos sitios tal como están. Renombrarlos es una pasada aparte.
- **El eclipse manda, solo.** En el hero es la figura de portada: el eclipse total, sin nada alrededor.
  (La primera v5 lo rodeaba de un *sistema* de tres órbitas con un planeta por producto; Matías lo descartó
  el mismo día: «las órbitas no van, el eclipse es total y figura de la portada».) El SVG `#sistema` tiene el
  viewBox recortado al eclipse —`310 70 340 340` sobre el sistema de coordenadas original, el centro sigue
  en 480,240 y el interior `#sis-core` es el de siempre— y el tamaño lo da el CSS: `min(400px, 78vw, 44vh)`
  de ancho, o sea una corona de ~226 px de diámetro en desktop y ~170 en un celular, sin empujar el titular
  bajo el pliegue. Respira, dos anillos de protuberancias giran en sentidos opuestos, la luna libra y deja
  ver un filo de sol, un enjambre de partículas trabaja detrás. Los gradientes `sp-*` siguen en sus `defs`
  porque los usa el diagrama de Dataflow. Vuelve en la banda de Dataflow como el motor, en el separador de
  Equipo (Byte y VRIO, heredado de v4) y en los dos retratos.
- **Cada vertical es un astro con sus sabores en órbita** (viñeta `.prod-vis` de cada banda, SVG propio de
  480×400, vanilla). El astro lleva la tecnología de la vertical en su superficie, en línea técnica sobre
  la esfera, no como ícono: en Analítico es **el ojo de un objetivo** (anillos, iris de ocho láminas,
  reflejo en el vidrio); en Espacio, **la ciudad de noche vista desde arriba** (trama de globo y un barrio
  de luces que se ve justamente del lado de la sombra); en Automoción, **el circuito** que rodea el astro
  (una pista con sus cinco secciones, sólo se ve la mitad de adelante). Un sol fuera de cuadro, arriba a la
  izquierda, ilumina los tres igual: terminador, filo de luz en el borde, y una umbra que el astro proyecta
  hacia abajo a la derecha. **Cada satélite es un sabor y un enlace** (`<a>` dentro del SVG, con `tabindex`,
  `aria-label`, halo al hover y al foco, y su órbita se enciende) a la web de ese sabor:

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
  móvil no se corte). Detrás, 48 motas de polvo propias de cada viñeta con paralaje al scroll. Cada órbita
  dibujada está ocupada por el satélite que la recorre; se fueron el arco de corona de la esquina y la
  elipse punteada vacía que tenía la primera v5. **Sumar un sabor es sumar un `<a class="sat">`** con su
  `data-orb` (`rx ry inclinación período fase sentido radio`): Estación de Servicio e Industria entrarán
  así en Espacio. `prefers-reduced-motion`: todo quieto en su posición inicial, sin transiciones.
- **El sentido del eclipse, dicho en la página** (banda Dataflow): *«Un eclipse es dos cosas que ya
  existían, alineadas por un instante. La luna es tu infraestructura. El sol es el motor. Lo que se ve es
  la corona: lo que la alineación deja pasar.»*
- **El cielo.** Un `<canvas id="cielo">` fijo detrás de todo emula el espacio: ~360 estrellas a 1440×900
  (densidad por área), con profundidad —las cercanas son más grandes, más brillantes, se corren más con
  el scroll (paralaje) y con el mouse—, titilan con fase propia, derivan lentísimo, y cada 9–20 s cruza un
  meteoro. Colores: blanco cálido, algunas doradas, azules y teal. Las bandas de sección son translúcidas
  para que se vea a través. `prefers-reduced-motion`: cielo estático, sin meteoros, sin órbitas animadas.
- **Dataflow como historia** (desde la rama `dataflow-historia`, 2026-10-10; reemplaza al diagrama estático
  *entradas → eclipse → tres sabores* con los tres pasos *Lee · Comprende · Actúa* y la nota de las 24 analíticas).
  La banda `#dataflow` se **recorre**: un escenario fijo con el flujo en canvas y cuatro cuadros que pasan con el
  scroll. Qué muestra cada cuadro, de dónde sale cada número y cómo se fotografía: **§0.5**. Enlace a
  dataflow.rialabs.ar («Universo Dataflow») al final del último cuadro. Regla de marca intacta: un solo nombre
  público, *Dataflow*; *Datamotor* aparece una sola vez, en chico, adentro del disco.
- **Barra de números medidos** (v4 traía cifras de mercado: 70 % de empresas sin IA, etc.):
  1 motor · 24 analíticas · 30 mil eventos por día en una instalación (Rosental, `dataflow-rosental/docs/ESTADO.md`) ·
  1.100 vehículos activos (Seprio). Criterio del laboratorio: si no está medido, no se dice.
- **Laboratorio** agrupa lo que todavía es pregunta, seis fichas (relevamiento de la carpeta `Proyectos/`
  del 2026-10-10):

| Ficha | Estado publicado | Origen | Enlace |
|---|---|---|---|
| **RIA Diálogo** (antes RIA Comms) | En uso · operación comercial de una concesionaria | `ria-comms` (Seprio sigue con el predecesor `seprio-comms`) | `/laboratorio/#p03` |
| Tránsito inteligente | Prototipo · medido en calle (−27 %) | `byt-traffic-demo` | `/laboratorio/#p04` |
| Deportes | Experimento · la cancha ya está resuelta (homografía, F1) | `dataflow-deportes` | — |
| Maqueta navegable | Prototipo · actividad simulada | `dataflow-smartcity-sapiens` / `-neander` | — |
| Fauna urbana | Absorbido · hoy es una vertical de RIA Espacio | `byt-pajaritos` (birdmap, demo a la Municipalidad 25/08) | — (birdmap.rialabs.ar es no comercial y no se linkea) |
| Estación IA | Activación · para eventos | `IA Fun Station` | — |

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
  del nombre; en móvil arriba. Bios iguales salvo la de Matías («arquitectura del motor y de los productos»).
- **Nav**: Analítico · Espacio · Automoción (con el punto de color de cada uno) · Dataflow · Laboratorio ·
  Equipo · *Conversemos*. En ≤860 px hay botón MENÚ con panel desplegable (v4 escondía los enlaces).
- **Contacto**: el pre-título ahora es la pregunta del laboratorio («¿Tenés un problema que nadie resolvió?»)
  y vuelve el copete de cierre. Footer © 2026.
- **Desenclipsar: el eclipse se toca** (rama `desenclipsar`, 2026-10-10; pedido verbatim en el registro de
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
- **Tema día.** `data-tema="dia"` en `<html>` conmuta las variables de `:root`: papel cálido `#f4efe4`,
  tinta `#1a1712`, el dorado sigue siendo el acento pero más oscuro (`#a66a06` / `#c47d0a`) para leerse
  sobre claro; azul, teal y dorado de producto oscurecidos; bandas, tarjetas y nav translúcidas en su
  equivalente claro (`--banda`, `--banda2`, `--tarjeta`, `--nav-bg`…); el eclipse en colores de tema
  (`--luna`, `--sol-tapado`, halos `--h1…--h6`: resplandor oscuro contra el negro, tintes dorados contra
  el papel). El cambio es gradual y universal (`--t-tema`, que el ciclo ajusta a cada fase: 2,5 s al
  aclarar, 3 s al oscurecer con la totalidad); el cielo de estrellas se apaga en día. Decisiones: la elipse
  del viaje tiene su punto bajo en la luna del hero y sube hacia ambos bordes (ry = 16 % de rx); la
  geometría se lee del DOM en cada fotograma, nada de pantalla está hardcodeado; si el sol no está en
  pantalla (página scrolleada), la elipse se centra en el viewport y la viajera entra y sale con un
  fundido; desde el logo la luna sigue al sol aunque la página todavía esté scrolleando hacia él. Ganchos:
  `?tema=dia` carga en día con el sol encendido y la luna fuera (sin animar); `?ciclo=<ms>` congela el
  ciclo en ese instante. Dataflow y laboratorio se rehacen en ramas paralelas: toman el día de las
  variables de `:root`; sus colores fijos de `main` no se tocaron.

### 0.2 Secuencia de la página (anclas)

`#inicio` hero → barra de números → `#productos` (`#analitico` · `#espacio` · `#automocion`) → `#dataflow` →
`#laboratorio` → `#metodologia` → `#equipo` → `#contacto` (separador orbital) → contacto → footer.

### 0.3 Assets nuevos

| Ruta | Qué es |
|---|---|
| `v5/index.html` | la home vigente, autocontenida |
| `assets/retrato-sebastian.jpg` · `assets/retrato-matias.jpg` | retratos 720×900 (4:5), ~70 KB y ~60 KB |
| `og-image.png` | tarjeta 1200×630: el eclipse solo + RIA Labs + la frase (regenerada el 10/10 al sacar las órbitas, con `OG=1 scripts/capturar-home.sh v5`). La anterior quedó en `og-image-v4.png` |
| `scripts/generar-retratos.py` | cómo se hicieron los retratos (abajo) |
| `scripts/capturar-home.sh` | fotografía la home completa con Chrome headless (desktop 1440 y móvil 390 por iframe; `OG=1` también la tarjeta, con el eclipse a 320 px; `QUERY=tema=dia` o `QUERY=ciclo=4200` fotografía el día o un instante del ciclo del eclipse, `NOMBRE=dia` nombra los PNG; `ALTO=9600` para la página entera). Levanta su propio `http.server` en 8895–8899 y lo mata por PID |

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

### 0.4 Pendientes que deja la v5

- Renombrar *RIA Comms* → *RIA Diálogo* en `/laboratorio/` (y decidir si va *Diálogo* o *Comunicación*).
- Los sitios de producto siguen diciendo *Byte Analítico* y *RIA Drivecore*; la home ya dice *RIA
  Analítico* y *RIA Automoción*.
- `/laboratorio/` presenta cinco proyectos de los cuales tres ya son producto; reordenarlo con el criterio
  de la home (productos arriba, laboratorio = lo que todavía es pregunta) es la próxima pasada.
- El satélite **Acceso** de RIA Espacio no enlaza a nada: Rosental y Mercado Fisherton son instalaciones con
  login. Cuando Acceso tenga página pública, es agregarle el `href`.
- Las viñetas de las verticales son SVG dibujado, no imágenes generadas: se decidió así para que sobrevivan a
  un tema claro (colores por variables), pesen cero y puedan moverse. Si alguna vez se quiere un render
  fotorrealista, el camino es el de los retratos (`scripts/generar-retratos.py`).

### 0.5 La banda Dataflow como historia (2026-10-10)

> Prompt de Matías, verbatim: «La idea de contar el dataflow tiene que ser mas visual, mas en modo historia, alli
> en ese espacio donde el usuario llega luego de los productos. Hay que mostrar mas flow. Y el motor presente con
> toda su maquina. Numeros y estadisticas de lo que hasta ahora procesamos tanto en laboratorio como en produccion.»

**Cómo funciona.** `<section class="df" id="dataflow" data-df="1..4">`: grilla de dos columnas. A la izquierda el
**escenario** (`.df-stage`, sticky bajo la nav) con un `<canvas>` y rótulos DOM; a la derecha cuatro
`article.df-cuadro` de ~86 vh cada uno. Un IntersectionObserver con franja central (`rootMargin: -45% 0 -45% 0`)
fija `data-df` al cuadro que cruza el centro de la pantalla; el canvas (énfasis entradas / motor / salidas) y el CSS
(opacidad de rótulos y cuadros) leen ese estado. En ≤860 px el escenario queda sticky arriba (44 vh, fondo opaco) y
los cuadros pasan por debajo. `prefers-reduced-motion`: un solo cuadro estático, sin sticky ni partículas en
movimiento. El loop corre sólo con la banda a la vista y se pausa con la pestaña oculta. Altura total de la banda:
~3.700 px en escritorio, ~3.300 px en un teléfono.

**El flujo (canvas).** Partículas que nacen en *cámaras · sensores · sistemas*, entran al eclipse, atraviesan
**seis compuertas** —Ingesta → Analíticas → Eventos → Almacén → Episodios → Intents, las etapas reales del motor
según `ria-datamotor/README.md` y `docs/BASE.md`— y salen hacia los tres planetas con el color de cada producto.
Cada compuerta se enciende al paso de una partícula (y la lista del cuadro 2 marca la más encendida); en
*Analíticas* saltan chispas y en *Eventos* nace un anillo del color del sabor. El eclipse se dibuja con la misma
gramática del resto de la página (aura, halo, protuberancias que giran, corona que respira, luna que libra), y
adentro se ve el plano técnico: carriles y las seis bandas numeradas. En columna alta (escritorio) el flujo baja;
en apaisado va de izquierda a derecha; toda la geometría se deriva del tamaño del escenario. Los colores se leen
de variables CSS (`--df-raw`, `--df-moon: var(--bg)`, `--df-ink`, `--df-card` y las de `:root`) y se releen si
cambia `data-tema`, para que el tema día no lo rompa.

**Los cuatro cuadros** (texto completo en `v5/index.html`):

1. *01 · Entra la realidad* — «Lo que ya tenés, tal como está.» 3 formas de entrar · 15 cuadros por segundo ·
   8 cámaras hoy · 0 cambios en la instalación.
2. *02 · El motor, por dentro* — «Seis etapas. Veinticuatro analíticas.» La lista de etapas con una línea cada
   una y el **catálogo vivo**: 24 fichas que se encienden de a una. Cierra: «Un catálogo, no un proyecto por
   cliente. Afuera, un solo nombre: Dataflow.»
3. *03 · Salen los sabores* — «El mismo motor, tres formas.» Una línea por producto (qué recibe cada uno) ·
   4 sabores corriendo a la vez · 1 manifiesto por sabor.
4. *04 · Lo que ya pasó por acá* — «Medido, no estimado.» Producción (el equipo de Rosario, 11 sep → 10 oct
   2026) y Laboratorio (el semáforo de la ochava), con contadores `data-df-count` (formato `es-AR`, prefijo y
   sufijo opcionales; arrancan cuando los números entran en pantalla).

**Números publicados → fuente.** Los del equipo salen del tablero de administración del motor
(`datamotor.rialabs.ar`, credencial en `~/.credentials/datamotor-tablero.txt`), consultado en **solo lectura** (GET
con sesión a `/api/estado`, `/api/catalogo`, `/api/historico?bucket=dia&desde=2026-07-01`) el **2026-10-10 02:59
-03**; el box corría el motor con contrato 1.104.0, 74 kinds, 4 sabores.

| Número en la página | Valor | Fuente |
|---|---|---|
| 3 formas de entrar (RTSP de la cámara, RTMP del sitio, nube del fabricante) | 3 | `dataflow-jockey-acceso/docs/ESTADO.md` («Cámaras»: RTMP del sitio → `rtsp://127.0.0.1:8554`, DoLynk), `dataflow-integradores/docs/ESTADO.md` (líneas 10 y 46: RTSP, RTMP `sitio`, DoLynk), `ria-datamotor/docs/ESTADO.md` (DoLynk Tier 1) |
| 15 cuadros por segundo por cámara | 15 | `ria-smartcity/docs/ESTADO.md:81` (LPR-15: techo 15 fps para todas las cámaras, 08/10), `dataflow-jockey-acceso/docs/ESTADO.md` (H.264 1080p 15 fps); tablero: `fps_objetivo: 15` en las 8 |
| 8 cámaras conectadas hoy | 8 | tablero `/api/estado` → `motor.camaras` (8 en catálogo: 3 en línea y 5 caídas en ese momento) |
| 0 cambios en la instalación | 0 | principio del método («por configuración, no por obra»), no una medición |
| 24 analíticas | 24 | `PROMPT-FUNDACIONAL-AUDITORIA-DATAMOTOR-2026-10-03.md:25`; `ria-datamotor/ria_datamotor/esquemas.py:1456` (comentario «sirve costo para las 24») — ver nota abajo |
| veredicto normal · atención · alerta | — | tablero `eventos.por_verdict` (777.630 / 179 / 6.982) |
| 4 sabores a la vez en el mismo equipo | 4 | tablero `motor.sabores`: `analitico`, `byte`, `jockey-acceso`, `rosental`, todos conectados |
| 784.790 eventos en el último mes | 784.790 | tablero `/api/historico` → `eventos.total_historico`; primer evento 2026-09-11 19:59, último 2026-10-10 05:59 |
| 130.520 en el día de más trabajo (2 de octubre) | 130.520 | ídem, `eventos.serie` con `bucket=dia`, 2026-10-02 |
| 20.750 patentes leídas | 20.750 | ídem, `por_analitica` → `lpr` |
| 330.163 autos · 172.162 personas · 57.498 motos · 74.018 camiones · 23.377 bicicletas | — | ídem, `por_tipo` |
| 49 W de placa de video en promedio | 48,67 | tablero `acumulados.potencia_w` (529 h muestreadas desde el 2026-09-18; 25,7 kWh de GPU) |
| 1.100 vehículos activos en la concesionaria | 1.100 | `drivecore-web/index.html:1008` («vehículos activos trazados en vivo»); cifra heredada de v4, no re-medida |
| 30 mil lecturas por día en una sola puerta | ~30 k/día | `dataflow-rosental/docs/ESTADO.md` **en el commit `13377c9`** (2026-09-16), línea 35: «`rosental_eventos` crece ~30 k/día (Betty)». La cita de §0.1 apunta a ese archivo; hoy la línea vive en el historial |
| −27 % de demora contra el tiempo fijo | −27 a −28 % | `byt-traffic-demo/README.md:94` (≈234 vs ≈322 veh·s, clip de desarrollo) |
| 15 cuadros por segundo en el navegador sin perder ninguno | 15 | `byt-traffic-demo/README.md:171` |
| 300 vehículos por hora en la ochava | 300 | `byt-traffic-demo/README.md:169` |

Por sabor, del mismo tablero (no está en la página, queda como referencia): `byte` (la ochava de Smartcity)
632.004 · `analitico` (Integradores) 131.822 · `jockey-acceso` 20.254 · `rosental` 711.

**Nota sobre las 24.** `ESQUEMAS_DECLARADOS` de `esquemas.py` (origin/main del 2026-10-10) tiene **25 claves**. Se
publican 24 porque `compuerta_movimiento` es un filtro previo (decide si un cuadro se analiza o no), no una
analítica; el número coincide con el prompt de auditoría del 03/10 y con el comentario del propio archivo. Si la
casa prefiere decir 25, hay que cambiarlo también en la barra de números del hero.

**Fotografiar.** `?df=N` (1–4) fija el estado N, deja sólo ese cuadro y saca el sticky; `&solo` esconde todo lo
que no sea la banda. Anclas `#df-c1`…`#df-c4` para caer en un cuadro con el escenario pegado. En una ventana de más
de 1.800 px de alto (captura de página entera) los cuatro cuadros quedan encendidos (`df-plano`). La página creció
unos 3.000 px: `scripts/capturar-home.sh` llega al pie con `ALTO=11000`.

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
> (Texto incrustado en la ilustración animada del hero en v4; versión v2 usaba "Tu infraestructura visual ya existe. Nosotros la hacemos pensar.")

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

### 7.1 Co-fundadores

> **Retratos (2026-08-14):** las fichas de los dos co-fundadores llevan **foto redonda de 112 px a la izquierda del nombre y el rol**, alineada a su altura (`.f-head`, flex con `align-items:center`), en el lugar que antes ocupaba el círculo con las iniciales. Las iniciales siguen en el DOM **debajo** de la imagen (`.f-init` dentro de `.f-photo`): si la foto no carga, el círculo sigue diciendo quién es. Archivos en `assets/equipo-<nombre>.jpg` (360×360, recorte cuadrado amplio —la cara no toca los bordes, que en máscara redonda se nota—, ~52 KB cada uno), servidos con ruta absoluta y `loading="lazy"`. Cada foto tiene al de la casa en su propio terreno: Sebastián en un centro de monitoreo, Matías entre pantallas de código.

**Sebastián Acedo**
- Rol: Co-fundador · Infraestructura & Seguridad
- Empresa: **Byte** (Compu-Byte) — compu-byte.com.ar
- Bio: Más de 25 años al frente de Byte, diseñando e implementando infraestructuras tecnológicas para empresas e instituciones de la región. Especialista en integración de sistemas, operaciones físicas y redes de alta complejidad. Aporta el acceso directo a clientes con infraestructura instalada, la solidez operativa y el conocimiento profundo de los entornos reales.
- Claim de Byte: "Seguridad electrónica e integración de sistemas"

**Matías Gallego**
- Rol: Co-fundador · Software & Estrategia
- Empresa: **VRIO Estudio** — vrio.ar
- Bio: Al frente de VRIO Estudio, dedicado al desarrollo de software disruptivo y la creación de soluciones tecnológicas de alta complejidad. Nuevos paradigmas, ingeniería creativa y estrategia disruptiva aplicados a problemas reales. Aporta la capacidad técnica de desarrollo, la arquitectura de sistemas de IA, la visión de producto y la filosofía de innovación que define el alma de RIA Labs.
- Claim de VRIO: "Software as an art form"

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
- **Ubicación:** Rosario, Santa Fe · Argentina
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
- **v1 / v2:** Bebas Neue + DM Sans + DM Mono (según README).
- Uso: Saira para titulares y UI; DM Mono para numeraciones, labels y detalles tipo "terminal".

### 9.3 Logo / icono principal

- `assets/ria-labs-eclipse-icon.svg` — Eclipse con halos cálidos y disco interior oscuro.
- Dos variantes en el sitio: eclipse estático (versión pequeña de nav) y eclipse animado con disco lunar orbitando (hero en v3/v4).

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
| `og-image.png` (raíz) | 137 KB | Open Graph 1200×630 para WhatsApp / Twitter Card |

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
| `/laboratorio/` | Laboratorio — modalidad de trabajo + cinco proyectos | `laboratorio/index.html` |
| `/v1/`, `/v2/`, `/v3/` | Prototipos históricos | — |

### 12.5 Anchors de `/laboratorio/`

- `#p01` — RIA Drivecore · `#p02` — Analítica de video · `#p03` — RIA Comms · `#p04` — Tránsito inteligente · `#p05` — RIA Smartcity
- `#metodo` — "Seis reglas que no negociamos"
- `#cierre` — "¿Tenés un problema que nadie resolvió?"

Su nav apunta al home con rutas absolutas (`/#servicios`, `/#caso`, …) y marca "Laboratorio" como activo. Un rail vertical fijo (visible ≥1340 px) indica en qué proyecto está el scroll.

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
- **Tagline poético:** "Tu infraestructura ya existe. Nosotros la hacemos pensar."
- **Misión implícita:** Hacer que la IA produzca valor real sobre la infraestructura que las empresas argentinas ya tienen instalada.
- **Visión implícita:** Ocupar el nicho donde infraestructura operativa y software de IA se encuentran — un espacio hoy vacío en el mercado argentino.
- **Valores operativos:** Simplicidad · Velocidad · Resultados medibles · Autonomía del cliente · Ingeniería creativa con rigor.
- **Origen:** Byte (25+ años, Sebastián Acedo) + VRIO (software as an art form, Matías Gallego) = RIA Labs.
- **Primer caso emblemático:** Byte Analítico para Seprio (Fiat Rosario) — 1.100 vehículos, 1 cámara, 100% trazabilidad.

---

*Documento generado a partir de `README.md`, `netlify.toml`, `v1–v4/index.html`, `assets/` y `ria-favicon/` — carpeta RIA.*
