from django.db import models


# Create your models here.

class Contract(models):
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


class ContractPrice(models):
    """
    detail price of the Contract
    """

    item = models.CharField(verbose_name='清单名称', null=True)
    contract = models.ForeignKey(Contract, verbose_name='所属合同', null=True)
    description = models.TextField(verbose_name='清单特征', null=True)
    unit = models.CharField(verbose_name='单位', max_length=12, null=True)
    priceNet = models.FloatField(verbose_name='不含税价', null=True)
    priceTaxed = models.FloatField(verbose_name='含税价', null=True)
    comment = models.CharField(verbose_name='备注', max_length=128, null=True)

    def __str__(self):
        return self.item
