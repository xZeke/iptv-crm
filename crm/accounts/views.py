from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import *
from .forms import CustomerForm, NewCustomer
from .filters import CustomerFilter
from django.db.models import F

import datetime

# Create your views here.

def home(request):
    customers = Customer.objects.all()

    total_customers = customers.count()

    today_date = datetime.date.today()
    end_date = today_date + datetime.timedelta(days=5)

    total_remind = Customer.objects.filter(expires__range=(today_date,end_date)).count()

    myFilter = CustomerFilter(request.GET, queryset= customers)
    customers = myFilter.qs

    context = {'customers':customers, 'total_customers':total_customers, 'myFilter': myFilter,'total_remind':total_remind}

    return render(request, 'accounts/dashboard.html', context)

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
    #customer.add_thirty()

    context = {'customer':customer, 'form':form}

    return render(request, 'accounts/customer.html', context)


def createCustomer(request):
    form = NewCustomer()
    if request.method == 'POST':
        print("Printing Post: ", request.POST)
        form = NewCustomer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}

    return render(request, 'accounts/customer_form.html', context)

def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = NewCustomer(instance=customer)
    if request.method == 'POST':
        form = NewCustomer(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customer', args=(pk)))
    context = {'form':form}

    return render(request, 'accounts/customer_form.html', context)


def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('/')

    context = {'customer':customer}
    return render(request, 'accounts/delete_customer.html', context)

def remindCustomer(request):

    today_date = datetime.date.today()
    end_date = today_date + datetime.timedelta(days=5)
    customers = Customer.objects.filter(expires__range=(today_date,end_date))

    context = {'customers':customers}
    return render(request, 'accounts/customer_remind.html', context)

#def customer_month(request, pk):
    #customer = Customer.objects.get(id=pk).update(expires=F('expires') + timedelta(days=30))
    #form = 
   # print('Hello')
        #customer.expires += timedelta(days=30)
        #customer.save(update_fields=['expires'])
   # context = {'customer':customer}

   # return render(request, 'accounts/customer.html', context)
