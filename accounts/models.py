from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('tutor', 'Tutor'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    age = models.IntegerField(null=True, blank=True)
    education_qualification = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    course = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)  # Example: "3 months"
    description = models.TextField()

    def __str__(self):
        return self.course_name