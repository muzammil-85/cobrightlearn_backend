from rest_framework import serializers
from .models import RecordedClass

class RecordedClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordedClass
        fields = '__all__'
