from django.shortcuts import render, redirect, reverse
from .forms import UserRegisterForm, UserLoginForm
from .models import UserProfile
from django.contrib.auth import logout, login, authenticate
from articles.models import ArticleInfo, TagInfo, ArticleTags
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def index(request):
    all_articles = ArticleInfo.objects.all()

    click_article = all_articles.order_by('-click_num')[:6]
    comment_article = all_articles.order_by('-comment_num')[:6]
    time_article = all_articles.order_by('-add_time')[:6]
    file_time = ArticleInfo.objects.dates('add_time', 'month')

    all_tags = TagInfo.objects.all()

    tag_id = request.GET.get('tagid', '')
    if tag_id:
        all_articles_tags = ArticleTags.objects.filter(tag_info_id=tag_id)
        all_articles = [item.article_info for item in all_articles_tags]

    year = request.GET.get('year', '')
    month = request.GET.get('month', '')
    if year and month:
        all_articles = all_articles.filter(add_time__year=year,add_time__month=month)
        # all_articles = ArticleInfo.objects.filter(add_time__year=year, add_time__month=month)
    pa = Paginator(all_articles, 2)
    # print(pa.count,pa.page_range,pa.num_pages)
    pagenum = request.GET.get('pagenum')
    try:
        page_list = pa.page(pagenum)
    except PageNotAnInteger:
        page_list = pa.page(1)
    except EmptyPage:
        page_list = pa.page(pa.num_pages)
    # print(page_list.object_list)

    return render(request, 'index.html', {
        'page_list': page_list,
        'click_article': click_article,
        'comment_article': comment_article,
        'time_article': time_article,
        'file_time': file_time,
        'all_tags': all_tags,
        'tagid': tag_id,
        'year': year,
        'month': month
    })


def user_register(request):
    if request.method == 'GET':
        return render(request, 'user_register.html')
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            username = user_register_form.cleaned_data['username']
            password = user_register_form.cleaned_data['password']
            password1 = user_register_form.cleaned_data['password1']
            user = UserProfile.objects.filter(username=username)
            if user:
                return render(request, 'user_register.html', {
                    'msg': '用户名存在'
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
            return render(request, 'user_register.html', {
                'user_register_form': user_register_form
            })


def user_login(request):
    if request.method == 'GET':
        return render(request, 'user_login.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return render(request, 'user_login.html', {
                    'msg': '用户名或密码错误'
                })
        else:
            return render(request, 'user_login.html', {
                'user_login_form': user_login_form
            })


def user_logout(request):
    logout(request)
    return redirect(reverse('index'))
