from django.shortcuts import render, redirect, reverse
from .models import StudentInfo


# Create your views here.
def index(request):
    return render(request, 'index.html')


def students_show(request):
    students_all = StudentInfo.objects.all()
    return render(request, 'students_show.html', {
        'students_all': students_all
    })


def students_add(request):
    if request.method == 'GET':
        return render(request, 'students_add.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        height = request.POST.get('height')
        gender = request.POST.get('gender')
        stuid = request.POST.get('stuid')
        # StudentInfo.objects.create(name=name,age=int(age),height=float(height),gender=gender,stuid=stuid)
        a = StudentInfo()
        a.name = name
        a.age = int(age)
        a.height = float(height)
        a.gender = gender
        a.stuid = stuid
        a.save()
        return redirect(reverse('students_index:students_show'))
