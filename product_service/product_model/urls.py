from django.urls import path, include
from .views import ProductModelViewset
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('product', ProductModelViewset, basename='product')

urlpatterns = [
    path("getproduct/", views.get_product_data, name = "getproduct"),
    path('', include(router.urls)),
    path('books/', views.get_book_data, name = 'get_book_data'),
    path('clothes/', views.get_clothe_data, name = 'get_clothe_data'),
    path('electronics/', views.get_electronic_data, name = 'get_electronic_data'),
    path('shoes/', views.get_shoes_data, name = 'get_shoes_data'),

    path('productinfo/', views.product_info, name = 'product_info'),
]