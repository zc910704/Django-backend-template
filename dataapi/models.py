from django.db import models

# Create your models here.

class CallList(models.Model):
  '''
  招标列表
  '''
  STATUS_CHOICES = (
    ('u','UpComing'),
    ('d', 'Doing'),
    ('f', 'Finished')
  )
  status = models.CharField('招标状态',max_length = 1, choices=STATUS_CHOICES)
  callname = models.CharField('招标单位', max_length=128)
  calldate = models.DateTimeField('招标日期')
  calllimit = models.BigIntegerField('招标限价')
  winner = models.CharField('中标人', max_length=128)
  method = models.CharField('评标方法', max_length=128)

  def __str__(self):
    return self.callname
  class Meta:
        # Meta 包含一系列选项，这里的ordering表示排序, - 表示逆序
        # 即当从数据库中取出时，以时间逆向排序
    ordering = ['-calldate']


class BidDetail(models.Model):
  '''
  投标人的单次投标详情
  '''
  biddername = models.CharField('投标公司法人名称',max_length=128)
  alias = models.CharField('投标公司别名',max_length=128, blank = True)
  bidderprice = models.BigIntegerField('投标价格')
  callfor = models.ForeignKey(CallList, on_delete = models.CASCADE)
  
  def __str__(self):
    return self.biddername
