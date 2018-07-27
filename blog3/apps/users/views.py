from django.shortcuts import render,redirect,reverse
from .models import UserProfile
from django.contrib.auth import logout,login,authenticate
from .forms import UserLoginForm,UserRegisterForm


# Create your views here.
def user_register(request):
    if request.method == 'GET':
        return render(request,'user_register.html')
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            username = user_register_form.cleaned_data['username']
            password = user_register_form.cleaned_data['password']
            password1 = user_register_form.cleaned_data['password1']
            user = UserProfile.objects.filter(username=username)
            if user:
                return render(request,'user_register.html',{
                    'msg':'用户名存在'
                })
            else:
                if password1 == password:
                    user = UserProfile()
                    user.username = username
                    user.set_password(password)
                    user.save()
                    return redirect(reverse('index'))
                else:
                    return render(request, 'user_register.html', {
                        'msg': '两次密码输入不一致'
                    })
        else:
            return render(request, 'user_register.html', {
                'user_register_form':user_register_form
            })

def user_login(request):
    if request.method == 'GET':
        return render(request,'user_login.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect(reverse('index'))
            else:
                return render(request, 'user_login.html', {
                    'msg': '用户名不存在'
                })
        else:
            return render(request, 'user_login.html', {
                'user_login_form': user_login_form
            })


def user_logout(request):
    logout(request)
    return redirect(reverse('index'))



