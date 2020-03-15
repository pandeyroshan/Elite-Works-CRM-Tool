from django import forms
from .models import SuperVisors,labour

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = SuperVisors
        fields = '__all__'

class labourForm(forms.ModelForm):
    class Meta:
        model = labour
        fields = '__all__'