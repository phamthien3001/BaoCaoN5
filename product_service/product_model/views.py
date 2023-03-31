# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from product_model.models import product_details

from product_model.serializers import ProductSerializer

from rest_framework import viewsets

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@csrf_exempt
def get_product_data(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    prodata = product_details.objects.all()
    for tbl_value in prodata.values():
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

def product_data(product_id):
    product = product_details.objects.filter(product_id = product_id)
    for data in product.values():
        return data

@csrf_exempt
def product_info(request):
    if request.method == 'POST':
        # resp = {}
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            product_id = val1.get('Product id')
            print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n')
            print(product_id)
            resp = {}
            if product_id:
                ## Calling the getting the user info.
                respdata = product_data(product_id)
                dict1 = {}
                if respdata:
                    dict1['Product Name'] = respdata.get('product_name','')
                    dict1['Price'] = respdata.get('price','')
                if dict1:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['data'] = dict1
                ### If a user is not found then it give failed as a response.
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'Product Not Found.'
            ### The field value is missing.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Fields is mandatory.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Request type is not matched.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')


class ProductModelViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    throttle_scope = "product_model"

    def get_queryset(self):
        product = product_details.objects.all()
        return product

@api_view(['GET'])
def get_book_data(request):
    url = 'http://127.0.0.1:3002/books'
    headers = {'Content-Type':'application/json'}
    response = requests.get(url, headers = headers)
    book = json.loads(response.content.decode('utf-8'))
    return Response(book, status = status.HTTP_200_OK)

@api_view(['GET'])
def get_clothe_data(request):
    url = 'http://127.0.0.1:3003/clothes'
    headers = {'Content-Type':'application/json'}
    response = requests.get(url, headers = headers)
    clothe = json.loads(response.content.decode('utf-8'))
    return Response(clothe, status = status.HTTP_200_OK)

@api_view(['GET'])
def get_electronic_data(request):
    url = 'http://127.0.0.1:3004/electronics'
    headers = {'Content-Type':'application/json'}
    response = requests.get(url, headers = headers)
    electronic = json.loads(response.content.decode('utf-8'))
    return Response(electronic, status = status.HTTP_200_OK)

@api_view(['GET'])
def get_shoes_data(request):
    url = 'http://127.0.0.1:3005/shoes'
    headers = {'Content-Type':'application/json'}
    response = requests.get(url, headers = headers)
    shoes = json.loads(response.content.decode('utf-8'))
    return Response(shoes, status = status.HTTP_200_OK)
    

