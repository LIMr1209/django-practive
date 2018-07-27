from django.shortcuts import render,HttpResponse


# Create your views here.
def news_index(request):
    return render(request, 'news_index.html')


def news_data(request, year, month, day):
    time = year + '年' + month + '月' + day + '日'
    return render(request,'news_data.html',{
        'time':time
    })


def show_form(request):
    if request.method=='GET':
        return render(request,'form.html')
    elif request.method=='POST':
        user=request.POST.get('user')
        password=request.POST.get('password')
        return  HttpResponse(user+password)