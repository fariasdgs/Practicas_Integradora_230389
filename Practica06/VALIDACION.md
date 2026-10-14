# Validación · Práctica 06

La entrega principal es `index.html`, un explorador de sketches autocontenido. El mapa `artifacts/recorridos.archify.html` es complementario y está integrado dentro de la entrega. Las comprobaciones de ambos artefactos se documentan por separado.

## Bocetos y controles

- **Resultado: 37/37 comprobaciones**, con evidencia en [sketches.check.json](artifacts/sketches.check.json).
- Tamaños: 1440×900, 1600×1000, 1920×1080, 2048×1320, 768×1024 y 390×844.
- Documento sin desbordamiento horizontal; desplazamiento interno del diagrama en móvil.
- Los límites `getBBox()` de cada texto SVG de los 14 bocetos permanecen dentro del área de pantalla del teléfono. No se recorta texto para ocultar desbordamientos.
- Los 14 paneles abren con nombre, elementos, propósito, acción siguiente y referencia.
- Selección de roles, restablecer, siguiente pantalla, tema claro/oscuro y `aria-pressed` comprobados.
- Enter y Escape enviados mediante eventos de teclado del navegador; apertura, cierre y devolución del foco comprobados.
- Regla de movimiento reducido comprobada mediante emulación de `prefers-reduced-motion`.
- Mapa complementario integrado comprobado sin necesitar otro archivo para su apertura.

El documento tiene desplazamiento vertical deliberado para acomodar los dos carriles, los estados alternos y las notas académicas. No se exige que todos esos contenidos entren en una única pantalla.

**Revisión visual: passed.** Se inspeccionaron las capturas reales claras y oscuras de 1440 y 2048 px, la vista móvil y el panel lateral. Se despejó una anotación que competía con la transición 07 durante una ronda de corrección. El mapa complementario se revisó en ambos temas: sus relaciones y etiquetas son legibles; su visor deja espacio libre inferior porque contiene un mapa horizontal breve, a diferencia de la entrega principal con sketches.

Huella del HTML final:

```text
output: Practica06/index.html
artifact_sha256: fa0a377f8d6b3bd40e0982e3afe89048a035128eb96902b82be359e3d08adcd9
artifact_bytes: 1139033
browser_evidence: passed (comprobación personalizada de sketches)
visual_review: passed (sketches)
correction_rounds: 1
```

## Mapa complementario de Archify

El comando `deliver workflow` terminó con código 0. La especificación quedó congelada tras validarse y no se modificó posteriormente. Resultado: **9/9 showcase, 0 errores, 0 advertencias**. La comprobación automática del visor completó los cuatro tamaños de escritorio y las capturas de ambos temas con Brave mediante el transporte CDP de Archify. El primer intento en el entorno restringido falló al iniciar el navegador; se repitió con permiso de ejecución y el recibo actual registra `pass`.

```text
diagram_type: workflow
output: Practica06/artifacts/recorridos.archify.html
specification_sha256: 509b93c2e1322580a396a7a4f9d485e35c52f311bab37ec0287c681b02a11aee
specification_bytes: 3900
artifact_sha256: e01643dba8d45ba86e0c92f86e301243cd59b0a0f67897dc5ef971eaf0b7d33f
artifact_bytes: 808031
validation: 9/9 showcase, 0 errors, 0 warnings
browser_evidence: passed
visual_review: failed (composición del visor aislado: espacio inferior amplio)
correction_rounds: 0
```

El resultado automático no implica aprobación visual: el mapa complementario aislado tiene una composición breve y no pasa el criterio de ocupar equilibradamente una pantalla grande del visor estándar. Se conserva como evidencia de navegación y no como entrega principal de sketches. La entrega principal satisface la composición solicitada y tiene revisión visual propia aprobada.

## Límites de fidelidad

Se contrastaron funciones públicas de registro, búsqueda, mensajes, perfil comercial y catálogo con las fuentes oficiales indicadas en la página. No se simula una sesión real ni se valida la interfaz oficial de una versión concreta de WhatsApp. Las pantallas alternas están marcadas como supuestos de presentación. Los pasos intermedios omitidos se explican en los paneles.
