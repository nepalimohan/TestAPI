from rest_framework import serializers
from . import models



class PurchaseRequisitionItem(serializers.ModelSerializer):
    class Meta:
        model = models.PurchaseRequisitionItem
        # fields = '_all_'
        exclude = [
                    "requisition",
                    "new",
                ]
        
class PurchaseRequisition(serializers.ModelSerializer):
    items = PurchaseRequisitionItem(many=True, read_only=True)
    requisition_data = PurchaseRequisitionItem(many=True, write_only=True)
    
    class Meta:
        model = models.PurchaseRequisition
        fields = '__all__'
        
    
    def create(self, validated_data):
        requisition_data = validated_data.pop("requisition_data", [])
        request = self.context.get("request")
        # user = request.user
        # validated_data["user"] = user
        requisition = models.PurchaseRequisition.objects.create(**validated_data)

        for item_data in requisition_data:
            models.PurchaseRequisitionItem.objects.create(requisition=requisition, **item_data)
        return requisition
    
    
    def update(self, instance, validated_data):
        requisition_data = validated_data.pop("requisition_data")
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        
        requisition_item_data = instance.items.all()
        
        for requisition_item_data, item_data in zip(requisition_item_data, requisition_data):
            for item_attr, item_value in item_data.items():
                setattr(requisition_item_data, item_attr, item_value)
            requisition_item_data.save()
        return instance
    
class PurchaseItemListViewset(serializers.ModelSerializer):
    
    class Meta:
        model = models.PurchaseRequisitionItem
        fields = '__all__'