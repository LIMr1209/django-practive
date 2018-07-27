"""day04_4 URL Configuration

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
from .views import hero_list,hero_delete,hero_update,hero_add


urlpatterns = [
    url(r'^hero_list/$', hero_list, name='hero_list'),
    url(r'^hero_delete/(\d+)/$', hero_delete, name='hero_delete'),
    url(r'^hero_update/(\d+)/$', hero_update, name='hero_update'),
    url(r'^hero_add/$', hero_add, name='hero_add')
]
