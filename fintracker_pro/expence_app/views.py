from django.shortcuts import render,redirect
from .forms import ExpenceFrom
from .models import Expence
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='signin_url')
def create_view(request):
    template_name='expence_app/create.html'
    form = ExpenceFrom()
    context={'form':form}
    if request.method == 'POST':
        form = ExpenceFrom(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.user=request.user
            exp.save()
        else:
            context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='signin_url')
def show_expence_view(request):
    template_name='expence_app/expence_data.html'
    expences = Expence.objects.filter(user=request.user)
    context={'expences':expences}
    return render(request,template_name,context)

@login_required(login_url='signin_url')
def update_expence(request,pk):
    template_name='expence_app/update.html'
    obj = get_object_or_404(Expence,pk=pk)
    form = ExpenceFrom(instance=obj)
    if request.method == 'POST':
        form = ExpenceFrom(request.POST,instance=obj)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.user=request.user
            exp.save()
            return redirect('show_expence_view_url')
    context = {'form':form}
    return render(request,template_name,context)

@login_required(login_url='signin_url')
def delete_view(request,pk):
    template_name='expence_app/delete.html'
    obj = get_object_or_404(Expence,pk=pk)
    context = {'obj':obj}
    if request.method=='POST':
        obj.delete()
        return redirect('show_expence_view_url')
    return render(request,template_name,context)




# [{'category': 'food', 'total_spend': 500.0},  ]
# views.py


@login_required(login_url='signin_url')
def dashboard(request):
    expences= list( Expence.objects.values("category").annotate(total_spend= Sum("amount")  ) )
    print(expences)
    labels = [ e['category'] for e in expences  ]
    values = [ e['total_spend'] for e in expences  ]

    context = {
        "labels": labels,
        "values": values,
    }
    return render(request, "expence_app/d.html", context)


