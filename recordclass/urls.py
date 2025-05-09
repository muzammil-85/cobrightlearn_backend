from rest_framework.routers import DefaultRouter
from .views import RecordedClassViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'recorded_classes', RecordedClassViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

