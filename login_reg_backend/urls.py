"""
URL configuration for login_reg_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        'message': 'Welcome to Login & Registration Backend API',
        'endpoints': {
            'register': '/api/auth/register/',
            'login': '/api/auth/login/',
            'logout': '/api/auth/logout/',
            'profile': '/api/auth/profile/',
            'change-password': '/api/auth/change-password/',
            'user-info': '/api/auth/user-info/',
            'check-email': '/api/auth/check-email/',
            'check-username': '/api/auth/check-username/',
            'admin': '/admin/',
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('', api_root, name='api_root'),
]
