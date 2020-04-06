from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from five.models import Person, IDCard


def hello(request: HttpRequest):
    return HttpResponse('ok')


def addperson(request: HttpRequest):
    username = request.GET.get('username')
    person = Person()
    person.p_name = username
    person.save()
    return HttpResponse('ok-%d' % person.id)


def addcard(request: HttpRequest):
    num = request.GET.get('idnum')
    idcard = IDCard()
    idcard.id_name = num
    idcard.save()
    return HttpResponse('ok-%d' % idcard.id)


def bindcard(request: HttpRequest):
    person = Person.objects.last()
    idcard = IDCard.objects.last()
    idcard.id_person = person
    idcard.save()
    return HttpResponse('ok-%d' % idcard.id)
