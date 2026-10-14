# Idea a futuro — el discurso de la Metaestructura

> Guardada el 2026-10-14 a pedido de Matías («guardemos el discurso de Trump como una idea a futuro»).
> Estuvo publicada en el hero de la v5 entre el 13 y el 14 de octubre de 2026 (commits `8e7519c` → `74d8603`)
> y salió cuando el hero volvió a ser el eclipse, el logo y la máquina. Los prompts verbatim que la originaron
> están en `docs/prompts-usuario/REGISTRO-2026-10.md` (13/10).

## La pieza

Un parlamento de político grandilocuente que presenta algo enorme que no termina de entender. El chiste es
el género, no la persona: el mandatario que vende, con superlativos, la tecnología de un laboratorio de
Rosario que no sabe pronunciar.

### Versión en castellano (la que estuvo en el hero, con el titular «Metaestructura»)

> Miren, tenemos gente increíble trabajando en esto. Los mejores ingenieros, tipos verdaderamente brillantes,
> de los que nadie había oído hablar antes, pero son genios absolutos. Y me dijeron: ‘Señor Presidente,
> tenemos algo tan grande, tan revolucionario, que va a cambiar el juego para siempre’.
>
> Le llamamos Metaestructura. Suena bien, ¿verdad? Metaestructura. Suena fuerte. No es una de esas ideas
> débiles y ridículas de la vieja política que cuestan trillones y no sirven para nada. Esto es real. Es
> hormigón, es acero, es tecnología digital de última generación, y está hecha en RIA Labs.

(La primera versión decía «Superestructura»; el 13/10 Matías la cambió por «Metaestructura».)

### Versión en inglés, ampliada (la que escribió Matías para un video, 13/10)

> "Look, we have incredible people working on this. The best engineers, truly brilliant guys—guys nobody had
> ever heard of before, but they are absolute geniuses. And they told me, 'Mr. President, we have something so
> big, so revolutionary, that it's going to change the game forever... We call it Superstructure... It's made
> in the laboratories of a company in Argentina called RIA Labs.. am I pronouncing it right? RIA.. RIA Labs..
> I have no idea, but what matters is they make it there, and it's for everybody..... Super-Structure......
> Sounds good, right? Superstructure. Sounds tough. It's not one of those weak, ridiculous ideas from the old
> political establishment that cost trillions and do nothing. This is real. It's not concrete, it's not
> steel, it's the next-generation digital technology, it's working now, and we have to use it... you know...
> you need it, because at the first moment you look at it you can't stop looking at it, it's beautiful...
> it's the light machine."

Si vuelve, la palabra se alinea con la home: *Metastructure* / *Metaestructura*. Y «the light machine» engancha
con la máquina que hoy está debajo del logo.

## Cómo se puede producir (y cómo no)

- **No:** video o voz hiperrealistas de Donald Trump (ni de ninguna persona real) diciendo el texto. Es un
  deepfake con respaldo comercial falso: riesgo de derecho a la imagen y de marca, y los servicios serios
  (Veo, Kling, Runway, HeyGen, Synthesia, ElevenLabs) lo prohíben y lo filtran.
- **Sí, en orden de preferencia:**
  1. **Un presidente ficticio en video con voz** (Veo 3.1 genera diálogo hablado): atril, bandera y sello
     genéricos, el tono y las pausas del género; seis o siete tomas de ~8 s cortadas como conferencia, con algún
     plano de la prensa y uno de pantalla con el eclipse. Estimado US$ 5–15 con repeticiones.
  2. **Versión animada** en el lenguaje gráfico de la casa, con una voz sintética de «orador político» diseñada
     desde cero.
  3. **Un actor imitador** con contrato, filmado.
  En cualquier caso, presentada como lo que es: una nota chica en mono («discurso de ficción»).

## Lo que ya estaba construido (recuperable desde git)

- Titular en **M PLUS Rounded 1c 800** (la tipografía que titula la onda de Dataflow), sentence case.
- La cita como `blockquote` de dos párrafos con una comilla de apertura grande, dorada, colgando a la izquierda.
- Audio al posar el mouse: `<audio preload="none">` con `assets/metaestructura.mp3` (+ `.ogg`); un `HEAD` al
  cargar decide si se activa; botón «escuchar ▶» para touch y para antes del primer clic (política de
  autoplay); script «LA FRASE HABLADA». Todo en `git show 74d8603:v5/index.html`.
