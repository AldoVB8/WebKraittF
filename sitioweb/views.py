from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'web/home-aldo.html')
def pages(request):
    return render(request, 'web/pages-aldo.html')

def contact(request):
    return render(request, 'web/contact-aldo.html')

def services(request):
    return render(request, 'web/services_aldo.html')

def nosotros(request):
    return render(request, 'web/nosotros-aldo.html')

PRODUCTS = {
    'diot-2025': {
        'title': 'Diot 2025',
        'badge': 'Producto Destacado',
        'badge_color': 'bg-blue-100 text-blue-800',
        'description': 'La solución definitiva para la Declaración Informativa de Operaciones con Terceros. Automatiza la carga de datos, valida RFCs y genera el archivo batch listo para el SAT en segundos.',
        'icon': 'description',
        'features': [
            {'title': 'Velocidad Incomparable', 'desc': 'Procesa miles de registros en segundos. Olvídate de las cargas manuales lentas y propensas a errores.', 'icon': 'bolt'},
            {'title': 'Validación Automática', 'desc': 'Detecta RFCs inválidos y errores de formato antes de enviar tu declaración. Evita multas y rechazos.', 'icon': 'check_circle'},
            {'title': 'Exportación Directa', 'desc': 'Genera el archivo .txt exacto que requiere el software del SAT. Sin pasos intermedios complicados.', 'icon': 'file_upload'},
        ],
        'specs': [
            'Compatible con Windows 10 y 11',
            'Importación desde Excel (XLS, XLSX, CSV)',
            'Actualizaciones automáticas del SAT',
            'Soporte técnico incluido',
            'Licencia anual o perpetua'
        ],
        'cta_text': 'Descargar Demo',
        'cta_link': '#',
        'secondary_cta': 'Ver Características',
        'specs_card_header': 'Especificaciones Técnicas',
        'card_cta_text': 'Contactar a Soporte',
        'show_card_cta': False
    },
    'adcofi': {
        'title': 'ADCOFI',
        'badge': 'Gestión Fiscal',
        'badge_color': 'bg-indigo-100 text-indigo-800',
        'description': 'Administrador de Comprobantes Fiscales. La herramienta esencial para organizar, validar y gestionar todos tus CFDI de manera eficiente y segura.',
        'icon': 'calculate',
        'features': [
            {'title': 'Comprobantes Fiscales', 'desc': 'Centraliza todos tus comprobantes en un solo lugar para un acceso rápido y sencillo.', 'icon': 'description'},
            {'title': 'Estatus de los comprobantes', 'desc': 'Verifica el estado actual de tus facturas directamente con el SAT.', 'icon': 'verified'},
            {'title': 'Resumen de tus Facturas', 'desc': 'Obtén reportes detallados y resúmenes de tus operaciones fiscales.', 'icon': 'pie_chart'},
        ],
        'specs': [
            'Windows 7, 8, 10, 11',
            'RAM: 2GB mínimo',
            'Espacio en disco: 50MB o superior',
            'Conexión a Internet estable'
        ],
        'cta_text': 'Descargar Demo',
        'cta_link': '#',
        'secondary_cta': 'Ver Características',
        'specs_card_header': 'Requisitos de Instalación',
        'card_cta_text': 'Contactar a Soporte',
        'show_card_cta': False
    },
    'validador-movil': {
        'title': 'Validador Móvil de CFDIs',
        'badge': 'Movilidad',
        'badge_color': 'bg-green-100 text-green-800',
        'description': 'Lleva el control de tus facturas en tu bolsillo. Escanea, valida y organiza tus CFDIs desde cualquier dispositivo móvil.',
        'icon': 'smartphone',
        'features': [
            {'title': 'Sin límite', 'desc': 'Escanea y valida tantos comprobantes como necesites sin restricciones.', 'icon': 'all_inclusive'},
            {'title': 'Validación SAT', 'desc': 'Conexión directa para verificar la autenticidad y vigencia de cada CFDI.', 'icon': 'check'},
            {'title': 'Genera PDFs', 'desc': 'Convierte tus XMLs validados en documentos PDF listos para compartir o imprimir.', 'icon': 'picture_as_pdf'},
        ],
        'price': '$300.00',
        'specs': [
            'Compatible con Android',
            'Requiere cámara para escaneo QR',
            'Conexión a Internet para validación'
        ],
        'cta_text': 'Comprar Ahora - $300.00',
        'cta_link': '#',
        'secondary_cta': 'Ver Características',
        'specs_card_header': 'Precio y Requisitos',
        'card_cta_text': 'Comprar Licencia',
        'show_card_cta': True
    },
    'visor-trifasico': {
        'title': 'Visor Trifásico de XML',
        'badge': 'Seguridad Fiscal',
        'badge_color': 'bg-yellow-100 text-yellow-800',
        'description': 'Protege tu empresa contra facturas falsas. Visualiza, valida y audita tus XMLs en tres niveles de seguridad.',
        'icon': 'shield',
        'features': [
            {'title': 'Visor XML', 'desc': 'Interpreta fácilmente el contenido técnico de cualquier archivo XML.', 'icon': 'visibility'},
            {'title': 'Validación SAT', 'desc': 'Confirma que el comprobante esté registrado y vigente en los servidores del SAT.', 'icon': 'verified_user'},
            {'title': 'Evita fraudes', 'desc': 'Detecta EFOS (Empresas Facturadoras de Operaciones Simuladas) automáticamente.', 'icon': 'block'},
        ],
        'price': '$1,690.00',
        'specs': [
            'Windows 7, 8, 10, 11',
            '.NET Framework 4.5+',
            'Conexión a Internet'
        ],
        'cta_text': 'Comprar - $1,690.00',
        'cta_link': '#',
        'secondary_cta': 'Ver Características',
        'specs_card_header': 'Inversión',
        'card_cta_text': 'Adquirir Licencia',
        'show_card_cta': True
    },
    'eric': {
        'title': 'ERIC',
        'badge': 'Impresión Fiscal',
        'badge_color': 'bg-pink-100 text-pink-800',
        'description': 'Escritor de Representación Impresa CFDI. Visualiza, genera y valida tus facturas con formatos personalizados y profesionales.',
        'icon': 'print',
        'features': [
            {'title': 'Automatización', 'desc': 'Sustituye de forma automática tus comprobantes CFDI proporcionando un formato personalizado.', 'icon': 'edit'},
            {'title': 'Ahorro de Tiempo', 'desc': 'Optimiza tu flujo de trabajo generando representaciones impresas en segundos.', 'icon': 'schedule'},
            {'title': 'Validación', 'desc': 'Asegura que tus documentos cumplan con los requisitos visuales y fiscales.', 'icon': 'rule'},
        ],
        'price': '$1,658.80',
        'specs': [
            'Windows 7, 8, 10, 11',
            '.NET Framework 3.5',
            'RAM: 2GB',
            'Espacio en disco: 50MB'
        ],
        'cta_text': 'Comprar - $1,658.80',
        'cta_link': '#',
        'secondary_cta': 'Ver Características',
        'specs_card_header': 'Precio de Lista',
        'card_cta_text': 'Adquirir Licencia',
        'show_card_cta': True
    },
    'rex': {
        'title': 'REX (Robot Extractor)',
        'badge': 'Automatización Total',
        'badge_color': 'bg-red-100 text-red-800',
        'description': 'Más que descarga masiva de XML, organiza tu tiempo. Descarga, convierte a Excel y concilia cancelaciones automáticamente.',
        'icon': 'smart_toy',
        'features': [
            {'title': 'Descarga Masiva', 'desc': 'Descarga rápidamente tus XML de forma masiva y genera PDFs por cada uno de tus comprobantes.', 'icon': 'download'},
            {'title': 'Exportación a Excel', 'desc': 'Genera un archivo de Excel con todos los datos necesarios para realizar tu contabilidad.', 'icon': 'table_view'},
            {'title': 'Conciliación', 'desc': 'Realiza conciliación de cancelaciones para mantener tus registros impecables.', 'icon': 'balance'},
        ],
        'price': '$2,418.02',
        'specs': [
            'Windows 7, 8, 10, 11',
            '.NET Framework 4.8',
            'RAM: 2GB',
            'Espacio en disco: 50MB'
        ],
        'cta_text': 'Comprar - $2,418.02',
        'cta_link': '#',
        'secondary_cta': 'Ver Características',
        'specs_card_header': 'Precio de Lista',
        'card_cta_text': 'Adquirir Licencia',
        'show_card_cta': True
    },
    'sfacil-factura': {
        'title': 'SFacil Factura Electrónica',
        'badge': 'Sistema SFacil',
        'badge_color': 'bg-blue-100 text-blue-800',
        'description': 'La forma más fácil y rápida de facturar. Emite CFDI 4.0, complementos de pago, notas de crédito y más, cumpliendo con todas las disposiciones del SAT.',
        'icon': 'receipt',
        'features': [
            {'title': 'CFDI 4.0 Listo', 'desc': 'Emite facturas con la versión más reciente del anexo 20. Cumple con todos los requisitos fiscales.', 'icon': 'check_circle'},
            {'title': 'Envío Automático', 'desc': 'Envía tus facturas por correo electrónico a tus clientes automáticamente al timbrar.', 'icon': 'send'},
            {'title': 'Complementos', 'desc': 'Soporte para Carta Porte, Pagos, Comercio Exterior y muchos más.', 'icon': 'extension'},
        ],
        'has_plans': True,
        'plans': [
            {'name': 'MICRO', 'price': '$3,166.80', 'highlight': False},
            {'name': 'PLUS', 'price': '$5,730.40', 'highlight': True, 'tag': 'POPULAR'},
            {'name': 'RED 2', 'price': '$8,595.60', 'desc': 'Soporte para 1 estación + 1 servidor', 'highlight': False},
        ],
        'specs': [
            'Windows 7, 8, 10, 11',
            'Procesador: 1.5 GHz',
            'RAM: 4GB',
            'Espacio: 100MB o superior'
        ],
        'cta_text': 'Ver Precios',
        'cta_link': '#',
        'secondary_cta': 'Ver Características',
        'specs_card_header': 'Requisitos del Sistema',
        'card_cta_text': 'Seleccionar Plan',
        'show_card_cta': False
    },
    'sfacil-conta-fiscal': {
        'title': 'SFacil Conta-Fiscal',
        'badge': 'Sistema SFacil',
        'badge_color': 'bg-blue-100 text-blue-800',
        'description': 'Ahorra tiempo al generar tus pólizas a partir de tus XML. Cumple al 100% con la Contabilidad Electrónica del SAT.',
        'icon': 'calculate',
        'features': [
            {'title': 'Cálculo Automatizado', 'desc': 'Calcula automáticamente Pagos Provisionales y Declaración Anual a partir de tus pólizas.', 'icon': 'edit_note'},
            {'title': 'Catálogos Completos', 'desc': 'Incluye Catálogos de Cuentas con equivalencias al Catálogo de Códigos Agrupadores del SAT.', 'icon': 'list'},
            {'title': 'Generación de Pólizas', 'desc': 'Genera automáticamente pólizas a partir de XML de compras, ventas y nóminas.', 'icon': 'post_add'},
        ],
        'has_plans': True,
        'plans': [
            {'name': 'MICRO', 'price': '$4,065.24', 'highlight': False},
            {'name': 'PLUS', 'price': '$9,103.60', 'highlight': True, 'tag': 'POPULAR'},
            {'name': 'RED 2', 'price': '$13,655.39', 'desc': 'Soporte para 1 estación + 1 servidor', 'highlight': False},
        ],
        'specs': [
            'Windows 7, 8, 10, 11',
            'Procesador: 1.5 GHz',
            'RAM: 4GB',
            'Espacio: 100MB o superior'
        ],
        'cta_text': 'Ver Precios',
        'cta_link': '#',
        'secondary_cta': 'Ver Características',
        'specs_card_header': 'Requisitos del Sistema',
        'card_cta_text': 'Seleccionar Plan',
        'show_card_cta': False
    },
    'sfacil-nominas': {
        'title': 'SFacil Nóminas',
        'badge': 'Sistema SFacil',
        'badge_color': 'bg-blue-100 text-blue-800',
        'description': 'Calcula y timbra tu nómina de forma sencilla. Cumple con todas las obligaciones laborales y fiscales en un solo lugar.',
        'icon': 'groups',
        'features': [
            {'title': 'Cálculo Exacto', 'desc': 'Calcula ISR, IMSS, Infonavit y más de forma automática y precisa.', 'icon': 'calculate'},
            {'title': 'Timbrado Masivo', 'desc': 'Timbra todos tus recibos de nómina en un solo clic. Ahorra horas de trabajo.', 'icon': 'file_upload'},
            {'title': 'Reportes Laborales', 'desc': 'Genera reportes de asistencia, vacaciones, aguinaldos y más para una mejor gestión.', 'icon': 'pie_chart'},
        ],
        'has_plans': True,
        'plans': [
            {'name': 'MICRO', 'price': '$3,855.50', 'highlight': False},
            {'name': 'PLUS', 'price': '$7,455.80', 'highlight': True, 'tag': 'POPULAR'},
            {'name': 'RED 2', 'price': '$12,303.50', 'desc': 'Soporte para 1 estación + 1 servidor', 'highlight': False},
        ],
        'specs': [
            'Windows 7, 8, 10, 11',
            'Procesador: 1.5 GHz',
            'RAM: 4GB',
            'Espacio: 100MB o superior'
        ],
        'cta_text': 'Ver Precios',
        'cta_link': '#',
        'secondary_cta': 'Ver Características',
        'specs_card_header': 'Requisitos del Sistema',
        'card_cta_text': 'Seleccionar Plan',
        'show_card_cta': False
    },
}

def product_detail(request, slug):
    product = PRODUCTS.get(slug)
    if not product:
        # Fallback or 404
        return render(request, 'web/pages-aldo.html') # Or specific 404
    return render(request, 'web/product-detail-aldo.html', {'product': product})