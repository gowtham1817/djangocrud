from django.shortcuts import render,redirect
from .models import detail,UserData
from django.contrib.auth import login,logout, authenticate
from .forms import registerForm,authenticationForm,detailForm
from django.contrib import messages
import json
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.



def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
                email = form.cleaned_data.get('email')
                name = form.cleaned_data.get('name')
                password = form.cleaned_data.get('password')
                user = UserData.objects.create(email=email,name=name,password=password)
                user.set_password(password)
                user.save()
                # messages.success(request,f'Account created for {name}!')
                return redirect('loginForm')
        else:
            email = form.data.get('email')
            name = form.data.get('name')
            if UserData.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
           
    return render(request,'register.html')  
   
    
    
def loginForm(request):
    if request.method == 'POST':
        form = authenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('form')
            else:
                messages.error(request,'invalid user name and password')
                return redirect('loginForm')
        else:
            messages.error(request,'invalid user name and password')
    else:
        Form = authenticationForm()
        return render(request,'login.html',{'loginForm':Form})


def logoutForm(request):
    logout(request)
    return redirect('loginForm')

def form(request):

    if request.method == 'POST':
        form = detailForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number') 
            id = request.POST.get('id') 
            if id:
                details = detail.objects.get(id=id)
                details.name = name
                details.email = email
                details.number = number
                details.save()
            else:
                detail.objects.create(
                    name = name,
                    email = email,
                    number = number
                )
            return redirect('form')
    details = detail.objects.all()
    id = request.GET.get('id', None)
    detailSet = None
    if id:
        try:
            detailSet = detail.objects.get(id=id)
        except:
            detailSet = None
    if 'q' in request.GET:
        q = request.GET.get('q',None)
        multiple_q = Q(Q(name__icontains=q) | Q(email__icontains=q))
        page = detail.objects.filter(multiple_q) 
    else:
        page = detail.objects.all()
    items_per_page = 7
    paginator = Paginator(page, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
   
      
    return render(request,'form.html',{'details':details, 'detailset': detailSet,'page':page})


def show(request):
    if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number') 
            details = detail(
                 name = name,
                 email = email,
                 number = number
            )
            details.save() 
            return redirect('form')
    else:
       
        details = detail.objects.all()
        return render(request,'form.html',{'details':details})



def deleteForm(request,id):
    details = detail.objects.get(id=id)
    if request.method == 'POST':

        details.delete()
        return redirect('form')
    return render(request,'form.html')