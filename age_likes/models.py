# models.py
from django.db import models
from django.utils import timezone

class UserAge(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    f_name = models.CharField(max_length=60, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ], blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    device_info = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)  # Field for DOB

    def __str__(self):
        return f"{self.username} - {self.name}"

class Like(models.Model):
    user_age = models.ForeignKey(UserAge, on_delete=models.CASCADE, related_name='likes')  # Establishing a relationship with UserAge

    def __str__(self):
        return f"Like for {self.user_age.name}"
