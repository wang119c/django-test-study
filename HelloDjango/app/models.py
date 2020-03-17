from django.db import models


# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=200, verbose_name="姓名")
    s_age = models.IntegerField(default=0)


class Person(models.Model):
    p_name = models.CharField(max_length=16, unique=True)
    p_age = models.IntegerField(default=18)
    p_sex = models.BooleanField(default=False, db_column='sex')
    p_hobby = models.CharField(max_length=32, null=True, blank=True)

    @classmethod
    def create(cls, p_name, p_age=180, p_sex=True, p_hobby='gaming'):
        return cls(p_name=p_name, p_age=p_age, p_sex=p_sex, p_hobby=p_hobby)

    class Meta:
        db_table = 'people'
