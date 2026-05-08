from django.shortcuts import render, redirect
from .models import Proyecto, Categoria, Cotizacion
from .forms import CotizacionForm

def home(request):
    proyectos = Proyecto.objects.all()

    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            Cotizacion.objects.create(
                nombre   = form.cleaned_data['nombre'],
                telefono = form.cleaned_data['telefono'],
                servicio = form.cleaned_data['servicio'],
                mensaje  = form.cleaned_data.get('mensaje', ''),
            )
            # Redirige con ?ok=1 para mostrar mensaje de éxito sin reenviar el form
            return redirect('home')
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

    proyectos = Proyecto.objects.filter(
        categoria=categoria
    )

    return render(
        request,
        'categoria_detalle.html',
        {
            'categoria': categoria,
            'proyectos': proyectos,
        }
    )