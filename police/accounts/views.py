from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
# Create your views here.
def home(request):
    queryset=Qualification.objects.filter(status=1)
    #pagination
    paginator = Paginator(queryset, 3)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    context={'queryset':users}
    return render(request,'home.html',context)
def jobs(request):
    queryset=Qualification.objects.filter(status=1)
    #pagination
    paginator = Paginator(queryset, 6)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    context={'queryset':users}
    return render (request,'jobs.html',context)
def jobdetails(request,pk_test):
    queryset=Qualification.objects.get(id=pk_test)
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'form sent successfully')
        else:
            messages.info(request, 'error sending form use yyyy-mm-dd')
    context={'queryset':queryset,'form':form}
    return render(request, 'jobdetails.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        
        contact = Contact( name=name,  email=email, subject=subject, message=message)
        contact.save()

        return render(request,'email_sent.html')
    
    return render(request, 'contact.html')
    