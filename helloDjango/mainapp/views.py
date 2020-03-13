from django.http import HttpResponse
from django.shortcuts import render, redirect
from mainapp.models import UserEntity


# Create your views here.
def user_list1(request):
    users = [
        {'id': 1, "name": 'disen'},
        {'id': 2, 'name': 'jack'},
        {'id': 3, 'name': 'wa'}
    ]
    return render(request, 'user/index.html', {
        'users': users,
        'msg': 'xxxxx'
    })


def user_list2(request):
    users = [
        {'id': 1, "name": 'disen'},
        {'id': 2, 'name': 'jack'},
        {'id': 3, 'name': 'wa'}
    ]
    msg = 'xxxxxxxx'
    return render(request, 'user/index.html', locals())


def add_user(request):
    name = request.GET.get("name", None)
    age = request.GET.get("age", None)
    phone = request.GET.get('phone', None)

    if not all((name, age, phone)):
        return HttpResponse("请求参数不完整", status=400)

    ul = UserEntity()
    ul.name = name
    ul.age = age
    ul.phone = phone
    ul.save()

    return redirect('/user/list3')


def user_list3(request):
    users = UserEntity.objects.all()
    msg = "优秀"
    return render(request, 'user/index.html', locals())
