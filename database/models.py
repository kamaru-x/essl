from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name
    

class Attendance(models.Model):
    device_sn = models.CharField(max_length=50)
    device_id = models.CharField(max_length=20)
    user_id = models.CharField(max_length=20)
    datetime = models.DateTimeField()
    status = models.CharField(max_length=10)
    work_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user_id} - {self.datetime}"