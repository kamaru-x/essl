from django.urls import path
from api.essl import views

app_name = 'essl_api'

urlpatterns = [
    path('essl/push/', views.Attendance.as_view(), name='essl-api')
]