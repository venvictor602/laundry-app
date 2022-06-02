from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'body.html')

def about(request):
    return render(request, 'about.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')
    

@login_required(login_url='login')
def dashboard(request):
    count_employee=Employee.objects.count()
    count_customer=Customer.objects.count()
    count_inventory=Inventory.objects.count()
    context={'count_employee':count_employee,'count_customer': count_customer,'count_inventory':count_inventory}
    return render(request, 'dashboard.html',context)

@login_required(login_url='login')
def employee(request):
    employee=Employee.objects.all()
    count=Employee.objects.count()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        job_type = request.POST['job_type']
        lga = request.POST['lga']
        state = request.POST['state']
        phone_no = request.POST['phone_no']

    
    
        employee = Employee( first_name=first_name, last_name=last_name, address=address, job_type=job_type, lga=lga, state=state,phone_no=phone_no )

        employee.save()
        messages.success(request, 'Form sent successfully')
        return redirect('employee')
    context={'employee':employee,'count':count}
    return render(request,'employee.html',context)

@login_required(login_url='login')
def customer(request):
    customer = Customer.objects.all
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form sent successfully')
        return redirect('customer')
    context={'customer':customer,'form':form}
    return render(request,'customer.html',context)

@login_required(login_url='login')
def editcustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form= CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully')
        return redirect('customer')
    context = {'form':form,'customer':customer}
    return render(request, 'search.html',context)

@login_required(login_url='login')
def deletecustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('customer')
    context = {'item':customer}
    return render(request, 'delete.html',context)

@login_required(login_url='login')
def addreport(request):
    report = Report.objects.all()
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form sent successfully')
        return redirect('report')
    context={'report':report,'form':form}
    return render(request,'addreport.html',context)

@login_required(login_url='login')
def report(request):
    report=Report.objects.all()
    context={'report':report}
    return render(request,'report.html',context)

@login_required(login_url='login')
def deletereport(request, pk):
    report = Report.objects.get(id=pk)
    if request.method == 'POST':
        report.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('report')
    context = {'item':report}
    return render(request, 'delete.html',context)

@login_required(login_url='login')
def editreport(request, pk):
    report = Report.objects.get(id=pk)
    form= ReportForm(instance=report)
    if request.method == 'POST':
        form = ReportForm(request.POST,request.FILES,instance=report)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully')
        return redirect('report')
    context = {'form':form,'report':report}
    return render(request, 'addreport.html',context)

def track(request):
    return render(request,'track.html')

def search(request):
    customers = Customer.objects.order_by('-created_at')
    if 'created_at' in request.GET:
        created_at = request.GET['created_at']
        if created_at:
            custo = Customer.objects.filter(created_at__iexact=created_at)
    context={'custo':custo,'customers':customers}
    return render(request,'search.html',context)

@login_required(login_url='login')
def addinventory(request):
    inventory = Inventory.objects.all()
    form = InventoryForm()
    if request.method == 'POST':
        form = InventoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form sent successfully')
        return redirect('inventory')
    context={'inventory':inventory,'form':form}
    return render(request,'addreport.html',context)

@login_required(login_url='login')
def inventory(request):
    inventory=Inventory.objects.all()
    context={'inventory':inventory}
    return render(request,'inventory.html',context)

@login_required(login_url='login')
def deleteinventory(request, pk):
    inventory = Inventory.objects.get(id=pk)
    if request.method == 'POST':
        inventory.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('inventory')
    context = {'item':inventory}
    return render(request, 'delete.html',context)

@login_required(login_url='login')
def editinventory(request, pk):
    inventory = Inventory.objects.get(id=pk)
    form= InventoryForm(instance=inventory)
    if request.method == 'POST':
        form = InventoryForm(request.POST,request.FILES,instance=inventory)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully')
        return redirect('inventory')
    context = {'form':form,'inventory':inventory}
    return render(request, 'addinventory.html',context)
