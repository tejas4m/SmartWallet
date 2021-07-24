
# Create your views here.

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Source,UserIncome
from django.contrib import messages
from userpreferences.models import UserPreferences
import json
from django.http import JsonResponse

# Create your views here.

@login_required(login_url="/authentication/login")

def index(request):
    source = Source.objects.all()
    income =UserIncome.objects.filter(owner = request.user)
    currency = UserPreferences.objects.get(user = request.user).currency

    context ={
        'income' : income,
        'currency':currency
    } 

    return render(request,'income/index.html',context)

@login_required(login_url="/authentication/login")

def add_income(request )    :
     sources = Source.objects.all()
     context ={
                'sources':sources,
                'values' : request.POST
               }
    
     if request.method == "GET":
         
          return render(request,'income/add_income.html',context)

     if request.method == "POST":
        amount = request.POST['amount']
        if not amount:
            messages.error(request,'Amount is required')
            return render(request,'income/add_income.html',context)

        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']
        if not description:
            messages.error(request,'Description is required')
            return render(request,'income/add_income.html',context)


        UserIncome.objects.create(owner=request.user, amount=amount,source=source,description=description,date=date   )
        messages.success(request,'Record saved successfully')   

        return redirect('income')

def income_edit(request,id):
    income = UserIncome.objects.get(pk=id)
    sources = Source.objects.all()

    context ={
        'income' : income,
         'values' : income,
         'sources' : sources
    }

    if request.method =="GET":
       return render(request,'income/edit_income.html' ,context)

    if request.method =="POST":
        amount = request.POST['amount']
        if not amount:
            messages.error(request,'Amount is required')
            return render(request,'income/edit_income.html',context)

        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']
        if not description:
            messages.error(request,'Description is required')
            return render(request,'income/edit_income.html',context)
       
      
        income.owner=request.user
        income.amount = amount
        income.date = date
        income.source = source
        income.description = description
        income.save()

        messages.success(request,'Record saved successfully')
        return redirect('income')
   

def delete_income(request, id):
    income = UserIncome.objects.get(pk=id)
    income.delete()
    messages.success(request,'Record removed')
    return redirect('income')