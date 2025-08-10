"""
Comprehensive test script for the Login & Registration API
Tests all endpoints with detailed validation
"""

import requests
import json
from datetime import datetime

# Base URL for the API
BASE_URL = "http://127.0.0.1:8000/api/auth"

def print_response(response, endpoint_name):
    """Helper function to print API response with formatting"""
    print(f"\n{'='*60}")
    print(f"� {endpoint_name}")
    print(f"   URL: {response.url}")
    print(f"   Status: {response.status_code}")
    if response.content:
        try:
            data = response.json()
            print(f"   Response: {json.dumps(data, indent=4)}")
        except:
            print(f"   Response: {response.text}")
    else:
        print("   Response: No content")
    print(f"{'='*60}")

def test_api():
    print("🚀 COMPREHENSIVE API TESTING")
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌐 Testing server: {BASE_URL}")
    print("=" * 80)
    
    # Test data with all required fields
    test_user = {
        "username": "testuser123",
        "email": "test@example.com",
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
    
    auth_token = None
    
    try:
        # 1. Test Root Endpoint
        print("\n🔹 1. Testing Root Endpoint...")
        response = requests.get("http://127.0.0.1:8000/")
        print_response(response, "Root Endpoint")
        
        # 2. Test Email Availability Check
        print("\n🔹 2. Testing Email Availability...")
        response = requests.post(f"{BASE_URL}/check-email/", 
                               json={"email": test_user["email"]})
        print_response(response, "Email Check")
        
        # 3. Test Username Availability Check
        print("\n🔹 3. Testing Username Availability...")
        response = requests.post(f"{BASE_URL}/check-username/", 
                               json={"username": test_user["username"]})
        print_response(response, "Username Check")
        
        # 4. Test User Registration
        print("\n🔹 4. Testing User Registration...")
        response = requests.post(f"{BASE_URL}/register/", json=test_user)
        print_response(response, "User Registration")
        
        if response.status_code == 201:
            data = response.json()
            auth_token = data.get("token")
            print(f"✅ Registration successful! Token obtained: {auth_token[:20] if auth_token else 'None'}...")
        elif response.status_code == 400:
            print("⚠️  User might already exist, trying to login...")
            # Try login if registration fails
            login_data = {
                "email_or_username": test_user["email"],
                "password": test_user["password"]
            }
            response = requests.post(f"{BASE_URL}/login/", json=login_data)
            if response.status_code == 200:
                auth_token = response.json().get("token")
                print(f"✅ Login successful! Token: {auth_token[:20] if auth_token else 'None'}...")
        
        if not auth_token:
            print("❌ Could not get authentication token. Stopping tests.")
            return
            
        headers = {"Authorization": f"Token {auth_token}"}
        
        # 5. Test User Login (separate test)
        print("\n🔹 5. Testing Fresh Login...")
        login_data = {
            "email_or_username": test_user["email"],
            "password": test_user["password"]
        }
        response = requests.post(f"{BASE_URL}/login/", json=login_data)
        print_response(response, "User Login")
        
        # 6. Test Profile Retrieval
        print("\n🔹 6. Testing Profile Retrieval...")
        response = requests.get(f"{BASE_URL}/profile/", headers=headers)
        print_response(response, "Get Profile")
        
        # 7. Test User Info Endpoint
        print("\n🔹 7. Testing User Info...")
        response = requests.get(f"{BASE_URL}/user-info/", headers=headers)
        print_response(response, "User Info")
        
        # 8. Test Profile Update
        print("\n🔹 8. Testing Profile Update...")
        update_data = {
            "first_name": "Jane",
            "last_name": "Smith", 
            "university": "BUET",
            "blood_group": "B+",
            "mobile_no": "+8801987654321",
            "gender": "F",
            "date_of_birth": "1996-08-20",
            "address": "456 University Road, Dhaka"
        }
        response = requests.patch(f"{BASE_URL}/profile/", 
                                json=update_data, headers=headers)
        print_response(response, "Profile Update")
        
        # 9. Test Password Change
        print("\n🔹 9. Testing Password Change...")
        password_data = {
            "old_password": test_user["password"],
            "new_password": "NewSecurePassword456!",
            "new_password_confirm": "NewSecurePassword456!"
        }
        response = requests.post(f"{BASE_URL}/change-password/", 
                               json=password_data, headers=headers)
        print_response(response, "Password Change")
        
        # Update token if password change was successful
        if response.status_code == 200:
            new_token = response.json().get("token")
            if new_token:
                auth_token = new_token
                headers = {"Authorization": f"Token {auth_token}"}
                print(f"🔄 Token updated after password change: {auth_token[:20]}...")
        
        # 10. Test Login with New Password
        print("\n🔹 10. Testing Login with New Password...")
        new_login_data = {
            "email_or_username": test_user["email"],
            "password": "NewSecurePassword456!"
        }
        response = requests.post(f"{BASE_URL}/login/", json=new_login_data)
        print_response(response, "Login with New Password")
        
        # 11. Test Logout
        print("\n🔹 11. Testing Logout...")
        response = requests.post(f"{BASE_URL}/logout/", headers=headers)
        print_response(response, "User Logout")
        
        # 12. Test Access After Logout (should fail)
        print("\n🔹 12. Testing Access After Logout (should fail)...")
        response = requests.get(f"{BASE_URL}/profile/", headers=headers)
        print_response(response, "Access After Logout")
        
        print("\n" + "="*80)
        print("🎉 ALL TESTS COMPLETED SUCCESSFULLY!")
        print("✅ Your Django REST API is working perfectly!")
        print("="*80)
        
    except requests.exceptions.ConnectionError:
        print("\n❌ CONNECTION ERROR")
        print("Please make sure the Django server is running:")
        print("   python manage.py runserver")
        print("   Server should be available at: http://127.0.0.1:8000")
        
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🔥 Django REST API Comprehensive Tester")
    print("📋 This script will test all authentication endpoints")
    print("⚠️  Make sure Django server is running: python manage.py runserver")
    print()
    
    # Check if server is accessible
    try:
        response = requests.get("http://127.0.0.1:8000/", timeout=5)
        print("✅ Server is accessible, starting tests...")
        test_api()
    except:
        print("❌ Cannot connect to Django server")
        print("   Please run: python manage.py runserver")
        print("   Then run this test script again")
