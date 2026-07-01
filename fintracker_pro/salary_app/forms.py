from django import forms
from .models import Salary

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        exclude=('user',)


        widgets={
            'date': forms.DateInput(attrs={'type': 'date','class': 'form-control' })
        }
        