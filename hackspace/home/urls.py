"""hackspace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="home"
urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.upload, name="upload"),
    path('card/<id>', views.card, name="card"),
    path('editform/<id>', views.editform, name="editform"),
    path('delete/<id>', views.delete, name="delete"),
    path('favourite/', views.favourite, name="favourite"),
    path('markFavourite/', views.markFavourite, name="markFavourite"),
    path('search/', views.search, name="search"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
