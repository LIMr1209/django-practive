from django.shortcuts import render, redirect, reverse
from .models import ArticleInfo, ArticleTags, TagInfo, Category, CommentInfo
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from .forms import ArticleAddForm, CommentForm
from django.http import JsonResponse

# Create your views here.

def index(request):
    all_articles = ArticleInfo.objects.all()

    click_sort = all_articles.order_by('-click_num')[:6]
    comment_sort = all_articles.order_by('-comment_num')[:6]
    recommend_sort = all_articles.order_by('-add_time')[:6]

    all_tags = TagInfo.objects.all()

    time_articles = ArticleInfo.objects.dates('add_time', 'month')

    tagid = request.GET.get('tagid', '')
    if tagid:
        all_articles_tags = ArticleTags.objects.filter(tag_info_id=tagid)
        all_articles = [item.article_info for item in all_articles_tags]
    year = request.GET.get('year', '')
    month = request.GET.get('month', '')
    if year and month:
        all_articles = all_articles.filter(add_time__year=year, add_time__month=month)

    pa = Paginator(all_articles, 2)
    page_num = request.GET.get('page')
    try:
        page_list = pa.page(page_num)
    except PageNotAnInteger:
        page_list = pa.page(1)
    except EmptyPage:
        page_list = pa.page(pa.num_pages)
    return render(request, 'index.html', {
        'all_articles': all_articles,
        'click_sort': click_sort,
        'comment_sort': comment_sort,
        'recommend_sort': recommend_sort,
        'all_tags': all_tags,
        'time_articles': time_articles,
        'page_list': page_list,
        'tagid': tagid,
        'year': year,
        'month': month

    })


def article_detail(request, art_id):
    if art_id:
        art = ArticleInfo.objects.filter(id=art_id)[0]
        art.click_num += 1
        art.save()
        art_tags = ArticleTags.objects.filter(article_info_id=art_id)
        tags_detail = [item.tag_info for item in art_tags]
        all_comments = art.commentinfo_set.all()

        all_articles = ArticleInfo.objects.all()
        click_sort = all_articles.order_by('-click_num')[:6]
        comment_sort = all_articles.order_by('-comment_num')[:6]
        recommend_sort = all_articles.order_by('-add_time')[:6]

        all_tags = TagInfo.objects.all()

        time_articles = ArticleInfo.objects.dates('add_time', 'month')

        return render(request, 'article_detail.html', {
            'art': art,
            'tags_detail': tags_detail,
            'all_comments': all_comments,
            'click_sort': click_sort,
            'comment_sort': comment_sort,
            'recommend_sort': recommend_sort,
            'all_tags': all_tags,
            'time_articles': time_articles,
        })
    else:
        pass


def comment_add(request, art_id):
    if art_id:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            content = comment_form.cleaned_data['comment']
            art = ArticleInfo.objects.filter(id=art_id)[0]
            art.comment_num += 1
            art.save()
            a = CommentInfo()
            a.comment_content = content
            a.comment_man = request.user
            a.comment_article = art
            a.save()
            return redirect(reverse('articles:article_detail', args=[art_id]))
        else:
            pass
    else:
        pass


def comment_delete(request, comment_id):
    if comment_id:
        a = CommentInfo.objects.filter(id=comment_id)[0]
        a.comment_article.comment_num -= 1
        art_id = a.comment_article.id
        a.comment_article.save()
        a.delete()
        return redirect(reverse('articles:article_detail', args=[art_id]))
    else:
        pass


def article_add(request):
    if request.method == 'GET':
        return render(request, 'article_add.html')
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


def love_add(request):
    artid = request.POST.get('artid','')
    if artid:
        art = ArticleInfo.objects.filter(id=artid)[0]
        art.love_num+=1
        art.save()
        return JsonResponse({
            'status':'ok',
        })
    else:
        pass
