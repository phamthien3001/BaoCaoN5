from django.urls import path, include
from .views import BookModelViewset
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('books', BookModelViewset, basename='books')

urlpatterns = [
    path("getbook/", views.get_book_data, name = "getbook"),
    path('', include(router.urls)),
]