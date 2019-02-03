from django.shortcuts import render
from students.models import Student
from company.models import *
from pprint import pprint


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
