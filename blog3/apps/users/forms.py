
from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=6, required=True, error_messages={
        'max_length': '用户名太长',
        'min_length': '用户名长度不够',
        'required': '用户名不能为空',
    })
    password = forms.CharField(max_length=10, min_length=3, required=True)
    password1 = forms.CharField(max_length=10, min_length=3, required=True)


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=10,min_length=6,required=True,error_messages={
        'max_length': '用户名太长',
        'min_length': '用户名长度不够',
        'required': '用户名不能为空',
    })
    password = forms.CharField(max_length=10,min_length=3,required=True)