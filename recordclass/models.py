from django.db import models

# Create your models here.
class RecordedClass(models.Model):
    class_name = models.CharField(max_length=255)
    tutor_name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)   # Auto-set date on creation
    time = models.TimeField(auto_now_add=True)   # Auto-set time on creation
    course_name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='recorded_thumbnails/')
    recorded_class_link = models.URLField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.class_name} (Recorded) by {self.tutor_name}"
