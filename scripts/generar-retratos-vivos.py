#!/usr/bin/env python3
"""Retratos vivos (2026-10-11): los dos cofundadores quietos, esperando la foto, con la melena al viento
de un ventilador. Tres etapas, todas reproducibles desde acá (ver CONTENIDO.md §0.3):

  1. fondo      unifica el eclipse de los dos retratos fijos con google/nano-banana como editor: misma idea
                en los dos (chico, alto, centrado sobre la cabeza, lejos y apagado), sin tocar cara, pelo,
                ropa, pose ni luz. Parte de la familia con melena (`assets/retrato-*.jpg`); con `-sobrio`
                aplica lo mismo a la familia sobria.
  2. video      clip de 5 s por persona con el MISMO retrato como primer y último cuadro (el truco del loop):
                kwaivgi/kling-v2.5-turbo-pro (start_image = end_image) o bytedance/seedance-1-pro
                (image = last_frame_image, camera_fixed). Guarda el mp4 y un .json con métricas y costo.
  3. post       ffmpeg: costura del loop con fundido cruzado corto de la cola sobre la cabeza (nunca ping-pong),
                720×900, mp4 H.264 yuv420p sin audio + webm VP9, ≤ 2 MB cada uno.

Uso:
  generar-retratos-vivos.py fondo <sebastian|matias|sebastian-sobrio|matias-sobrio> [n=3]
  generar-retratos-vivos.py fondo-ref <persona> <referencia.jpg> [n]   # igualar el eclipse al de otra imagen
  generar-retratos-vivos.py video <kling|seedance> <sebastian|matias> [n=1] [imagen.jpg]
  generar-retratos-vivos.py tira <clip.mp4>                   # tira de cuadros + primer/último cuadro, para mirar
  generar-retratos-vivos.py medir <clip.mp4>                  # ¿pulsa el eclipse? ¿se mueve el fondo? ¿empalma el loop?
  generar-retratos-vivos.py post <persona> <clip.mp4> [clip2.mp4 ...]   # loop con el tramo móvil, ver abajo
  generar-retratos-vivos.py igualar-eclipse <origen> <ref> <salida> cx cy rcx rcy [cy_nuevo]   # post PIL, ver abajo
  generar-retratos-vivos.py exportar <origen> <destino>       # recorte 4:5 → 720×900 JPG progresivo q84
  generar-retratos-vivos.py ladoalado <salida.png> <a.jpg> <b.jpg> [...]
  generar-retratos-vivos.py costura <persona> [clip.mp4]   # ¿empalma el loop? ¿pestañea en el corte? ¿salta del póster?

Familia stand (2026-10-31, ver §4 abajo): persona = `matias-stand` | `sebastian-stand`; salida `assets/retrato-stand-<p>.{jpg,mp4,webm}`.
  generar-retratos-vivos.py fondo-stand <sebastian|matias> [n=3]   # el sobrio sin su eclipse chico + luz de borde del lado del centro
  generar-retratos-vivos.py fondo-stand-plano <persona> [n]        # la alternativa del primer brief (fondo liso); no se usa
  generar-retratos-vivos.py medir-stand <sobrio.jpg> <variante.jpg> [...]   # parecido (cara), contexto, ¿se fue el eclipse?, ¿de qué lado la luz?
  generar-retratos-vivos.py video kling <persona>-stand [n] <variante.jpg>  # prompt sin viento; el contexto casi quieto
  generar-retratos-vivos.py medir-fondo <clip.mp4>                 # como `medir`, con cajas de cielo (no hay eclipse)
  generar-retratos-vivos.py vinetear <origen> <destino> [w h]      # para mirar la viñeta antes del post
  generar-retratos-vivos.py post <persona>-stand <clip> [clip2]    # clips enteros, rotado al cuadro más quieto, viñeta, 480×600, póster = cuadro 0
  generar-retratos-vivos.py costura <persona>-stand                # con el póster de la familia
  GUARDAR_CUADROS=1 deja los PNG del loop en `_capturas/retratos-vivos/final/<persona>-cuadros/` para probar codificaciones.

Las variantes caen en `_capturas/retratos-vivos/` (ignorado); sólo lo elegido se exporta a `assets/`.
Token de Replicate en ~/.credentials/replicate.env. Precios leídos de Replicate el 2026-10-11:
nano-banana US$ 0,039/imagen · kling-v2.5-turbo-pro US$ 0,07/s (0,35 el clip) · seedance-1-pro US$ 0,03/0,06/0,15
por segundo a 480p/720p/1080p (0,30 el clip a 720p).

Lo que quedó hecho (2026-10-11, rama `retratos-vivos`; reconstruido de los .json y de los cuadros, ver CONTENIDO.md §0.3):
  fondo   14 ediciones nano-banana (US$ 0,55). matias ← fondo-matias-1 · sebastian ← fondo-sebastian-4 + igualar-eclipse con
          fondo-matias-1 de referencia · sobrios ← fondo-*-sobrio-2 + igualar-eclipse. Los cuatro pasaron por `exportar`.
  video   6 seedance (US$ 1,80) y 10 kling (US$ 3,50); los kling 4 y 5 de cada persona con VIENTO=fuerte. Se usaron los kling.
  post    matias ← kling-matias-2 (cuadros ~21–90) → kling-matias-4 (~15–90) → kling-matias-5 (~27–110): 246 cuadros, 10,25 s.
          sebastian ← kling-sebastian-1 (~16–100) → kling-sebastian-4 (~23–88) → kling-sebastian-5 (~25–88): 232 cuadros, 9,67 s.
          Las tres juntas de cada loop (dos adentro y la del cierre) caen bajo un pestañeo: el peso de la cara elige pares de
          cuadros con los ojos iguales, y los iguales son los cerrados. La costura del cierre mide menos que un paso entre
          cuadros consecutivos, y póster ↔ cuadro 0 también (`costura`): el arranque no salta, pestañea.
  costo   ≈ US$ 5,85 en total (sin contar generaciones fallidas, si las hubo; no quedaron registradas).

Lo que quedó hecho (2026-10-31, rama `retratos-stand`, familia stand; ver CONTENIDO.md §0.3):
  fondo   12 ediciones nano-banana (US$ 0,47): 6 con fondo liso (primer brief, descartadas, `fondo-stand-plano-*`) y 6 con el
          contexto conservado y sólo el eclipse chico afuera. Elegidas `fondo-stand-matias-1` (borde dorado a la derecha,
          legible) y `fondo-stand-sebastian-3` (borde a la izquierda). Cara intacta en las seis (mirado cara a cara al 100 %).
  video   5 kling (US$ 1,75), 1268×1632, 122 cuadros: matias 1–3, sebastian 1–2. Pelo quieto en todos, fondo sin pulsos
          (lum del cielo ×1,00–1,09, dif de fondo ≤ 1,6), cámara fija. Descartado matias-1: pestañeo lento (0,4 s de ojos
          cerrados) y deriva de cabeza entre 1,3 y 2,5 s.
  post    sebastian ← kling-1 → kling-2 enteros, juntas 107→3 y 118→9, rotado 83: 215 cuadros, 8,96 s; matias ← kling-2 → kling-3,
          juntas 118→4 y 116→3, rotado 73: 229 cuadros, 9,54 s. Fundido de 6 cuadros; las juntas empalman cuadros casi
          iguales (los dos clips salen de la misma foto: cara 0,7–0,8 contra 0,6 de paso medio). El cuadro 0 (= póster) es el
          centro del segundo más quieto con los ojos abiertos. Cierre a 192×240 (la escala de la portada): 0,55–0,71 total,
          grano del códec (I-frame contra último P-frame), no un salto de imagen; póster ↔ cuadro 0: 0,67–0,76.
  costo   ≈ US$ 2,22 (12 ediciones + 5 clips; sin fallos cobrados: el único 429 fue al crear, antes del cobro).

Segunda vuelta (2026-11-01, misma rama): «como dos personas que miran a la camara sonrien y pestanean» + «redondear las
imagenes de fondo… se tienen que difuminar con el fondo de la pagina».
  video   4 kling más (US$ 1,40): matias 4–5, sebastian 3–4, con la sonrisa como evento del prompt (aparece a ~1,1 s, abierta
          con dientes entre ~1,4 y ~3,3 s, vuelve a la media sonrisa de la foto a ~3,6 s) y sin «expression/smile change» en
          el negativo. Los cuatro sirven: cabeza quieta, pelo inmóvil, fondo sin pulsos (cielo ×1,06–1,12), pestañeos.
  post    matias ← kling-4 → kling-5 (juntas 118→3 y 118→8, rotado 195): 227 cuadros, 9,46 s; sebastian ← kling-3 → kling-4
          (115→3 y 118→4, rotado 213): 228 cuadros, 9,50 s. Dos sonrisas por loop. El cuadro 0 (= póster) ahora se elige con
          ojos Y boca en reposo (ZONA_BOCA). Viñeta ELÍPTICA centrada en la cara (plena hasta 0,28, cielo puro en 0,80 del
          radio): bordes del cuadro = #0b0a14 medido, sin rectángulo. Cierre a 192×240: 0,35 (antes 0,55–0,71: la elipse deja
          más cielo puro y menos ruido de códec); póster ↔ cuadro 0: 0,84–0,85. Pesos: Matías 15 KB / 141 KB / 96 KB,
          Sebastián 19 KB / 173 KB / 117 KB (jpg / mp4 / webm).
  costo   ≈ US$ 1,40 esta vuelta; ≈ US$ 3,62 la familia stand completa.
"""
import base64, json, os, re, subprocess, sys, time, urllib.request, pathlib, concurrent.futures

TOKEN = None
for line in open(os.path.expanduser("~/.credentials/replicate.env")):
    if line.startswith("REPLICATE_API_TOKEN="):
        TOKEN = line.split("=", 1)[1].strip()
assert TOKEN, "sin token"
# Desde el 31/10 api.replicate.com responde 403 al User-Agent por defecto de urllib («Python-urllib/3.x»);
# con cualquier otro responde 200. Se instala un opener con nombre propio para todas las llamadas (y las descargas).
urllib.request.install_opener(urllib.request.build_opener())
urllib.request._opener.addheaders = [("User-Agent", "rialabs-retratos-vivos/1.0")]

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ASSETS = RAIZ / "assets"
OUT = RAIZ / "_capturas" / "retratos-vivos"
OUT.mkdir(parents=True, exist_ok=True)
FFMPEG = "/opt/homebrew/bin/ffmpeg"
FFPROBE = "/opt/homebrew/bin/ffprobe"

PRECIO = {"nano-banana": 0.039, "kling": 0.07 * 5, "kling-s": 0.07, "seedance": {"480p": 0.03 * 5, "720p": 0.06 * 5, "1080p": 0.15 * 5}}

# ══════════════════════════════════════════════════════════════════════════════════════════════════
# 1. FONDO — la idea común del eclipse en los dos retratos
# ══════════════════════════════════════════════════════════════════════════════════════════════════
# Lo que pidió Matías: «los logos de RIA de fondo si están presentes está bien pero debe ser siguiendo una
# idea común en ambas imágenes y mucho más de fondo». La idea común, escrita una sola vez:
ECLIPSE_COMUN = (
    "Change ONLY the solar eclipse in the background, and make it the same in look, size and placement as described here: "
    "a SMALL total solar eclipse — a black disc with a thin golden corona ring — on the dark back wall, far behind him. "
    "Size: its diameter is about one fifth of the image width. Placement: horizontally centered on the vertical axis of his head, "
    "high in the frame, its center about 15 percent of the image height below the top edge, well above the top of his head, "
    "with empty dark wall between the eclipse and his hair. "
    "It is far away and out of focus (soft bokeh edges, consistent with the shallow depth of field of the portrait), and DIM: "
    "the corona glows at roughly a third of the brightness of the current one, with only a faint warm halo on the wall around it, "
    "so it reads as a quiet detail of the room, not as a halo around the person. "
    "Remove every trace of the current, larger eclipse. The eclipse is BEHIND everything: any strands of hair in front of it stay in front, sharp. "
    "Keep absolutely everything else pixel-identical: his face, expression, eyes, skin, hair (every strand, same shape and volume), "
    "beard, clothes, pose, framing, the lighting on him, the background screens and objects, the grain and the colors. Photorealistic. "
)
FONDO = {
    "sebastian": ("Edit this photograph. The man with glasses, grey-streaked beard, a navy jacket and a long blond mane flying in the wind "
                  "stays exactly as he is, and so do the video wall of street cameras on the left and the equipment rack with blue LEDs on the right. "
                  + ECLIPSE_COMUN),
    "matias":    ("Edit this photograph. The man with crossed arms, dark blazer, stubble beard and long blond hair streaming back to the left "
                  "stays exactly as he is, and so do the monitors with code and the blue wireframe city behind him. " + ECLIPSE_COMUN),
}
# Con la consigna común nano-banana le hizo a Sebastián un eclipse más chico y más alto que a Matías (≈7 % del ancho
# contra ≈12 %). Igualarlo pasándole el retrato de Matías como referencia NO sirve: la edición con dos imágenes le
# contagia el fondo (monitores, brazos cruzados) o mueve el encuadre (probado, 3 de 3). Sí sirve escribirle los
# números medidos del eclipse elegido de Matías (`fondo-matias-1`): diámetro ≈ 12 % del ancho, centro ≈ 14 % de alto.
FONDO["sebastian"] = FONDO["sebastian"].replace(
    "Size: its diameter is about one fifth of the image width.",
    "Size: its diameter is about 12 percent of the image width — a bit less than half the width of his face, clearly larger than a dot.") \
    .replace("its center about 15 percent of the image height below the top edge",
             "its center about 14 percent of the image height below the top edge")
FONDO["sebastian-sobrio"] = FONDO["sebastian"].replace("a long blond mane flying in the wind", "short hair")
FONDO["matias-sobrio"] = FONDO["matias"].replace("and long blond hair streaming back to the left", "and short dark hair")

# ══════════════════════════════════════════════════════════════════════════════════════════════════
# 2. VIDEO — quietos esperando la foto, pero vivos; la melena al viento de un ventilador
# ══════════════════════════════════════════════════════════════════════════════════════════════════
# Pedido textual: «segundos en los cuales pestañamos, nuestro pelo vuela suavemente con el viento, miramos a la
# cámara en posición estática como esperando la foto, pero se nota que estamos ahí» · «las melenas tienen que
# volar al movimiento de un ventilador, moverse en el aire como símbolo de potencia y visión».
VIVO_COMUN = (
    "Locked-off photographic portrait on a tripod: the camera does not move at all, the framing is identical from the first "
    "frame to the last. The man holds his pose completely still, looking straight into the lens, waiting for the photo to be "
    "taken, his expression unchanged. He is clearly alive: he blinks naturally twice, his chest rises and falls with slow quiet "
    "breathing, and his head has the tiniest natural micro-movements. {PELO} The wind is strong and sustained for the whole clip, "
    "never a timid breeze, and his face is never covered. {ROPA} The background stays perfectly still: {FONDO} and the small "
    "golden eclipse ring on the back wall do not move or flicker. Constant lighting throughout, the same warm amber key light and "
    "cool blue fill. Same face, same identity, {RASGOS} from start to finish. Photoreal, cinematic, 24 fps, no morphing. "
    "The last frame matches the first frame exactly so the clip loops seamlessly."
)
VIVO = {
    "sebastian": VIVO_COMUN.format(
        PELO=("His long blond mane is blown continuously by a powerful studio fan from the front: the hair streams open to both sides "
              "and upward, billowing and flowing in the air in long elegant waves, a symbol of power and vision, every strand in motion "
              "all the time."),
        ROPA="The collar of his navy jacket flutters very slightly in the wind.",
        FONDO="the video wall of street-camera feeds, the equipment rack with blue LEDs",
        RASGOS="same rectangular glasses, same grey-streaked beard, same calm half-smile"),
    "matias": VIVO_COMUN.format(
        PELO=("His long blond hair is blown continuously by a powerful studio fan from the front-right: the hair streams backward and to "
              "the left of the frame, flowing in the air in long elegant waves, a symbol of power and vision, every strand in motion "
              "all the time, his face fully visible."),
        ROPA="He keeps his arms crossed; the lapel of his dark blazer moves very slightly in the wind.",
        FONDO="the monitors with code, the blue wireframe city model",
        RASGOS="same stubble beard, same knowing half-smile, same crossed arms"),
}
# Ronda de reserva (VIENTO=fuerte): Kling dejó el pelo casi quieto en 4 de 6 clips de la primera ronda (diferencia media
# cuadro a cuadro en la zona de la melena < 1,5 sobre 255); se le pide amplitud explícita.
VIENTO_FUERTE = (" IMPORTANT: the wind is the strongest element of the shot. The fan blows hard and without pause: the hair "
                 "whips, lifts and billows with LARGE amplitude the whole five seconds, strands rising high, crossing and "
                 "streaming, constantly changing shape; at no moment does the hair hang still. The face, the body and the "
                 "background remain perfectly still.")
NEGATIVO = ("camera movement, zoom, pan, dolly, handheld shake, face change, identity change, different person, expression change, "
            "smile change, talking, mouth opening, head turning away, extra limbs, extra hands, text, watermark, flicker, lighting change, "
            "warping, morphing, blur, cartoon, hair covering the face, background movement")

# ══════════════════════════════════════════════════════════════════════════════════════════════════
# 4. STAND (2026-10-31) — los dos en las esquinas de abajo de la portada, posando para la foto, sin pelo agregado
# ══════════════════════════════════════════════════════════════════════════════════════════════════
# Pedido textual de Matías: «a cada costado del logo las imagenes de los ceos, Matias y Sebastian, en movimiento como
# posando esperando que le saquen la foto con el parpadeo de ojos y todo, pero sin pelo agregado. La idea es mostrar los
# CEOs que estan presentes en el stand como una primera vista cuando se visita la home de la empresa». Y, al ver la
# portada: «abajo de la maquina, del lado izquierdo, a la altura de RIA, pone la imagen viva de Matias desarrollador, y
# a la misma altura pero del lado derecho, abajo de la red de sistemas, pone la foto viva de Sebastian de Byte».
# Parte de la familia sobria (`retrato-*-sobrio.jpg`), que es «sin pelo agregado». MATÍAS va a la IZQUIERDA y SEBASTIÁN
# a la DERECHA (al revés que en #equipo). El contexto se conserva —«Matías desarrollador»: las pantallas de código y la
# maqueta; «Sebastián de Byte»: el muro de cámaras y el rack—; lo único que sale es el eclipse chico de cada uno, porque
# en la portada hay UN solo eclipse, el del hero. Una luz de borde cálida y sutil del lado que mira al centro: derecha
# en Matías, izquierda en Sebastián. En post, una viñeta que cae a #0b0a14 (el cielo de v5) subordina el contexto y
# deja el borde listo para que la portada lo funda con el cielo de estrellas con una máscara CSS. Nunca se espeja una
# cara. Medido en los sobrios: la luz cálida de Matías entra por la IZQUIERDA (mejilla izquierda 170 contra 82) y la
# de Sebastián por la DERECHA (169 contra 91); con los lados invertidos la clave de cada uno queda del lado de afuera
# y el borde dorado del lado del eclipse: dos luces, no una contradicción, pero queda anotado.
CIELO = (11, 10, 20)   # #0b0a14, el cielo de v5
FONDO_STAND_COMUN = (
    "Make exactly two changes. "
    "ONE: remove the small solar eclipse ring floating above his head, filling that area with the same plain dark wall "
    "that surrounds it, seamlessly, with no trace, no glow and no mark left. "
    "TWO: add a thin, soft, warm golden rim light coming from the {LADO} edge of the frame, grazing only the {LADO} "
    "outline of his hair, ear, cheek, jaw and shoulder, as if a distant golden eclipse glowed off-frame to the {LADO}. "
    "It is gentle and narrow, never a flare, never a halo on the wall, and it does not brighten the background. "
    "Keep absolutely everything else pixel-identical: his face, expression, eyes, gaze, skin, hair (every strand, same "
    "shape, no added hair), beard, glasses, clothes, pose, framing, scale and position in the frame, the existing key "
    "light and fill light on him, {CONTEXTO}, the grain and the colors. Do not mirror or flip the image. Photorealistic."
)
FONDO_STAND = {
    "matias":    ("Edit this photograph. The man with crossed arms, dark blazer over a black tee, stubble beard and short dark "
                  "hair stays exactly as he is. "
                  + FONDO_STAND_COMUN.format(LADO="RIGHT", CONTEXTO="the monitors with code and the blue wireframe city model behind him")),
    "sebastian": ("Edit this photograph. The man with rectangular glasses, short hair, a grey-streaked beard and a navy jacket "
                  "over a beige tee stays exactly as he is. "
                  + FONDO_STAND_COMUN.format(LADO="LEFT", CONTEXTO="the video wall of street-camera feeds on the left and the "
                                                                    "equipment rack with blue LEDs on the right")),
}
# Alternativa descartada el mismo día (primer brief: «fondo casi plano y muy oscuro, sin objetos»): las seis variantes
# quedaron en `_capturas/retratos-vivos/fondo-stand-plano-*.jpg` (3 por persona, US$ 0,23), con el parecido intacto y el
# fondo liso pero más gris-azul que #0b0a14. No se usan: Matías pidió conservar el contexto que los identifica.
FONDO_STAND_PLANO_COMUN = (
    "Replace the ENTIRE background with a plain, flat, matte backdrop of one uniform, very dark color: an almost-black "
    "night blue-violet, hex #0b0a14 (RGB 11, 10, 20). No objects at all, no screens, no furniture, no walls with texture, "
    "no eclipse, no light sources, no gradient, no vignette, no haze, no bokeh circles: just the dark flat color edge to "
    "edge, including above his head and at the corners, as if he were photographed in front of a dark velvet cloth in a "
    "black studio. Remove every trace of {OBJETOS}. "
    "Then add ONE subtle touch: a thin, soft, warm golden rim light coming from the {LADO} edge of the frame, grazing "
    "only the {LADO} outline of his hair, ear, cheek, jaw and shoulder, as if a distant golden eclipse glowed off-frame "
    "to the {LADO}. It is gentle and narrow, never a flare, never a halo on the backdrop, and it does not brighten the "
    "backdrop itself. "
    "Keep absolutely everything else pixel-identical: his face, expression, eyes, gaze, skin, hair (every strand, same "
    "shape, no added hair), beard, glasses, clothes, pose, framing, scale and position in the frame, the existing key "
    "light and fill light on him, the grain and the colors. Do not mirror or flip the image. Photorealistic."
)
FONDO_STAND_PLANO = {   # con los lados del PRIMER brief (Sebastián a la izquierda, luz desde la derecha; Matías al revés)
    "sebastian": ("Edit this photograph. The man with rectangular glasses, short hair, a grey-streaked beard and a navy jacket "
                  "over a beige tee stays exactly as he is. "
                  + FONDO_STAND_PLANO_COMUN.format(OBJETOS="the video wall of street-camera feeds on the left, the equipment rack "
                                                           "with blue LEDs on the right and the small eclipse ring above his head",
                                                   LADO="RIGHT")),
    "matias":    ("Edit this photograph. The man with crossed arms, dark blazer over a black tee, stubble beard and short dark "
                  "hair stays exactly as he is. "
                  + FONDO_STAND_PLANO_COMUN.format(OBJETOS="the monitors with code on the left, the blue wireframe city model on "
                                                           "the right, the desk, and the small eclipse ring above his head",
                                                   LADO="LEFT")),
}
# El clip: lo mismo que VIVO_COMUN pero SIN viento. Posando quietos esperando la foto: respiración, dos o tres pestañeos,
# la mirada a cámara. El pelo no se mueve (ni ventilador ni brisa), cámara fija, luz constante. El contexto puede tener vida
# mínima (un cursor, un brillo leve en el código; las cámaras del muro casi quietas), nunca scroll ni cambios de contenido:
# la costura del loop funde dos clips, y si las pantallas cambian de contenido el fundido se ve. Si aun así complica la
# costura, quietas.
# Segunda vuelta (2026-11-01). Matías, al ver la portada: «recuerda hacer las fotos vivas, como dos personas que miran a la
# camara sonrien y pestanean». La primera vuelta pedía «la media sonrisa se tensa y se relaja casi imperceptiblemente» y
# llevaba «expression change, smile change, mouth opening» en el negativo: salió boca cerrada, no se leía «sonríen». Ahora
# la sonrisa es el evento del clip —aparece, se sostiene, se relaja— y vuelve a la expresión de la foto al final (el truco
# del loop lo exige). El cuadro 0 (= póster) se elige después, en post, en un momento neutro.
VIVO_STAND_COMUN = (
    "Locked-off photographic portrait on a tripod: the camera does not move at all, the framing is identical from the "
    "first frame to the last. The man stands still, posing for the photographer, looking straight into the lens the "
    "whole time. During the clip he breaks into a warm, genuine, friendly smile at the camera: the smile builds naturally "
    "over about a second, his lips part to show a hint of his teeth, his cheeks lift and his eyes crease with it; he holds "
    "the open smile for a couple of seconds, then it relaxes gently back to his calm {SONRISA} by the end of the clip. He "
    "blinks naturally two or three times. His chest rises and falls with slow quiet breathing and his head has the "
    "tiniest natural micro-movements. There is NO wind and NO fan: his hair does not move at all, not a single strand, and "
    "his clothes do not move. {ROPA} The background stays in place and almost still: {FONDO}. No scrolling, no content "
    "changing, no flashing, no shadows passing, no light pulsing. Constant lighting throughout: the same warm key light on "
    "his face and the same thin golden rim light on his {LADO} edge. Same face, same identity, {RASGOS} from start to "
    "finish. Photoreal, cinematic, 24 fps, no morphing. The last frame matches the first frame exactly so the clip loops "
    "seamlessly."
)
VIVO_STAND = {
    "matias-stand":    VIVO_STAND_COMUN.format(
        SONRISA="knowing half-smile", ROPA="He keeps his arms crossed, still.", LADO="right",
        FONDO="the monitors with code may show at most a cursor blinking or a faint shimmer of the text, and the blue "
              "wireframe city model does not move",
        RASGOS="same stubble beard, same eyes, same crossed arms"),
    "sebastian-stand": VIVO_STAND_COMUN.format(
        SONRISA="calm half-smile", ROPA="The collar of his navy jacket stays still.", LADO="left",
        FONDO="the video wall of street-camera feeds is nearly frozen, with at most a faint shimmer, and the equipment "
              "rack with blue LEDs keeps its LEDs steadily lit, not blinking",
        RASGOS="same rectangular glasses, same grey-streaked beard, same eyes"),
}
# Tercera vuelta (2026-11-01, más tarde). Matías, con la portada integrada: «Podemos hacer que los videos de Sebastian y
# Matias sean más largos, y las sonrizas mas lentas? En loop, esos videos parece como que rien y se ponen serios muy
# rapidos». Clips de 10 s (Kling acepta duration 5 | 10 con start=end; US$ 0,70 el de 10) con la sonrisa repartida en el
# tiempo: ~2 s en reposo, ~3 s en armarse, ~3 s sostenida, ~2 s en volver, y reposo hasta el final. El loop largo se arma
# después con los clips neutros de la primera vuelta (kling-*-stand-1/2/3), que no cuestan nada.
VIVO_STAND_LENTO_COMUN = (
    "Locked-off photographic portrait on a tripod: the camera does not move at all, the framing is identical from the "
    "first frame to the last. The man stands still, posing for the photographer, looking straight into the lens the "
    "whole time, relaxed and unhurried. Timeline of the ten seconds: for the first two seconds he simply holds his calm "
    "{SONRISA}, breathing quietly. Then a warm, genuine smile builds VERY SLOWLY, over about three full seconds, like a "
    "slow sunrise: the corners of his mouth lift little by little, his lips part gradually to show a hint of his teeth, "
    "his cheeks rise and his eyes crease gently. He holds the full open smile, steady and kind, for about three seconds. "
    "Then the smile fades just as slowly, over about two seconds, back to his calm {SONRISA}, which he holds until the "
    "end. Nothing is sudden: every change of expression is gradual and gentle, never a quick grin, never a laugh. He "
    "blinks naturally a few times at normal speed. His chest rises and falls with slow quiet breathing and his head has "
    "the tiniest natural micro-movements. There is NO wind and NO fan: his hair does not move at all, not a single "
    "strand, and his clothes do not move. {ROPA} The background stays in place and almost still: {FONDO}. No scrolling, "
    "no content changing, no flashing, no shadows passing, no light pulsing. Constant lighting throughout: the same warm "
    "key light on his face and the same thin golden rim light on his {LADO} edge. Same face, same identity, {RASGOS} "
    "from start to finish. Photoreal, cinematic, 24 fps, no morphing. The last frame matches the first frame exactly so "
    "the clip loops seamlessly."
)
VIVO_STAND_LENTO = {
    "matias-stand":    VIVO_STAND_LENTO_COMUN.format(
        SONRISA="knowing half-smile", ROPA="He keeps his arms crossed, still.", LADO="right",
        FONDO="the monitors with code may show at most a cursor blinking or a faint shimmer of the text, and the blue "
              "wireframe city model does not move",
        RASGOS="same stubble beard, same eyes, same crossed arms"),
    "sebastian-stand": VIVO_STAND_LENTO_COMUN.format(
        SONRISA="calm half-smile", ROPA="The collar of his navy jacket stays still.", LADO="left",
        FONDO="the video wall of street-camera feeds is nearly frozen, with at most a faint shimmer, and the equipment "
              "rack with blue LEDs keeps its LEDs steadily lit, not blinking",
        RASGOS="same rectangular glasses, same grey-streaked beard, same eyes"),
}
# El negativo de la familia stand NO lleva «expression change, smile change, mouth opening» (la sonrisa es el evento).
NEGATIVO_STAND = ("camera movement, zoom, pan, dolly, handheld shake, face change, identity change, different person, talking, "
                  "head turning away, looking away, extra limbs, extra hands, text, watermark, flicker, lighting change, warping, "
                  "morphing, blur, cartoon, grimace, exaggerated smile, laughing, wind, breeze, fan, hair moving, hair blowing, "
                  "clothes moving, scrolling text, screens changing, LEDs blinking")
NEGATIVO_STAND_LENTO = NEGATIVO_STAND + ", sudden expression change, fast smile, quick grin"


# ── Replicate ─────────────────────────────────────────────────────────────────────────────────────
def data_uri(p):
    return "data:image/jpeg;base64," + base64.b64encode(open(p, "rb").read()).decode()

def replicate(modelo, entrada, timeout=900):
    body = json.dumps({"input": entrada}).encode()
    req = urllib.request.Request(f"https://api.replicate.com/v1/models/{modelo}/predictions", data=body, method="POST",
                                 headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json", "Prefer": "wait=60"})
    for intento in range(6):   # 429 al crear (seis a la vez lo disparan): esperar y volver a intentar; no se cobró nada
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                pred = json.load(r)
            break
        except urllib.error.HTTPError as e:
            if e.code != 429 or intento == 5: raise
            time.sleep(8 * (intento + 1))
    t0 = time.time()
    while pred.get("status") not in ("succeeded", "failed", "canceled"):
        if time.time() - t0 > timeout:
            raise TimeoutError(pred["id"])
        time.sleep(4)
        req = urllib.request.Request(f"https://api.replicate.com/v1/predictions/{pred['id']}", headers={"Authorization": f"Bearer {TOKEN}"})
        with urllib.request.urlopen(req, timeout=60) as r:
            pred = json.load(r)
    return pred

def _siguiente(patron):
    """Número de la próxima variante: el mayor que haya + 1 (contar archivos pisa huecos: pasó el 31/10 con sebastian-3)."""
    nums = [int(m.group(1)) for f in OUT.glob(patron) for m in [re.search(r"-(\d+)\.\w+$", f.name)] if m]
    return (max(nums) if nums else 0) + 1

def bajar(pred, dest):
    url = pred["output"] if isinstance(pred["output"], str) else pred["output"][0]
    urllib.request.urlretrieve(url, dest)


# ── 1. fondo ──────────────────────────────────────────────────────────────────────────────────────
def fondo(persona, n=3, referencia=None):
    origen = ASSETS / f"retrato-{persona}.jpg"
    prompt = FONDO[persona]
    refs = [origen]
    if referencia:
        refs.append(pathlib.Path(referencia))
        prompt = ("Edit the FIRST image only. Replace its solar eclipse with one that matches the eclipse of the SECOND image EXACTLY "
                  "in size, position within the frame, dimness, softness and look, so that the two photographs read as the same photo "
                  "session. Use the second image ONLY for the eclipse. " + prompt.split("Edit this photograph. ", 1)[1])
    def uno(i):
        dest = OUT / f"fondo-{persona}{'-ref' if referencia else ''}-{i + 1}.jpg"
        pred = replicate("google/nano-banana", {"prompt": prompt, "image_input": [data_uri(r) for r in refs],
                                                "aspect_ratio": "4:5", "output_format": "jpg"})
        if pred["status"] != "succeeded":
            return f"{dest.name} FALLÓ: {pred.get('error')}"
        bajar(pred, dest)
        return f"{dest.name} ok ({pred.get('metrics', {}).get('predict_time')} s, US$ {PRECIO['nano-banana']:.3f})"
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for f in concurrent.futures.as_completed([ex.submit(uno, i) for i in range(n)]):
            print(f.result(), flush=True)


# ── 4. fondo-stand: el sobrio sin su eclipse chico, con luz de borde del lado del centro (contexto conservado) ──
def fondo_stand(persona, n=3, plano=False):
    origen = ASSETS / f"retrato-{persona}-sobrio.jpg"
    pref = f"fondo-stand-{'plano-' if plano else ''}{persona}"
    base = _siguiente(f"{pref}-*.jpg") - 1
    prompt = (FONDO_STAND_PLANO if plano else FONDO_STAND)[persona]
    def uno(i):
        dest = OUT / f"{pref}-{base + i + 1}.jpg"
        pred = replicate("google/nano-banana", {"prompt": prompt, "image_input": [data_uri(origen)],
                                                "aspect_ratio": "4:5", "output_format": "jpg"})
        if pred["status"] != "succeeded":
            return f"{dest.name} FALLÓ: {pred.get('error')}"
        bajar(pred, dest)
        return f"{dest.name} ok ({pred.get('metrics', {}).get('predict_time')} s, US$ {PRECIO['nano-banana']:.3f})"
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for f in concurrent.futures.as_completed([ex.submit(uno, i) for i in range(n)]):
            print(f.result(), flush=True)

# Caja del eclipse chico en los sobrios (las dos familias lo tienen en el mismo lugar: igualado el 11/10).
CAJA_ECLIPSE_SOBRIO = (0.38, 0.03, 0.66, 0.22)

def medir_stand(origen, *variantes):
    """Para elegir la variante de fondo-stand, contra el sobrio original: la diferencia en la zona de la cara (el
    parecido: cuanto menor, menos tocó nano-banana la cara), la diferencia del resto del cuadro fuera de la caja del
    eclipse (¿conservó el contexto?), la luminancia en la caja del eclipse (en el original ≈ 25–30 con el anillo; sin
    anillo baja a la de la pared, ≈ 13–19), y el brillo del borde de la persona a cada lado (zona de hombro y oreja
    sin fondo), para ver de qué lado quedó la luz de borde y cuánto subió."""
    from PIL import Image, ImageChops, ImageStat
    persona = "matias" if "matias" in str(origen) else "sebastian"
    o = Image.open(origen).convert("RGB")
    w, h = o.size
    box = lambda c: (int(c[0] * w), int(c[1] * h), int(c[2] * w), int(c[3] * h))
    cara, ecl = box(ZONA_CARA[persona]), box(CAJA_ECLIPSE_SOBRIO)
    # bordes de la persona: la franja de la oreja/mejilla y del hombro a cada lado (mismo encuadre en los dos sobrios)
    bordes = {"matias": {"izq": (0.28, 0.38, 0.36, 0.72), "der": (0.62, 0.38, 0.70, 0.72)},
              "sebastian": {"izq": (0.28, 0.38, 0.36, 0.72), "der": (0.64, 0.38, 0.72, 0.72)}}[persona]
    lum = lambda im, c: ImageStat.Stat(im.crop(box(c) if isinstance(c[0], float) else c).convert("L")).mean[0]
    print(f"{pathlib.Path(origen).name}: eclipse lum {lum(o, ecl):.1f} · borde izq {lum(o, bordes['izq']):.1f} · borde der {lum(o, bordes['der']):.1f}")
    for v in variantes:
        im = Image.open(v).convert("RGB")
        if im.size != o.size: im = im.resize(o.size, Image.LANCZOS)
        d = ImageChops.difference(o, im)
        dcara = sum(ImageStat.Stat(d.crop(cara)).mean) / 3
        resto = d.copy(); resto.paste((0, 0, 0), ecl)        # fuera de la caja del eclipse
        dresto = sum(ImageStat.Stat(resto).mean) / 3
        print(f"{pathlib.Path(v).name}: {Image.open(v).size[0]}×{Image.open(v).size[1]} · cara dif {dcara:.2f} · resto dif {dresto:.2f}"
              f" · eclipse lum {lum(im, ecl):.1f} · borde izq {lum(im, bordes['izq']):.1f} ({lum(im, bordes['izq']) - lum(o, bordes['izq']):+.1f})"
              f" · borde der {lum(im, bordes['der']):.1f} ({lum(im, bordes['der']) - lum(o, bordes['der']):+.1f})")


# ── viñeta hacia el cielo (post, PIL): subordina el contexto y deja el borde listo para la máscara CSS ──
# Segunda vuelta (2026-11-01). Matías: «trata de redondear las imagenes de fondo de esas dos fotos. Los fondos de las fotos
# se tienen que difuminar con el fondo de la pagina». La primera viñeta era un rectángulo redondeado (norma 3, plena hasta
# 0,42 del semilado, a cero en 1,02 —o sea, en el borde mismo—) y, sin máscara CSS, se leía el rectángulo. Ahora es una
# ELIPSE centrada en la cara (CX, CY en fracción del cuadro), plena hasta R0 y a #0b0a14 PURO en R1 < 1, con los radios
# medidos desde el centro hasta el borde (RX = semiancho, RY = distancia del centro al borde de abajo): f = 1 adentro de
# R0, cae con smoothstep a 0 en R1, y el píxel se mezcla hacia CIELO con 1 − f. El contexto se intuye, no se recorta.
# Se calcula una sola vez por tamaño y se aplica con Image.composite a cada cuadro y al póster: todos la misma viñeta.
VINETA = {"CX": 0.5, "CY": 0.44, "R0": 0.28, "R1": 0.80, "RX": 0.5, "RY": 0.56, "P": 2.0}
_mascaras = {}

def mascara_vineta(tam):
    from PIL import Image
    if tam in _mascaras: return _mascaras[tam]
    w, h = tam; CX, CY, R0, R1, RX, RY, P = (VINETA[k] for k in ("CX", "CY", "R0", "R1", "RX", "RY", "P"))
    m = Image.new("L", tam); px = m.load()
    for y in range(h):
        ny = abs((y / (h - 1)) - CY) / RY
        for x in range(w):
            nx = abs((x / (w - 1)) - CX) / RX
            r = (nx ** P + ny ** P) ** (1 / P)
            t = min(max((r - R0) / (R1 - R0), 0.0), 1.0)
            px[x, y] = round(255 * (1 - t * t * (3 - 2 * t)))
    _mascaras[tam] = m
    return m

def vinetear(im):
    from PIL import Image
    return Image.composite(im, Image.new("RGB", im.size, CIELO), mascara_vineta(im.size))

def vinetear_archivo(origen, destino, tam=None):
    from PIL import Image
    im = Image.open(origen).convert("RGB")
    if tam: im = im.resize(tam, Image.LANCZOS)
    vinetear(im).save(destino, "JPEG", quality=90)
    print(destino)


# ── 2. video ──────────────────────────────────────────────────────────────────────────────────────
def video(modelo, persona, n=1, imagen=None, resolucion="720p"):
    stand = persona in VIVO_STAND
    lenta = stand and os.environ.get("SONRISA") == "lenta"      # tercera vuelta: la sonrisa lenta, pensada para 10 s
    dur = int(os.environ.get("DURACION", 5))                     # kling: 5 | 10
    img = pathlib.Path(imagen) if imagen else ASSETS / f"retrato-{persona}.jpg"
    uri = data_uri(img)
    prompt = (VIVO_STAND_LENTO if lenta else VIVO_STAND)[persona] if stand else VIVO[persona] + (VIENTO_FUERTE if os.environ.get("VIENTO") == "fuerte" else "")
    if modelo == "kling":
        nombre, entrada = "kwaivgi/kling-v2.5-turbo-pro", {
            "prompt": prompt, "negative_prompt": (NEGATIVO_STAND_LENTO if lenta else NEGATIVO_STAND) if stand else NEGATIVO,
            "start_image": uri, "end_image": uri, "duration": dur}
        costo = PRECIO["kling-s"] * dur
    elif modelo == "seedance":
        nombre, entrada = "bytedance/seedance-1-pro", {
            "prompt": prompt, "image": uri, "last_frame_image": uri, "duration": 5, "resolution": resolucion,
            "camera_fixed": True, "fps": 24}
        costo = PRECIO["seedance"][resolucion]
    else:
        raise SystemExit("modelo: kling | seedance")
    base = _siguiente(f"{modelo}-{persona}-*.mp4") - 1
    def uno(i):
        k = base + i + 1
        dest = OUT / f"{modelo}-{persona}-{k}.mp4"
        e = dict(entrada)
        if modelo == "seedance":
            e["seed"] = 1000 + k
        t0 = time.time()
        pred = replicate(nombre, e)
        if pred["status"] != "succeeded":
            return f"{dest.name} FALLÓ: {pred.get('error')}"
        bajar(pred, dest)
        meta = {"modelo": nombre, "version": pred.get("version"), "id": pred["id"], "persona": persona, "imagen": str(img),
                "entrada": {k2: v for k2, v in e.items() if not str(v).startswith("data:")}, "metrics": pred.get("metrics"),
                "costo_usd": costo, "espera_s": round(time.time() - t0)}
        (OUT / f"{modelo}-{persona}-{k}.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False))
        return f"{dest.name} ok ({pred.get('metrics', {}).get('predict_time')} s de cómputo, {meta['espera_s']} s de espera, US$ {costo:.2f})"
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for f in concurrent.futures.as_completed([ex.submit(uno, i) for i in range(n)]):
            print(f.result(), flush=True)


# ── tira de cuadros, primer y último cuadro ────────────────────────────────────────────────────────
def tira(clip):
    clip = pathlib.Path(clip)
    base = (clip if clip.resolve().parent == OUT.resolve() else OUT / clip.name).with_suffix("")   # nunca al lado de un asset
    sh = lambda *a: subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", *a], check=True)
    sh("-i", str(clip), "-vf", "fps=2,scale=240:-1,tile=10x1", "-frames:v", "1", f"{base}-tira.png")
    sh("-i", str(clip), "-vf", "scale=480:-1", "-frames:v", "1", f"{base}-primero.png")
    sh("-sseof", "-0.05", "-i", str(clip), "-update", "1", "-vf", "scale=480:-1", f"{base}-ultimo.png")
    print(f"{base}-tira.png  {base}-primero.png  {base}-ultimo.png")


# ── medir un clip: ¿el eclipse parpadea? ¿la cámara se mueve? ¿el último cuadro empalma con el primero? ──
def medir(clip, caja_eclipse=None, caja_fondo=None, fps=4):
    """Muestrea el clip a `fps` y mide, por cuadro: luminancia media en la caja del eclipse (si pulsa, se ve),
    diferencia media contra el primer cuadro en una caja de fondo quieto (si la cámara se mueve o la luz cambia, sube),
    y la diferencia del último cuadro contra el primero (la costura del loop). Cajas como fracciones x0,y0,x1,y1."""
    import tempfile, glob
    from PIL import Image, ImageChops, ImageStat
    clip = pathlib.Path(clip)
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-i", str(clip), "-vf", f"fps={fps},scale=360:-1", f"{td}/f%03d.png"], check=True)
        fr = [Image.open(f).convert("RGB") for f in sorted(glob.glob(f"{td}/f*.png"))]
    w, h = fr[0].size
    ce = caja_eclipse or (0.38, 0.03, 0.66, 0.22)
    cf = caja_fondo or (0.70, 0.55, 0.99, 0.75)
    box = lambda c: (int(c[0] * w), int(c[1] * h), int(c[2] * w), int(c[3] * h))
    lum = [ImageStat.Stat(f.crop(box(ce)).convert("L")).mean[0] for f in fr]
    dif = [sum(ImageStat.Stat(ImageChops.difference(fr[0].crop(box(cf)), f.crop(box(cf)))).mean) / 3 for f in fr]
    costura = sum(ImageStat.Stat(ImageChops.difference(fr[0], fr[-1])).mean) / 3
    print(f"{clip.name}: eclipse lum {min(lum):.1f}–{max(lum):.1f} (×{max(lum) / max(min(lum), 1):.2f}) · fondo dif máx {max(dif):.1f} · costura último↔primero {costura:.1f}")
    return lum, dif, costura

# ── 3. post: el loop se arma con el tramo en movimiento ───────────────────────────────────────────
# Con el mismo retrato como primer y último cuadro, los dos modelos dejan el pelo QUIETO ~0,5–1 s al principio y
# ~1 s al final (medido: diferencia cuadro a cuadro < 1/255 en la zona de la melena). Un loop del clip entero
# tendría ~2 s de pelo congelado por vuelta. Por eso el loop se construye con el tramo móvil de cada clip: se busca
# el par de cuadros (cola de uno, cabeza del siguiente —o del mismo, si es uno solo—) que más se parecen y se
# cortan ahí con un fundido cruzado corto (6 cuadros = 0,25 s). Nunca ping-pong: el pelo no vuelve para atrás.
ZONA_PELO = {"matias": (0.0, 0.1, 0.55, 0.55), "sebastian": (0.0, 0.0, 1.0, 0.45)}
# La cara pesa ×25 al elegir el par de cuadros del corte: el pestañeo de cada clip cae a ~1 s, justo donde arranca el
# pelo, y si el corte cae ahí el fundido mezcla un ojo cerrado con uno abierto (párpado fantasma). Con el peso, el
# corte se corre unos cuadros y las dos caras del fundido tienen los ojos igual.
ZONA_CARA = {"matias": (0.35, 0.30, 0.65, 0.60), "sebastian": (0.33, 0.28, 0.67, 0.60)}
PESO_CARA = 25
# La zona de los ojos sola, para `costura`: ahí se ven los pestañeos.
ZONA_OJOS = {"matias": (0.40, 0.40, 0.62, 0.50), "sebastian": (0.36, 0.36, 0.64, 0.46)}
# Familia stand: el mismo encuadre que los sobrios, así que las zonas de cara y ojos son las mismas. Lo que no hay es
# melena: la «zona del pelo» pasa a ser la persona entera (cara y pecho: pestañeos, respiración, micro-movimientos) y
# sirve para medir en `costura`, no para recortar: en los clips stand NO hay cabeza ni cola congeladas (medido el 31/10:
# contra el cuadro 0 la persona ya difiere 0,2 en el cuadro 2 y la diferencia crece suave hasta ~2,5; contra el último
# cuadro baja suave hasta 0,34 en el penúltimo). Posando quieto, el tramo útil es el clip entero, y la junta la elige
# la búsqueda de pares con el peso de la cara, en las ventanas de la cola y la cabeza (30 cuadros).
for _p in ("matias", "sebastian"):
    ZONA_CARA[f"{_p}-stand"] = ZONA_CARA[_p]; ZONA_OJOS[f"{_p}-stand"] = ZONA_OJOS[_p]
    ZONA_PELO[f"{_p}-stand"] = (0.15, 0.15, 0.85, 1.0)
TAMANO = {"stand": (480, 600)}   # por defecto 720×900; stand va chico (200–260 CSS px de alto) en la primera pantalla, ≤ 1 MB por clip
# Codificación (H.264 crf, VP9 crf, extras x264, extras vp9). Barrido del 31/10 sobre el loop stand de Sebastián (215 cuadros,
# 480×600): a crf 24 el mp4 pesa 135 KB pero cada cuadro queda a 0,90 del PNG (ruido de cuantización en la viñeta y la cara);
# crf 22 + aq-mode=3 (más bits a lo oscuro) baja a 0,79 por 216 KB; crf 18, a 0,67 por 457 KB. VP9 crf 24 + aq-mode 2: 0,78
# por 163 KB. Con ≤ 1 MB de tope por archivo, el medio es el punto: la nitidez a 240 px de alto no cambia entre 22 y 18.
CRF = {"stand": (22, 24)}        # por defecto (24, 34)
# Un solo keyframe por loop: libvpx-vp9 mete uno cada 128 cuadros por defecto (medido: cuadro 128 del webm de Sebastián) y
# x264 cada 250; cada keyframe adentro del loop es un «pop» de grano como el del cierre. `-g 999` > cualquier loop.
EXTRA_X264 = {"stand": ["-g", "999", "-x264-params", "aq-mode=3"]}
EXTRA_VP9 = {"stand": ["-g", "999", "-aq-mode", "2"]}

def _familia(persona):
    return ("stand", persona[:-6]) if persona.endswith("-stand") else (None, persona)

def _salida(persona):
    fam, nombre = _familia(persona)
    return ASSETS / (f"retrato-{fam}-{nombre}" if fam else f"retrato-{nombre}")

def duracion(clip):
    out = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(clip)],
                         capture_output=True, text=True, check=True).stdout.strip()
    return float(out)

def _extraer(clip, td, nombre, tam=(720, 900)):
    w, h = tam
    subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-i", str(clip), "-vf",
                    f"scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h},setsar=1,fps=24",
                    f"{td}/{nombre}-%04d.png"], check=True)
    import glob
    return sorted(glob.glob(f"{td}/{nombre}-*.png"))

def _tramo_movil(chicos, zona):
    from PIL import ImageChops, ImageStat
    w, h = chicos[0].size
    b = (int(zona[0] * w), int(zona[1] * h), int(zona[2] * w), int(zona[3] * h))
    pel = [f.crop(b) for f in chicos]
    d = [ImageStat.Stat(ImageChops.difference(a, bb)).mean[0] for a, bb in zip(pel, pel[1:])]
    a = next((i for i in range(len(d) - 3) if all(x >= 1.0 for x in d[i:i + 3])), 0)
    z = next((i + 1 for i in range(len(d) - 1, 2, -1) if all(x >= 1.0 for x in d[i - 2:i + 1])), len(chicos) - 1)
    return a, z, d

def _dif(a, b, cara=None):
    from PIL import ImageChops, ImageStat
    d = ImageStat.Stat(ImageChops.difference(a, b)).mean[0]
    if cara:
        d += PESO_CARA * ImageStat.Stat(ImageChops.difference(a.crop(cara), b.crop(cara))).mean[0]
    return d

# La boca, para que el cuadro 0 (= póster) tampoco caiga en plena sonrisa: la mediana por píxel de ojos + boca es la
# expresión de casi todo el tiempo (ojos abiertos, boca en reposo) y el cuadro 0 es el que menos se aparta de ella en ±12.
ZONA_BOCA = {"matias": (0.40, 0.49, 0.62, 0.58), "sebastian": (0.38, 0.46, 0.64, 0.56)}
for _p in ("matias", "sebastian"):
    ZONA_BOCA[f"{_p}-stand"] = ZONA_BOCA[_p]

def _cuadro_quieto(cuadros, zona_ojos, radio=12, zona_boca=None, centro=None, ancho=72):
    """Índice del cuadro cuyo entorno (±radio) tiene la menor desviación máxima de los ojos (y la boca, si se pasa) contra
    su mediana por píxel: lejos de cualquier pestañeo o sonrisa, con la cara como está casi todo el tiempo."""
    from PIL import Image, ImageChops, ImageStat
    w, h = cuadros[0].size
    z = (int(zona_ojos[0] * w), int(zona_ojos[1] * h), int(zona_ojos[2] * w), int(zona_ojos[3] * h))
    if zona_boca:   # ojos y boca, una sobre otra, en una sola imagen chica
        zb = (int(zona_boca[0] * w), int(zona_boca[1] * h), int(zona_boca[2] * w), int(zona_boca[3] * h))
        def juntar(im):
            g = im.convert("L"); u = Image.new("L", (60, 40))
            u.paste(g.crop(z).resize((60, 20), Image.BILINEAR), (0, 0)); u.paste(g.crop(zb).resize((60, 20), Image.BILINEAR), (0, 20))
            return u
        ojos = [juntar(im) for im in cuadros]
    else:
        ojos = [im.convert("L").crop(z).resize((60, 20), Image.BILINEAR) for im in cuadros]
    px = [o.load() for o in ojos]; ref = Image.new("L", ojos[0].size); rp = ref.load()
    for y in range(ojos[0].height):
        for x in range(ojos[0].width):
            v = sorted(p[x, y] for p in px); rp[x, y] = v[len(v) // 2]
    dev = [ImageStat.Stat(ImageChops.difference(o, ref)).mean[0] for o in ojos]
    n = len(dev)
    peor = [max(dev[(i + k) % n] for k in range(-radio, radio + 1)) for i in range(n)]
    candidatos = range(n) if centro is None else [(centro + t) % n for t in range(-ancho, ancho + 1)]   # ±3 s del centro
    return min(candidatos, key=lambda i: (peor[i], dev[i]))

def _rotar_sonrisa(cuadros, R0, segundos, zona_ojos, zona_boca, radio=12):
    """Devuelve (R, ini, fin): R rota el loop para que la sonrisa arranque en `segundos`, ajustado al cuadro quieto más
    cercano; ini/fin son la sonrisa medida (índices en el loop sin rotar, con el cuadro R0 como boca en reposo)."""
    from PIL import ImageChops, ImageStat
    n = len(cuadros); w, h = cuadros[0].size
    zb = (int(zona_boca[0] * w), int(zona_boca[1] * h), int(zona_boca[2] * w), int(zona_boca[3] * h))
    zo = (int(zona_ojos[0] * w), int(zona_ojos[1] * h), int(zona_ojos[2] * w), int(zona_ojos[3] * h))
    g = [im.convert("L") for im in cuadros]
    d = lambda a, b, z: ImageStat.Stat(ImageChops.difference(a.crop(z), b.crop(z))).mean[0]
    boca = [d(x, g[R0], zb) for x in g]; pico = max(boca) or 1
    alto = [v / pico > 0.35 for v in boca]
    # la sonrisa más larga (tramo circular de cuadros altos)
    mejor = None; i = 0
    while i < n:
        if alto[i]:
            j = i
            while alto[j % n] and j - i < n: j += 1
            if mejor is None or j - i > mejor[1] - mejor[0]: mejor = (i, j)
            i = j
        else: i += 1
    ini, fin = mejor if mejor else (R0, R0)
    R = (ini - round(segundos * 24)) % n
    # el cuadro quieto (ojos y boca en reposo, sin pestañeo en ±radio) más cercano a R, dentro de ±3 s
    return _cuadro_quieto(cuadros, zona_ojos, radio, zona_boca, centro=R), ini, fin

def post(persona, clips, fundido=6, ventana=30):
    """clips: uno o más mp4 de la misma persona (y del mismo modelo, para que no cambie el color). Salida:
    assets/retrato-<persona>.mp4 (H.264 yuv420p, sin audio, faststart) y .webm (VP9), 720×900, 24 fps.
    Familia stand (`<persona>-stand`): assets/retrato-stand-<persona>.{mp4,webm} a TAMANO['stand'] y además el
    póster assets/retrato-stand-<persona>.jpg, que es EXACTAMENTE el cuadro 0 del loop (JPG progresivo q84)."""
    import tempfile
    from PIL import Image
    F = int(fundido)
    fam, _ = _familia(persona)
    tam, (crf_h264, crf_vp9) = TAMANO.get(fam, (720, 900)), CRF.get(fam, (24, 34))
    with tempfile.TemporaryDirectory() as td:
        rutas = [_extraer(c, td, f"c{k}", tam) for k, c in enumerate(clips)]
        chicos = [[Image.open(r).convert("L").resize((240, 300), Image.BILINEAR) for r in rs] for rs in rutas]
        tramos = []
        for k, ch in enumerate(chicos):
            if fam == "stand":   # posando quieto no hay tramo congelado que recortar: el clip entero
                a, z = 0, len(ch) - 1
                # RECORTE="k:a-b[,k:a-b]" limita el clip k a los cuadros [a, b] (tercera vuelta: para igualar el largo de los
                # dos loops se acorta un clip neutro; la junta se busca en la cola nueva y el fundido hace el resto)
                for r in filter(None, os.environ.get("RECORTE", "").split(",")):
                    kk, ab = r.split(":"); 
                    if int(kk) == k: a, z = (int(x) for x in ab.split("-"))
                print(f"  {pathlib.Path(clips[k]).name}: {len(ch)} cuadros, " + ("entero" if (a, z) == (0, len(ch) - 1) else f"recortado a {a}–{z}") + f" ({(z - a + 1) / 24:.2f} s)")
            else:
                a, z, _ = _tramo_movil(ch, ZONA_PELO[persona])
                print(f"  {pathlib.Path(clips[k]).name}: {len(ch)} cuadros, pelo en movimiento del {a} al {z} ({(z - a) / 24:.2f} s)")
            tramos.append([a, z])
        n = len(clips)
        w, h = chicos[0][0].size; zc = ZONA_CARA[persona]
        cara = (int(zc[0] * w), int(zc[1] * h), int(zc[2] * w), int(zc[3] * h))
        # un corte por junta k→k+1 (la última junta cierra el loop con el primero): el par (i, j) más parecido
        cortes = []
        for k in range(n):
            k2 = (k + 1) % n
            a, z = tramos[k]; a2, z2 = tramos[k2]
            mejor = None
            # la cola puede entrar unos cuadros en la zona quieta (el pelo frena, la cara vuelve a la pose) y la cabeza
            # arrancar unos cuadros antes del movimiento: ahí las dos caras del fundido son casi la misma foto
            # (el fundido necesita F/2 cuadros a cada lado del corte: en la familia stand la cola y la cabeza llegan al borde)
            for i in range(max(z - ventana, a + 24), min(z + 12, len(chicos[k]) - 1 - F // 2) + 1):
                for j in range(max(a2 - 8, F // 2), min(a2 + ventana, len(chicos[k2]) - 1) + 1):
                    if k == k2 and j + 24 > i: continue
                    v = _dif(chicos[k][i], chicos[k2][j], cara)
                    if mejor is None or v < mejor[0]: mejor = (v, i, j)
            cortes.append(mejor)
            print(f"  junta {k}→{k2}: cuadro {mejor[1]} → {mejor[2]} (dif ponderada {mejor[0]:.1f}, "
                  f"cara {_dif(chicos[k][mejor[1]].crop(cara), chicos[k2][mejor[2]].crop(cara)):.1f})")
        # cada tramo k va desde la cabeza que le dejó la junta k-1 hasta la cola que le pide la junta k
        salida = []
        for k in range(n):
            _, i_fin, _ = cortes[k]
            _, _, j_ini = cortes[(k - 1) % n]
            s0, e0 = j_ini - F // 2, i_fin + F // 2
            cuerpo = [Image.open(r).convert("RGB") for r in rutas[k][s0:e0 + 1]]
            salida.append(cuerpo)
        # fundidos: los últimos F cuadros de cada tramo se funden con los primeros F del siguiente. Los F primeros
        # cuadros de CADA tramo (también del 0) viven sólo dentro del fundido que los precede, que para el tramo 0
        # es el último del loop: así, al reiniciar, el cuadro que sigue al fundido final es cuerpo0[F], sin salto.
        final = []; centros = []
        for k in range(n):
            cuerpo = salida[k]; sig = salida[(k + 1) % n]
            final.extend(cuerpo[F:-F])
            centros.append(len(final) + F // 2)
            for t in range(F):
                al = (t + 1) / (F + 1)
                final.append(Image.blend(cuerpo[-F + t], sig[t], al))
        if fam == "stand":
            # El cuadro 0 es el póster, así que no puede caer en un pestañeo ni al lado de uno. Como es un loop, se rota:
            # el cuadro 0 pasa a ser el centro del segundo más quieto en la zona de los ojos (la menor desviación máxima
            # contra la mediana por píxel en ±12 cuadros), los fundidos quedan adentro y el cierre es un paso cualquiera.
            R = _cuadro_quieto(final, ZONA_OJOS[persona], zona_boca=ZONA_BOCA[persona])
            # SONRISA_EN=<segundos> (tercera vuelta): para que los dos loops no sonrían a la vez, el cuadro 0 se corre para
            # que la sonrisa (la boca lejos de la del cuadro quieto, > 35 % del pico) arranque en ese segundo; el cuadro 0
            # resultante se ajusta al cuadro quieto más cercano (ojos y boca en reposo) para que el póster siga neutro.
            if os.environ.get("SONRISA_EN"):
                R, ini, fin = _rotar_sonrisa(final, R, float(os.environ["SONRISA_EN"]), ZONA_OJOS[persona], ZONA_BOCA[persona])
                print(f"  SONRISA_EN={os.environ['SONRISA_EN']}: la sonrisa medida iba de {ini / 24:.2f} a {fin / 24:.2f} s; cuadro 0 → {R}")
            R = (R + int(os.environ.get("ROTAR_EXTRA", 0))) % len(final)   # ajuste fino a mano, en cuadros, si hace falta
            final = final[R:] + final[:R]
            centros = sorted((c - R) % len(final) for c in centros)
            print(f"  rotado {R} cuadros: el cuadro 0 es el más quieto con los ojos abiertos y la boca en reposo; fundidos en "
                  + ", ".join(f"{c / 24:.2f} s" for c in centros))
            if not os.environ.get("SIN_VINETA"):   # la misma viñeta en todos los cuadros (y en el póster)
                final = [vinetear(im) for im in final]
        (OUT / "final").mkdir(exist_ok=True)
        for k, c in enumerate(centros):   # el cuadro del centro de cada fundido, para mirarlo
            final[c].save(OUT / "final" / f"{persona}-junta-{k + 1}.png")
        for q, im in enumerate(final):
            im.save(f"{td}/o-{q:04d}.png")
        if os.environ.get("GUARDAR_CUADROS"):   # los PNG del loop, para probar codificaciones sin rearmar
            import shutil
            cu = OUT / "final" / f"{persona}-cuadros"; shutil.rmtree(cu, ignore_errors=True); shutil.copytree(td, cu, ignore=shutil.ignore_patterns("c*"))
        print(f"  loop: {len(final)} cuadros = {len(final) / 24:.2f} s · centros de fundido en "
              + ", ".join(f"{c / 24:.2f} s" for c in centros) + f" (cuadros guardados en {OUT / 'final'})")
        dest = _salida(persona)
        if fam == "stand":   # el póster es el cuadro 0 del loop, el mismo PNG que entra al encoder
            final[0].save(f"{dest}.jpg", "JPEG", quality=84, progressive=True, optimize=True)
            final[0].save(OUT / "final" / f"{persona}-cuadro-0.png")
        ent = ["-hide_banner", "-loglevel", "error", "-y", "-framerate", "24", "-i", f"{td}/o-%04d.png", "-an"]
        subprocess.run([FFMPEG, *ent, "-c:v", "libx264", "-preset", "slow", "-crf", str(crf_h264), "-pix_fmt", "yuv420p",
                        "-movflags", "+faststart", "-tune", "film", *EXTRA_X264.get(fam, []), f"{dest}.mp4"], check=True)
        subprocess.run([FFMPEG, *ent, "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", str(crf_vp9), "-row-mt", "1", "-deadline", "good",
                        "-cpu-used", "1", "-pix_fmt", "yuv420p", *EXTRA_VP9.get(fam, []), f"{dest}.webm"], check=True)
    for ext in (("jpg", "mp4", "webm") if fam == "stand" else ("mp4", "webm")):
        pth = pathlib.Path(f"{dest}.{ext}")
        print(f"{pth.name}: {pth.stat().st_size / 1024:.0f} KB" + ("" if ext == "jpg" else f", {duracion(pth):.2f} s"))


# ── lento: re-temporizar SÓLO un tramo de un clip (la sonrisa) con interpolación de movimiento ──────
# Plan B de la tercera vuelta, si Kling no hace la sonrisa lenta ni a 10 s: el tramo [a, b) del clip se estira ×factor con
# `minterpolate` (mci + aobmc + bidir: cuadros intermedios por compensación de movimiento, no duplicados) y el resto queda a
# velocidad natural. Sale un mp4 casi sin pérdida (crf 10) que entra a `post` como un clip más. Los pestañeos que caigan
# dentro del tramo se ralentizan también: elegir [a, b) sin pestañeos (`costura` los lista) o aceptar uno más lento.
# Revisar cuadro a cuadro (tira a 12 fps de la boca y los ojos): minterpolate puede dejar un labio doble o un párpado fantasma.
def lento(clip, salida, factor, *tramos):
    """tramos: pares a b (cuadros, [a, b)) en orden creciente; cada uno se estira ×factor. Los tramos no deben contener pestañeos."""
    clip = pathlib.Path(clip); factor = float(factor); cortes = [int(x) for x in tramos]
    assert len(cortes) % 2 == 0 and cortes == sorted(cortes), "tramos: pares a b crecientes"
    n = int(subprocess.run([FFPROBE, "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries", "stream=nb_read_frames",
                            "-of", "csv=p=0", str(clip)], capture_output=True, text=True, check=True).stdout.strip())
    bordes = [0] + cortes + [n]           # segmentos alternados: normal, lento, normal, lento, …, normal
    partes = []; etiquetas = []
    for k, (a, b) in enumerate(zip(bordes, bordes[1:])):
        if b <= a: continue
        et = f"s{k}"; etiquetas.append(et)
        if k % 2 == 1:
            partes.append(f"[0:v]trim=start_frame={a}:end_frame={b},setpts=(PTS-STARTPTS)*{factor},"
                          f"minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1[{et}]")
        else:
            partes.append(f"[0:v]trim=start_frame={a}:end_frame={b},setpts=PTS-STARTPTS[{et}]")
    fc = ";".join(partes) + ";" + "".join(f"[{e}]" for e in etiquetas) + f"concat=n={len(etiquetas)}:v=1:a=0[v]"
    subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-i", str(clip), "-filter_complex", fc, "-map", "[v]",
                    "-r", "24", "-c:v", "libx264", "-preset", "slow", "-crf", "10", "-pix_fmt", "yuv420p", str(salida)], check=True)
    extra = sum((b - a) * (factor - 1) for a, b in zip(cortes[::2], cortes[1::2]))
    print(f"{salida}: " + ", ".join(f"{a}–{b} ({(b - a) / 24:.2f} s → {(b - a) * factor / 24:.2f} s)" for a, b in zip(cortes[::2], cortes[1::2]))
          + f" ×{factor} · clip {n} → ≈{n + extra:.0f} cuadros")


# ── costura: ¿empalma el loop? ¿pestañea en el corte? ¿salta del póster al cuadro 0? ─────────────────
def costura(persona, clip=None):
    """Mide el clip final (o el que se pase) a 240×300 en gris: el paso medio entre cuadros consecutivos (total, zona del
    pelo, zona de la cara) y, contra eso, la diferencia último ↔ primero —si es menor o parecida, la costura no se ve—;
    los tramos con los ojos lejos de la mediana por píxel (los pestañeos marcados —los suaves, y los que caen bajo un
    fundido, no llegan al umbral: para esos, mirar la tira— y si uno cruza el corte); y la diferencia del
    póster (assets/retrato-<persona>.jpg) contra el cuadro 0 —si en el pelo es menor que el paso, el arranque no salta."""
    import tempfile, glob
    from PIL import Image, ImageChops, ImageStat
    clip = pathlib.Path(clip) if clip else pathlib.Path(f"{_salida(persona)}.mp4")
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-i", str(clip), "-vf", "scale=240:300",
                        "-fps_mode", "passthrough", f"{td}/f%04d.png"], check=True)
        fr = [Image.open(f).convert("L") for f in sorted(glob.glob(f"{td}/f*.png"))]
    w, h = fr[0].size
    box = lambda z: (int(z[0] * w), int(z[1] * h), int(z[2] * w), int(z[3] * h))
    zp, zc, zo = box(ZONA_PELO[persona]), box(ZONA_CARA[persona]), box(ZONA_OJOS[persona])
    d = lambda a, b, z=None: ImageStat.Stat(ImageChops.difference(a.crop(z) if z else a, b.crop(z) if z else b)).mean[0]
    media = lambda xs: sum(xs) / len(xs)
    ct, cp, cc = ([d(a, b, z) for a, b in zip(fr, fr[1:])] for z in (None, zp, zc))
    print(f"{clip.name}: {len(fr)} cuadros = {len(fr) / 24:.2f} s")
    zona = "persona" if _familia(persona)[0] == "stand" else "pelo"   # en la familia stand la zona móvil es la persona entera
    print(f"  paso entre cuadros consecutivos · total {media(ct):.2f} (máx {max(ct):.2f}) · {zona} {media(cp):.2f} (máx {max(cp):.2f})"
          f" · cara {media(cc):.2f} (máx {max(cc):.2f})")
    print(f"  último ↔ primero                · total {d(fr[-1], fr[0]):.2f} · {zona} {d(fr[-1], fr[0], zp):.2f} · cara {d(fr[-1], fr[0], zc):.2f}")
    ojos = [f.crop(zo) for f in fr]; px = [o.load() for o in ojos]; bw, bh = ojos[0].size
    ref = Image.new("L", (bw, bh)); rp = ref.load()      # mediana por píxel: los ojos están abiertos casi todo el tiempo
    for y in range(bh):
        for x in range(bw):
            v = sorted(p[x, y] for p in px); rp[x, y] = v[len(v) // 2]
    do = [d(o, ref) for o in ojos]; umbral = 2 * sorted(do)[len(do) // 2]
    tramos, cur = [], None
    for i, v in enumerate(do):
        if v > umbral: cur = [i, i] if cur is None else [cur[0], i]
        elif cur: tramos.append(tuple(cur)); cur = None
    if cur: tramos.append(tuple(cur))
    cruza = bool(tramos) and (tramos[0][0] == 0 or tramos[-1][1] == len(fr) - 1)
    print("  pestañeos (ojos lejos de la mediana): " + (", ".join(f"{a}–{b} ({a / 24:.2f} s)" for a, b in tramos) or "ninguno")
          + (" · uno cruza el corte" if cruza else ""))
    if persona in ZONA_BOCA:
        # Sonrisas: la boca lejos de la del cuadro 0 (que en el loop es neutro por la rotación, y en un clip crudo es la foto),
        # normalizada al pico; una sonrisa es un tramo ≥ 0,5 s por encima del 35 % del pico. (Con la mediana no sirve: en un
        # clip de 10 s la sonrisa ocupa más de la mitad y la mediana ES la sonrisa.) Se imprime también cuánto tarda en subir
        # del 20 % al 80 % del pico y en bajar del 80 % al 20 %: eso es lo que se percibe como «lenta» o «rápida».
        zb = box(ZONA_BOCA[persona]); bocas = [f.crop(zb) for f in fr]
        db = [d(o, bocas[0]) for o in bocas]; pico = max(db) or 1; niv = [v / pico for v in db]
        son, cur = [], None
        for i, v in enumerate(niv):
            if v > 0.35: cur = [i, i] if cur is None else [cur[0], i]
            elif cur: son.append(tuple(cur)); cur = None
        if cur: son.append(tuple(cur))
        son = [t for t in son if t[1] - t[0] >= 12]
        det = []
        for a, b in son:
            sube = next((i for i in range(a, b + 1) if niv[i] >= 0.8), b) - next((i for i in range(max(a - 24, 0), b + 1) if niv[i] >= 0.2), a)
            baja = next((i for i in range(b, min(b + 24, len(niv) - 1) + 1) if niv[i] <= 0.2), b) - next((i for i in range(b, a, -1) if niv[i] >= 0.8), b)
            det.append(f"{a / 24:.1f}–{b / 24:.1f} s ({(b - a) / 24:.1f} s; sube en {sube / 24:.1f} s, baja en {baja / 24:.1f} s)")
        print("  sonrisas (boca > 35 % del pico, ≥ 0,5 s): " + (", ".join(det) or "ninguna"))
    poster = pathlib.Path(f"{_salida(persona)}.jpg")
    if poster.exists():
        p = Image.open(poster).convert("L").resize((w, h), Image.LANCZOS)
        print(f"  póster ↔ cuadro 0               · total {d(p, fr[0]):.2f} · {zona} {d(p, fr[0], zp):.2f} · cara {d(p, fr[0], zc):.2f}")


# ── igualar el eclipse en post (PIL) ──────────────────────────────────────────────────────────────
# nano-banana no agranda el eclipse por texto (3 de 3 el 10/10, 7 de 7 hoy). Como alrededor del eclipse hay pared lisa,
# se puede escalar EN SU LUGAR el parche del eclipse de la variante elegida hasta el radio de corona medido en la
# imagen de referencia, con una máscara radial suave. Es una operación de post, no una generación.
def perfil_radial(im, cx, cy, rmax=150):
    L = im.convert("L").load()
    acc = [0.0] * rmax; cnt = [0] * rmax
    for y in range(cy - rmax, cy + rmax):
        for x in range(cx - rmax, cx + rmax):
            r = int(((x - cx) ** 2 + (y - cy) ** 2) ** 0.5)
            if r < rmax: acc[r] += L[x, y]; cnt[r] += 1
    return [a / c if c else 0 for a, c in zip(acc, cnt)]

def centro_corona(im, cx, cy, R=90):
    """Afina el centro con el centroide de los píxeles dorados en un radio R."""
    px = im.convert("RGB").load(); xs = []; ys = []
    for y in range(cy - R, cy + R):
        for x in range(cx - R, cx + R):
            r, g, b = px[x, y]
            if r > 90 and g > 55 and b < 80 and r - b > 60 and (x - cx) ** 2 + (y - cy) ** 2 < R * R: xs.append(x); ys.append(y)
    return round(sum(xs) / len(xs)), round(sum(ys) / len(ys))

def radio_corona(im, cx, cy):
    perf = perfil_radial(im, cx, cy)
    return max(range(6, len(perf)), key=lambda r: perf[r])

def igualar_eclipse(origen, referencia, salida, cx, cy, rcx, rcy, cy_nuevo=None):
    from PIL import Image, ImageDraw, ImageFilter
    im = Image.open(origen).convert("RGB"); ref = Image.open(referencia).convert("RGB")
    cx, cy = centro_corona(im, cx, cy); rcx, rcy = centro_corona(ref, rcx, rcy)
    r0, r1 = radio_corona(im, cx, cy), radio_corona(ref, rcx, rcy)
    f = r1 / r0
    print(f"origen: centro {(cx, cy)} radio corona {r0} px · referencia: centro {(rcx, rcy)} radio {r1} px · factor {f:.2f}")
    half = int(r0 * 2.6)                       # el parche incluye el halo
    parche = im.crop((cx - half, cy - half, cx + half, cy + half))
    nh = int(half * f)
    parche = parche.resize((2 * nh, 2 * nh), Image.LANCZOS)
    masc = Image.new("L", parche.size, 0)
    ImageDraw.Draw(masc).ellipse((nh * 0.12, nh * 0.12, 2 * nh - nh * 0.12, 2 * nh - nh * 0.12), fill=255)
    masc = masc.filter(ImageFilter.GaussianBlur(nh * 0.14))
    # primero se tapa el eclipse chico con pared limpia (un parche de pared de al lado), después se pega el grande
    pared = im.crop((cx - half - 2 * half, cy - half, cx - half, cy + half)).transpose(Image.FLIP_LEFT_RIGHT)
    mp = Image.new("L", pared.size, 0); ImageDraw.Draw(mp).ellipse((half * 0.1, half * 0.1, 2 * half - half * 0.1, 2 * half - half * 0.1), fill=255)
    mp = mp.filter(ImageFilter.GaussianBlur(half * 0.14))
    im.paste(pared, (cx - half, cy - half), mp)
    ncy = cy_nuevo if cy_nuevo is not None else cy
    im.paste(parche, (cx - nh, ncy - nh), masc)
    im.save(salida, "JPEG", quality=95)
    print(salida, "centro nuevo", (cx, ncy), "radio nuevo ≈", round(r0 * f))

# ── exportar / lado a lado ─────────────────────────────────────────────────────────────────────────
def exportar(origen, destino):
    from PIL import Image
    im = Image.open(origen).convert("RGB")
    w, h = im.size
    r = 4 / 5
    if w / h > r:
        nw = round(h * r); x0 = (w - nw) // 2; im = im.crop((x0, 0, x0 + nw, h))
    elif w / h < r:
        nh = round(w / r); y0 = (h - nh) // 2; im = im.crop((0, y0, w, y0 + nh))
    im.resize((720, 900), Image.LANCZOS).save(destino, "JPEG", quality=84, progressive=True, optimize=True)
    print(destino)

def ladoalado(salida, *imgs, alto=600):
    from PIL import Image
    ims = [Image.open(p).convert("RGB") for p in imgs]
    ims = [im.resize((round(im.width * alto / im.height), alto), Image.LANCZOS) for im in ims]
    lienzo = Image.new("RGB", (sum(im.width for im in ims) + 8 * (len(ims) - 1), alto), (20, 20, 20))
    x = 0
    for im in ims:
        lienzo.paste(im, (x, 0)); x += im.width + 8
    lienzo.save(salida)
    print(salida)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    if a[0] == "fondo":
        fondo(a[1], int(a[2]) if len(a) > 2 else 3)
    elif a[0] == "fondo-ref":
        fondo(a[1], int(a[3]) if len(a) > 3 else 3, referencia=a[2])
    elif a[0] == "fondo-stand":   # fondo-stand <sebastian|matias> [n=3]
        fondo_stand(a[1], int(a[2]) if len(a) > 2 else 3)
    elif a[0] == "fondo-stand-plano":   # la alternativa del primer brief (fondo liso); no se usa
        fondo_stand(a[1], int(a[2]) if len(a) > 2 else 3, plano=True)
    elif a[0] == "medir-stand":   # medir-stand <sobrio-original.jpg> <variante.jpg> [...]
        medir_stand(a[1], *a[2:])
    elif a[0] == "vinetear":   # vinetear <origen.jpg> <destino.jpg> [ancho alto]: para mirar la viñeta antes del post
        vinetear_archivo(a[1], a[2], (int(a[3]), int(a[4])) if len(a) > 4 else None)
    elif a[0] == "video":
        video(a[1], a[2], int(a[3]) if len(a) > 3 else 1, a[4] if len(a) > 4 else None,
              os.environ.get("RESOLUCION", "720p"))
    elif a[0] == "medir":
        for c in a[1:]:
            medir(c)
    elif a[0] == "medir-fondo":   # medir-fondo <clip.mp4> [...]: el stand no tiene eclipse; las cajas son dos parches de cielo
        for c in a[1:]:
            medir(c, caja_eclipse=(0.0, 0.0, 0.2, 0.12), caja_fondo=(0.84, 0.3, 1.0, 0.6))
    elif a[0] == "tira":
        for c in a[1:]:
            tira(c)
    elif a[0] == "post":   # post <persona> <clip.mp4> [clip2.mp4 ...]   (FUNDIDO=6 cuadros por defecto)
        post(a[1], a[2:], int(os.environ.get("FUNDIDO", 6)))
    elif a[0] == "lento":   # lento <clip.mp4> <salida.mp4> <factor> a b [a2 b2 ...]
        lento(a[1], a[2], a[3], *a[4:])
    elif a[0] == "costura":   # costura <persona> [clip.mp4]
        costura(a[1], a[2] if len(a) > 2 else None)
    elif a[0] == "igualar-eclipse":   # origen referencia salida cx cy rcx rcy [cy_nuevo]
        igualar_eclipse(a[1], a[2], a[3], *map(int, a[4:8]), cy_nuevo=int(a[8]) if len(a) > 8 else None)
    elif a[0] == "exportar":
        exportar(a[1], a[2])
    elif a[0] == "ladoalado":
        ladoalado(a[1], *a[2:])
    else:
        raise SystemExit(__doc__)
