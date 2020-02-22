from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from projects.models import Tender,other_contractors_bid
from .forms import TenderAdd,ContractorForm
# Create your views here.

@login_required
def index(request):
    tender_objects = Tender.objects.all()
    success_tender = Tender.objects.all().filter(bid_status='Yes')
    print(success_tender)
    context = {
        'total_tender' : len(tender_objects),
        'success_tender' : len(success_tender)
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
def tender_details(request,id):
    tender_object = Tender.objects.get(id=id)
    other_contractor = other_contractors_bid.objects.filter(tender=tender_object)
    context = {
        'tender_object' : tender_object,
        'other_contractors' : other_contractor
    }
    return render(request,'projects/tender_detail.html',context)

@login_required
def add_tender(request):
    if request.method == 'POST':
        form = TenderAdd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = TenderAdd()
    return render(request,'projects/add_tender.html',{'form' : form})

@login_required
def my_tender(request):
    tender_list = Tender.objects.filter(bid_status='Yes')
    context = {
        'tender_list': tender_list
    }
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