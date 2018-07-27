from django.shortcuts import render, redirect, reverse
from .models import LoLHero


# Create your views here.
def index(request):
    return render(request, 'index.html')


def hero_show(request):
    hero_list = LoLHero.objects.all()
    return render(request, 'hero_list.html', {
        'hero_list': hero_list
    })


def hero_add(request):
    if request.method == 'GET':
        return render(request, 'hero_add.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        byname = request.POST.get('byname')
        price = request.POST.get('price')
        gender = request.POST.get('gender')
        type = request.POST.get('type')
        LoLHero.objects.create(name=name,byname=byname,price=int(price),gender=gender,type=type)
        return redirect(reverse('lol:hero_show'))