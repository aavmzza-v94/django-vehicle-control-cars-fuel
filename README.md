# 🚗 App Django - Control de Vehículos

Aplicación web desarrollada en **Django + Docker + PostgreSQL**, con autenticación mediante **OAuth2 (Google)** y gestión de:

* Marcas
* Modelos
* Vehículos

---

# 🧱 Tecnologías utilizadas

* Python 3.12
* Django 5.x
* PostgreSQL
* Docker & Docker Compose
* HTMX / AJAX
* Bootstrap
* django-allauth (OAuth2)

---

# ⚙️ Levantar el proyecto

## 1️⃣ Clonar repositorio

```bash
git clone <repo-url>
cd app-django-curso-2024
```

---

## 2️⃣ Levantar con Docker

```bash
docker compose up --build
```

👉 Si ya estaba construido:

```bash
docker compose up
```

---

## 3️⃣ Ejecutar migraciones

```bash
docker compose exec web python manage.py migrate
```

---

## 4️⃣ Crear superusuario

```bash
docker compose exec web python manage.py createsuperuser
```

---

## 5️⃣ Acceder a la app

* App: http://localhost:8000
* Admin: http://localhost:8000/admin

---

# 🔐 Configuración OAuth2 (Google)

## 1️⃣ Crear credenciales

Ir a:

👉 https://console.cloud.google.com/

Crear:

* OAuth Client ID
* Tipo: **Web application**

---

## 2️⃣ Configurar URLs

### Orígenes autorizados:

```text
http://localhost:8000
```

---

### URI de redirección:

```text
http://localhost:8000/accounts/google/login/callback/
```

⚠️ IMPORTANTE:

* Debe terminar en `/`
* Debe ser EXACTA

---

## 3️⃣ Configurar en Django Admin

Entrar a:

```
/admin/socialaccount/socialapp/
```

Agregar:

* Provider: Google
* Client ID
* Secret Key
* Sites → seleccionar `localhost`

---

## 4️⃣ settings.py

```python
SITE_ID = 1

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

SOCIALACCOUNT_LOGIN_ON_GET = True
```

---

# 🧠 Lógica del sistema

## 🔗 Relación de entidades

```
Marca → Modelo → Vehículo
```

---

## ⚠️ Orden obligatorio

### 1️⃣ Crear Marca

Ejemplo:

* Toyota
* Ford

---

### 2️⃣ Crear Modelo

Cada modelo pertenece a una marca:

* Corolla → Toyota
* Focus → Ford

---

### 3️⃣ Crear Vehículo

El vehículo depende del modelo:

* Modelo
* Registro (patente)
* Año
* Tipo
* Unidad de medida

---

## 💥 IMPORTANTE

👉 Si no existen modelos → **NO se puede guardar vehículo**
👉 Si no existen marcas → **NO se pueden crear modelos**

---

# 👤 Seguridad por usuario

Cada registro guarda:

```text
uc → usuario creador
um → usuario modificador
```

---

## 🔐 Filtro de datos

```python
if request.user.is_superuser:
    registros = Vehiculo.objects.all()
else:
    registros = Vehiculo.objects.filter(uc=request.user)
```

---

👉 Resultado:

* Superuser → ve todo
* Usuario normal → solo sus registros

---

# 📊 DataTables (server-side)

Endpoint:

```text
/control/vehicles/dt
```

Funcionalidades:

* Paginación
* Búsqueda
* Filtros

---

# 🧩 Modales (UX)

Las operaciones se hacen mediante modales:

* Crear
* Editar
* Eliminar

---

⚠️ Importante:

```text
/control/vehicles/new
```

👉 NO debe abrirse directamente
👉 Solo mediante botón (AJAX / HTMX)

---

# 🐛 Problemas comunes

## ❌ No guarda vehículo

✔ Verificar:

* Existen marcas
* Existen modelos
* Se seleccionó modelo

---

## ❌ Tabla vacía

✔ Verificar:

* Usuario logueado
* Filtro por `uc`
* No estar con otro usuario

---

## ❌ OAuth no funciona

✔ Revisar:

* Redirect URI exacta
* Client ID correcto
* Site configurado en admin

---

## ❌ Docker sin internet (WSL)

Editar:

```bash
sudo nano /etc/resolv.conf
```

Agregar:

```text
nameserver 8.8.8.8
nameserver 1.1.1.1
```

---

# 🚀 Mejoras futuras

* HTMX completo (sin recarga)
* Refresh automático de tabla
* Filtro dinámico Marca → Modelo
* Validaciones en vivo
* UI mejorada

---

# 👨‍💻 Autor

Proyecto de práctica avanzada con Django + Docker + OAuth2.

---
