import random

from django.db.models import Max
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from two.models import Student, User, Grade, Customer


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
        "hobby": "打游戏"
    }
    return render(request, 'student_list.html', context=context)


def get_user(request):
    username = "123"
    password = '123'

    users = User.objects.filter(u_name=username)
    if users.count():
        user = users.first()
        if user.u_password == password:
            print('ok')
        else:
            print('bu')
    else:
        print('u b z')
    return HttpResponse('ok')


def get_grade(request):
    grades = Grade.objects.filter(student__s_name='12312')
    for grade in grades:
        print(grade)

    return HttpResponse('ok')


def get_curstomer(request):
    res = Customer.objects.aggregate(Max('c_cost'))
    print(res)
    return HttpResponse('ok')


def have_request(request):
    print(request.path)
    print(request.method)
    print(request.GET)
    print(request.POST)
    return HttpResponse('ok')


