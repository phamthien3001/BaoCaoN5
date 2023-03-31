from django.urls import path, include
from .views import ClotheModelViewset
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('clothes', ClotheModelViewset, basename='clothes')

urlpatterns = [
    path("getclothe/", views.get_clothe_data, name = "getclothe"),
    path('', include(router.urls)),
]