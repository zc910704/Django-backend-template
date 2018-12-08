from django.db import models


# Create your models here.

class CallList(models.Model):
    """
    list for the call 招标列表
    """
    STATUS_CHOICES = (
        ('u', 'UpComing'),
        ('d', 'Doing'),
        ('f', 'Finished')
    )
    status = models.CharField('招标状态', max_length=1, choices=STATUS_CHOICES, null=True)
    callname = models.CharField('招标项目', max_length=128, null=True)
    calldate = models.DateTimeField('招标日期', null=True)
    calllimit = models.FloatField('招标限价', null=True)
    winner = models.CharField('中标人', max_length=128, null=True)
    method = models.CharField('评标方法', max_length=128, null=True)

    def __str__(self):
        return self.callname

    class Meta:
        # Meta 包含一系列选项，这里的ordering表示排序, - 表示逆序
        # 即当从数据库中取出时，以时间逆向排序
        ordering = ['-calldate']


class BidDetail(models.Model):
    """
    投标人的单次投标详情
    """
    biddername = models.CharField('投标公司法人名称', max_length=128, null=True)
    alias = models.CharField('投标公司别名', max_length=128, null=True)
    bidderprice = models.FloatField('投标价格', null=True)
    callfor = models.ForeignKey(CallList, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.biddername
