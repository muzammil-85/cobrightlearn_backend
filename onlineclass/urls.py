from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OnlineClassViewSet

router = DefaultRouter()
router.register(r'online-classes', OnlineClassViewSet, basename='onlineclass')

urlpatterns = [
    path('api/', include(router.urls)),
]
