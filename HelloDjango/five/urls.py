from django.conf.urls import url
from django.contrib import admin

from five import views

urlpatterns = [
    url(r'^hello', views.hello, name='hello'),
    url(r'^addperson', views.addperson, name='addperson'),
    url(r'^addcard', views.addcard, name='addcard'),
    url(r'^bindcard', views.bindcard, name='bindcard'),
]
