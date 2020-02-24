from django.shortcuts import render
from .models import SuperVisors,labour
from .forms import SupervisorForm
from django.contrib.auth.models import User
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

def create_super(request):
    if request.method == 'POST':
        form = SupervisorForm(request.POST,request.FILES)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.create_user(username, 'random@gmail.com', password)
            user.save()
            form.save()
    else:
        form = SupervisorForm()
    return render(request,'employee/create_super.html',{'form':form})