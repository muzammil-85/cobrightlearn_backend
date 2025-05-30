from django.contrib import admin

from accounts.models import Course, User

# Register your models here.
admin.site.register(User)
admin.site.register(Course)