from django.db import models


# Create your models here.

class Person(models.Model):
    p_name = models.CharField(max_length=16)
    p_sex = models.BooleanField(default=False)
    objects = models.Manager()


class IDCard(models.Model):
    id_name = models.CharField(max_length=18, unique=18)
    id_person = models.OneToOneField(Person , null=True ,blank=True)
    objects = models.Manager()
