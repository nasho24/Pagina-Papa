from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    titulo          = models.CharField(max_length=200, verbose_name="Título del Trabajo")
    descripcion     = models.TextField(verbose_name="¿Qué se hizo?")
    categoria       = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen          = models.ImageField(upload_to='proyectos/', null=True, blank=True)
    fecha_finalizado = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo

# ──────────────────────────────────────────
# Solicitudes de cotización
# ──────────────────────────────────────────
class Cotizacion(models.Model):
    ESTADO_CHOICES = [
        ('nueva',      'Nueva'),
        ('contactado', 'Contactado'),
        ('cerrado',    'Cerrado'),
    ]

    nombre    = models.CharField(max_length=100, verbose_name="Nombre del cliente")
    telefono  = models.CharField(max_length=20,  verbose_name="Teléfono / WhatsApp")
    servicio  = models.CharField(max_length=50,  verbose_name="Servicio solicitado")
    mensaje   = models.TextField(blank=True,      verbose_name="Mensaje")
    fecha     = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de solicitud")
    estado    = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='nueva',
        verbose_name="Estado",
    )

    class Meta:
        verbose_name = "Cotización"
        verbose_name_plural = "Cotizaciones"
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.nombre} — {self.servicio} ({self.fecha.strftime('%d/%m/%Y')})"