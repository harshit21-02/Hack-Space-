from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status, viewsets
from .serializer import SubmissionSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import submission

class SubmissionAPIView(viewsets.ModelViewSet):
    queryset = submission.objects.all()
    serializer_class = SubmissionSerializer