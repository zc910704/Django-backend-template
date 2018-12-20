from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Extend_User(models.Model):
    """
    拓展默认用户
    """

    gender = (
        ('male', '男'),
        ('none', '未知'),
        ('female', '女'),
    )

    role = (
        (0, 'admin'),
        (1, 'superuser'),
        (2, 'user'),
        (3, 'quest')
    )

    real_name = models.CharField(max_length=128, blank=True)
    avatar = models.CharField(max_length=128, blank=True)
    roles = models.SmallIntegerField(verbose_name='权限', choices=role, default='quest')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=32, choices=gender, default='未知')

    def __str__(self):
        return self.real_name

    class Meta:
        ordering = ['user']
        verbose_name = '用户'
        verbose_name_plural = '用户'

        """ 
        各字段含义：
            name为真实名字，最长不超过128个字符；
            性别使用了一个choice，只能选择男或者女，默认为男；
            使用__str__帮助人性化显示对象信息；
            元数据里定义显示顺序；
         """
