from django.conf.urls import url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'^index/', views.index),
    url(r'^add/', views.add_person),
    url(r'^add1/', views.add_person1),
    url(r'^list/', views.get_person),
    url(r'^temp/', views.temp),
    url(r'^home/', views.home, name='home'),
    url(r'^getticket/', views.get_ticket),
    url(r'^get_info/', views.get_info),
    url(r'^set_cookies/', views.set_cookies),
    url(r'^login/', views.login),
]
