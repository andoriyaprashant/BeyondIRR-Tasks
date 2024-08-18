
from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    arn_number = models.CharField(max_length=20, unique=True, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    def __str__(self):
        return self.email

class LogRequest(models.Model):
    url = models.CharField(max_length=255)
    status_code = models.IntegerField()
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    payload = models.TextField()
    response = models.TextField()
    is_success = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.method} {self.url} - {self.status_code}"