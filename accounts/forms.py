from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import PerfilUsuario


class RegistroForm(UserCreationForm):
    """
    Formulario de registro con los campos del prototipo del documento:
    nombre, documento, correo, contraseña (x2) y rol. Usa el User que
    Django trae por defecto y guarda documento y rol en PerfilUsuario.
    """
    nombre = forms.CharField(required=True, label="Nombre", widget=forms.TextInput(attrs={"placeholder": "Nombre completo"}))
    documento = forms.CharField(required=True, label="Documento", widget=forms.TextInput(attrs={"placeholder": "C.C. / N.I.T."}))
    email = forms.EmailField(required=True, label="Correo electrónico")
    rol = forms.ChoiceField(required=True, label="Rol", choices=PerfilUsuario.ROLES, initial="Paciente")

    class Meta:
        model = User
        fields = ["username", "nombre", "documento", "email", "password1", "password2", "rol"]
        labels = {
            "username": "Usuario",
        }

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.first_name = self.cleaned_data["nombre"]
        usuario.email = self.cleaned_data["email"]
        if commit:
            usuario.save()
            PerfilUsuario.objects.create(
                usuario=usuario,
                documento=self.cleaned_data["documento"],
                rol=self.cleaned_data["rol"],
            )
        return usuario


class LoginForm(AuthenticationForm):
    """
    Formulario de inicio de sesión que acepta correo O usuario, como dice
    el prototipo. Si lo escrito parece un correo, se busca a qué usuario
    pertenece y se inicia sesión con ese usuario.
    """
    username = forms.CharField(label="Correo o usuario", widget=forms.TextInput(attrs={"autofocus": True}))

    def clean_username(self):
        dato = self.cleaned_data["username"].strip()
        if "@" in dato:
            usuario = User.objects.filter(email__iexact=dato).first()
            if usuario:
                return usuario.username
        return dato
