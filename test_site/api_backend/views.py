from rest_framework import viewsets
from django.contrib.auth.models import User
from . import serializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer

