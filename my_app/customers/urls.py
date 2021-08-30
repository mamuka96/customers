"""my_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import *

urlpatterns = [
    path('customers/', CustomersList.as_view(), name='customers-list'),
    path('professions/', ProfessionsList.as_view(), name='professions-list'),
    path('create_customers/', CreatorCustomers.as_view(), name='create_customers'),
    path('create_professions/', CreatorProfessions.as_view(), name='create_professions'),

]