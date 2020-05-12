"""shareandcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from product import views
from django.conf.urls.static import static
from shareandcare import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('Products/', views.Product, name='Product'),
    path('proddetails/<id>',
         views.Productdetails, name='Productdetails'),
    path('accounts/login/', views.login_view),
    path('accounts/logout/', views.logout_view),
    path('accounts/register/', views.register_view),
    path('Products/entry/', views.Entry),
    path('myprofile', views.myprofile),
]
