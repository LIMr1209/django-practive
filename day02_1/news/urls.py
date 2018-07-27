"""day02_1 URL Configuration

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
from .views import show_news,new_date

urlpatterns = [
    url(r'^show_news/$',show_news,name='show_news'),
    # url(r'^new_date/(\d+)/(\d+)/(\d+)/$',new_date,name='new_date'),
    url(r'^new_date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$',new_date,name='new_date')
]
