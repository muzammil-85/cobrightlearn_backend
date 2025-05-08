from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('api/password_reset/', include('rest_passwordreset.urls')),
    
]
