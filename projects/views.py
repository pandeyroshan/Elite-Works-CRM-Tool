from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from projects.models import Tender,other_contractors_bid, Projects
from employee.models import SuperVisors, labour
from .forms import TenderAdd,ContractorForm,ProjectForm
import os
# Create your views here.

@login_required
def index(request):
    project_data = Projects.objects.all().values()
    for i in range(len(project_data)):
        try:
            supervisor = SuperVisors.objects.get(project=project_data[i]['id'])
        except:
            supervisor = {'name': 'Not Allocated'}
        project_data[i]['supervisor'] = supervisor
        project_data[i]['tender'] = Tender.objects.get(id=project_data[i]['tender_id'])
    context = {
        'total_tender' : len(Tender.objects.all()),
        'success_tender' : len(Tender.objects.all().filter(bid_status='Yes')),
        'projects' : len(Projects.objects.all()),
        'SuperVisors': len(SuperVisors.objects.all()),
        'all_project': project_data
    }
    return render(request,'projects/index.html',context)

@login_required
def tender(request):
    tender_list = Tender.objects.all()
    context = {
        'tender_list': tender_list
    }
    return render(request,'projects/tender_page.html',context)

@login_required
def tender_details(request,uuid_no):
    try:
        tender_object = Tender.objects.get(uuid_no=uuid_no)
        projects = Projects.objects.all().filter(tender=tender_object).values()
    except:
        tender_object = {}
    other_contractor = other_contractors_bid.objects.filter(tender=tender_object)
    for i in range(len(projects)):
        try:
            supervisor = SuperVisors.objects.get(project=projects[i]['id'])
        except:
            supervisor = {'name': 'Not Allocated'}
        projects[i]['supervisor'] = supervisor
    context = {
        'tender_object' : tender_object,
        'other_contractors' : other_contractor,
        'projects' : projects
    }
    return render(request,'projects/tender_detail.html',context)

@login_required
def add_tender(request):
    if request.method == 'POST':
        form = TenderAdd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/tender/')
    else:
        form = TenderAdd()
    return render(request,'projects/add_tender.html',{'form' : form})

@login_required
def my_tender(request):
    tender_list = Tender.objects.filter(bid_status='Yes')
    context = {
        'tender_list': tender_list
    }
    for data in tender_list:
        print(data.uuid_no)
    return render(request,'projects/my_tender.html',context)

@login_required
def add_contractor(request,id):
    tender = Tender.objects.get(id=id)
    if request.method == 'POST':
        form = ContractorForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.tender = Tender.objects.get(id=id)
            form_data.save()
            return redirect('/tender')
    else:
        form = ContractorForm()
    return render(request,'projects/add_contractor.html',{'form':form,'tender':tender})

@login_required
def edit_tender(request,id):
    if request.method == 'POST':
        form = TenderAdd(request.POST,request.FILES)
        if form.is_valid():
            tender = Tender.objects.get(id=id)
            tender.tender_number = request.POST.get('tender_number')
            tender.tender_name = request.POST.get('tender_name')
            tender.tender_submission_date = request.POST.get('tender_submission_date')
            tender.physical_submission_date = request.POST.get('physical_submission_date')
            tender.tech_bid_opening_date = request.POST.get('tech_bid_opening_date')
            tender.bid_status = request.POST.get('bid_status')
            tender.prize_bid = request.POST.get('prize_bid')
            tender.tender_purchase_reciept = request.FILES.get('tender_purchase_reciept')
            tender.tender_confirmation_reciept = request.FILES.get('tender_confirmation_reciept')
            tender.save()
            return redirect('/tender/')
        pass
    else:
        tender = Tender.objects.get(id=id)
        form = TenderAdd(initial={
            'tender_number' : tender.tender_number,
            'tender_name' : tender.tender_name,
            'tender_submission_date': tender.tender_submission_date,
            'physical_submission_date': tender.physical_submission_date,
            'tech_bid_opening_date': tender.tech_bid_opening_date,
            'bid_status': tender.bid_status,
            'prize_bid': tender.prize_bid
        })
    return render(request,'projects/edit_tender.html',{'form':form})


@login_required
def edit_project(request,id):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Projects.objects.get(id=id)
            project.project_name = request.POST.get('project_name')
            project.start_date = request.POST.get('start_date')
            project.save()
            return redirect('/project/'+str(id)+'/')
    else:
        project = Projects.objects.get(id=id)
        form = ProjectForm(initial={
            'project_name': project.project_name,
            'start_date' : project.start_date
        })
    return render(request,'projects/edit_project.html',{'form': form})


@login_required
def all_projects(request):
    project_data = Projects.objects.all().values()
    for i in range(len(project_data)):
        try:
            supervisor = SuperVisors.objects.get(project=project_data[i]['id'])
        except:
            supervisor = {'name': 'Not Allocated'}
        project_data[i]['supervisor'] = supervisor
        project_data[i]['tender'] = Tender.objects.get(id=project_data[i]['tender_id'])
    return render(request,'projects/project.html',{'projects': project_data})

@login_required
def add_project(request,id):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.tender = Tender.objects.get(id=id)
            form_data.save()
            return redirect('/projects/')
        pass
    else:
        form = ProjectForm()
    return render(request,'projects/add_project.html',{'form':form})


@login_required
def project_details(request,id):
    try:
        supervisor = SuperVisors.objects.get(project=id)
    except:
        supervisor = {'name' : 'Not Alloted'}
    return render(request,'projects/project_detail.html',{
        'project': Projects.objects.get(id=id),
        'supervisor': supervisor,
        'total_labour': len(labour.objects.all().filter(project = id)),
        'employee' : labour.objects.all().filter(project=id)
        })

@login_required
def testing(request):
    return render(request,'projects/testing.html')