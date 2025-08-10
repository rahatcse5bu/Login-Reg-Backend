# Project Structure

```
Login-Reg-Backend/
├── .venv/                          # Virtual environment
├── authentication/                 # Authentication app
│   ├── management/
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── create_test_superuser.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py                    # Admin configuration
│   ├── apps.py                     # App configuration
│   ├── models.py                   # User model
│   ├── serializers.py              # API serializers
│   ├── tests.py                    # Tests (default)
│   ├── urls.py                     # URL patterns
│   └── views.py                    # API views
├── login_reg_backend/              # Main project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                 # Project settings
│   ├── urls.py                     # Main URL configuration
│   └── wsgi.py
├── db.sqlite3                      # SQLite database
├── manage.py                       # Django management script
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
└── test_api.py                     # API testing script
```

## Quick Start Commands

1. **Start the server:**
   ```bash
   python manage.py runserver
   ```

2. **Create superuser:**
   ```bash
   python manage.py create_test_superuser
   ```

3. **Test the API:**
   ```bash
   python test_api.py
   ```

4. **Access admin panel:**
   http://localhost:8000/admin/
   - Username: admin
   - Password: admin123

5. **API Root:**
   http://localhost:8000/

## Key Features Implemented

✅ Custom User Model with extended fields
✅ User Registration with validation
✅ Login/Logout with token authentication
✅ Profile management (GET/UPDATE)
✅ Password change functionality
✅ Email/Username availability checking
✅ Admin panel configuration
✅ CORS support for frontend integration
✅ Comprehensive API documentation
✅ Error handling and validation
✅ Test scripts for API verification
