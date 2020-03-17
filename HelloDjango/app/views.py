import random

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpRequest
from django.shortcuts import render, loader
from django.urls import reverse

from app.models import Person


# Create your views here.

def hello(request):
    temp = loader.get_template('index.html')
    content = temp.render()
    return HttpResponse(content)


def index(request):
    return render(request, 'index.html')


# def home(request):
#     return render(request, 'index.html')


def add_person(request):
    for i in range(15):
        person = Person()
        person.p_name = "tom%d" % i
        person.p_age = i
        person.p_sex = i % 2
        person.save()
    return HttpResponse("ok")


def get_person(request):
    # persons = Person.objects.filter(p_age__gt=2).filter(p_age__lt=8)
    persons = Person.objects.exclude(p_age__gt=2)
    context = {
        "persons": persons
    }

    return render(request, "app/person_list.html", context=context)


def add_person1(request):
    # p = Person.objects.create(
    #     p_name='张三',
    #     p_age=18,
    #     p_sex=1
    # )
    # p.save()

    p = Person.create('jack')
    p.save()
    return HttpResponse("ok")


def temp(request):
    return render(request, 'app/home.html', context={'title': 'home'})


def home(request):
    return render(request, 'app/home_mine.html', context={'title': 'home_mine'})


def get_ticket(request):
    # if random.randrange(10) > 5:
    #     return HttpResponseRedirect('/index/home')
    # else:
    #     return HttpResponseRedirect('dxxx')

    url = reverse("second:hello")
    return HttpResponseRedirect(url)


def get_info(request):
    #    print(request.COOKIES.get("name"))
    print(request.get_signed_cookie('name', salt='1111'))

    return JsonResponse(data={
        'a': 'ahdhasd'
    })


def set_cookies(request):
    response = HttpResponse("设置cookie")
    # response.set_cookie("name", 'ddd')

    response.set_signed_cookie('name', 'dddd', salt='1111')
    # print(request.COOKIES['name'])
    # print(request.get_signed_cookie('name'))

    return response


def login(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        request.session['username'] = username
        return HttpResponse("ok")


def mine(request: HttpRequest):
    username = request.session.get('username')
    print(username)


