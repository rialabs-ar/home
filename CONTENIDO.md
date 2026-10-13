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
| 02 | **RIA Espacios** (antes RIA Espacio, hasta el 13/10) | *espacio.* Extensión que contiene toda la materia existente. Parte de esa extensión que ocupa cada objeto sensible. Capacidad de un lugar. | los **sabores** de smartcity: Ciudad · Predio · Acceso · Barrio y centro comercial | `#2fd0c8` teal | smartcity.rialabs.ar |
| 03 | **RIA Automoción** | *automoción.* Facultad o condición de lo que se mueve por sí mismo. Estudio o descripción de las máquinas que se desplazan por la acción de un motor y particularmente de los automóviles. | la concesionaria (antes **RIA Drivecore**; la página lo dice debajo del nombre) | `#EF9F27` dorado | drivecore.rialabs.ar |

  Los nombres públicos de los sitios de destino todavía dicen *Byte Analítico* y *RIA Drivecore*: la home
  usa los nombres nuevos y enlaza a esos sitios tal como están. Renombrarlos es una pasada aparte.
- **El hero dice «Superestructura» y abajo va una frase, no una explicación** (rama `hero-texto`, 2026-10-13;
  pedido verbatim de Matías en `docs/prompts-usuario/2026-10-13-superestructura.md`: *«el texto "de ver a saber"
  y toda la explicacion de abajo me resulta muy ñoño. Prefiero expresar una idea con un titulo y una frase. El
  titulo es " super estructura" con una fuente destacable pero amable, mas cercana a la idea de la onda
  dataflow»*). El titular es **una sola palabra, «Superestructura»**, como la usa la frase, en sentence case (en
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
  > Le llamamos Superestructura. Suena bien, ¿verdad? Superestructura. Suena fuerte. No es una de esas ideas débiles
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
  mecanismo ya está: **`assets/superestructura.mp3`** (y, opcional además, `assets/superestructura.ogg`) —ese
  nombre exacto, en esa carpeta, y se activa solo—. Al cargar, un `HEAD` al mp3 decide: si no existe, no se ve
  nada. Si existe, **al posar el mouse sobre la cita suena y al salir se pausa y rebobina**; como sin un clic
  previo en la página los navegadores rechazan `play()` (política de autoplay), el error se traga en silencio y
  queda un **botón chico en mono, «escuchar ▶»**, a la derecha del bloque, que alterna reproducir/pausar y sirve en
  touch; después de cualquier clic en la página el hover ya suena. Lo que arranca el botón no lo corta el mouse al
  salir (termina solo); mientras suena, la comilla grande se enciende. `preload="none"`: no descarga nada hasta
  que se pide. `prefers-reduced-motion` no cambia nada. Script: sección «LA FRASE HABLADA», al final del
  `<script>` principal.

  Los metadatos se alinearon con el titular: `<title>`, `og:title` y `twitter:title` dicen **«RIA Labs —
  Superestructura»** y el «Un motor, tres productos, un laboratorio» de antes pasó a las descripciones (la `meta
  description` arranca con «Superestructura: un motor, tres productos, un laboratorio…»). `og-image.png` queda por
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
  ancho, o sea un disco de ~218 px de diámetro en desktop y ~166 en un celular, con la corona desbordando
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
  nombra; *Datamotor* ya no aparece en la página.
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
    banda); el trazado se rearma al cruzar el breakpoint sin perder el estado de la reacción. `prefers-reduced-motion`:
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
- **Laboratorio es la casa** (rama `laboratorio-casa`, 2026-10-10; pedido verbatim en el registro de prompts:
  «un laboratorio como un centro de experimentación y creación, más búsqueda y aventura, más imaginación y
  trabajo… más en nuestra cosa, nuestra casa»). Antes era una grilla de seis fichas iguales con rótulo de
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
  **«nuestra ochava»** y las dos puertas de la casa son «la ochava» y «el taller». Quedan menciones en `/laboratorio/`
  (otra pasada). Y el producto **RIA Espacio pasó a llamarse RIA Espacios** («explica mejor la naturaleza de la
  versión reproducible en sabores»): nav, menú, banda, satélites, Laboratorio y metadatos; la entrada de diccionario
  sigue siendo *espacio.* en singular y el ancla `#espacio` no cambió para no romper enlaces.

### 0.2 Secuencia de la página (anclas)

`#inicio` hero → `#maquina` (la máquina, con el pie «Tu infraestructura ya existe. / Nosotros la hacemos pensar.») →
`#productos` (`#analitico` · `#espacio` · `#automocion`) → `#dataflow` →
`#laboratorio` → `#metodologia` → `#equipo` → `#contacto` (separador orbital) → contacto → footer.

### 0.3 Assets nuevos

| Ruta | Qué es |
|---|---|
| `v5/index.html` | la home vigente, autocontenida |
| `assets/retrato-sebastian.jpg` · `assets/retrato-matias.jpg` | retratos vigentes 720×900 (4:5): la familia **con melena** (~120 KB y ~103 KB desde el 11/10, con el eclipse unificado). Son el **póster** de los retratos vivos y la foto que queda con `prefers-reduced-motion` |
| `assets/retrato-sebastian.mp4` / `.webm` · `assets/retrato-matias.mp4` / `.webm` | **retratos vivos** (2026-10-11): clips 720×900, 24 fps, en loop (9,67 s y 10,25 s), H.264 `yuv420p` sin audio + VP9. Sebastián 1,09 MB / 0,90 MB · Matías 0,83 MB / 0,65 MB |
| `assets/retrato-sebastian-sobrio.jpg` · `assets/retrato-matias-sobrio.jpg` | la familia **sobria**: los mismos retratos sin la melena (~82 KB y ~79 KB, con el mismo eclipse unificado). Para cambiar de familia alcanza con renombrar; la sobria no tiene clip |
| `scripts/generar-retratos-vivos.py` | cómo se hicieron el eclipse unificado y los retratos vivos (abajo): `fondo`, `video`, `post`, y `costura` para medir el loop |
| `assets/eclipse-corona.webp` · `.jpg` | **la corona fotográfica** (2026-10-12): WebP 1000×1000 con alfa desde la luminancia, 150 KB, el disco negro centrado a r = 0,1515 del lado. El jpg (37 KB) es la misma toma sobre negro. **Desde el 13/10 la página no carga ninguno de los dos** (la corona es la flama procedural); quedan en el repo por si el ciclo o la foto vuelven |
| `assets/eclipse-sol.webp` | la fotósfera en luz blanca, 720×720, alfa = disco (r = 0,4873 del lado), 20 KB. Desde el 13/10 va en `data-href`: se descarga sólo cuando el ciclo o `?tema=dia` la piden |
| `assets/eclipse-luna.webp` | la luna llena teñida al dorado, 720×720, alfa = disco, 22 KB: la cara iluminada de la luna viajera. Desde el 13/10, `data-href` como la del sol |
| `logos/ria-anillo-{color,blanco,negro,outline}.svg` · `logos/ria-anillo-lockup-horizontal-{color,blanco,negro,outline}.svg` | **el isotipo anillo** (2026-10-13, la screen 2 de Matías) y su lockup horizontal con el wordmark en Saira; §9.3 y `logos/README.md`. PNG de los cuatro isotipos a 256/512/1024/2048 en `logos/png/` (`bash logos/build-pngs.sh ria-anillo-color.svg …`, ahora con fallback a Chrome headless si no hay cairosvg). Los lockups no tienen PNG: sin Saira instalada saldrían con otra fuente |
| `favicon.svg` | el anillo (grosor 9 de 92, un poco más grueso que el de marca, para que a 16 px siga siendo un aro). Hasta el 13/10, el eclipse de halos de v4. `favicon.ico` y `ria-favicon/` siguen siendo los viejos |
| `scripts/generar-eclipse.py` | cómo se generaron y procesaron las tres (abajo): `corona`, `sol`, `luna`, `medir`, `post-*`, `hoja` |
| `og-image.png` | tarjeta 1200×630: el eclipse con la flama ecuánime + RIA Labs + «Superestructura» en M PLUS Rounded (regenerada el 13/10 con `OG=1 scripts/capturar-home.sh v5`; el modo OG esconde la cita y el control de audio) |
| `scripts/generar-retratos.py` | cómo se hicieron los retratos (abajo) |
| `scripts/capturar-home.sh` | fotografía la home completa con Chrome headless (desktop 1440 y móvil 390 por iframe; `OG=1` también la tarjeta, con el eclipse a 320 px; `QUERY=tema=dia`, `QUERY=ciclo=4200`, `QUERY=t=43200000` o `QUERY=estrella=1000` / `estrella=no` fotografía el día, un instante del ciclo del eclipse, la página con el reloj adelantado (astros y banda Dataflow) o la estrella de luz del hero fija en su pico / apagada (sin QUERY sale apagándose: la primera asoma a los 4,5 s y Chrome fotografía a los ~6); la QUERY aplica también a la tarjeta OG; `NOMBRE=dia` nombra los PNG; `ALTO=16000` para la página entera, que mide ~11.300 px en desktop desde el 13/10). Levanta su propio `http.server` en 8895–8899 y lo mata por PID |

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

### 0.4 Pendientes que deja la v5

- Renombrar *RIA Comms* → *RIA Diálogo* en `/laboratorio/` (y decidir si va *Diálogo* o *Comunicación*).
- Los sitios de producto siguen diciendo *Byte Analítico* y *RIA Drivecore*; la home ya dice *RIA
  Analítico* y *RIA Automoción*.
- `/laboratorio/` presenta cinco proyectos de los cuales tres ya son producto; reordenarlo con el criterio
  de la home (productos arriba, laboratorio = lo que todavía es pregunta) es la próxima pasada.
- `/laboratorio/` tiene una referencia vieja: el proyecto 05 dice «El proyecto 03 contestó su pregunta»
  hablando de Tránsito, que desde el reordenamiento del 14/08 es el 04.
- Las maquetas Sapiens y Neander están en vivo (`sapiens.dataflow.rialabs.ar`, `neander.dataflow.rialabs.ar`)
  como prototipos sin control de acceso y con la actividad marcada como simulada; la home no las enlaza
  desde la expedición 04. Decidir si se enlazan.
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
  puertas en Rosario: Byte… y VRIO»). Es otra pasada.
- Si el desenclipsar vuelve (`DESENCLIPSAR_ACTIVO = true`), el isotipo de la nav —hoy el anillo— ya no tiene luna que
  acompañe el viaje; decidir si el anillo acompaña de otra forma o no acompaña.
- Los contadores de la banda Dataflow proyectan la lectura del tablero del 10/10/2026 (§0.5): cada tanto conviene
  cargar una lectura nueva (constantes al principio del script «DATAFLOW · la onda» y la fecha en `.df-nota`), porque
  con los meses la proyección se aleja de lo medido. Y la curva horaria es plausible, no medida: cuando el tablero
  exponga la serie por hora, va la real.
- **`assets/superestructura.mp3` todavía no existe** (y `.ogg`, opcional): el audio de la frase del hero lo genera
  Matías. Con el archivo en esa ruta exacta el hover y el botón «escuchar» se activan solos (§0.1); hasta entonces
  no se ve nada. Y `og-image.png` sigue mostrando «DE VER A SABER»: regenerarla con `OG=1 scripts/capturar-home.sh v5`.
- Las viñetas de las verticales son SVG dibujado, no imágenes generadas: se decidió así para que sobrevivan a
  un tema claro (colores por variables), pesen cero y puedan moverse. Si alguna vez se quiere un render
  fotorrealista, el camino es el de los retratos (`scripts/generar-retratos.py`).

### 0.5 La banda Dataflow como onda (2026-10-12)

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

> **Superestructura**
>
> (Titular del hero de v5 desde el 2026-10-13: una sola palabra, sentence case, en M PLUS Rounded 1c 800, la redonda
> de la onda de Dataflow. Debajo va la frase de Matías como cita —texto completo en §0.1—, que cierra en «está
> hecha en RIA Labs».)

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
- **v5 desde 2026-10-13:** además **M PLUS Rounded 1c 800**, sólo para el titular del hero («Superestructura») y la
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
- **Tagline poético:** "Superestructura" (desde el 2026-10-13: el titular del hero, una palabra, con la frase que cierra en «está hecha en RIA Labs» debajo). Históricos: "De ver a saber" (v5, del 10 al 13/10/2026) y "Tu infraestructura ya existe. Nosotros la hacemos pensar."
- **Misión implícita:** Hacer que la IA produzca valor real sobre la infraestructura que las empresas argentinas ya tienen instalada.
- **Visión implícita:** Ocupar el nicho donde infraestructura operativa y software de IA se encuentran — un espacio hoy vacío en el mercado argentino.
- **Valores operativos:** Simplicidad · Velocidad · Resultados medibles · Autonomía del cliente · Ingeniería creativa con rigor.
- **Origen:** Byte (25+ años, Sebastián Acedo) + VRIO (software as an art form, Matías Gallego) = RIA Labs.
- **Primer caso emblemático:** Byte Analítico para Seprio (Fiat Rosario) — 1.100 vehículos, 1 cámara, 100% trazabilidad.

---

*Documento generado a partir de `README.md`, `netlify.toml`, `v1–v4/index.html`, `assets/` y `ria-favicon/` — carpeta RIA.*
