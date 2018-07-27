from django.shortcuts import render, redirect, reverse
from .models import UserProfile
from hashlib import sha1


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
                'msg': '用户已经存在'
            })
        else:
            if password == password1:
                a = UserProfile()
                a.username = username
                a.password = sha1(password.encode('utf-8')).hexdigest()
                a.save()
                return redirect(reverse('index'))
            else:
                return render(request, 'user_register.html', {
                    'msg': '两次密码输入不一致'
                })


def user_login(request):
    if request.method == 'GET':
        return render(request, 'user_login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        checkname = request.POST.get('checkname', '')
        password = sha1(password.encode('utf_8')).hexdigest()
        print(password)
        user = UserProfile.objects.filter(username=username, password=password)
        if user:
            # ret = redirect(reverse('index'))
            # # ret.set_cookie('uname',username,max_age=10)
            # ret.set_cookie('uname',username)
            # # ret.delete_cookie('uname')
            # return ret
            if checkname:
                request.session['checkname'] = username
            else:
                #通过此方法获取session  checkname 键的值，获取不到为空，不报错
                if request.session.get('checkname'):
                    del request.session['checkname']
            request.session['uname'] = username
            return redirect(reverse('index'))
        else:
            return render(request, 'user_login.html', {
                'msg': '用户或者密码不正确'
            })


def user_logout(request):
    del request.session['uname']
    # request.session.clear()
    # request.session.flush()
    return redirect(reverse('index'))
