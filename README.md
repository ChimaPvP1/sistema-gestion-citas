# Sistema de Gestión de Citas — Autenticación de Usuarios

Entrega: **Configuración del Entorno y Autenticación de Usuarios**
Framework: **Django** (Python) · Base de datos: **SQLite** (incluida en Python, no hay que instalar nada aparte)

## ¿Qué trae este proyecto?

- Registro de usuarios (crea una cuenta con usuario, correo y contraseña).
- Inicio de sesión (login).
- Cierre de sesión (logout).
- Una página de inicio que **solo se puede ver si iniciaste sesión** (así se comprueba que la autenticación funciona).
- Interfaz sencilla en HTML con un poco de CSS, sin librerías externas de diseño.

---

## 1. Requisitos previos

Tener **Python 3.10 o superior** instalado. Para comprobarlo, abre una terminal (CMD, PowerShell o Terminal) y escribe:

```
python --version
```

Si no lo tienes, descárgalo de [python.org/downloads](https://www.python.org/downloads/).

---

## 2. Configurar el entorno virtual

Un entorno virtual es una carpeta aislada donde se instalan las librerías **solo para este proyecto**, sin mezclarlas con otros. Desde la carpeta del proyecto (donde está `manage.py`):

**Windows (CMD o PowerShell):**
```
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```
python3 -m venv venv
source venv/bin/activate
```

Cuando el entorno esté activo, verás `(venv)` al inicio de la línea de la terminal.

## 3. Instalar Django

Con el entorno virtual activo:

```
pip install -r requirements.txt
```

## 4. Crear la base de datos

Django crea automáticamente el archivo de base de datos (`db.sqlite3`) y las tablas necesarias (usuarios, sesiones, etc.) con este comando:

```
python manage.py migrate
```

Esto es lo que cumple el entregable de "crear la base de datos y las configuraciones iniciales".

## 5. Ejecutar el proyecto

```
python manage.py runserver
```

Abre el navegador en: **http://127.0.0.1:8000/**

Como aún no has iniciado sesión, te va a redirigir automáticamente a la pantalla de login. Desde ahí:

1. Haz clic en **"Regístrate aquí"** y crea una cuenta de prueba.
2. Verás la página de inicio con el mensaje "¡Bienvenido, [tu usuario]!" — esto confirma que la autenticación funciona.
3. Prueba cerrar sesión y volver a entrar con las mismas credenciales.
4. Prueba entrar con una contraseña incorrecta para ver el mensaje de error.

### (Opcional) Ver los usuarios registrados en el panel de administración

Esto es una forma extra de comprobar que la base de datos está guardando los usuarios:

```
python manage.py createsuperuser
```

Sigue las instrucciones (usuario, correo, contraseña) y luego entra a **http://127.0.0.1:8000/admin/** con esos datos. Ahí, en "Users", verás todos los usuarios que se han registrado.

---

## 6. Subir el proyecto a GitHub

1. Crea un repositorio nuevo y vacío en [github.com](https://github.com/new) (sin README, sin .gitignore — ya los trae este proyecto).
2. En la terminal, dentro de la carpeta del proyecto:

```
git init
git add .
git commit -m "Configuración inicial del proyecto y autenticación de usuarios"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/NOMBRE-DEL-REPOSITORIO.git
git push -u origin main
```

Reemplaza la URL por la de tu repositorio (la copias del botón verde "Code" en GitHub).

> El archivo `.gitignore` ya está configurado para que **no** se suban el entorno virtual (`venv/`) ni el archivo `db.sqlite3` — cada persona que clone el repositorio genera su propia base de datos local con `python manage.py migrate`.

---

## Estructura del proyecto

```
proyecto_login/
├── citas_sistema/       # Configuración del proyecto (settings, urls)
├── accounts/             # App de autenticación (registro, home)
│   ├── forms.py          # Formulario de registro
│   ├── views.py          # Lógica de registro y página protegida
│   ├── urls.py
│   └── templates/accounts/
├── templates/
│   ├── base.html          # Plantilla base con el diseño
│   └── registration/login.html
├── manage.py
├── requirements.txt
└── .gitignore
```
