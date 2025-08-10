"""
Test script for the Login & Registration API
Run this after starting the Django server to test the endpoints
"""

import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:8000/api/auth"

def test_api():
    print("🚀 Testing Login & Registration API")
    print("=" * 50)
    
    # Test data
    test_user = {
        "username": "testuser123",
        "email": "test@example.com",
        "password": "testpassword123",
        "password_confirm": "testpassword123",
        "first_name": "Test",
        "last_name": "User",
        "university": "Test University",
        "blood_group": "A+",
        "mobile_no": "+1234567890",
        "gender": "M",
        "date_of_birth": "1995-01-01",
        "address": "123 Test Street, Test City"
    }
    
    # 1. Test Root Endpoint
    print("1. Testing root endpoint...")
    try:
        response = requests.get("http://localhost:8000/")
        if response.status_code == 200:
            print("✅ Root endpoint working")
            print(f"   Response: {response.json()['message']}")
        else:
            print("❌ Root endpoint failed")
    except Exception as e:
        print(f"❌ Root endpoint error: {e}")
    
    print()
    
    # 2. Test Email Check
    print("2. Testing email availability check...")
    try:
        response = requests.post(f"{BASE_URL}/check-email/", 
                               json={"email": test_user["email"]})
        if response.status_code == 200:
            exists = response.json()["exists"]
            print(f"✅ Email check working - Email exists: {exists}")
        else:
            print("❌ Email check failed")
    except Exception as e:
        print(f"❌ Email check error: {e}")
    
    print()
    
    # 3. Test User Registration
    print("3. Testing user registration...")
    try:
        response = requests.post(f"{BASE_URL}/register/", json=test_user)
        if response.status_code == 201:
            print("✅ Registration successful")
            data = response.json()
            token = data["token"]
            print(f"   User: {data['user']['first_name']} {data['user']['last_name']}")
            print(f"   Token: {token[:20]}...")
        else:
            print("❌ Registration failed")
            print(f"   Error: {response.json()}")
            return
    except Exception as e:
        print(f"❌ Registration error: {e}")
        return
    
    print()
    
    # 4. Test Login
    print("4. Testing user login...")
    try:
        login_data = {
            "email_or_username": test_user["email"],
            "password": test_user["password"]
        }
        response = requests.post(f"{BASE_URL}/login/", json=login_data)
        if response.status_code == 200:
            print("✅ Login successful")
            data = response.json()
            auth_token = data["token"]
            print(f"   Welcome: {data['user']['first_name']} {data['user']['last_name']}")
        else:
            print("❌ Login failed")
            print(f"   Error: {response.json()}")
            return
    except Exception as e:
        print(f"❌ Login error: {e}")
        return
    
    print()
    
    # 5. Test Profile Retrieval
    print("5. Testing profile retrieval...")
    try:
        headers = {"Authorization": f"Token {auth_token}"}
        response = requests.get(f"{BASE_URL}/profile/", headers=headers)
        if response.status_code == 200:
            print("✅ Profile retrieval successful")
            profile = response.json()
            print(f"   Email: {profile['email']}")
            print(f"   University: {profile['university']}")
            print(f"   Blood Group: {profile['blood_group']}")
        else:
            print("❌ Profile retrieval failed")
    except Exception as e:
        print(f"❌ Profile retrieval error: {e}")
    
    print()
    
    # 6. Test Profile Update
    print("6. Testing profile update...")
    try:
        headers = {"Authorization": f"Token {auth_token}"}
        update_data = {
            "university": "Updated University",
            "mobile_no": "+9876543210"
        }
        response = requests.put(f"{BASE_URL}/profile/", 
                              json=update_data, headers=headers)
        if response.status_code == 200:
            print("✅ Profile update successful")
            updated_profile = response.json()
            print(f"   Updated University: {updated_profile['university']}")
            print(f"   Updated Mobile: {updated_profile['mobile_no']}")
        else:
            print("❌ Profile update failed")
    except Exception as e:
        print(f"❌ Profile update error: {e}")
    
    print()
    
    # 7. Test Logout
    print("7. Testing logout...")
    try:
        headers = {"Authorization": f"Token {auth_token}"}
        response = requests.post(f"{BASE_URL}/logout/", headers=headers)
        if response.status_code == 200:
            print("✅ Logout successful")
            print(f"   Message: {response.json()['message']}")
        else:
            print("❌ Logout failed")
    except Exception as e:
        print(f"❌ Logout error: {e}")
    
    print()
    print("🎉 API Testing Complete!")
    print("=" * 50)

if __name__ == "__main__":
    print("Make sure the Django server is running on http://localhost:8000")
    print("Run: python manage.py runserver")
    print()
    
    try:
        test_api()
    except KeyboardInterrupt:
        print("\n\n🛑 Testing interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
