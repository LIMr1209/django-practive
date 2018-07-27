from django.shortcuts import render,redirect,reverse
from .models import UserProfile
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth import logout,login,authenticate


# Create your views here.
def user_register(request):
    if request.method == 'GET':
        return render(request, 'user_register.html')
    else:
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            password1 = register_form.cleaned_data['password1']
            user = UserProfile.objects.filter(username=username)
            if user:
                return render(request,'user_register.html',{
                    'msg':'用户名存在'
                })
            else:
                if password == password1:
                    user = UserProfile()
                    user.username = username
                    user.set_password(password)
                    user.save()
                    return redirect(reverse('index'))
                else:
                    return render(request, 'user_register.html', {
                        'msg': '密码不一致'
                    })
        else:
            return render(request,'user_register.html',{
                'register_form':register_form
            })

def user_login(request):
    if request.method == 'GET':
        return render(request,'user_login.html')
    else:
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect(reverse('index'))
            else:
                return render(request, 'user_login.html', {
                    'msg': '用户名或密码错误'
                })
        else:
            return render(request, 'user_login.html', {
                'login_form': login_form
            })
def user_logout(request):
    logout(request)
    return redirect(reverse('index'))
