from django.urls import path, include
from .views import ElectronicModelViewset
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('electronics', ElectronicModelViewset, basename='electronics')

urlpatterns = [
    path("getelectronic/", views.get_electronic_data, name = "getelectronic"),
    path('', include(router.urls)),
]