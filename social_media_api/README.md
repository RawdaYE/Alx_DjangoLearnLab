# Social Media API

## Setup
1. Clone the repo
2. Install requirements: `pip install django djangorestframework djangorestframework-authtoken`
3. Run migrations: `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`
5. Start server: `python manage.py runserver`

## API Endpoints
- **Register:** `/api/accounts/register/`  
  - POST `{"username": "...", "email": "...", "password": "..."}`
- **Login:** `/api/accounts/login/`  
  - POST `{"username": "...", "password": "..."}`

## User Model
- `username`, `email`, `password` (default)
- `bio`, `profile_picture`, `followers` (custom fields)
- Token returned on register/login for authentication


# Deployment Instructions

1. Set environment variables:
   - DJANGO_SECRET_KEY
   - DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
2. Install dependencies: pip install -r requirements.txt
3. Collect static files: python manage.py collectstatic
4. Apply migrations: python manage.py migrate
5. Run server: gunicorn social_media_api.wsgi
6. Access admin: /admin
