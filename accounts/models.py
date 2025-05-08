from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    education_qualification = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    course = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username
