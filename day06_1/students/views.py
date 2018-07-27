from django.shortcuts import render, redirect, reverse
from .models import BanClass, CardId, StudentInfo
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url='/users/user_login')
def student_list(request):
    students = StudentInfo.objects.all()
    return render(request, 'student_list.htm', {
        'students': students,
        'flag': 'list'
    })


@login_required(login_url='/users/user_login')
def student_delete(request, stu_id):
    student = StudentInfo.objects.filter(id=stu_id)
    student.delete()
    return redirect(reverse('students:student_list'))


@login_required(login_url='/users/user_login')
def student_update(request, stu_id):
    if request.method == 'GET':
        if stu_id:
            all_bans = BanClass.objects.all()
            student = StudentInfo.objects.filter(id=stu_id)[0]
            return render(request, 'student_update.htm', {
                'all_bans': all_bans,
                'student': student
            })
        else:
            pass
    else:
        if stu_id:
            stu_name = request.POST.get("stu_name", '')
            stu_age = request.POST.get("stu_age", '')
            stu_gender = request.POST.get("stu_gender", '')
            stu_class = request.POST.get("stu_class", '')
            stu_card = request.POST.get("stu_card", '')
            student = StudentInfo.objects.filter(id=stu_id)[0]
            student.name = stu_name
            student.age = int(stu_age)
            student.gender = stu_gender
            ban = BanClass.objects.filter(name=stu_class)[0]
            student.stu_ban = ban
            student.save()
            student.cardid.id_number = stu_card
            student.cardid.save()
            return redirect(reverse('students:student_list'))
        else:
            pass


@login_required(login_url='/users/user_login')
def student_add(request):
    if request.method == 'GET':
        all_bans = BanClass.objects.all()
        return render(request, 'student_add.html', {
            'all_bans': all_bans,
            'flag': 'add'
        })
    else:
        stu_name = request.POST.get("stu_name", '')
        stu_age = request.POST.get("stu_age", '')
        stu_gender = request.POST.get("stu_gender", '')
        stu_class = request.POST.get("stu_class", '')
        stu_card = request.POST.get("stu_card", '')
        student = StudentInfo()
        student.name = stu_name
        student.age = int(stu_age)
        student.gender = stu_gender
        ban = BanClass.objects.filter(name=stu_class)[0]
        student.stu_ban = ban
        student.save()
        card = CardId()
        card.id_number = stu_card
        card.stu_card = student
        card.save()
        return redirect(reverse('students:student_list'))
