from django.shortcuts import render, redirect, reverse
from .models import UserProfile
from hashlib import sha1
from datetime import timedelta


# Create your views here.
def index(request):
    return render(request, 'index.html')


def user_register(request):
    if request.method == 'GET':
        return render(request, 'user_register.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password1 = request.POST.get('password1', '')
        user = UserProfile.objects.filter(username=username)
        if user:
            return render(request, 'user_register.html', {
                'msg': "用户名已经存在"
            })
        else:
            if password1 == password:
                user = UserProfile()
                user.username = username
                user.password = sha1(password.encode('utf-8')).hexdigest()
                user.save()
                return redirect(reverse('index'))
            else:
                return render(request, 'user_register.html', {
                    'msg': "两次输入的密码不一致"
                })


def user_login(request):
    if request.method == 'GET':
        return render(request, 'user_login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        checkname = request.POST.get('checkname')
        password = sha1(password.encode('utf-8')).hexdigest()
        user = UserProfile.objects.filter(username=username, password=password)
        if user:
            # ret = redirect(reverse('index'))
            # ret.set_cookie('uname', username, max_age=10)
            # return ret
            if checkname:
                request.session['checkname'] = username
            else:
                if request.session.get('checkname'):
                    del request.session['checkname']
            request.session['uname'] = username
            request.session.set_expiry(timedelta(seconds=10))
            # print(request.COOKIES.get('session_id'))
            return redirect(reverse('index'))
        else:
            return render(request, 'user_login.html', {
                'msg': "用户名或密码输入错误"
            })


def user_logout(request):
    request.session.flush()
    # request.session.clear()
    return redirect(reverse('index'))
