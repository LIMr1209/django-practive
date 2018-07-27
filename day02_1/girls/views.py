from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def show_girls(request):
    return render(request,'girls_indez.html')
def girls_date(request):
    name=request.GET.get("name",'')
    age=request.GET.get('age','未知')
    gender=request.GET.get('gender','未知')
    return render(request,'girls_date.html',{
        'name':name,
        'age':age,
        'gender':gender,
    })