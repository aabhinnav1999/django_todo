from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

@login_required
def home(request):
    if request.method=='POST':
        task=request.POST.get('task')
        new_todo=todo(user=request.user,todo_name=task)
        new_todo.save()

    all_todos=todo.objects.filter(user=request.user)
    context={
        'todos':all_todos
    }
    return render(request,'todoapp/todo.html',context)

# def register(request):
#     if request.user.is_authenticated:
#         return redirect('home-page')
#     if request.method=='POST':
#         username=request.POST.get('username')
#         email=request.POST.get('email')
#         password=request.POST.get('password')

#         if len(password)<4:
#             messages.error(request,'password must be atleast 4 characters')
#             return redirect('register')

#         get_all_users_by_username=User.objects.filter(username=username)

#         if get_all_users_by_username:
#             messages.error(request,'username already exists, try another')
#             return redirect('register')

#         new_user=User.objects.create_user(username=username,email=email,password=password)
#         new_user.save()
#         messages.success(request,'user successfully created, login now!')
#     return render(request,'todoapp/register.html',{})

def register(request):
    # context={}
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if len(password)<4:
            messages.error(request,'password must be atleast 4 characters')
            return redirect('register')

        get_all_users_by_username=User.objects.filter(username=username)

        if get_all_users_by_username:
            messages.error(request,'username already exists, try another')
            return redirect('register')

        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request,'user successfully created, login now!')

        m=datetime.datetime.now().minute
        s=datetime.datetime.now().second

        while True:
            if datetime.datetime.now().second==int(s)+5 and datetime.datetime.now().minute==m:
                # print('if',datetime.datetime.now().minute,datetime.datetime.now().second)
                # context['flag']=True
                # print(context)
                return redirect('login')
            elif datetime.datetime.now().minute==m+1:
                # print('elif',datetime.datetime.now().minute,datetime.datetime.now().second)
                # context['flag']=True
                # print(context)
                return redirect('login')

    return render(request,'todoapp/register.html',{})

def logoutview(request):
    logout(request)
    return redirect('login')

def loginpage(request):
    # context={}
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')

        validate_user=authenticate(username=username,password=password)

        if validate_user is not None:
            login(request,validate_user)
            return redirect('home-page')
        else:
            # context['flag']=False
            messages.error(request,'wrong user details or user does not exist')
            return redirect('login')

    return render(request,'todoapp/login.html',{})

@login_required
def Deletetask(request,name):
    get_todo=todo.objects.get(user=request.user,todo_name=name)
    get_todo.delete()
    return redirect('home-page')

@login_required
def Updatetask(request,name):
    get_todo=todo.objects.get(user=request.user,todo_name=name)
    get_todo.status=True
    get_todo.save()
    return redirect('home-page')
