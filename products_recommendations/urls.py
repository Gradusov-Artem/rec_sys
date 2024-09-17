"""products_recommendations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from products_app.views import create_company, list_company, create_warehouse, list_warehouse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/create', create_company, name='create_company'),
    path('company/list', list_company, name='list_company'),
    path('warehouse/create', create_warehouse, name='create_warehouse'),
    path('warehouse/list', list_warehouse, name='list_warehouse'),
]
