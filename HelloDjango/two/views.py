from django.http import HttpResponse
from django.shortcuts import render

from two.models import Student


# Create your views here.


def index(request):
    return HttpResponse("hello two")


def add_student(request):
    student = Student()
    student.s_name = "张安"
    # student.s_age = 12
    student.save()
    return HttpResponse("添加成功" + student.s_name)


def get_students(request):
    students = Student.objects.all()
    for student in students:
        print(student.s_name)

    context = {
        "hobby" : "打游戏"
    }
    return render(request, 'student_list.html', context=context)
