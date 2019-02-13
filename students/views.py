from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student
from company.models import *
from pprint import pprint as pp
import datetime

def index(request):
    list_student = Student.objects.all()
    students = list()
    for item in list_student:
        student = dict()
        student['id'] = item.id
        student['fio'] = item.name
        student['phone'] = item.phone
        student['middle'] = item.studentattestatege_set.get().middle
        student["lesson"] = item.studentattestatege_set.get().lesson
        student["score"] = item.studentattestatege_set.get().score
        students.append(student)

    return render(request, 'students/index.html', locals())


def student(request, student_id):
    student_id = student_id
    return render(request, "students/item.html", locals())

#Добавление нового студента
def ajax_add_student(request):

    name = request.POST.get('name')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    birth = request.POST.get('birth')
    school = request.POST.get('school')
    money = request.POST.get('money')
    created = datetime.datetime.now()
    updated = datetime.datetime.now()

    s = Student(name=name,
                address=address,
                phone=phone,
                birth=birth,
                school=school,
                money=money,
                created=created,
                updated=updated)
    s.save()
    # Нужно еще добавить поля
    return HttpResponse('Создано')
