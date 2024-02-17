from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import {tablename}
from .serializers import {tablename}Serializer

class {tablename}Views(APIView):