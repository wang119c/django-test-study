from django.conf.urls import url
from django.contrib import admin

from app import views

from two import views

from three import views

urlpatterns = [
    url(r'^index/', views.index),

]
