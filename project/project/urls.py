"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from webpage.views import home_page
from webpage.views import user_login
from webpage.views import success_page
from webpage.views import admission
from webpage.views import credits

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home_page),
    path('login/', user_login),
    path('success/',success_page),
    path('admission/',admission),
    path('credits/',credits)
]
