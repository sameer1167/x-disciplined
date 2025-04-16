from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['id', 'title', 'due_date', 'status']
        fields='__all__'
