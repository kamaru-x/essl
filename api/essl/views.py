from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from database.models import Attendance
from api.essl.serializers import AttendanceSerializer


class Attendance(generics.ListCreateAPIView):
    queryset = Attendance.objects.all().order_by('-datetime')
    serializer_class = AttendanceSerializer

    def get(self, request, *args, **kwargs):
        records = self.get_queryset()
        serializer = self.get_serializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("OK", status=status.HTTP_200_OK, content_type="text/plain")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)