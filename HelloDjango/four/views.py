import hashlib
import random
import time

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from four.models import Student


def reg(request: HttpRequest):
    if request.method == 'GET':
        return render(request, './reg.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            stu = Student()
            stu.s_name = username
            stu.s_password = password
            stu.save()
            return HttpResponse('ok')
        except Exception as e:
            return redirect(reverse('four:reg'))


def login(request: HttpRequest):
    if request.method == 'GET':
        return render(request, './login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        stus = Student.objects.filter(s_name=username, s_password=password)
        if stus.exists():
            stu = stus.first()
            ip = request.META.get('REMOTE_ADDR')
            token = generate_token(ip, username)
            stu.s_token = token
            stu.save()
            response = HttpResponse('ok')
            response.set_cookie('token', token)
            return response
    return redirect(reverse('four:login'))


def generate_token(ip, username):
    c_time = time.ctime()
    r = username
    return hashlib.new('md5', (ip + c_time + r).encode('utf-8')).hexdigest()
