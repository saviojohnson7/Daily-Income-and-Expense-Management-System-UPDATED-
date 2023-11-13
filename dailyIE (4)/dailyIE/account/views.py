from django.shortcuts import render,redirect

# Create your views here.
def home1(request):
    context={'bal':get_balance(request),'incb':get_income(request),'expb':get_expense(request)}
    
    return render(request,'home.html',context)

from django.contrib.auth.forms import UserCreationForm

def reg1(request):
    if request.method=="POST":
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/reg')
    
    else:
        q=UserCreationForm
        s={'k':q}
        return render(request,'form.html',s)


from .models import LoginForm
from django.contrib.auth import authenticate,login,logout
# from django.contrib import messages as m


def login12(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:

            request.session['uid']=user.id # session id is stored in user.id. id is stored in uid
            login(request,user)
            return redirect('/')
        else:
            f=LoginForm
            context={'d':f}
            return render(request,'login.html',context)
    else:
        f=LoginForm
        context={'d':f}
        return render(request,'login.html',context)
    

def logout12(request):
    logout(request)
    return redirect('/')

from income.models import Income
from expense.models import Expense

def get_balance(request):
    uid=request.session.get('uid')  
    incl=Income.objects.filter(user=uid)
    expl=Expense.objects.filter(user=uid)

    total_income=0
    total_expense=0

    for i in incl:
        total_income=total_income + i.income
      

    for i in expl:
        total_expense=total_expense + i.expense

    return total_income - total_expense


def get_income(request):
    uid=request.session.get('uid')  
    incl=Income.objects.filter(user=uid)
    

    total_income=0
    for i in incl:
        total_income=total_income + i.income
      
    return total_income 


def get_expense(request):
    uid=request.session.get('uid')  
    
    expl=Expense.objects.filter(user=uid)

    total_expense=0
    for i in expl:
        total_expense=total_expense + i.expense

    return  total_expense


from django.contrib.auth.models import User
from .models import UserForm, UserForm1
def edit1(request):
    uid=request.session.get('uid')
    u=User.objects.get(id=uid)       # object means the username
    if request.method=='POST':
        f=UserForm(request.POST,instance=u)
        f.save()
        return redirect('/')
    
    else:

        f=UserForm(instance=u)
        context={'edit2':f}
        return render(request,'updateuser.html',context)

# create model for edit profile, go to models

def change_name(request):
     uid=request.session.get('uid')
     u=User.objects.get(id=uid)       # object means the username
     if request.method=='POST':
        f=UserForm1(request.POST,instance=u)
        f.save()
        return redirect('/')
    
     else:

        f=UserForm1(instance=u)
        context={'edit3':f}
        return render(request,'upusername.html',context)
     


def about1(request):
    return render(request,'about.html')
    


