from django.urls import path, include
from .views_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'submission', SubmissionAPIView)

urlpatterns = [
    path('', include(router.urls)),
]