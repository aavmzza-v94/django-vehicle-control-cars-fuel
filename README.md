# 🚗 Django Vehicle Management System

## 📌 Overview

Web application built with Django + Docker + PostgreSQL that allows management of:

* Vehicles
* Brands
* Models

Includes Google OAuth2 authentication, server-side DataTables, and dynamic UI with HTMX/AJAX.

---

## 🧱 Tech Stack

* Python 3.12
* Django 5.x
* PostgreSQL
* Docker & Docker Compose
* Bootstrap
* HTMX / AJAX
* django-allauth (OAuth2)

---

## ⚙️ Getting Started

### Clone repository

```bash
git clone <repo-url>
cd app-django-curso-2024
```

### Run with Docker

```bash
docker compose up --build
```

If already built:

```bash
docker compose up
```

### Apply migrations

```bash
docker compose exec web python manage.py migrate
```

### Create superuser

```bash
docker compose exec web python manage.py createsuperuser
```

### Access the app

* App: http://localhost:8000
* Admin: http://localhost:8000/admin

---

## 🔐 OAuth2 Setup (Google)

### Step 1: Create credentials

Go to: https://console.cloud.google.com/

Create:

* OAuth Client ID
* Type: Web application

---

### Step 2: Configure URLs

Authorized origin:

```
http://localhost:8000
```

Redirect URI:

```
http://localhost:8000/accounts/google/login/callback/
```

Important:

* Must end with `/`
* Must be exact

---

### Step 3: Configure in Django Admin

Go to:

```
/admin/socialaccount/socialapp/
```

Add:

* Provider: Google
* Client ID
* Secret Key
* Site: localhost

---

### Step 4: settings.py

```python
SITE_ID = 1

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

SOCIALACCOUNT_LOGIN_ON_GET = True
```

---

## 🧠 System Logic

### Entity Relationships

```
Brand → Model → Vehicle
```

---

### Required Order

1. Create Brand
2. Create Model (linked to Brand)
3. Create Vehicle (linked to Model)

---

### Important Rules

* If no brands exist → cannot create models
* If no models exist → cannot create vehicles

---

## 👤 User Security

Each record stores:

* uc → created by user
* um → updated by user

---

### Data Filtering

```python
if request.user.is_superuser:
    records = Vehiculo.objects.all()
else:
    records = Vehiculo.objects.filter(uc=request.user)
```

---

## 📊 DataTables

Endpoint:

```
/control/vehicles/dt
```

Features:

* Pagination
* Search
* Filtering

---

## 🧩 Modals

Operations:

* Create
* Edit
* Delete

Important:

```
/control/vehicles/new
```

* Should NOT be accessed directly
* Use only via AJAX / HTMX

---

## 🐛 Common Issues

### Vehicle not saving

Check:

* Brands exist
* Models exist
* Model selected

---

### Empty table

Check:

* User logged in
* Filtering by `uc`
* Correct user session

---

### OAuth not working

Check:

* Redirect URI exact
* Client ID correct
* Site configured

---

### Docker without internet (WSL)

Edit:

```bash
sudo nano /etc/resolv.conf
```

Add:

```
nameserver 8.8.8.8
nameserver 1.1.1.1
```

---

## 🚀 Future Improvements

* Full HTMX integration
* Auto-refresh tables
* Dynamic filtering Brand → Model
* Live validations
* UI improvements

---

## 📁 Project Structure

```
project/
│
├── app/
├── templates/
├── static/
├── docker/
├── manage.py
└── docker-compose.yml
```

---

## 👨‍💻 Author

Agustin Alejandro Villarreal Mazza
