from django.shortcuts import render, redirect, reverse
from .models import ArticleInfo, Category, TagInfo, ArticleTag, CommentInfo
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from .forms import CommentForm, ArticleAddForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    all_article = ArticleInfo.objects.all()

    click_sort = all_article.order_by('-click_num')[:6]
    comment_sort = all_article.order_by('-comment_num')[:6]
    recommend_sort = all_article.order_by('-add_time')[:6]

    article_times = ArticleInfo.objects.dates('add_time', 'month')

    all_tags = TagInfo.objects.all()

    tag_id = request.GET.get('tagid', '')
    if tag_id:
        all_article_tags = ArticleTag.objects.filter(taginfo_id=tag_id)
        all_article = [item.articleinfo for item in all_article_tags]
    year = request.GET.get('year', '')
    month = request.GET.get('month', '')
    if year and month:
        all_article = all_article.filter(add_time__year=year, add_time__month=month)

    page_num = request.GET.get('page', '')
    pa = Paginator(all_article, 2)
    try:
        page_list = pa.page(page_num)
    except PageNotAnInteger:
        page_list = pa.page(1)
    except EmptyPage:
        page_list = pa.page(pa.num_pages)
    return render(request, 'index.html', {
        'all_article': all_article,
        'page_list': page_list,
        'click_sort': click_sort,
        'comment_sort': comment_sort,
        'recommend_sort': recommend_sort,
        'article_times': article_times,
        'all_tags': all_tags,
        'tag_id': tag_id,
        'year': year,
        'month': month
    })


def article_detail(request, art_id):
    if art_id:
        all_article = ArticleInfo.objects.all()
        click_sort = all_article.order_by('-click_num')[:6]
        comment_sort = all_article.order_by('-comment_num')[:6]
        recommend_sort = all_article.order_by('-add_time')[:6]

        article_times = ArticleInfo.objects.dates('add_time', 'month')

        all_tags = TagInfo.objects.all()
        art = ArticleInfo.objects.filter(id=art_id)[0]
        art.click_num += 1
        art.save()
        art_tags = ArticleTag.objects.filter(articleinfo_id=art_id)
        tags_detail = [item.taginfo for item in art_tags]

        comments = art.commentinfo_set.all()

        return render(request, 'article_detail.html', {
            'art': art,
            'tags_detail': tags_detail,
            'comments': comments,
            'click_sort': click_sort,
            'comment_sort': comment_sort,
            'recommend_sort': recommend_sort,
            'article_times': article_times,
            'all_tags': all_tags,
        })
    else:
        pass


@login_required(login_url='/users/user_login')
def comment_add(request, art_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        if art_id:
            comment = comment_form.cleaned_data['comment']
            art = ArticleInfo.objects.filter(id=art_id)[0]
            art.comment_num += 1
            art.save()
            a = CommentInfo()
            a.comment_article = art
            a.comment_man = request.user
            a.comment_content = comment
            a.save()
            return redirect(reverse('articles:article_detail', args=[art_id]))
        else:
            pass
    else:
        # return redirect(reverse('articles:article_detail' , args=[art_id,comment_form]))

        pass


@login_required(login_url='/users/user_login')
def comment_delete(request, comment_id):
    if comment_id:
        comment = CommentInfo.objects.filter(id=comment_id)[0]
        art_id = comment.comment_article_id
        comment.delete()
        art = ArticleInfo.objects.filter(id=art_id)[0]
        art.comment_num -= 1
        if art.comment_num <= 0:
            art.comment_num = 0
        art.save()
        return redirect(reverse('articles:article_detail', args=[art_id]))
    else:
        pass


@login_required(login_url='/users/user_login')
def love_add(request):
    # if request.is_ajax()
    art_id = request.POST.get('artid', '')
    if art_id:
        art = ArticleInfo.objects.filter(id=art_id)[0]
        art.love_num += 1
        art.save()
        return JsonResponse({
            'status': 'ok'
        })


@login_required(login_url='/users/user_login')
def article_add(request):
    if request.method == 'GET':
        return render(request, 'articles_add.html')
    else:
        article_add_form = ArticleAddForm(request.POST, request.FILES)
        if article_add_form.is_valid():
            arttitle = article_add_form.cleaned_data['arttitle']
            artdesc = article_add_form.cleaned_data['artdesc']
            artcontent = article_add_form.cleaned_data['artcontent']
            artimage = article_add_form.cleaned_data['artimage']
            art = ArticleInfo()
            art.title = arttitle
            art.desc = artdesc
            art.content = artcontent
            art.image = artimage
            art.author = request.user
            art.category_id = 1
            art.save()
            return redirect(reverse('index'))
        else:
            pass
