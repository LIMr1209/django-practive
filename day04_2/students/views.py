from django.shortcuts import render,redirect,reverse
from .models import CardId, StudentsInfo, BanClass


# Create your views here.
def index(request):
    return render(request, 'index.html')


def students_list(request):
    students = StudentsInfo.objects.all()
    return render(request, 'students_list.html', {
        'students': students
    })


def students_delete(request,stu_id):
    if stu_id:
        student = StudentsInfo.objects.filter(id=stu_id)[0]
        student.cardid.delete()
        student.delete()
        return redirect(reverse('students:students_list'))
    else:
        pass


def students_update(request,stu_id):
    if request.method == 'GET':
        if stu_id:
            all_bans = BanClass.objects.all()
            studnet = StudentsInfo.objects.filter(id=stu_id)[0]
            return render(request,'students_update.html',{
                'student':studnet,
                'all_bans':all_bans
            })
        else:
            pass
    else:
        if stu_id:
            stu_name = request.POST.get('stu_name', '')
            stu_age = request.POST.get('stu_age', '')
            stu_gender = request.POST.get('stu_gender', '')
            stu_class = request.POST.get('stu_class', '')
            stu_card = request.POST.get('stu_card', '')

            studnet = StudentsInfo.objects.filter(id=stu_id)[0]
            studnet.name = stu_name
            studnet.age = int(stu_age)
            studnet.gender = stu_gender

            ban = BanClass.objects.filter(name=stu_class)[0]
            studnet.stu_class = ban
            studnet.save()

            studnet.cardid.id_number=stu_card
            studnet.cardid.save()
            return  redirect(reverse('students:students_list'))


def students_add(request):
    if request.method == 'GET':
        all_bans=BanClass.objects.all()

        return render(request,'students_add.html',{
            'all_bans':all_bans
        })
    if request.method == 'POST':
        student = StudentsInfo()
        stu_name = request.POST.get('stu_name', '')
        stu_age = request.POST.get('stu_age', '')
        stu_gender = request.POST.get('stu_gender', '')
        stu_class = request.POST.get('stu_class', '')
        stu_card = request.POST.get('stu_card', '')
        student.name = stu_name
        student.age = int(stu_age)
        student.gender = stu_gender


        ban = BanClass.objects.filter(name=stu_class)[0]
        student.stu_class = ban
        student.save()

        card = CardId()
        card.id_number = stu_card
        card.student = student
        card.save()

        return redirect(reverse('students:students_list'))