# 📚 Django Login & Registration Backend - Complete API Documentation

## 🌐 Base Information

**Base URL**: `http://127.0.0.1:8000`  
**API Base URL**: `http://127.0.0.1:8000/api/auth`  
**Version**: Django 3.2.25 with MySQL Backend  
**Authentication**: Token-based Authentication  
**Content-Type**: `application/json`  

---

## 🔗 API Endpoints Overview

| Method | Endpoint | Description | Auth Required | 
|--------|----------|-------------|---------------|
| GET | `/` | Root endpoint with API info | No |
| POST | `/api/auth/register/` | Register new user | No |
| POST | `/api/auth/login/` | User login | No |
| POST | `/api/auth/logout/` | User logout | Yes |
| GET | `/api/auth/profile/` | Get user profile | Yes |
| PATCH | `/api/auth/profile/` | Update user profile | Yes |
| POST | `/api/auth/change-password/` | Change password | Yes |
| GET | `/api/auth/user-info/` | Get user info | Yes |
| POST | `/api/auth/check-email/` | Check email availability | No |
| POST | `/api/auth/check-username/` | Check username availability | No |

---

## 🔐 Authentication

### Token-Based Authentication
All protected endpoints require an Authorization header:

```
Authorization: Token YOUR_TOKEN_HERE
```

### Example Headers for Protected Routes:
```json
{
  "Content-Type": "application/json",
  "Authorization": "Token f9c31b0b982eaef2d65c715cd1a0378c50a7fc58"
}
```

---

## 📋 User Model Fields

### Required Fields:
- `username` (string, unique, max 150 chars)
- `email` (string, unique, valid email)
- `password` (string, min 8 chars)
- `first_name` (string, max 50 chars)
- `last_name` (string, max 50 chars)

### Optional Fields:
- `university` (string, max 200 chars)
- `blood_group` (string, choices: A+, A-, B+, B-, AB+, AB-, O+, O-)
- `mobile_no` (string, max 15 chars)
- `gender` (string, choices: M, F, O, N)
- `date_of_birth` (date, format: YYYY-MM-DD)
- `address` (text)

### System Fields (Read-only):
- `id` (integer, auto-increment)
- `date_joined` (datetime)
- `last_login` (datetime)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 🎯 Detailed API Endpoints

### 1. Root Endpoint
**Get API Information**

```http
GET http://127.0.0.1:8000/
```

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Response (200 OK):**
```json
{
  "message": "Welcome to Login & Registration Backend API",
  "endpoints": {
    "register": "/api/auth/register/",
    "login": "/api/auth/login/",
    "logout": "/api/auth/logout/",
    "profile": "/api/auth/profile/",
    "change-password": "/api/auth/change-password/",
    "user-info": "/api/auth/user-info/",
    "check-email": "/api/auth/check-email/",
    "check-username": "/api/auth/check-username/",
    "admin": "/admin/"
  }
}
```

---

### 2. User Registration
**Register a new user with all fields**

```http
POST http://127.0.0.1:8000/api/auth/register/
```

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Request Body:**
```json
{
  "username": "johndoe123",
  "email": "john.doe@example.com",
  "password": "SecurePassword123!",
  "password_confirm": "SecurePassword123!",
  "first_name": "John",
  "last_name": "Doe",
  "university": "University of Dhaka",
  "blood_group": "A+",
  "mobile_no": "+8801234567890",
  "gender": "M",
  "date_of_birth": "1995-05-15",
  "address": "123 Main Street, Dhaka, Bangladesh"
}
```

**Response (201 Created):**
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 3,
    "username": "johndoe123",
    "email": "john.doe@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "university": "University of Dhaka",
    "blood_group": "A+",
    "mobile_no": "+8801234567890",
    "gender": "M",
    "date_of_birth": "1995-05-15",
    "address": "123 Main Street, Dhaka, Bangladesh",
    "date_joined": "2025-08-11T01:35:35.927344Z",
    "last_login": null,
    "created_at": "2025-08-11T01:35:35.929360Z",
    "updated_at": "2025-08-11T01:35:36.109904Z"
  },
  "token": "f9c31b0b982eaef2d65c715cd1a0378c50a7fc58"
}
```

**Error Response (400 Bad Request):**
```json
{
  "email": ["User with this email already exists."],
  "username": ["A user with that username already exists."],
  "password": ["This password is too common."]
}
```

---

### 3. User Login
**Login with email or username**

```http
POST http://127.0.0.1:8000/api/auth/login/
```

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Request Body (Email):**
```json
{
  "email_or_username": "john.doe@example.com",
  "password": "SecurePassword123!"
}
```

**Request Body (Username):**
```json
{
  "email_or_username": "johndoe123",
  "password": "SecurePassword123!"
}
```

**Response (200 OK):**
```json
{
  "message": "Login successful",
  "user": {
    "id": 3,
    "username": "johndoe123",
    "email": "john.doe@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "university": "University of Dhaka",
    "blood_group": "A+",
    "mobile_no": "+8801234567890",
    "gender": "M",
    "date_of_birth": "1995-05-15",
    "address": "123 Main Street, Dhaka, Bangladesh",
    "date_joined": "2025-08-11T01:35:35.927344Z",
    "last_login": "2025-08-11T01:40:22.802706Z",
    "created_at": "2025-08-11T01:35:35.929360Z",
    "updated_at": "2025-08-11T01:35:36.109904Z"
  },
  "token": "f9c31b0b982eaef2d65c715cd1a0378c50a7fc58"
}
```

**Error Response (400 Bad Request):**
```json
{
  "non_field_errors": ["Invalid credentials"]
}
```

---

### 4. User Logout
**Logout and invalidate token**

```http
POST http://127.0.0.1:8000/api/auth/logout/
```

**Headers:**
```json
{
  "Content-Type": "application/json",
  "Authorization": "Token f9c31b0b982eaef2d65c715cd1a0378c50a7fc58"
}
```

**Request Body:** (Empty)
```json
{}
```

**Response (200 OK):**
```json
{
  "message": "Logout successful"
}
```

**Error Response (401 Unauthorized):**
```json
{
  "detail": "Invalid token."
}
```

---

### 5. Get User Profile
**Retrieve current user's profile**

```http
GET http://127.0.0.1:8000/api/auth/profile/
```

**Headers:**
```json
{
  "Content-Type": "application/json",
  "Authorization": "Token f9c31b0b982eaef2d65c715cd1a0378c50a7fc58"
}
```

**Response (200 OK):**
```json
{
  "id": 3,
  "username": "johndoe123",
  "email": "john.doe@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "university": "University of Dhaka",
  "blood_group": "A+",
  "mobile_no": "+8801234567890",
  "gender": "M",
  "date_of_birth": "1995-05-15",
  "address": "123 Main Street, Dhaka, Bangladesh",
  "date_joined": "2025-08-11T01:35:35.927344Z",
  "last_login": "2025-08-11T01:40:22.802706Z",
  "created_at": "2025-08-11T01:35:35.929360Z",
  "updated_at": "2025-08-11T01:35:36.109904Z"
}
```

---

### 6. Update User Profile
**Update current user's profile (partial update)**

```http
PATCH http://127.0.0.1:8000/api/auth/profile/
```

**Headers:**
```json
{
  "Content-Type": "application/json",
  "Authorization": "Token f9c31b0b982eaef2d65c715cd1a0378c50a7fc58"
}
```

**Request Body (Partial Update):**
```json
{
  "first_name": "Jane",
  "last_name": "Smith",
  "university": "BUET",
  "blood_group": "B+",
  "mobile_no": "+8801987654321",
  "gender": "F"
}
```

**Response (200 OK):**
```json
{
  "id": 3,
  "username": "johndoe123",
  "email": "john.doe@example.com",
  "first_name": "Jane",
  "last_name": "Smith",
  "university": "BUET",
  "blood_group": "B+",
  "mobile_no": "+8801987654321",
  "gender": "F",
  "date_of_birth": "1995-05-15",
  "address": "123 Main Street, Dhaka, Bangladesh",
  "date_joined": "2025-08-11T01:35:35.927344Z",
  "last_login": "2025-08-11T01:40:22.802706Z",
  "created_at": "2025-08-11T01:35:35.929360Z",
  "updated_at": "2025-08-11T01:45:15.375313Z"
}
```

---

### 7. Change Password
**Change user's password**

```http
POST http://127.0.0.1:8000/api/auth/change-password/
```

**Headers:**
```json
{
  "Content-Type": "application/json",
  "Authorization": "Token f9c31b0b982eaef2d65c715cd1a0378c50a7fc58"
}
```

**Request Body:**
```json
{
  "old_password": "SecurePassword123!",
  "new_password": "NewSecurePassword456!",
  "new_password_confirm": "NewSecurePassword456!"
}
```

**Response (200 OK):**
```json
{
  "message": "Password changed successfully",
  "token": "6c86a46d005332af4d444daf0147aeb71873c4c6"
}
```

**Error Response (400 Bad Request):**
```json
{
  "old_password": ["Old password is incorrect"],
  "new_password": ["This password is too common."]
}
```

---

### 8. Get User Info
**Get current user information (same as profile)**

```http
GET http://127.0.0.1:8000/api/auth/user-info/
```

**Headers:**
```json
{
  "Content-Type": "application/json",
  "Authorization": "Token f9c31b0b982eaef2d65c715cd1a0378c50a7fc58"
}
```

**Response (200 OK):**
```json
{
  "id": 3,
  "username": "johndoe123",
  "email": "john.doe@example.com",
  "first_name": "Jane",
  "last_name": "Smith",
  "university": "BUET",
  "blood_group": "B+",
  "mobile_no": "+8801987654321",
  "gender": "F",
  "date_of_birth": "1995-05-15",
  "address": "123 Main Street, Dhaka, Bangladesh",
  "date_joined": "2025-08-11T01:35:35.927344Z",
  "last_login": "2025-08-11T01:40:22.802706Z",
  "created_at": "2025-08-11T01:35:35.929360Z",
  "updated_at": "2025-08-11T01:45:15.375313Z"
}
```

---

### 9. Check Email Availability
**Check if email already exists**

```http
POST http://127.0.0.1:8000/api/auth/check-email/
```

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Request Body:**
```json
{
  "email": "john.doe@example.com"
}
```

**Response (200 OK):**
```json
{
  "exists": true
}
```

**Error Response (400 Bad Request):**
```json
{
  "error": "Email is required"
}
```

---

### 10. Check Username Availability
**Check if username already exists**

```http
POST http://127.0.0.1:8000/api/auth/check-username/
```

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Request Body:**
```json
{
  "username": "johndoe123"
}
```

**Response (200 OK):**
```json
{
  "exists": true
}
```

**Error Response (400 Bad Request):**
```json
{
  "error": "Username is required"
}
```

---

## 🛡️ Error Handling

### Common HTTP Status Codes:

| Status Code | Description | When It Occurs |
|-------------|-------------|----------------|
| 200 | OK | Successful GET, PATCH requests |
| 201 | Created | Successful POST (registration) |
| 400 | Bad Request | Validation errors, invalid data |
| 401 | Unauthorized | Invalid/missing token |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Endpoint doesn't exist |
| 405 | Method Not Allowed | Wrong HTTP method |
| 500 | Internal Server Error | Server error |

### Error Response Format:
```json
{
  "field_name": ["Error message for this field"],
  "another_field": ["Another error message"],
  "non_field_errors": ["General error message"]
}
```

### Authentication Errors:
```json
{
  "detail": "Invalid token."
}
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

---

## 🔧 Field Validation Rules

### Password Requirements:
- Minimum 8 characters
- Cannot be too common
- Cannot be entirely numeric
- Cannot be too similar to user information

### Email Requirements:
- Valid email format
- Unique (no duplicates)
- Required field

### Username Requirements:
- Maximum 150 characters
- Unique (no duplicates)
- Letters, numbers, and @/./+/-/_ characters only

### Blood Group Choices:
- `A+`, `A-`, `B+`, `B-`, `AB+`, `AB-`, `O+`, `O-`

### Gender Choices:
- `M` (Male)
- `F` (Female)
- `O` (Other)
- `N` (Prefer not to say)

---

## 📱 Frontend Integration Examples

### JavaScript/Fetch Example:

```javascript
// Registration
const registerUser = async (userData) => {
  const response = await fetch('http://127.0.0.1:8000/api/auth/register/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData)
  });
  
  const data = await response.json();
  
  if (response.ok) {
    // Store token
    localStorage.setItem('authToken', data.token);
    return data;
  } else {
    throw new Error(data);
  }
};

// Login
const loginUser = async (email, password) => {
  const response = await fetch('http://127.0.0.1:8000/api/auth/login/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      email_or_username: email,
      password: password
    })
  });
  
  const data = await response.json();
  
  if (response.ok) {
    localStorage.setItem('authToken', data.token);
    return data;
  } else {
    throw new Error(data);
  }
};

// Get Profile (Protected Route)
const getUserProfile = async () => {
  const token = localStorage.getItem('authToken');
  
  const response = await fetch('http://127.0.0.1:8000/api/auth/profile/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Token ${token}`
    }
  });
  
  const data = await response.json();
  
  if (response.ok) {
    return data;
  } else {
    throw new Error(data);
  }
};

// Update Profile
const updateProfile = async (updateData) => {
  const token = localStorage.getItem('authToken');
  
  const response = await fetch('http://127.0.0.1:8000/api/auth/profile/', {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Token ${token}`
    },
    body: JSON.stringify(updateData)
  });
  
  const data = await response.json();
  
  if (response.ok) {
    return data;
  } else {
    throw new Error(data);
  }
};

// Logout
const logoutUser = async () => {
  const token = localStorage.getItem('authToken');
  
  const response = await fetch('http://127.0.0.1:8000/api/auth/logout/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Token ${token}`
    }
  });
  
  if (response.ok) {
    localStorage.removeItem('authToken');
    return true;
  } else {
    throw new Error('Logout failed');
  }
};
```

### React Hook Example:

```javascript
import { useState, useEffect } from 'react';

const useAuth = () => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('authToken'));
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (token) {
      fetchUserProfile();
    }
  }, [token]);

  const fetchUserProfile = async () => {
    try {
      setLoading(true);
      const response = await fetch('http://127.0.0.1:8000/api/auth/profile/', {
        headers: {
          'Authorization': `Token ${token}`,
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        const userData = await response.json();
        setUser(userData);
      } else {
        logout();
      }
    } catch (error) {
      console.error('Error fetching profile:', error);
      logout();
    } finally {
      setLoading(false);
    }
  };

  const login = async (email, password) => {
    try {
      setLoading(true);
      const response = await fetch('http://127.0.0.1:8000/api/auth/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email_or_username: email,
          password: password
        })
      });

      if (response.ok) {
        const data = await response.json();
        setToken(data.token);
        setUser(data.user);
        localStorage.setItem('authToken', data.token);
        return data;
      } else {
        const errorData = await response.json();
        throw new Error(JSON.stringify(errorData));
      }
    } catch (error) {
      throw error;
    } finally {
      setLoading(false);
    }
  };

  const logout = async () => {
    try {
      if (token) {
        await fetch('http://127.0.0.1:8000/api/auth/logout/', {
          method: 'POST',
          headers: {
            'Authorization': `Token ${token}`,
            'Content-Type': 'application/json'
          }
        });
      }
    } catch (error) {
      console.error('Logout error:', error);
    } finally {
      setToken(null);
      setUser(null);
      localStorage.removeItem('authToken');
    }
  };

  return {
    user,
    token,
    loading,
    login,
    logout,
    isAuthenticated: !!token && !!user
  };
};

export default useAuth;
```

---

## 🔧 Environment Variables

```bash
# .env file
DB_NAME=login_reg_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306

SECRET_KEY=your_secret_key_here
DEBUG=True

# CORS Settings
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8080
```

---

## 🚀 Testing

### Run API Tests:
```bash
python test_api.py
```

### Test Coverage:
- ✅ User Registration (all fields)
- ✅ User Login (email and username)
- ✅ User Logout
- ✅ Profile Management
- ✅ Password Change
- ✅ Email/Username Availability
- ✅ Authentication & Authorization
- ✅ Error Handling

---

## 📊 Database Schema

### User Table (`authentication_user`):
```sql
CREATE TABLE authentication_user (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  password VARCHAR(128) NOT NULL,
  last_login DATETIME(6),
  is_superuser TINYINT(1) NOT NULL,
  username VARCHAR(150) UNIQUE NOT NULL,
  is_staff TINYINT(1) NOT NULL,
  is_active TINYINT(1) NOT NULL,
  date_joined DATETIME(6) NOT NULL,
  email VARCHAR(254) UNIQUE NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  university VARCHAR(200),
  blood_group VARCHAR(3),
  mobile_no VARCHAR(15),
  gender VARCHAR(1),
  date_of_birth DATE,
  address LONGTEXT,
  created_at DATETIME(6) NOT NULL,
  updated_at DATETIME(6) NOT NULL
);
```

### Token Table (`authtoken_token`):
```sql
CREATE TABLE authtoken_token (
  key VARCHAR(40) PRIMARY KEY,
  created DATETIME(6) NOT NULL,
  user_id BIGINT UNIQUE NOT NULL,
  FOREIGN KEY (user_id) REFERENCES authentication_user(id)
);
```

---

## 🏗️ Project Structure

```
f:\Projects\Login-Reg-Backend\
├── authentication/              # Authentication app
│   ├── models.py               # User model
│   ├── serializers.py          # API serializers
│   ├── views.py                # API views
│   ├── urls.py                 # URL routing
│   ├── admin.py                # Admin configuration
│   └── migrations/             # Database migrations
├── login_reg_backend/          # Main project
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py                 # WSGI configuration
├── .env                        # Environment variables
├── requirements.txt            # Dependencies
├── test_api.py                 # API testing script
└── manage.py                   # Django management
```

---

## 🎯 Production Considerations

### Security:
- Use HTTPS in production
- Set `DEBUG = False`
- Use strong `SECRET_KEY`
- Configure proper CORS settings
- Use environment variables for sensitive data

### Database:
- Use connection pooling
- Set up database backups
- Monitor query performance
- Use database indexes

### Deployment:
- Use production WSGI server (Gunicorn)
- Set up reverse proxy (Nginx)
- Configure static file serving
- Set up monitoring and logging

---

## 📞 Support & Resources

### Documentation Files:
- `API_DOCUMENTATION.md` - Complete API guide
- `MYSQL_SETUP.md` - Database setup guide
- `COMPLETE_SETUP_SUCCESS.md` - Setup summary

### Test Files:
- `test_api.py` - Comprehensive API testing

### Configuration:
- `.env` - Environment variables
- `requirements.txt` - Python dependencies

---

**🎊 Your Django REST API with MySQL is fully documented and ready for frontend integration!**
