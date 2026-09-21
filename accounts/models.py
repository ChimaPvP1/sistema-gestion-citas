from django.contrib.auth.models import User
from django.db import models


class PerfilUsuario(models.Model):
    """
    Información adicional del usuario que pide el prototipo de registro
    del documento teórico: documento de identidad y rol dentro del sistema.
    Los roles corresponden a los stakeholders identificados en el proyecto.
    """
    ROLES = [
        ("Paciente", "Paciente"),
        ("Profesional", "Profesional"),
        ("Personal Administrativo", "Personal Administrativo"),
        ("Administrador del Sistema", "Administrador del Sistema"),
        ("Gerente / Dueño", "Gerente / Dueño"),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    documento = models.CharField("Documento (C.C. / N.I.T.)", max_length=20)
    rol = models.CharField("Rol", max_length=30, choices=ROLES, default="Paciente")

    def __str__(self):
        return f"{self.usuario.username} ({self.rol})"
