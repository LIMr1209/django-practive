from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def cf_index(request):
    return render(request, 'cf_index.html')


def gun(request, a, b, c, name):
    rmb = a + b + c + '元'
    return render(request, 'gun.html', {
        'name': name,
        'rmb': rmb
    })
