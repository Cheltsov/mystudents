from django.shortcuts import render
from students.models import Student

def index(request):

    list_student = Student.objects.all()

    return render(request, 'students/index.html', locals())
