from django.contrib import admin
from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'precio')
    search_fields = ('marca', 'modelo')

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.has_perm('vehiculo.add_vehiculo')

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.has_perm('vehiculo.change_vehiculo')

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.has_perm('vehiculo.delete_vehiculo')