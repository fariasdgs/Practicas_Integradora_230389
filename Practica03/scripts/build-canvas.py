"""Construye el explorador autocontenido a partir del contenido y la plantilla."""
from pathlib import Path
import json
root = Path(__file__).resolve().parents[1]
data = json.loads((root / 'artifacts/contenido-canvas.json').read_text())
payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
template = (root / 'scripts/canvas.template.html').read_text()
(root / 'artifacts/canvas-final.html').write_text(template.replace('__CANVAS_DATA__', payload))
print('Generado: Practica03/artifacts/canvas-final.html')
