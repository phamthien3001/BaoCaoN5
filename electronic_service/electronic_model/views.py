# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from electronic_model.models import Electronic

from electronic_model.serializers import ElectronicSerializer

from rest_framework import viewsets

@csrf_exempt
def get_electronic_data(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    electronicdata = Electronic.objects.all()
    for tbl_value in electronicdata.values():
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

class ElectronicModelViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ElectronicSerializer
    throttle_scope = "electronic_model"

    def get_queryset(self):
        electronic = Electronic.objects.all()
        return electronic
    

