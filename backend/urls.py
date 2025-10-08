from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('database.urls')),
    path('api/', include('api.essl.urls', namespace='essl_api')),
    path('admin/', admin.site.urls),
]
