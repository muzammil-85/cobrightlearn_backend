from rest_framework import serializers
from .models import OnlineClass

class OnlineClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineClass
        fields = '__all__'
