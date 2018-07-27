from django.shortcuts import render, redirect, reverse
from .models import CardId, BanClass, StudentInfo


# Create your views here.
def index(request):
    return render(request, 'index.html')


def students_list(request):
    all_students = StudentInfo.objects.all()
    return render(request, 'students_list.html', {
        'all_students': all_students
    })


def students_update(request, stu_id):
    if request.method == 'GET':
        if stu_id:
            student = StudentInfo.objects.filter(id=stu_id)[0]
            all_bans = BanClass.objects.all()
            return render(request, 'students_update.html', {
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

            student = StudentInfo.objects.filter(id=stu_id)[0]
            student.name = stu_name
            student.age = int(stu_age)
            student.gender = stu_gender
            # 找到指定班级名称的班级对象
            ban = BanClass.objects.filter(name=stu_class)[0]
            # 让该学生对象通过关系字段与班级对象建立关系
            # student.stuclass_id =ban.id
            student.stuclass = ban

            student.save()
            # 通过学生对象.子对象类名(小写) 拿到学号对象 修改它的学号为传过来的学号
            student.cardid.id_number = stu_card
            student.cardid.save()
            return redirect(reverse('students:students_list'))
        else:
            pass


def students_delete(request, stu_id):
    if stu_id:
        student = StudentInfo.objects.filter(id=stu_id)[0]
        # 先删子表，在删主表
        student.cardid.delete()
        student.delete()
        #重定向（复用会话）  reverse 反响解析
        return redirect(reverse('students:students_list'))
    else:
        pass
def students_add(request):
    if request.method == 'GET':
        all_bans = BanClass.objects.all()
        return render(request,'students_add.html',{
            'all_bans':all_bans
        })
    else:
        student = StudentInfo()
        stu_name = request.POST.get('stu_name', '')
        stu_age = request.POST.get('stu_age', '')
        stu_gender = request.POST.get('stu_gender', '')
        stu_class = request.POST.get('stu_class', '')
        stu_card = request.POST.get('stu_card', '')
        student.name = stu_name
        student.age = int(stu_age)
        student.gender = stu_gender
        # 找到指定班级名称的班级对象
        ban = BanClass.objects.filter(name=stu_class)[0]
        # 让该学生对象通过关系字段与班级对象建立关系
        # student.stuclass_id = ban.id
        student.stuclass = ban
        student.save()
       #创建一个学号对象，该学号的id_number 等于传过来的stu_card
        card = CardId()
        card.id_number =stu_card
        #让该学号对象通过关系字段与学生对象建立关系
        # card.student_id=student.id
        card.student = student
        card.save()

        return redirect(reverse('students:students_list'))