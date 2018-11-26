from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.ContractPrice)
admin.site.register(models.Contract)
