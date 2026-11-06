from django.contrib import admin

# Register your models here.
from django_tenants.admin import TenantAdminMixin
from core.models import Client, Domain

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', '__str__')

    #Como cada Tenant puede tener múltiples dominios, hacer esto en la lista del admin puede generar el problema de consultas N+1 (una consulta a la base de datos por cada fila para traer su dominio).
#Para optimizarlo y hacer que tu administrador cargue al instante, añade prefetch_related en tu admin.py:

    # Optimiza la consulta trayendo todos los dominios de un solo golpe
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('domains')

    def display_name_with_domain(self, obj):
        domain = obj.domains.all()[0].domain if obj.domains.all() else "sin dominio"
        return f"{obj.name} ({domain})"
    
@admin.register(Domain)
class DomainAdmin(TenantAdminMixin, admin.ModelAdmin):
    pass