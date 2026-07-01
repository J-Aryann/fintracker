from django.shortcuts import render ,redirect
from .forms import InvestmentForm
from .models import Investment
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='signin_url')
def create_investment(request):
    template_name='investment_app/form.html'
    form = InvestmentForm()
    if request.method=='POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            inv = form.save(commit=False)
            inv.user=request.user
            inv.save()
    context={'form':form}
    return render(request,template_name,context)


@login_required(login_url='signin_url')
def show_investment(request):
    template_name='investment_app/investment_data.html'
    investments= Investment.objects.filter(user = request.user)
    context={'investments':investments}
    return render(request,template_name,context)


@login_required(login_url='signin_url')
def update_view(request,pk):
    template_name='investment_app/update.html'
    obj = get_object_or_404(Investment ,pk=pk)
    form = InvestmentForm(instance=obj)
    if request.method=='POST':
        form =InvestmentForm(request.POST,instance=obj)
        if form.is_valid():
            inv = form.save(commit=False)
            inv.user=request.user
            inv.save()
            return redirect('show_investment_url')
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='signin_url')
def delete_view(request,pk):
    template_name='investment_app/delete.html'
    obj = get_object_or_404(Investment,pk=pk)
    context={'obj':obj}
    if request.method=='POST':
        obj.delete()
        return redirect('show_investment_url')
    return render(request,template_name,context)


@login_required(login_url='signin_url')
def dashboard_investment(request):
    template_name='investment_app/dashboard.html'
    investment= list( Investment.objects.values("type_invest").annotate(total_spend= Sum("amount_invest")  ) )
    print(investment)
    labels = [ i['type_invest'] for i in investment  ]
    values = [ i['total_spend'] for i in investment  ]
    context = {
        "labels": labels,
        "values": values,
    }
    return render (request,template_name,context)
