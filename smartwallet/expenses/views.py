
from abc import ABCMeta
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages
from userpreferences.models import UserPreferences
import datetime

# Create your views here.

@login_required(login_url="/authentication/login")

def index(request):
    categories = Category.objects.all()
    expense =Expense.objects.filter(owner = request.user)
    currency = UserPreferences.objects.get(user = request.user).currency

    context ={
        'expenses' : expense,
        'currency':currency
    }

    return render(request,'expenses/index.html',context)
def add_expense(request )    :
     categories = Category.objects.all()
     context ={'categories':categories,
                'values' : request.POST
               }
    
     if request.method == "GET":
         
          return render(request,'expenses/add_expense.html',context)

     if request.method == "POST":
        amount = request.POST['amount']
        if not amount:
            messages.error(request,'Amount is required')
            return render(request,'expenses/add_expense.html',context)

        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']
        if not description:
            messages.error(request,'Description is required')
            return render(request,'expenses/add_expense.html',context)\

        Expense.objects.create(owner=request.user, amount=amount,category=category,description=description,date=date   )
        messages.success(request,'Expense saved successfully')   

        return redirect('expenses')


def expense_edit(request,id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()

    context ={
        'expense' : expense,
         'values' : expense,
         'categories' : categories
    }

    if request.method =="GET":
       return render(request,'expenses/edit-expense.html' ,context)

    if request.method =="POST":
        amount = request.POST['amount']
        if not amount:
            messages.error(request,'Amount is required')
            return render(request,'expenses/edit-expense.html',context)

        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']
        if not description:
            messages.error(request,'Description is required')
            return render(request,'expenses/edit-expense.html',context)\

       
      
        expense.owner=request.user
        expense.amount = amount
        expense.date = date
        expense.category = category
        expense.description = description

        expense.save()

        messages.success(request,'Expense saved successfully')
        return redirect('expenses')
   

def delete_expense(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request,'Expense removed')
    return redirect('expenses')

def expense_catogory_summary(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date - datetime.timedelta(days=30*6)
    expenses = Expense.objects.filter(owner = request.user, date__gte= six_months_ago, date__lte = todays_date)
    finalrep = {}
    def get_category (expense):
        return expense.category

    category_list= list(set(map(get_category,expenses)))

    def get_expense_category_amount(category):
        amount = 0 
        filter_by_category = expenses.filter(category = category)
        for item in filter_by_category:
            amount +=item.amount
        return amount
    
    for x in expenses:
        for y in category_list:
            finalrep[y] = get_expense_category_amount(y)

    return JsonResponse({'expense_catogory_data' : finalrep}, safe=False)


def stats_view(request):
    return render(request, 'expenses/stats.html')            