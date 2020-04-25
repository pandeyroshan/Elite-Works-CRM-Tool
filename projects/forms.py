from django import forms
from .models import Tender,other_contractors_bid, Projects, Bugs, Features
from bootstrap_datepicker_plus import DatePickerInput

class TenderAdd(forms.ModelForm):

    class Meta:
        model = Tender
        fields = '__all__'
        widgets = {
            'tender_submission_date': DatePickerInput(format='%Y-%m-%d'),
            'physical_submission_date': DatePickerInput(format='%Y-%m-%d'),
            'tech_bid_opening_date': DatePickerInput(format='%Y-%m-%d'),
            'bid_price_opening_date': DatePickerInput(format='%Y-%m-%d'),
        }

class ContractorForm(forms.ModelForm):

    class Meta:
        model = other_contractors_bid
        fields = ('contractor_info','contractor_price',)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('project_name','start_date',)
        widgets = {
            'start_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }

class BugForm(forms.ModelForm):

    class Meta:
        model = Bugs
        exclude = ('ticket','bug_status','message')

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = '__all__'