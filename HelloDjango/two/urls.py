from django.conf.urls import url
from django.contrib import admin

from app import views

from two import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^addstudent/', views.add_student),
    url(r'^get/', views.get_students),

    url(r'^get_user/', views.get_user),
    url(r'^get_grade/', views.get_grade),
    url(r'^get_curstomer/', views.get_curstomer),

    url(r'^haverequest/', views.have_request),


]
