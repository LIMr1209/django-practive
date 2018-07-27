from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def girls_index(request):
    return render(request,'girls_index.html')
def girls_data(request):
    name=request.GET.get('name','')
    age=request.GET.get('age','未知')
    gender=request.GET.get('gender','未知')
    return render(request,'girls_data.html',{
        'name':name,
        'age':age,
        'gender':gender,
    })