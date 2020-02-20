from django import forms
from .models import Tender

class TenderAdd(forms.ModelForm):

    class Meta:
        model = Tender
        fields = '__all__'