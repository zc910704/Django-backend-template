from django.db import models


# Create your models here.

class Contract(models.Model):
    """
    history contract data that have been signed.
    """

    contractName = models.CharField(verbose_name='合同名称', max_length=128, null=True)
    contractDate = models.DateField(verbose_name='合同日期', null=True)
    contractLocation = models.CharField(verbose_name='合同签署地', max_length=64, null=True)
    contractComment = models.CharField(verbose_name='合同备注', max_length=256, null=True)

    def __str__(self):
        return self.contractName

    class Meta:
        ordering = ['-contractDate']


class ContractPrice(models.Model):
    """
    detail price of the Contract
    """
    contract = models.ForeignKey(Contract, verbose_name='所属合同', null=True, on_delete=models.CASCADE)
    classify = models.CharField(verbose_name='分类', max_length=128, null=True)
    itemId = models.IntegerField(verbose_name='项目编码', null=True)
    item = models.CharField(verbose_name='清单名称', max_length=128, null=True)
    feature = models.TextField(verbose_name='项目特征', null=True)
    computeRules = models.TextField(verbose_name='计算规则', null=True)
    description = models.TextField(verbose_name='项目内容', null=True)
    unit = models.CharField(verbose_name='单位', max_length=12, null=True)
    count = models.IntegerField(verbose_name='工程量', null=True)
    priceNet = models.FloatField(verbose_name='不含税价', null=True)
    taxRate = models.FloatField(verbose_name='税率', null=True, default=10.0)
    priceTaxed = models.FloatField(verbose_name='含税价', null=True)
    comment = models.CharField(verbose_name='备注', max_length=256, null=True)

    def __str__(self):
        return self.item
    
    class Meta:
        ordering = ['contract']


class BidPrice(models.Model):
    """
    detail price of the Contract
    """
    contract = models.ForeignKey(Contract, verbose_name='所属投标', null=True, on_delete=models.CASCADE)
    classify = models.CharField(verbose_name='分类', max_length=128, null=True)
    itemId = models.IntegerField(verbose_name='项目编码', null=True)
    item = models.CharField(verbose_name='清单名称', max_length=128, null=True)
    feature = models.TextField(verbose_name='项目特征', null=True)
    description = models.TextField(verbose_name='项目内容', null=True)
    unit = models.CharField(verbose_name='单位', max_length=12, null=True)
    count = models.IntegerField(verbose_name='工程量', null=True)
    priceNet = models.FloatField(verbose_name='不含税价', null=True)
    taxRate = models.FloatField(verbose_name='税率', null=True, default=10.0)
    priceTaxed = models.FloatField(verbose_name='含税价', null=True)
    comment = models.CharField(verbose_name='备注', max_length=256, null=True)

    def __str__(self):
        return self.item

    class Meta:
        ordering = ['contract']
