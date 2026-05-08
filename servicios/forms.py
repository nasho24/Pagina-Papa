from django import forms
 
SERVICIOS = [
    ('', 'Selecciona un servicio...'),
    ('ventanas', 'Ventanas (aluminio / termopanel)'),
    ('puertas', 'Puertas de interior y exterior'),
    ('banos', 'Baños (shower, muebles, accesorios)'),
    ('terminaciones', 'Terminaciones y guardapolvos'),
    ('otro', 'Otro / consulta general'),
]
 
class CotizacionForm(forms.Form):
    nombre    = forms.CharField(max_length=100, label='Tu nombre')
    telefono  = forms.CharField(max_length=20,  label='Teléfono / WhatsApp')
    servicio  = forms.ChoiceField(choices=SERVICIOS, label='¿Qué necesitas?')
    mensaje   = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        label='Cuéntanos más (medidas, ubicación, urgencia…)',
        required=False,
    )
 