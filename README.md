🚗 Django App - Vehicle Management

Web application built with Django + Docker + PostgreSQL, featuring authentication via OAuth2 (Google) and management of:

Brands
Models
Vehicles
🧱 Tech Stack
Python 3.12
Django 5.x
PostgreSQL
Docker & Docker Compose
HTMX / AJAX
Bootstrap
django-allauth (OAuth2)
⚙️ Getting Started
1️⃣ Clone the repository
git clone <repo-url>
cd app-django-curso-2024
2️⃣ Run with Docker
docker compose up --build

👉 If already built:

docker compose up
3️⃣ Apply migrations
docker compose exec web python manage.py migrate
4️⃣ Create superuser
docker compose exec web python manage.py createsuperuser
5️⃣ Access the app
App: http://localhost:8000
Admin: http://localhost:8000/admin
🔐 OAuth2 Setup (Google)
1️⃣ Create credentials

Go to:

👉 https://console.cloud.google.com/

Create:

OAuth Client ID
Type: Web application
2️⃣ Configure URLs
Authorized origins:
http://localhost:8000
Redirect URI:
http://localhost:8000/accounts/google/login/callback/

⚠️ IMPORTANT:

Must end with /
Must be EXACT
3️⃣ Configure in Django Admin

Go to:

/admin/socialaccount/socialapp/

Add:

Provider: Google
Client ID
Secret Key
Sites → select localhost
4️⃣ settings.py
SITE_ID = 1

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

SOCIALACCOUNT_LOGIN_ON_GET = True
🧠 System Logic
🔗 Entity relationships
Brand → Model → Vehicle
⚠️ Required order
1️⃣ Create Brand

Example:

Toyota
Ford
2️⃣ Create Model

Each model belongs to a brand:

Corolla → Toyota
Focus → Ford
3️⃣ Create Vehicle

Vehicle depends on model:

Model
License plate (register)
Year
Type
Unit of measure
💥 IMPORTANT

👉 If no models exist → vehicle cannot be saved
👉 If no brands exist → models cannot be created

👤 User Security

Each record stores:

uc → created by user
um → updated by user
🔐 Data filtering
if request.user.is_superuser:
    records = Vehiculo.objects.all()
else:
    records = Vehiculo.objects.filter(uc=request.user)

👉 Result:

Superuser → sees everything
Regular user → sees only their own records
📊 DataTables (server-side)

Endpoint:

/control/vehicles/dt

Features:

Pagination
Search
Filtering
🧩 Modals (UX)

Operations are handled through modals:

Create
Edit
Delete

⚠️ Important:

/control/vehicles/new

👉 Should NOT be accessed directly
👉 Only via button (AJAX / HTMX)

🐛 Common Issues
❌ Vehicle not saving

✔ Check:

Brands exist
Models exist
Model is selected
❌ Empty table

✔ Check:

User is logged in
uc filtering
Not using a different user
❌ OAuth not working

✔ Check:

Exact redirect URI
Correct Client ID
Site configured in admin
❌ Docker without internet (WSL)

Edit:

sudo nano /etc/resolv.conf

Add:

nameserver 8.8.8.8
nameserver 1.1.1.1
🚀 Future Improvements
Full HTMX integration (no page reloads)
Auto-refresh DataTable
Dynamic Brand → Model filtering
Live validations
UI improvements
👨‍💻 Author

Practice project built with Django + Docker + OAuth2.