from django.shortcuts import render
from database.models import Attendance

# Create your views here.
def index(request):
    records = Attendance.objects.all()

    context = {
        'records' : records
    }
    return render(request, 'index.html', context)