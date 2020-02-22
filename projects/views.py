from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Tender,other_contractors_bid
from .forms import TenderAdd
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
        print(form.errors)
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