from django.shortcuts import render, redirect, reverse
from .models import ArticleInfo, ArticleTags, TagInfo, CommentInfo
from .forms import CommentForm,ArticleAddForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def article_detail(request, article_id):
    if article_id:
        art = ArticleInfo.objects.filter(id=article_id)[0]

        all_art_tags = ArticleTags.objects.filter(article_info_id=article_id)
        all_tags_detail = [item.tag_info for item in all_art_tags]

        all_articles = ArticleInfo.objects.all()
        click_article = all_articles.order_by('-click_num')[:6]
        comment_article = all_articles.order_by('-comment_num')[:6]
        time_article = all_articles.order_by('-add_time')[:6]
        file_time = ArticleInfo.objects.dates('add_time', 'month')
        all_tags = TagInfo.objects.all()

        all_comment = art.commentinfo_set.all()

        return render(request, 'article_detail.html', {
            'art': art,
            'all_tags_detail': all_tags_detail,
            'click_article': click_article,
            'comment_article': comment_article,
            'time_article': time_article,
            'file_time': file_time,
            'all_tags': all_tags,
            'all_comment': all_comment
        })
    else:
        pass


@login_required(login_url='/users/user_login')
def comment_add(request, article_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        if article_id:
            content = comment_form.cleaned_data['comment']
            a = CommentInfo()
            a.comment_content = content
            a.comment_man_id = request.user.id
            a.comment_article_id = article_id
            a.save()

            a.comment_article.comment_num += 1
            a.comment_article.save()
            return redirect(reverse('articles:article_detail', args=[article_id]))
        else:
            pass
    else:
        pass


@login_required(login_url='/users/user_login')
def comment_delete(request, comment_id):
    if comment_id:
        comment = CommentInfo.objects.filter(id=comment_id)[0]
        art = ArticleInfo.objects.filter(id=comment.comment_article_id)[0]
        comment.delete()
        art.comment_num -= 1
        if comment.comment_article.comment_num <= 0:
            comment.comment_article.comment_num = 0
        art.save()
        return redirect(reverse('articles:article_detail', args=[art.id]))
    else:
        pass


def love_add(request):
    artid =request.POST.get('artid')
    if artid:
        art = ArticleInfo.objects.filter(id=artid)[0]
        art.love_num+=1
        art.save()
        return JsonResponse({
            'status':'ok'
        })
    else:
        pass

def article_add(request):
    if request.method == 'GET':
        return render(request,'article_add.html')
    else:
        art_add_form = ArticleAddForm(request.POST,request.FILES)
        if art_add_form.is_valid():
            art_title = art_add_form.cleaned_data['arttitle']
            art_desc = art_add_form.cleaned_data['artdesc']
            art_image = art_add_form.cleaned_data['artimage']
            art_content = art_add_form.cleaned_data['artcontent']
            art = ArticleInfo()
            art.title = art_title
            art.desc = art_desc
            art.image = art_image
            art.content = art_content
            art.author = request.user
            art.category_id = 1
            art.save()
            return redirect(reverse('index'))
        else:
            pass