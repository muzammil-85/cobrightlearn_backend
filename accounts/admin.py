from django.contrib import admin

from accounts.models import Course, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Course)