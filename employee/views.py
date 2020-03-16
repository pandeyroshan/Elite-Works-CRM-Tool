from django.shortcuts import render,redirect
from .models import SuperVisors,labour
from employee.models import Projects
from .forms import SupervisorForm,labourForm,SupervisorUpdateForm
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

def update_supervisor(request,id):
    if request.method=='POST':
        print(request.POST)
        supervisor = SuperVisors.objects.get(id=id)
        supervisor.project = Projects.objects.get(id = request.POST.get('project'))
        supervisor.name = request.POST.get('name')
        supervisor.mobile_number = request.POST.get('mobile_number')
        supervisor.alter_number = request.POST.get('alter_number')
        supervisor.address = request.POST.get('address')
        supervisor.aadhar_number = request.POST.get('aadhar_number')
        supervisor.pan_number = request.POST.get('pan_number')
        supervisor.highest_qual = request.POST.get('highest_qual')
        supervisor.tech_certificate_name = request.POST.get('tech_certificate_name')
        supervisor.UAN_number = request.POST.get('UAN_number')
        if request.POST.get('is_employee') == 'on':
            supervisor.is_employee = True
        elif request.POST.get('is_employee') == 'off':
            supervisor.is_employee = False
        supervisor.save()
        return redirect('/supervisor/')
    else:
        supervisor = SuperVisors.objects.get(id=id)
        form = SupervisorUpdateForm(initial={
            'project' : supervisor.project,
            'name' : supervisor.name ,
            'mobile_number' : supervisor.mobile_number,
            'alter_number' : supervisor.alter_number,
            'address' : supervisor.address,
            'aadhar_number' : supervisor.aadhar_number,
            'pan_number' : supervisor.pan_number,
            'highest_qual' : supervisor.highest_qual,
            'tech_certificate_name' : supervisor.tech_certificate_name,
            'UAN_number' : supervisor.UAN_number,
            'is_employee' : supervisor.is_employee
        })
        return render(request,'employee/update_supervisor.html',{'form': form,})

def update_employee(request,id):
    pass

def supervisor_detail(request,id):
    supervisor = SuperVisors.objects.get(id=id)
    return render(request,'employee/employee.html',{'supervisor':supervisor})