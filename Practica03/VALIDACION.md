# Validación de Práctica 03

## Explorador de cuadros ampliables

- Archivo: `artifacts/canvas-final.html`, generado desde `contenido-canvas.json` y `scripts/canvas.template.html` mediante `scripts/build-canvas.py`.
- Esta vista es una extensión HTML complementaria al mapa Archify; no se le atribuyen los controles ni los recibos del generador de Archify.
- Pruebas en Chrome: apertura de los nueve cuadros, contenido, cierre con retorno del foco, Enter, Escape, navegación anterior/siguiente y bloques relacionados.
- Sin desbordamiento de la portada en 1440×900, 1600×1000, 1920×1080 y 2048×1320. A 390×844 se permite desplazamiento vertical, sin desbordamiento horizontal; lo mismo se comprobó en el detalle móvil.
- Impresión: los nueve bloques se incluyen en la estructura imprimible, con fuentes e indicadores.
- Revisión visual: portada clara y panel ampliado oscuro inspeccionados. Los detalles largos permiten desplazamiento dentro del diálogo.
- [Recibo de interacción](artifacts/canvas-interactivo.check.json), vinculado al SHA-256 del HTML.
- Capturas: [clara](artifacts/canvas-interactivo.light.png), [oscura](artifacts/canvas-interactivo.dark.png), [detalle](artifacts/canvas-interactivo.detail.png).

## Mapa base Archify

- Tipo `architecture`, nueve bloques sin conexiones causales.
- Archivo: [canvas-base.html](artifacts/canvas-base.html). Conserva el mapa anterior y sus funciones de zoom, tema y exportación.
- Validación: 9/9 showcase, cero errores y advertencias.
- Evidencia automatizada de navegador: passed en los cuatro tamaños de escritorio.
- [Recibo de entrega](artifacts/canvas-base.delivery.json) y [evidencia de navegador](artifacts/canvas-base.visual-check.json).
- specification_sha256: `43bd08e7dd8f539c413cf046bbdd399fe862eb921cb8c6029c9d3313afe04d28`.
- artifact_sha256: `8089e09f3eb9d29e19b8625c2cfcd88842a981db31ccc5a8f109cd2993b3ecee`.

## Alcance del contenido

Los ejemplos e indicadores añadidos son propuestas académicas. H señala hipótesis, F1–F5 enlazan fuentes oficiales y las clasificaciones del Canvas son interpretaciones. No se afirman costos internos ni resultados comerciales de WhatsApp. La vista tradicional y el boceto inicial se conservan como síntesis y comparación.
