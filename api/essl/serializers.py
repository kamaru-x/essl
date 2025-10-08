from rest_framework import serializers
from database.models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = [
            'device_sn', 'device_id', 'user_id', 'datetime', 'status', 'work_code'
        ]