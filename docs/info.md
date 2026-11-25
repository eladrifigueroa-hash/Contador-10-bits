<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

El proyecto es un contador decimal síncrono de 0 a 9. Usa un registro de 4 bits (`count`) que se incrementa en cada flanco de subida de `clk`. Cuando el valor llega a 9, el siguiente flanco lo regresa a 0, por lo que la secuencia es 0, 1, 2, ..., 9, 0, 1, ...

El reinicio es síncrono y activo en bajo: mientras `rst_n` esté en 0, el contador se pone en 0 en el siguiente flanco de reloj.

El valor actual se muestra en binario en los 4 bits bajos de la salida (`uo[3:0]`). Los bits `uo[7:4]` siempre valen 0. Las entradas `ui_in` y `uio_in` no se usan, y los pines bidireccionales están configurados como entradas.

## How to test

1. Aplica una señal de reloj a `clk`.
2. Mantén `rst_n` en bajo durante al menos un ciclo de reloj y luego súbelo a alto. La salida `uo[3:0]` debe quedar en 0000.
3. En cada flanco de subida de `clk`, la salida debe avanzar: 0000, 0001, 0010, ..., 1001 (9) y luego volver a 0000.
4. Para reiniciar en cualquier momento, baja `rst_n` durante un ciclo de reloj.

## External hardware

No se requiere hardware externo. Opcionalmente se pueden conectar 4 LEDs (con resistencias limitadoras) a `uo[3:0]` para ver el conteo en binario.
