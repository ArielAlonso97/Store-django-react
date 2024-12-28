from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Definir el queryset (todos los objetos de MiModelo)
    serializer_class = UserSerializer  # Asociar el serializer con el ViewSet
    
    
    

