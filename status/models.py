from django.db import models
from datetime import datetime


# Create your models here.


class RecentUpdate(models.Model):
    """
    the Recent update of site
    """
    time = models.DateTimeField(verbose_name='发布时间', auto_now=True, null=True)
    title = models.CharField(verbose_name='更新标题', max_length=64, null=True)
    content = models.CharField(verbose_name='更新内容', max_length=256, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time']
