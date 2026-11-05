from django.contrib import admin

# Register your models here.
from django_tenants.admin import TenantAdminMixin
from core.models import Client, Domain

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Domain)
class DomainAdmin(TenantAdminMixin, admin.ModelAdmin):
    pass