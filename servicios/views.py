import urllib.parse
from django.shortcuts import render, redirect
from .models import Proyecto, Categoria, Cotizacion
from .forms import CotizacionForm

def home(request):
    proyectos = Proyecto.objects.all()

    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            # 1. Guardamos en la base de datos
            cotizacion = Cotizacion.objects.create(
                nombre   = form.cleaned_data['nombre'],
                telefono = form.cleaned_data['telefono'],
                servicio = form.cleaned_data['servicio'],
                mensaje  = form.cleaned_data.get('mensaje', ''),
            )
            
            # 2. Extraemos los datos para armar el mensaje de WhatsApp
            nombre = form.cleaned_data['nombre']
            telefono_cliente = form.cleaned_data['telefono']
            servicio_key = form.cleaned_data['servicio']
            mensaje = form.cleaned_data.get('mensaje', '')

            servicio_label = dict(form.fields['servicio'].choices).get(servicio_key, servicio_key)

            # 3. Diseñamos el mensaje con negritas para que se lea claro
            texto_whatsapp = (
                f"Nueva Solicitud desde la Web\n\n"
                f"Nombre: {nombre}\n"
                f"Teléfono: {telefono_cliente}\n"
                f"Servicio solicitado: {servicio_label}\n"
            )
            
            if mensaje:
                texto_whatsapp += f"\U0001F4AC *Detalles:* {mensaje}\n"

            # 4. Convertimos el texto a un formato seguro para URLs 
            texto_codificado = urllib.parse.quote(texto_whatsapp)

            # 5. Generamos la URL final con el número 
            url_api_whatsapp = f"https://wa.me/56961092914?text={texto_codificado}"

            # 6. Redireccionamos directamente a WhatsApp
            return redirect(url_api_whatsapp)
    else:
        form = CotizacionForm()

    enviado = request.GET.get('enviado') == '1'

    return render(request, 'home.html', {
        'proyectos': proyectos,
        'form': form,
        'enviado': enviado,
    })

def categoria_detalle(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    proyectos = Proyecto.objects.filter(categoria=categoria)

    return render(
        request,
        'categoria_detalle.html',
        {
            'categoria': categoria,
            'proyectos': proyectos,
        }
    )