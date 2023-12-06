from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from purchase_requisition import views as requisition_views

router = DefaultRouter()
router.register(r'purchase-requisition', requisition_views.PurchaseRequisitionViewsets, basename='requisition')
router.register(r'requisition-item', requisition_views.PurchaseRequisitionItemViewsets, basename='requisition_item')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
