from django import forms
from .models import Tender,other_contractors_bid, Projects

class TenderAdd(forms.ModelForm):

    class Meta:
        model = Tender
        fields = '__all__'

class ContractorForm(forms.ModelForm):

    class Meta:
        model = other_contractors_bid
        fields = ('contractor_info','contractor_price',)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('project_name','start_date','supervisor','labours')