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
