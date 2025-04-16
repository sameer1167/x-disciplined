import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from timezone_field import TimeZoneField

class Users(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=False, blank=False, null=False) #Make this field unique after development
    timezone = TimeZoneField(default='Asia/Kolkata')  # Default India time
    def __str__(self):
        return self.username
