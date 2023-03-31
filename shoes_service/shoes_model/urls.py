from django.urls import path, include
from .views import ShoesModelViewset
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('shoes', ShoesModelViewset, basename='shoes')

urlpatterns = [
    path("getshoes/", views.get_shoes_data, name = "getshoes"),
    path('', include(router.urls)),
]