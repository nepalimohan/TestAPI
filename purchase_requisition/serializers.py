from rest_framework import serializers
from . import models



class PurchaseRequisitionItem(serializers.ModelSerializer):
    class Meta:
        model = models.PurchaseRequisitionItem
        # fields = '_all_'
        exclude = [
                    "requisition_item",
                    "new",
                ]
        
class PurchaseRequisition(serializers.ModelSerializer):
    items = PurchaseRequisitionItem(many=True, read_only=True)
    requisition_item_data = PurchaseRequisitionItem(many=True, write_only=True)
    
    class Meta:
        model = models.PurchaseRequisition
        fields = '__all__'
        
    
    def create(self, validated_data):
        items = validated_data.pop("requisition_item_data", [])
        print(items)
        request = self.context.get("request")
        # user = request.user
        # validated_data["user"] = user
        requisition = models.PurchaseRequisition.objects.create(**validated_data)

        for item_data in items:
            models.PurchaseRequisitionItem.objects.create(requisition_item=requisition, **item_data)
            print(item_data)
        return requisition
    
class PurchaseItemListViewset(serializers.ModelSerializer):
    
    class Meta:
        model = models.PurchaseRequisitionItem
        fields = '__all__'