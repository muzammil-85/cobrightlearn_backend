from django.urls import include, path
from .views import CourseListView, PhoneTokenObtainPairView, RegisterView, StudentListView, TutorListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', CourseListView, basename='course')


urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='api-register'),
    path('api/login/', PhoneTokenObtainPairView.as_view(), name='phone_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/list-students/', StudentListView.as_view(), name='students-list'),
    path('api/list-tutors/', TutorListView.as_view(), name='tutors-list'),
    path('api/', include(router.urls)),

]
