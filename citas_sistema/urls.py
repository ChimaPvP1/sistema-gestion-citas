from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from accounts.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login y logout ya vienen resueltos por Django; solo le decimos
    # qué plantilla usar y el formulario que acepta correo o usuario.
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Todo lo demás (home, registro) lo maneja la app accounts.
    path('', include('accounts.urls')),
]
