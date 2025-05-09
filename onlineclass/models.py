from django.db import models

class OnlineClass(models.Model):
    class_name = models.CharField(max_length=255)
    tutor_name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)   # Auto-set date on creation
    time = models.TimeField(auto_now_add=True)   # Auto-set time on creation
    thumbnail = models.ImageField(upload_to='online_thumbnails/')
    course_name = models.CharField(max_length=255)
    online_class_link = models.URLField()

    def __str__(self):
        return f"{self.class_name} by {self.tutor_name}"
