from django.db import models


# Create your models here.


class User(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=256)


class Order(models.Model):
    o_num = models.CharField(max_length=16, unique=True)
    o_time = models.DateField(auto_now_add=True)


class Grade(models.Model):
    g_name = models.CharField(max_length=16)
    objects = models.Manager()


class Student(models.Model):
    s_name = models.CharField(max_length=200, verbose_name="姓名")
    s_age = models.IntegerField(default=0)
    s_grade = models.ForeignKey(Grade, default=0)
    objects = models.Manager()


class Customer(models.Model):
    c_name = models.CharField(max_length=16)
    c_cost = models.IntegerField(default=18)
    objects = models.Manager()