from mongoengine import Document, StringField, EmailField, DateTimeField, DateField
from datetime import datetime

class UserProfile(Document):
    """MongoDB document for storing user profile data"""
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say'),
    )
    
    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    
    # Link to Django User
    django_user_id = StringField(required=True, unique=True)
    
    # Basic fields
    username = StringField(max_length=150, required=True, unique=True)
    email = EmailField(required=True, unique=True)
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    
    # Additional fields
    university = StringField(max_length=200)
    blood_group = StringField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    mobile_no = StringField(max_length=15)
    gender = StringField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = DateField()
    address = StringField()
    
    # Timestamps
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    
    meta = {
        'collection': 'user_profiles',
        'indexes': ['email', 'username', 'django_user_id']
    }
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
