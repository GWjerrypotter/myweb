from django.contrib.auth.models import AbstractUser
from django.db import models


class DeptMent(models.Model):
    dept_name = models.CharField(max_length=32, verbose_name='部门名称')
    dept_phone = models.CharField(max_length=13, verbose_name='部门电话')
    dept_remark = models.TextField(max_length=128, null=True, blank=True, verbose_name='部门备注')

    def __str__(self):
        return self.dept_name

    class Meta(object):
        verbose_name = '部门管理'
        verbose_name_plural = verbose_name


class Users(AbstractUser):
    user_name = models.CharField(max_length=16, verbose_name='姓名')
    user_phone = models.CharField(max_length=11, verbose_name='用户手机号')
    dept = models.ForeignKey(DeptMent, on_delete=models.CASCADE, null=True, verbose_name='所属部门')
    user_remark = models.TextField(max_length=128, null=True, blank=True, verbose_name='用户备注')

    def __str__(self):
        return self.user_name

    class Meta(object):
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name
