# Práctica 03 · Boceto de Modelo Canvas con Archify

**Aplicación:** WhatsApp · **Materia:** Integradora · **Valor indicado:** 10 firmas (asignación docente; no acreditadas por este documento).

[Ver Canvas tradicional](index.html) · [Explorar resultado Archify](artifacts/canvas-final.html) · [Consultar boceto inicial](artifacts/canvas-inicial.html)

## 1. Elección de la aplicación

Se eligió WhatsApp por su utilidad para comunicación personal y comercial y su acceso desde dispositivos móviles, web y escritorio [F1]. Ejemplo cotidiano propuesto: coordinar un equipo escolar y compartir archivos desde el teléfono o la computadora. Este ejemplo no afirma una experiencia personal del estudiante.

El alcance comprende mensajería personal, Business App y Business Platform. El análisis es un boceto académico, no el modelo oficial ni un inventario completo de negocios de Meta. No se asume igualdad de funciones entre dispositivos.

## 2. Prompt inicial y generación

Se redactó el [prompt inicial](prompts/01-inicial.md). Se tradujo su solicitud a una especificación JSON y se generó el [primer HTML con Archify](artifacts/canvas-inicial.html). Archify renderiza JSON: el prompt orienta al asistente que prepara la especificación; no se presenta como una API de texto de la herramienta.

La versión instalada de Archify no tiene un esquema nativo para Business Model Canvas. Se adaptó el tipo `architecture` como mapa de nueve categorías, sin conexiones: los bloques no representan pasos secuenciales. Los tipos técnicos internos no atribuyen infraestructura a WhatsApp. La interfaz fija y el atributo `html lang` del visor Archify usan inglés por limitación del generador; el contenido académico está en español.

## 3. Revisión del primer resultado

| Criterio | Hallazgo inicial | Mejora aplicada |
| --- | --- | --- |
| Cobertura | Contiene nueve bloques | Se conservan los nueve |
| Precisión | “Personas y empresas” mezcla segmentos | Se distinguen personas, pequeños negocios y empresas con API |
| Ingresos | “Servicios para empresas” es ambiguo | Se indica cobro de mensajes sujetos a tarifa y excepciones |
| Evidencia | El boceto no cita fuentes | Se agregan F1–F5 y marcas H |
| Costos | No explica categorías ni incertidumbre | Se describen categorías como hipótesis, sin cantidades |
| Presentación | Cuadrícula de bloques, no disposición tradicional | Se agrega una vista tradicional complementaria |

El primer resultado era útil como estructura, pero insuficiente para explicar el negocio. La revisión corresponde al análisis asistido realizado en esta práctica; no sustituye la evaluación del docente.

## 4. Prompt mejorado y modelo final

El [prompt mejorado](prompts/02-mejorado.md) añade alcance, segmentos, fuentes, hipótesis y formato. Se obtuvo un [mapa final de Archify](artifacts/canvas-final.html) y una [vista tradicional](index.html) con el desarrollo completo.

### Socios clave

- Integradores de Business Platform y proveedores de soluciones empresariales. [F4]
- Tiendas de aplicaciones y proveedores de conectividad como aliados de distribución y acceso. [H]

### Actividades clave

- Desarrollo de mensajería e integraciones para negocios. [F1, F4]
- Mantenimiento, prevención de abuso y operación continua. [H]

### Propuesta de valor

- Mensajes y archivos accesibles desde móvil, web y escritorio. [F1]
- Atención comercial mediante perfiles, catálogos e integraciones. [F2, F4]

### Relación con clientes

- Ayuda y autoservicio para usuarios de la aplicación. [F5]
- Acompañamiento de integradores para clientes empresariales. [H]

### Segmentos de clientes

- Personas que necesitan comunicarse; pequeños negocios. [F1, F2]
- Empresas que integran atención y notificaciones mediante API. [F4]

### Recursos clave

- Aplicaciones y API como base del servicio. [F1, F4]
- Infraestructura, personal técnico y red de usuarios. [H]

### Canales

- Aplicaciones móviles, WhatsApp Web y escritorio. [F1]
- Business App y Business Platform para acceso empresarial. [F2, F4]

### Estructura de costos

- Infraestructura y operación del servicio. [H]
- Desarrollo, seguridad, soporte y personal; sin cifras públicas verificadas en este trabajo. [H]

### Fuentes de ingresos

- Business Platform: cobro por mensajes entregados sujetos a tarifa; varía por categoría y mercado. [F3]
- Existen mensajes y ventanas gratuitas. Otros productos comerciales quedan fuera de este boceto. [F3]

**Coherencia del modelo:** los canales permiten entregar comunicación personal y atención comercial. Las empresas con necesidades de integración constituyen un segmento monetizable mediante Business Platform. Los recursos y actividades propuestos explican las categorías de costos como hipótesis, sin atribuir presupuestos internos a la empresa.

## 5. Documentación y buenas prácticas

- Rama de trabajo: `practica03`.
- Prompts y JSON conservados para reproducibilidad; primera versión preservada.
- Enlaces relativos, nombres descriptivos y fuentes oficiales.
- HTML autocontenido de Archify y vista tradicional sin dependencias externas de ejecución.
- Evidencias de validación separadas de la revisión del contenido.

### Reproducción

Con Node.js y la habilidad Archify instalada, sustituye `<ARCHIFY>` por su directorio:

```sh
node <ARCHIFY>/bin/archify.mjs validate architecture Practica03/artifacts/canvas-final.json --quality showcase --json
node <ARCHIFY>/bin/archify.mjs deliver architecture Practica03/artifacts/canvas-final.json Practica03/artifacts/canvas-final.html --quality showcase --json
node <ARCHIFY>/bin/archify.mjs visual-check Practica03/artifacts/canvas-final.html --json
```

Abre `Practica03/index.html` en un navegador. GitHub muestra el código HTML; para verlo como página se requiere abrir el archivo local o una publicación en Pages. Consulta [VALIDACION.md](VALIDACION.md) para las comprobaciones efectuadas.

## Fuentes

Consulta: 23 de septiembre de 2026. F = fuente oficial; H = hipótesis académica. La selección y ubicación de cada idea en el Canvas son interpretación del análisis.

- **F1**: [Mensajería y acceso multiplataforma](https://www.whatsapp.com/messaging?lang=en).
- **F2**: [WhatsApp Business App](https://whatsappbusiness.com/products/business-app/).
- **F3**: [Precios de Business Platform](https://whatsappbusiness.com/products/platform-pricing/).
- **F4**: [WhatsApp Business Platform](https://whatsappbusiness.com/products/business-platform/).
- **F5**: [Centro de ayuda](https://faq.whatsapp.com/).

## Conclusión

Un prompt general produjo un mapa correcto en estructura, pero poco específico. Añadir segmentos, alcance, evidencia y criterios de presentación permitió explicar mejor el valor y la monetización. La gratuidad de funciones personales no implica ausencia de ingresos empresariales. Las hipótesis de costos y recursos requieren información interna para validarse.

## Pendientes de entrega académica

El estudiante debe revisar el contenido y adaptar el ejemplo a su uso real. La consigna compartida no especifica portada, formato de evidencia ni cómo se obtienen las 10 firmas; la evaluación y las firmas corresponden al docente.
