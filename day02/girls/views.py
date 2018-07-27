from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    a='哈哈'
    list=[1,2,3,4,5]
    dict={'name':'张三','age':40}
    context={'a':a,'list':list,'dict':dict}
    return  render(request,'index.html',context)
def meinv(request):
    return render(request,'meinv.html')
def zly(request):

    return  HttpResponse('哈哈，没有')
