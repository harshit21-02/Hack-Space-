from rest_framework import serializers
from .models import *

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = submission
        fields = '__all__'
