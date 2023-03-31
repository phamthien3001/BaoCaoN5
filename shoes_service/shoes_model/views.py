# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from shoes_model.models import Shoes

from shoes_model.serializers import ShoesSerializer

from rest_framework import viewsets

@csrf_exempt
def get_shoes_data(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    shoesdata = Shoes.objects.all()
    for tbl_value in shoesdata.values():
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

class ShoesModelViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ShoesSerializer
    throttle_scope = "shoes_model"

    def get_queryset(self):
        shoes = Shoes.objects.all()
        return shoes
    

