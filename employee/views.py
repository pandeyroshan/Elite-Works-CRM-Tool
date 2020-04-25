from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import SuperVisors,labour,Attendance
from django.contrib.auth.decorators import login_required
from employee.models import Projects
from .forms import SupervisorForm,labourForm,SupervisorUpdateForm,LabourUpdateForm
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.query import QuerySet
import datetime
import bs4 as bs
import urllib.request
import os
import json
# Create your views here.

@login_required
def get_all_supervisor(request):
    context = {
        'supervisors' : SuperVisors.objects.all()
    }
    return render(request,'employee/all_supervisor.html',context)

def get_all_employee(request):
    context = {
        'employee' : labour.objects.all()
    }
    return render(request,'employee/all_employee.html',context)

@login_required
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

@login_required
def create_labour(request):
    if request.method == 'POST':
        form = labourForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/labour/')
    else:
        form = labourForm()
    return render(request,'employee/add_labour.html',{'form':form})

@login_required
def mark_attandance(request,id):
    if str(request.user) == str(SuperVisors.objects.get(project=id)) or request.user.is_superuser: # success
        if request.method == 'POST':
            print(request.POST)
            project = Projects.objects.get(id=id)
            labours = labour.objects.all().filter(project=project)
            date = request.POST.get('date')
            shift = request.POST.get('shift')
            for data in labours:
                shift_status = request.POST.get(str(data.id)+'S')
                if request.POST.get(str(data.id))=='P':
                    att_object = Attendance.objects.create(project=project,date=date,labour=data,shift=shift_status)
                else:
                    att_object = Attendance.objects.create(project=project,date=date,labour=data,shift=shift_status)
                att_object.save()
            return redirect('/project/'+str(id))
        else:
            project = Projects.objects.get(id=id)
            labours = labour.objects.all().filter(project=project)
            for data in labours:
                data.SC = str(data.id) + str('S') # Shift Choice
            return render(request,'employee/attandance.html',{
                'project' : project,
                'labours' : labours,
                'total_labour': len(labours)
            })
    else:
        return render(request,'projects/404.html')

@login_required
def update_supervisor(request,id):
    if request.method=='POST':
        supervisor = SuperVisors.objects.get(id=id)
        supervisor.project.clear()
        json_data = json.dumps({k: request.POST.getlist(k) for k in request.POST.keys()})
        print(json_data)
        dict_data = json.loads(json_data)
        project_ids = dict_data['project']
        for id in project_ids:
            obj = Projects.objects.get(id=int(id))
            supervisor.project.add(obj)
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
        return render(request,'employee/update_supervisor.html',{'form': form})



@login_required
def update_labour(request,id):
    if request.method=='POST':
        labour_obj = labour.objects.get(id=id)
        labour_obj.name = request.POST.get('name')
        labour_obj.project = Projects.objects.get(id=int(request.POST.get('project')))
        labour_obj.mobile_number = request.POST.get('mobile_number')
        labour_obj.alter_number = request.POST.get('alter_number')
        labour_obj.address = request.POST.get('address')
        labour_obj.aadhar_number = request.POST.get('aadhar_number')
        labour_obj.pan_number = request.POST.get('pan_number')
        labour_obj.highest_qual = request.POST.get('highest_qual')
        labour_obj.tech_certificate_name = request.POST.get('tech_certificate_name')
        labour_obj.UAN_number = request.POST.get('UAN_number')
        labour_obj.save()
        return redirect('/labour/')
    else:
        labour_obj = labour.objects.get(id=id)
        form = LabourUpdateForm(initial={
            'project': labour_obj.project,
            'name' : labour_obj.name ,
            'mobile_number' : labour_obj.mobile_number,
            'alter_number' : labour_obj.alter_number,
            'address' : labour_obj.address,
            'aadhar_number' : labour_obj.aadhar_number,
            'pan_number' : labour_obj.pan_number,
            'highest_qual' : labour_obj.highest_qual,
            'tech_certificate_name' : labour_obj.tech_certificate_name,
            'UAN_number' : labour_obj.UAN_number,
        })
        return render(request,'employee/update_labour.html',{'form': form})


@login_required
def supervisor_detail(request,id):
    supervisor = SuperVisors.objects.get(id=id)
    return render(request,'employee/employee.html',{'supervisor':supervisor})

@login_required
def view_attandance(request,id):
    project = Projects.objects.get(id=id)
    labours = labour.objects.all().filter(project=project)
    supervisor = SuperVisors.objects.get(project=id)
    raw_data = Attendance.objects.filter(project=project).values('date').distinct().order_by('-date')
    for i in range(len(raw_data)): #add statistics in every individual data
        total = 0
        present = 0
        absent = 0
        date = raw_data[i]['date']
        date_shift = Attendance.objects.all().filter(project=project,date=date).values('shift')
        for data in date_shift:
            if data['shift'] != 'R':
                present+=1
            else:
                absent+=1
        raw_data[i]['present'] = present
        raw_data[i]['absent'] = absent
    print(raw_data)
    return render(request,'employee/show_attandance.html',{
        'project': project,
        'total_labour':len(labours),
        'supervisor':supervisor,
        'major_data':raw_data
    })

@login_required
def detail_attandance(request,year,month,day,id):
    date = datetime.date(year,month,day)
    att_data = Attendance.objects.all().filter(project=Projects.objects.get(id=id),date=date)
    return render(request,'employee/detail_attandance.html',{
        'att_data' : att_data,
        'date' : date,
        'total' : len(att_data),
        'project' : Projects.objects.get(id=id)
    })

@login_required
def labour_detail_page(request,id):
    obj = labour.objects.get(id=id)
    return render(request,'employee/labour.html',{'labour': obj})

@login_required
def delete_supervisor(request,id):
    obj = SuperVisors.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def delete_labour(request,id):
    obj = labour.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))