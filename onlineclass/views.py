from rest_framework import viewsets
from .models import OnlineClass
from .serializers import OnlineClassSerializer
from rest_framework.permissions import IsAuthenticated

class OnlineClassViewSet(viewsets.ModelViewSet):
    queryset = OnlineClass.objects.all()
    serializer_class = OnlineClassSerializer
    permission_classes = [IsAuthenticated]

    
