from django.shortcuts import render,HttpResponse

# Create your views here.
def show_news(request):
    return render(request,'news_index.html')
def new_date(request,month,day,year):
    context={'time':year+'年'+month+'月'+day+'日'}
    return render(request,'new_data.html',context)