from django.conf.urls import url
from django.contrib import admin

from app import views

from two import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^addstudent/', views.add_student),
    url(r'^get/', views.get_students),
]
