from django.contrib import admin
from .models import Categoria, Proyecto, Cotizacion
from django.utils.html import format_html
 
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
 
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display    = ('mostrar_foto', 'titulo', 'categoria', 'fecha_finalizado')
    list_filter     = ('categoria', 'fecha_finalizado')
    search_fields   = ('titulo', 'descripcion')
    list_editable   = ('fecha_finalizado',)
 
    def mostrar_foto(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;border-radius:5px;object-fit:cover;" />',
                obj.imagen.url,
            )
        return "Sin foto"
    mostrar_foto.short_description = 'Imagen'
 
# ──────────────────────────────────────────
# NUEVO: Panel de cotizaciones
# ──────────────────────────────────────────
@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'telefono', 'servicio', 'fecha', 'estado_badge')
    list_filter   = ('estado', 'servicio')
    search_fields = ('nombre', 'telefono', 'mensaje')
    list_editable = ()          
    readonly_fields = ('fecha',)
    ordering      = ('-fecha',)
 
    # Colores por estado en la lista
    def estado_badge(self, obj):
        colores = {
            'nueva':      ('background:#fef3c7;color:#92400e', '🔔 Nueva'),
            'contactado': ('background:#dbeafe;color:#1e40af', '📞 Contactado'),
            'cerrado':    ('background:#d1fae5;color:#065f46', '✅ Cerrado'),
        }
        estilo, etiqueta = colores.get(obj.estado, ('', obj.estado))
        return format_html(
            '<span style="padding:2px 8px;border-radius:99px;font-size:12px;{}">{}</span>',
            estilo, etiqueta,
        )
    estado_badge.short_description = 'Estado'
 
admin.site.site_header  = "Administración — Maestro Ventanero"
admin.site.site_title   = "Panel de Control"
admin.site.index_title  = "Gestión de Servicios y Proyectos"