# 🚀 Quick API Reference Card

## 🔗 Base URLs
- **Server**: `http://127.0.0.1:8000`
- **API**: `http://127.0.0.1:8000/api/auth`
- **Admin**: `http://127.0.0.1:8000/admin`

## 🔐 Authentication
```
Authorization: Token YOUR_TOKEN_HERE
```

## 📋 Quick Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| `GET` | `/` | ❌ | API info |
| `POST` | `/api/auth/register/` | ❌ | Register user |
| `POST` | `/api/auth/login/` | ❌ | Login user |
| `POST` | `/api/auth/logout/` | ✅ | Logout user |
| `GET` | `/api/auth/profile/` | ✅ | Get profile |
| `PATCH` | `/api/auth/profile/` | ✅ | Update profile |
| `POST` | `/api/auth/change-password/` | ✅ | Change password |
| `GET` | `/api/auth/user-info/` | ✅ | Get user info |
| `POST` | `/api/auth/check-email/` | ❌ | Check email |
| `POST` | `/api/auth/check-username/` | ❌ | Check username |

## 📝 User Fields

### Required:
- `username`, `email`, `password`, `first_name`, `last_name`

### Optional:
- `university`, `blood_group`, `mobile_no`, `gender`, `date_of_birth`, `address`

### Choices:
- **Blood Group**: `A+`, `A-`, `B+`, `B-`, `AB+`, `AB-`, `O+`, `O-`
- **Gender**: `M` (Male), `F` (Female), `O` (Other), `N` (Prefer not to say)

## 🎯 Quick Examples

### Register:
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john123",
    "email": "john@example.com",
    "password": "SecurePass123!",
    "password_confirm": "SecurePass123!",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

### Login:
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email_or_username": "john@example.com",
    "password": "SecurePass123!"
  }'
```

### Get Profile:
```bash
curl -X GET http://127.0.0.1:8000/api/auth/profile/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### Update Profile:
```bash
curl -X PATCH http://127.0.0.1:8000/api/auth/profile/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "university": "BUET",
    "blood_group": "A+"
  }'
```

## ⚡ Status Codes
- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `404` - Not Found

## 🧪 Test
```bash
python test_api.py
```

**📖 Full Documentation**: See `COMPLETE_API_DOCUMENTATION.md`
