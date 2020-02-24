from django import forms
from .models import SuperVisors

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = SuperVisors
        fields = '__all__'