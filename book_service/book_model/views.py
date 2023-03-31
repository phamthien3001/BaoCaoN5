# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from book_model.models import Book

from book_model.serializers import BookSerializer

from rest_framework import viewsets

@csrf_exempt
def get_book_data(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    bookdata = Book.objects.all()
    for tbl_value in bookdata.values():
        data.append(tbl_value)
    # If data is available then it returns the data.
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

class BookModelViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    throttle_scope = "book_model"

    def get_queryset(self):
        book = Book.objects.all()
        return book
    

