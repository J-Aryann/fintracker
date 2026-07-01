from django import forms
from .models import Expence

class ExpenceFrom(forms.ModelForm):
    class Meta:
        model = Expence
        exclude=('user',)


        widgets={
            'date': forms.DateInput(attrs={'type': 'date','class': 'form-control' })
        }