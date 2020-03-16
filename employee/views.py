from django.shortcuts import render,redirect
from .models import SuperVisors,labour
from .forms import SupervisorForm,labourForm
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
            return redirect('/supervisor/')
    else:
        form = SupervisorForm()
    return render(request,'employee/create_super.html',{'form':form})


def handler404(request,exception):
    return render(request,'projects/404.html')


def handler500(request):
    return render(request,'projects/404.html')

def create_labour(request):
    if request.method == 'POST':
        form = labourForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/labour/')
    else:
        form = labourForm()
    return render(request,'employee/add_labour.html',{'form':form})

def mark_attandance(request,id):
    # here id is the project id
    print(request.user)
    print(SuperVisors.objects.get(project=id))
    if str(request.user) == str(SuperVisors.objects.get(project=id)) or request.user.is_superuser: # success
        return render(request,'employee/attandance.html')
    else:
        return render(request,'projects/404.html')