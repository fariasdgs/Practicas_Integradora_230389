"""Genera una página sin dependencias externas, con bocetos propios y mapa Archify."""
from pathlib import Path
import json, html, base64

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    'registro': ('Registro y verificación', 'https://faq.whatsapp.com/506595211487528/'),
    'busqueda': ('Búsquedas en WhatsApp', 'https://faq.whatsapp.com/1131773267485499/?cms_platform=iphone&locale=es_LA'),
    'mensajes': ('Mensajería', 'https://www.whatsapp.com/messaging?lang=en'),
    'business': ('WhatsApp Business App', 'https://faq.whatsapp.com/641572844337957'),
    'catalogo': ('Acerca del catálogo', 'https://faq.whatsapp.com/405903568419894/'),
    'ver': ('Consultar un catálogo', 'https://faq.whatsapp.com/494713302702908/'),
}

def screen(id, name, role, purpose, elements, action, next_id, source, kind, note=''):
    return dict(id=id, name=name, role=role, purpose=purpose, elements=elements,
                action=action, next=next_id, source=source, kind=kind, note=note)

screens = [
    screen('p-acceso', 'Registro / acceso', 'persona', 'Confirmar la propiedad del número de teléfono para acceder a la cuenta.', ['País y prefijo', 'Número de teléfono', 'Código de registro de seis dígitos', 'Continuar'], 'Introduce el número y completa la verificación; se omiten los pasos de configuración inicial.', 'p-chats', 'registro', 'login'),
    screen('p-chats', 'Chats', 'persona', 'Ver las conversaciones personales y localizar una conversación comercial previa.', ['Lista de chats', 'Vista previa de mensajes', 'Búsqueda', 'Acceso a un nuevo chat'], 'Toca buscar para localizar el chat o sus mensajes.', 'p-buscar', 'busqueda', 'chats'),
    screen('p-buscar', 'Buscar', 'persona', 'Encontrar mensajes en el historial. El ejemplo usa una conversación existente con un negocio.', ['Campo de búsqueda', 'Filtros de contenido', 'Resultado con remitente', 'Extracto del mensaje'], 'Toca el resultado para abrir el mensaje en su conversación.', 'p-chat', 'busqueda', 'search'),
    screen('p-chat', 'Conversación', 'persona', 'Consultar un producto mediante un mensaje al negocio.', ['Nombre del negocio', 'Burbujas de mensajes', 'Caja de texto', 'Enviar y adjuntar', 'Indicador de envío'], 'Envía la consulta (conexión 10) y toca el nombre del negocio para ver su perfil.', 'p-perfil', 'mensajes', 'chat'),
    screen('p-perfil', 'Perfil del negocio', 'persona', 'Consultar información pública de un negocio que ha configurado WhatsApp Business.', ['Nombre y categoría', 'Descripción', 'Horario y dirección', 'Acceso al catálogo'], 'Abre el catálogo publicado por el negocio.', 'p-catalogo', 'ver', 'profile'),
    screen('p-catalogo', 'Catálogo', 'persona', 'Explorar productos o servicios publicados por el negocio.', ['Listado de artículos', 'Marcadores de imagen originales', 'Nombre y precio de ejemplo', 'Acceso al detalle de un artículo'], 'Fin de este recorrido. Puede volver al chat para continuar la consulta.', None, 'catalogo', 'catalog'),
    screen('n-acceso', 'Registro Business', 'negocio', 'Verificar el número usado por el negocio en la aplicación WhatsApp Business.', ['Indicación de cuenta comercial', 'Número del negocio', 'Código de verificación', 'Continuar'], 'Completa la verificación y la configuración inicial, resumidas en este boceto.', 'n-chats', 'business', 'business-login'),
    screen('n-chats', 'Chats del negocio', 'negocio', 'Revisar conversaciones de clientes y abrir una consulta recibida.', ['Lista de clientes', 'Mensajes recientes', 'Indicador de mensaje sin leer', 'Etiquetas como ejemplo de organización'], 'Toca la conversación de Ana cuando llegue su consulta.', 'n-chat', 'business', 'business-chats'),
    screen('n-chat', 'Atención al cliente', 'negocio', 'Leer la consulta del cliente y responder desde la conversación comercial.', ['Nombre del cliente', 'Consulta entrante', 'Respuesta del negocio', 'Caja de mensaje', 'Adjuntar y enviar'], 'Vuelve a Chats y abre las herramientas del negocio → Catálogo. Es una navegación resumida, no un salto directo desde el chat.', 'n-catalogo', 'catalogo', 'business-chat'),
    screen('n-catalogo', 'Gestionar catálogo', 'negocio', 'Administrar los productos o servicios del catálogo propio.', ['Lista de artículos propios', 'Añadir artículo', 'Nombre y precio', 'Acceso a edición'], 'Vuelve a las herramientas del negocio y abre el perfil comercial; se omite la pantalla intermedia.', 'n-perfil', 'catalogo', 'manage'),
    screen('n-perfil', 'Perfil comercial', 'negocio', 'Actualizar la información que los clientes consultan en el perfil.', ['Nombre del negocio', 'Categoría y descripción', 'Dirección y horario', 'Controles de edición'], 'Fin del recorrido. La información publicada puede consultarse en el perfil del negocio del carril superior.', None, 'business', 'edit-profile'),
    screen('e-offline', 'Sin conexión', 'alterno', 'Mostrar un mensaje pendiente mientras el dispositivo no tiene conexión.', ['Aviso de conectividad', 'Mensaje pendiente', 'Indicador de reloj', 'Conversación existente'], 'Recupera la conexión y vuelve a la conversación; el envío depende de la conectividad.', 'p-chat', 'mensajes', 'offline', 'Supuesto: se propone la ubicación y el texto del aviso. No representa una pantalla oficial independiente.'),
    screen('e-empty', 'Búsqueda sin resultados', 'alterno', 'Explicar que la consulta no coincide con mensajes del historial.', ['Consulta escrita', 'Estado vacío', 'Sugerencia de cambiar palabras'], 'Cambia la consulta y vuelve a buscar.', 'p-buscar', 'busqueda', 'empty', 'Supuesto: redacción y composición del estado vacío. La búsqueda solo consulta contenido accesible en el historial.'),
    screen('e-unavailable', 'Contenido no disponible', 'alterno', 'Representar un artículo de catálogo que ya no puede consultarse.', ['Marcador de artículo', 'Aviso de indisponibilidad', 'Regreso al catálogo'], 'Vuelve al catálogo y elige otro artículo.', 'p-catalogo', 'catalogo', 'unavailable', 'Supuesto: estado ilustrativo de un artículo retirado. El aviso exacto puede variar; no se afirma que exista esta pantalla concreta.'),
]

def text(x, y, value, size=12, weight=400, color='#444', anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{html.escape(value)}</text>'

def rect(x,y,w,h,fill='#e8e8e8',r=6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="#bbb" stroke-width=".7"/>'

def circle(x,y,r=12):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ddd" stroke="#aaa"/>'

def row(y,name,msg,badge=False):
    return circle(30,y+7)+text(49,y+5,name,11,600)+text(49,y+21,msg,9)+ (circle(150,y+6,6) if badge else '')+f'<path d="M18 {y+33}H162" stroke="#ddd"/>'

def bubble(y,msg,out=False):
    return rect(40 if out else 18,y,120,39,'#ddd' if out else '#f6f6f6')+text(48 if out else 26,y+16,msg,10)+text(143 if out else 120,y+31,'10:24' + (' ✓' if out else ''),7,anchor='end')

def thumbnail(x,y,w=62,h=52):
    return rect(x,y,w,h,'#eee')+f'<path d="M{x+10} {y+h-12}l14-16 10 9 12-20 10 27" fill="none" stroke="#aaa" stroke-width="1.5"/>'

def wireframe(s):
    kind=s['kind']; parts=[]
    parts += [rect(2,2,176,296,'#fbfbfb',21),rect(10,10,160,280,'#fff',15),rect(69,14,42,5,'#444',3),text(20,32,'9:41',8,600),text(160,32,'▰',8,anchor='end')]
    head={'login':'Tu número','business-login':'Cuenta del negocio','chats':'Chats','business-chats':'Chats · Business','search':'Buscar','chat':'Tienda Luna','business-chat':'Ana','profile':'Tienda Luna','edit-profile':'Perfil comercial','catalog':'Catálogo','manage':'Tu catálogo','offline':'Tienda Luna','empty':'Buscar','unavailable':'Artículo'}[kind]
    parts += [text(19,56,head,13,600),'<path d="M16 65H164" stroke="#ccc"/>']
    if kind in ('login','business-login'):
        parts += [circle(90,99,20),text(90,104,'B' if kind=='business-login' else '01',14,600,anchor='middle'),text(90,139,'Verifica tu teléfono',11,600,anchor='middle'),rect(20,154,140,24),text(29,170,'México  +52',11),rect(20,187,140,24,'#fafafa'),text(29,203,'Número de teléfono',10),text(20,232,'Código de registro',10),text(20,250,'_  _  _  _  _  _',16),rect(32,260,116,19,'#ccc'),text(90,273,'Continuar',10,600,anchor='middle')]
    elif kind in ('chats','business-chats'):
        parts += [rect(18,77,144,24,'#f4f4f4'),text(27,93,'⌕  Buscar',11)]
        if kind=='chats':
            parts += [row(120,'Equipo escolar','Nos vemos mañana'),row(174,'Tienda Luna','Tenemos ese modelo'),row(228,'Familia','Audio · 0:12')]
        else:
            parts += [row(120,'Ana','¿Está disponible?',True),rect(50,146,65,13,'#eee'),text(56,156,'Consulta nueva',8),row(189,'Carlos','Gracias por la ayuda'),text(20,253,'Clientes · Etiquetas',10)]
    elif kind=='search':
        parts += [rect(18,78,144,27,'#eee'),text(27,96,'luna',12),rect(18,117,60,19,'#f5f5f5'),text(25,130,'Mensajes',9),rect(86,117,70,19,'#f5f5f5'),text(95,130,'Documentos',9),text(20,161,'RESULTADO',8,600),circle(31,187,12),text(50,182,'Tienda Luna',11,600),text(50,199,'Tenemos ese modelo',9),text(20,243,'En tus conversaciones',10),text(20,260,'No busca negocios nuevos',9)]
    elif kind in ('chat','business-chat','offline'):
        parts += [text(19,81,'Hoy',9),bubble(96,'Hola, buen día'),bubble(148,'¿Está disponible?',kind!='business-chat')]
        if kind=='business-chat':parts += [bubble(200,'Sí, te comparto info',True)]
        elif kind=='offline':parts += [rect(18,201,144,30,'#eee'),text(25,214,'Sin conexión',10,600),text(25,225,'Mensaje pendiente ◷',8)]
        else:parts += [text(21,219,'Consulta enviada al negocio',9),text(21,238,'Toca el nombre para el perfil',8)]
        parts += [rect(18,258,117,22,'#f4f4f4'),text(25,273,'Mensaje…  +',9),circle(150,269,10),text(150,273,'›',15,600,anchor='middle')]
    elif kind in ('profile','edit-profile'):
        parts += [circle(90,101,25),text(90,105,'TL',12,600,anchor='middle'),text(90,146,'Tienda Luna',14,600,anchor='middle'),text(90,163,'Accesorios',10,anchor='middle')]
        if kind=='profile':
            parts += [text(20,193,'Artículos para tu día',10),text(20,217,'Lun–Vie · 9:00–18:00',10),text(20,237,'Centro, local 4',10),rect(20,253,140,25,'#ddd'),text(90,270,'Ver catálogo  ›',10,600,anchor='middle')]
        else:
            for y,label in [(183,'Descripción'),(217,'Dirección'),(251,'Horario')]:
                parts += [rect(19,y,142,26,'#fafafa'),text(27,y+17,label+'   ✎',10)]
    elif kind in ('catalog','manage'):
        if kind=='manage':parts += [rect(20,78,140,23,'#ddd'),text(90,93,'+ Añadir artículo',10,600,anchor='middle')]
        else:parts += [text(20,88,'Tienda Luna · 2 artículos',10)]
        for y,title,price in [(113,'Bolsa de tela','$120'),(196,'Estuche','$80')]:
            parts += [thumbnail(19,y,54,60),text(82,y+17,title,10,600),text(82,y+37,price,11),text(82,y+56,'Editar  ✎' if kind=='manage' else 'Ver detalle ›',9)]
    elif kind=='empty':
        parts += [rect(18,78,144,27),text(27,96,'zzzzzz',12),circle(85,155,22),text(85,162,'⌕',26,anchor='middle'),text(90,203,'Sin resultados',13,600,anchor='middle'),text(90,225,'Prueba otra palabra',10,anchor='middle'),text(90,244,'en tus mensajes',10,anchor='middle')]
    elif kind=='unavailable':
        parts += [thumbnail(49,85,82,68),text(90,184,'No disponible',13,600,anchor='middle'),text(90,207,'No se puede consultar',10,anchor='middle'),text(90,224,'este artículo',10,anchor='middle'),rect(23,249,134,26,'#ddd'),text(90,266,'Volver al catálogo',10,600,anchor='middle')]
    parts += [rect(66,284,48,3,'#666',2)]
    return '<svg class="wireframe" viewBox="0 0 180 300" role="img" aria-label="'+html.escape('Boceto original: '+s['name'])+'" xmlns="http://www.w3.org/2000/svg" font-family="Arial, sans-serif">'+''.join(parts)+'</svg>'

byid={s['id']:s for s in screens}
def phone(s,number):
    return f'<button class="screen" data-id="{s["id"]}" aria-pressed="false" aria-haspopup="dialog" aria-label="Explorar {html.escape(s["name"])}"><span class="screen-caption"><span class="step">{number}</span>{html.escape(s["name"])}</span>{wireframe(s)}<span class="screen-hint">'+('Supuesto · Ver detalle' if s['role']=='alterno' else 'Explorar pantalla ↗')+'</span></button>'

def arrow(number,label,wide=False):
    return f'<div class="transition {"wide" if wide else ""}" aria-label="Paso {number}: {html.escape(label)}"><span class="edge-number">{number:02}</span><span class="edge-label">{html.escape(label)}</span><span class="edge-line" aria-hidden="true"></span></div>'

def lane(role,ids,actions,start):
    pieces=[]
    for i,id in enumerate(ids):
        cls='phone-cell'; col=i+1 if role=='persona' or i<2 else i+2
        if i==len(ids)-1:cls+=' last'
        pieces.append(f'<div class="{cls}" style="grid-column:{col}">'+phone(byid[id],f'{i+1:02}')+(arrow(start+i,actions[i],role=='negocio' and i==1) if i<len(actions) else '')+'</div>')
    return '<div class="lane-phones">'+''.join(pieces)+'</div>'

icon_person='<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="7" r="4"/><path d="M4 22v-3a8 8 0 0 1 16 0v3"/></svg>'
icon_shop='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 9l2-6h14l2 6M3 9v4h18V9M5 13v8h14v-8M10 21v-6h4v6"/></svg>'
lanes=''
for role,title,app,icon,ids,actions,start in [
    ('persona','Persona usuaria','WhatsApp Messenger',icon_person,['p-acceso','p-chats','p-buscar','p-chat','p-perfil','p-catalogo'],['Verifica número','Toca buscar','Abre resultado','Toca nombre','Abre catálogo'],1),
    ('negocio','Negocio','WhatsApp Business',icon_shop,['n-acceso','n-chats','n-chat','n-catalogo','n-perfil'],['Verifica número','Abre consulta','Herramientas → catálogo','Herramientas → perfil'],6)]:
    if role=='negocio':lanes+='<div class="bridge" aria-label="Conexión 10: el mensaje enviado por la persona llega a la conversación del negocio"><div class="bridge-line"><span>10 · Envía consulta → el negocio recibe el mensaje</span></div></div>'
    lanes+=f'<section class="lane" data-role="{role}" aria-label="Recorrido de {title}"><div class="lane-heading"><button class="role-button" data-role-select="{role}" aria-pressed="false">{icon}<strong>{title}</strong><span>{app}</span></button><span class="lane-count">{len(ids)} pantallas · recorrido de ejemplo</span></div>'+lane(role,ids,actions,start)+'</section>'

alternates=''
for s,origin,num in [(byid['e-offline'],'Desde Conversación · pierde conexión','A'),(byid['e-empty'],'Desde Buscar · no hay coincidencias','B'),(byid['e-unavailable'],'Desde Catálogo · artículo retirado','C')]:
    alternates+='<article class="alternate"><div><span class="alt-origin">'+origin+'</span><p class="alt-branch">↳ '+s['name']+'</p><p>'+s['purpose']+'</p><span class="badge">Supuesto de presentación</span></div>'+phone(s,num)+'</article>'

template=(ROOT/'scripts/template.html').read_text()
data=json.dumps(dict(screens=screens,sources=SOURCES),ensure_ascii=False).replace('<','\\u003c')
archify=base64.b64encode((ROOT/'artifacts/recorridos.archify.html').read_bytes()).decode()
output=template.replace('__LANES__',lanes).replace('__ALTERNATES__',alternates).replace('__DATA__',data).replace('__ARCHIFY__',archify)
(ROOT/'index.html').write_text(output)
print('Generado: Practica06/index.html')
