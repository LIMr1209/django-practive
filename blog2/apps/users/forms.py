from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(min_length=6, max_length=10, required=True, error_messages={
        "min_length": '用户名太短',
        'max_length': '用户名太长',
        'required': '不能为空'
    })
    password = forms.CharField(min_length=3, max_length=10, required=True)
    password1 = forms.CharField(min_length=3, max_length=10, required=True)


class UserLoginForm(forms.Form):
    username = forms.CharField(min_length=6, max_length=10, required=True, error_messages={
        "min_length": '用户名太短',
        'max_length': '用户名太长',
        'required': '不能为空'
    })
    password = forms.CharField(min_length=3, max_length=10, required=True)
