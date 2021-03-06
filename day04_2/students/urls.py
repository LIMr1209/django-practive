"""day04_2 URL Configuration

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
from .views import students_list,students_delete,students_update,students_add

urlpatterns = [
    url(r'^students_list/$',students_list,name='students_list'),
    url(r'^students_delete/(\d+)/$',students_delete,name='students_delete'),
    url(r'^students_update/(\d+)/$',students_update,name='students_update'),
    url(r'^students_add/$', students_add, name='students_add')
]

