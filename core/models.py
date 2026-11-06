from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
    
    #Cambiar el método __str__ hará que el cliente se muestre con su dominio en todo el panel de administración (incluyendo campos de búsqueda, filtros y relaciones de clave foránea):
    def __str__(self):
        # Intentamos obtener el dominio principal asociado
        try:
            domain = self.domains.filter(is_primary=True).first()
            if not domain:
                domain = self.domains.first()
            
            domain_name = domain.domain if domain else "Sin dominio"
        except Exception:
            domain_name = "Sin dominio"

        return f"{self.name} - (dominio:{domain_name})"


class Domain(DomainMixin):
    pass

