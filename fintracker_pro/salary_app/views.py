from django.shortcuts import render, redirect
from .forms import SalaryForm
from .models import Salary
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='signin_url')
def create_salary(request):
    template_name='salary_app/create_form.html'
    form = SalaryForm()
    if request.method=='POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            sal = form.save(commit=False)
            sal.user=request.user
            sal.save()
    context={'form':form}
    return render(request,template_name,context)


@login_required(login_url='signin_url')
def show_salary(request):
    template_name='salary_app/salary_data.html'
    salarys = Salary.objects.filter(user=request.user)
    context = {'salarys':salarys}
    return render(request,template_name,context)


@login_required(login_url='signin_url')
def update_view(request,pk):
    template_name='salary_app/update.html'
    obj= get_object_or_404(Salary,pk=pk)
    form =SalaryForm(instance=obj)
    if request.method =='POST':
        form = SalaryForm(request.POST,instance=obj)
        if form.is_valid():
            sal = form.save(commit=False)
            sal.user=request.user
            sal.save()
            return redirect('show_salary_url')
    context={'form':form}
    return render(request,template_name,context)


@login_required(login_url='signin_url')
def delete_view(request,pk):
    template_name='salary_app/salary_delete.html'
    obj=get_object_or_404(Salary,pk=pk)
    context={'obj':obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('show_salary_url')
    return render(request,template_name,context)


@login_required(login_url='signin_url')
def salary_dashboard(request):
    template_name='salary_app/salary_dashboard.html'
    salary= list( Salary.objects.values("source").annotate(total_spend= Sum("amount")  ) )
    print(salary)
    labels = [ s['source'] for s in salary  ]
    values = [ s['total_spend'] for s in   salary]
    context = {
        "labels": labels,
        "values": values,
    }
    return render(request,template_name,context)