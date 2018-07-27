"""blog3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import article_detail, comment_add, comment_delete, article_add, love_add

urlpatterns = [
    url(r'^article_detail/(\d+)$', article_detail, name='article_detail'),
    url(r'^comment_add/(\d+)$', comment_add, name='comment_add'),
    url(r'^comment_delete/(\d+)$', comment_delete, name='comment_delete'),
    url(r'^article_add/$', article_add, name='article_add'),
    url(r'^love_add/$', love_add, name='love_add'),
]
