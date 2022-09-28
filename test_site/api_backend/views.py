from rest_framework import viewsets
from django.contrib.auth.models import User
from . import serializer, models

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer


class StudentPerformanceViewSet(viewsets.ModelViewSet):
    queryset = models.StudentPerformance.objects.all()
    serializer_class = serializer.StudentPerformanceSerializer
