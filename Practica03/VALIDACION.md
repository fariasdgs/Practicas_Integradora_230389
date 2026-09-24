# Validación de la práctica

- Tipo Archify: `architecture`, adaptado como mapa de nueve bloques sin flechas.
- Validación final: **9/9 showcase**, cero errores y cero advertencias.
- Evidencia automatizada del visor final: **passed**. Sin desbordamiento a 1440×900, 1600×1000, 1920×1080 y 2048×1320.
- Revisión visual: **passed** para las capturas finales clara 1440×900 y oscura 2048×1320: nueve bloques visibles, sin solapamientos ni texto recortado.
- Vista tradicional: captura revisada a 1600×1000. Nueve bloques, fuentes y leyenda visibles. Esta vista complementaria no usa el validador Archify.
- Correcciones geométricas: una en el candidato inicial (ancho de viewBox de 1400 a 1380); cero en el final.
- La primera ejecución de Chrome fue bloqueada por el entorno; la repetición con permiso terminó correctamente. El recibo vigente contiene la evidencia válida.
- La revisión visual no equivale a validar los datos internos de WhatsApp ni a una aprobación docente.

## Identidad del resultado final

- specification_sha256: `43bd08e7dd8f539c413cf046bbdd399fe862eb921cb8c6029c9d3313afe04d28`
- artifact_sha256: `8089e09f3eb9d29e19b8625c2cfcd88842a981db31ccc5a8f109cd2993b3ecee`

[Recibo de entrega](artifacts/canvas-final.delivery.json) · [Evidencia de navegador](artifacts/canvas-final.visual-check.json) · [Ver capturas en línea](https://fariasdgs.github.io/Practicas_Integradora_230389/Practica03/artifacts/canvas-final.visual-check.html) · [Vista tradicional](artifacts/canvas-tradicional.png)

## Revisión previa al merge

- Se comprobaron 30 referencias locales en los README, la documentación y los HTML: todos los destinos existen.
- Los nueve bloques y sus textos coinciden entre el README, el Canvas tradicional y `contenido-canvas.json`.
- La validación del JSON final se ejecutó nuevamente: 9/9 comprobaciones, sin errores ni advertencias.
- Los hashes de los HTML inicial y final coinciden con sus recibos de navegador; el JSON y HTML finales coinciden con el recibo de entrega. La evidencia visual anterior sigue correspondiendo a estos archivos, sin una nueva inspección de navegador.
- La API de GitHub Pages informó `built`, con origen `practica03` y `/`.
- La comprobación directa de las páginas públicas agotó el tiempo de conexión desde el entorno de revisión. Esto no permite confirmar su accesibilidad actual ni demuestra que los enlaces estén rotos; queda pendiente abrirlos en el navegador del estudiante.
- Se corrigió el enlace de las capturas para abrir la página publicada y se documentó el cambio de origen de Pages después del merge.
