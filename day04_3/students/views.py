from django.shortcuts import render, redirect, reverse
from .models import BanClass, CardId, StudentsInfo


# Create your views here.
def index(request):
    return render(request, 'index.html')


def student_list(request):
    students = StudentsInfo.objects.all()
    return render(request, 'student_list.html', {
        'students': students
    })


def student_delete(request, stu_id):
    if stu_id:
        student = StudentsInfo.objects.filter(id=stu_id)[0]
        student.cardid.delete()
        student.delete()

        return redirect(reverse('students:student_list'))
    else:
        pass


def student_update(request, stu_id):
    if request.method == 'GET':
        if stu_id:
            all_bans = BanClass.objects.all()
            student = StudentsInfo.objects.filter(id=stu_id)[0]
            return render(request, 'student_update.html', {
                'student': student,
                'all_bans': all_bans
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
            student = StudentsInfo.objects.filter(id=stu_id)[0]
            student.name = stu_name
            student.age = int(stu_age)
            student.gender = stu_gender

            ban = BanClass.objects.filter(name=stu_class)[0]
            student.stu_class = ban
            student.save()

            student.cardid.id_number = stu_card
            student.cardid.save()

            return redirect(reverse('students:student_list'))
        else:
            pass


def student_add(request):
    if request.method == 'GET':
        all_bans = BanClass.objects.all()
        return render(request, 'student_add.html', {
            "all_bans": all_bans
        })
    else:
        stu_name = request.POST.get('stu_name', '')
        stu_age = request.POST.get('stu_age', '')
        stu_gender = request.POST.get('stu_gender', '')
        stu_class = request.POST.get('stu_class', '')
        stu_card = request.POST.get('stu_card', '')
        student = StudentsInfo()
        student.name = stu_name
        student.age = int(stu_age)
        student.gender = stu_gender

        ban = BanClass.objects.filter(name=stu_class)[0]
        student.stu_class = ban
        student.save()

        card = CardId()
        card.id_number=stu_card
        card.student=student
        card.save()

        return redirect(reverse('students:student_list'))
