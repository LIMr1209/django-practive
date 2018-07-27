from django.shortcuts import render, redirect, reverse
from .models import Camp, Hero, EnglishName


# Create your views here.
def index(request):
    return render(request, 'index.html')


def hero_list(request):
    all_heros = Hero.objects.all()
    return render(request, 'hero_list.html', {
        'all_heros': all_heros
    })


def hero_delete(request, hero_id):
    if hero_id:
        hero = Hero.objects.filter(id=hero_id)[0]
        hero.englishname.delete()
        hero.delete()
        return redirect(reverse('lol:hero_list'))
    else:
        pass


def hero_update(request, hero_id):
    if request.method == 'GET':
        if hero_id:
            hero = Hero.objects.filter(id=hero_id)[0]
            all_camps = Camp.objects.all()
            return render(request, 'hero_update.html', {
                'hero': hero,
                'all_camps': all_camps

            })
        else:
            pass
    else:
        if hero_id:
            hero_name = request.POST.get('hero_name', '')
            hero_byname = request.POST.get('hero_byname', '')
            hero_gender = request.POST.get('hero_gender', '')
            hero_camp = request.POST.get('hero_camp', '')
            hero_english_name = request.POST.get('hero_english_name', '')
            hero = Hero.objects.filter(id=hero_id)[0]
            hero.name = hero_name
            hero.byname = hero_byname
            hero.gender = hero_gender
            camp = Camp.objects.filter(name=hero_camp)[0]
            hero.hero_camp = camp
            hero.save()
            hero.englishname.name = hero_english_name
            hero.englishname.save()
            return redirect(reverse('lol:hero_list'))
        else:
            pass


def hero_add(request):
    if request.method == 'GET':
        all_camps = Camp.objects.all()
        return render(request, 'hero_add.html', {
            'all_camps': all_camps
        })
    else:
        hero_name = request.POST.get('hero_name', '')
        hero_byname = request.POST.get('hero_byname', '')
        hero_gender = request.POST.get('hero_gender', '')
        hero_camp = request.POST.get('hero_camp', '')
        hero_english_name = request.POST.get('hero_english_name', '')
        hero = Hero()
        hero.name = hero_name
        hero.byname = hero_byname
        hero.gender = hero_gender
        camp = Camp.objects.filter(name=hero_camp)[0]
        hero.hero_camp = camp
        hero.save()

        english = EnglishName()
        english.name = hero_english_name
        english.hero = hero
        english.save()
        return redirect(reverse('lol:hero_list'))
