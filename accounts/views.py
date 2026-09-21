from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegistroForm


def registro(request):
    """
    Muestra el formulario de registro y crea el usuario cuando lo envía.
    Si el registro es exitoso, deja al usuario con la sesión ya iniciada.
    """
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "¡Cuenta creada correctamente!")
            return redirect("home")
    else:
        form = RegistroForm()

    return render(request, "accounts/registro.html", {"form": form})


@login_required
def home(request):
    """
    Página que solo puede ver un usuario que ya inició sesión.
    Sirve para comprobar que la autenticación está funcionando.
    """
    return render(request, "accounts/home.html")
