from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def index(request):
    return render(request, 'index.html')


def user_register(request):
    if request.method == 'GET':
        return render(request, 'user_register.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password1 = request.POST.get('password', '')
        user = User.objects.filter(username=username)
        if user:
            return render(request, 'user_register.html', {
                'msg': '该账号已存在'
            })
        else:
            if password == password1:
                user = User()
                user.username = username
                user.set_password(password)
                user.save()
                return redirect(reverse('index'))
            else:
                return render(request, 'user_register.html', {
                    'msg': '两次输入密码不一致'
                })


def user_login(request):
    if request.method == 'GET':
        return render(request, 'user_login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        a = authenticate(username=username,password=password)
        if a:
            login(request,a)
            return redirect(reverse('index'))
        else:
            return render(request, 'user_login.html', {
                'msg': '账号或密码错误'
            })

def user_logout(request):
    logout(request)
    return redirect(reverse('index'))
