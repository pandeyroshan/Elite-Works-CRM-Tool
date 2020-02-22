from django.shortcuts import render
from .models import SuperVisors,labour
# Create your views here.

def get_all_supervisor(request):
    context = {
        'supervisors' : SuperVisors.objects.all()
    }
    return render(request,'employee/all_supervisor.html',context)
    pass

def get_all_employee(request):
    context = {
        'employee' : labour.objects.all()
    }
    return render(request,'employee/all_employee.html',context)