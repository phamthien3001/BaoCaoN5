# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from clothe_model.models import Clothe

from clothe_model.serializers import ClotheSerializer

from rest_framework import viewsets

@csrf_exempt
def get_clothe_data(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    clothedata = Clothe.objects.all()
    for tbl_value in clothedata.values():
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

class ClotheModelViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClotheSerializer
    throttle_scope = "clothe_model"

    def get_queryset(self):
        clothe = Clothe.objects.all()
        return clothe
    

