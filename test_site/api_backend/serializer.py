from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

# Serializers define the API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class StudentPerformanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.StudentPerformance
        fields = [
            "gender",
            "race_ethnicity",
            "parental_level_of_education",
            "lunch",
            "test_preparation_course",
            "math_score",
            "reading_score",
            "writing_score",
        ]
