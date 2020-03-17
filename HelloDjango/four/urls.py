from django.conf.urls import url
from django.contrib import admin

from four import views

urlpatterns = [
    url(r'^reg', views.reg, name='reg'),
    url(r'^login' , views.login , name='login' )
]
