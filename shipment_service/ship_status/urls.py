from django.urls import path
from . import views

urlpatterns = [
    path("shipment_status/", views.shipment_status, name = "shipment_status"),
]