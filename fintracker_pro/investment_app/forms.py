from django import forms
from .models import Investment

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        exclude=('user',)

        widgets={
            'date': forms.DateInput(attrs={'type': 'date','class': 'form-control' })
        }