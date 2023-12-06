from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.PurchaseRequisition)
admin.site.register(models.PurchaseRequisitionItem)