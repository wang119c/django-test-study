from django.db import models


# Create your models here.
class UserEntity(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return  self.name

    class Meta:
        db_table = 'app_user'
        verbose_name = '客户管理'
        verbose_name_plural = verbose_name
