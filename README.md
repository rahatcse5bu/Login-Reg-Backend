# Login & Registration Backend

A Django REST API backend for user authentication with comprehensive user profile management.

## Features

- User Registration with extended profile fields
- Login/Logout functionality
- Token-based authentication
- User profile management
- Password change functionality
- Email and username availability checking
- Admin panel for user management

## User Model Fields

- **Basic Fields**: username, email, password, first_name, last_name
- **Extended Fields**: university, blood_group, mobile_no, gender, date_of_birth, address
- **System Fields**: created_at, updated_at, date_joined, last_login

## API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description | Authentication Required |
|--------|----------|-------------|------------------------|
| POST | `/api/auth/register/` | Register a new user | No |
| POST | `/api/auth/login/` | Login user | No |
| POST | `/api/auth/logout/` | Logout user | Yes |
| GET/PUT | `/api/auth/profile/` | Get/Update user profile | Yes |
| POST | `/api/auth/change-password/` | Change password | Yes |
| GET | `/api/auth/user-info/` | Get current user info | Yes |
| POST | `/api/auth/check-email/` | Check if email exists | No |
| POST | `/api/auth/check-username/` | Check if username exists | No |

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Login-Reg-Backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## API Usage Examples

### 1. User Registration

**POST** `/api/auth/register/`

```json
{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123",
    "password_confirm": "securepassword123",
    "first_name": "John",
    "last_name": "Doe",
    "university": "Example University",
    "blood_group": "A+",
    "mobile_no": "+1234567890",
    "gender": "M",
    "date_of_birth": "1995-05-15",
    "address": "123 Main St, City, Country"
}
```

**Response:**
```json
{
    "message": "User registered successfully",
    "user": {
        "id": 1,
        "username": "johndoe",
        "email": "john@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "university": "Example University",
        "blood_group": "A+",
        "mobile_no": "+1234567890",
        "gender": "M",
        "date_of_birth": "1995-05-15",
        "address": "123 Main St, City, Country"
    },
    "token": "your-auth-token-here"
}
```

### 2. User Login

**POST** `/api/auth/login/`

```json
{
    "email_or_username": "john@example.com",
    "password": "securepassword123"
}
```

**Response:**
```json
{
    "message": "Login successful",
    "user": {
        "id": 1,
        "username": "johndoe",
        "email": "john@example.com",
        "first_name": "John",
        "last_name": "Doe"
    },
    "token": "your-auth-token-here"
}
```

### 3. Get User Profile

**GET** `/api/auth/profile/`

**Headers:**
```
Authorization: Token your-auth-token-here
```

**Response:**
```json
{
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "university": "Example University",
    "blood_group": "A+",
    "mobile_no": "+1234567890",
    "gender": "M",
    "date_of_birth": "1995-05-15",
    "address": "123 Main St, City, Country",
    "date_joined": "2025-08-11T10:30:00Z",
    "last_login": "2025-08-11T12:15:00Z"
}
```

### 4. Update User Profile

**PUT** `/api/auth/profile/`

**Headers:**
```
Authorization: Token your-auth-token-here
Content-Type: application/json
```

```json
{
    "first_name": "John Updated",
    "university": "New University",
    "mobile_no": "+9876543210"
}
```

### 5. Change Password

**POST** `/api/auth/change-password/`

**Headers:**
```
Authorization: Token your-auth-token-here
```

```json
{
    "old_password": "securepassword123",
    "new_password": "newsecurepassword456",
    "new_password_confirm": "newsecurepassword456"
}
```

### 6. Check Email Availability

**POST** `/api/auth/check-email/`

```json
{
    "email": "test@example.com"
}
```

**Response:**
```json
{
    "exists": false
}
```

### 7. Logout

**POST** `/api/auth/logout/`

**Headers:**
```
Authorization: Token your-auth-token-here
```

**Response:**
```json
{
    "message": "Logout successful"
}
```

## Gender Choices

- `M`: Male
- `F`: Female
- `O`: Other
- `N`: Prefer not to say

## Blood Group Choices

- `A+`, `A-`
- `B+`, `B-`
- `AB+`, `AB-`
- `O+`, `O-`

## Authentication

This API uses Token-based authentication. After login or registration, include the token in the Authorization header:

```
Authorization: Token your-auth-token-here
```

## Admin Panel

Access the Django admin panel at `/admin/` to manage users, view registrations, and perform administrative tasks.

## Error Handling

The API returns appropriate HTTP status codes and error messages:

- `400 Bad Request`: Invalid data or validation errors
- `401 Unauthorized`: Authentication required
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

Example error response:
```json
{
    "email": ["User with this email address already exists."],
    "password": ["This password is too short. It must contain at least 8 characters."]
}
```

## Development Notes

- The API includes CORS headers for frontend integration
- SQLite database is used by default (change in settings.py for production)
- Token authentication is implemented for API access
- All passwords are hashed using Django's built-in password hashing
- Input validation is implemented for all fields
- Email uniqueness is enforced
- The custom User model extends Django's AbstractUser
