from django.contrib import admin

from .models import PerfilUsuario


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    """Permite ver documento y rol de cada usuario en el panel /admin."""
    list_display = ("usuario", "documento", "rol")
    list_filter = ("rol",)
