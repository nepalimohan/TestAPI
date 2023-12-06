from django.db import models
from django.contrib.auth.models import User
from . choices import StatusChoices, UsedStatusChoices


class ID(models.Model):
	unique_id = models.PositiveIntegerField()
	name = models.CharField(max_length=50)
	tenant_id = models.CharField(max_length=50, default='')

	class Meta:
		db_table = u'ID'

	@staticmethod
	def createID(name:str):
		id = 0
		if ID.objects.filter(name=name).exists():
			id = ID.objects.filter(name=name).values('unique_id').aggregate(models.Max('unique_id'))['unique_id__max'] #type: ignore
			id = ID.objects.create(name=name[:3],unique_id=id+1)
		else:
			id = ID.objects.create(name=name[:3],unique_id=100)
		return f'{id.name}{id.unique_id}'

# Create your models here.
class PurchaseRequisition(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, related_name='user_purchase_requisition')
	# tenant_id = models.ForeignKey(dashmodel.Tenant, on_delete=models.PROTECT, blank=True, null=True, related_name='tenant_purchase_requisition')
	unique_id = models.CharField(max_length=255, default="", blank=True, null=True)
	title = models.CharField(max_length=255, null=True, blank=True)
	entry_date = models.CharField(max_length=255, null=True, blank=True)
	english_entry_date = models.CharField(max_length=255, null=True, blank=True)
	due_date = models.CharField(max_length=255, null=True, blank=True)
	english_due_date = models.CharField(max_length=255, null=True, blank=True)
	
	status = models.CharField(
		max_length=255, choices=StatusChoices.choices, default='draft'
	)
	# narration = models.CharField(max_length=5000, null=True, blank=True)
	narration = models.TextField(max_length=5000, null=True, blank=True)
	entry_by = models.CharField(max_length=255, null=True, blank=True, default='admin')
	# approval_user = models.ForeignKey(User, on_delete=models.PROTECT ,null=True, blank=True)
	approved_by = models.CharField(max_length=255, null=True, blank=True)
	cancelled_by = models.CharField(max_length=255, null=True, blank=True)
	english_cancel_date = models.CharField(max_length=255, null=True, blank=True)
	nepali_cancel_date = models.CharField(max_length=255, null=True, blank=True)
	english_approve_date = models.CharField(max_length=255, null=True, blank=True)
	nepali_approve_date = models.CharField(max_length=255, null=True, blank=True)
	submit_for_approval_nepali_date = models.CharField(max_length=255, null=True, blank=True)
	submit_for_approval_english_date = models.CharField(max_length=255, null=True, blank=True)
	used_status = models.CharField(max_length=50,blank=True, null=True, choices=UsedStatusChoices.choices, default='not used')
	
	class Meta:
		db_table = u'PurchaseRequisition'
		ordering = ['-id']

	def __str__(self) -> str:
		return f"{self.id}"

	def save(self, *args, **kwargs):
		if self.unique_id == '' or self.unique_id is None:
			self.unique_id = ID.createID("REQ")
		super().save(*args, **kwargs)


class PurchaseRequisitionItem(models.Model):
	requisition_item = models.ForeignKey(
		PurchaseRequisition,
		on_delete=models.PROTECT,
		null=True,
		blank=True,
		related_name="items",
	)
	
	item_code = models.CharField(max_length=255, null=True, blank=True)
	item_name = models.CharField(max_length=255, null=True, blank=True)
	uom = models.CharField(max_length=255, null=True, blank=True)
	quantity = models.FloatField(null=True, blank=True)
	new = models.BooleanField(default=False)
	remaining = models.FloatField(null=True, blank=True, default=0)
	used_status = models.CharField(max_length=50,blank=True, null=True, choices=UsedStatusChoices.choices, default='not used')

	class Meta:
		db_table = u'PurchaseRequisitionItem'

	def __str__(self) -> str:
		return f"{self.requisition_item.id}"