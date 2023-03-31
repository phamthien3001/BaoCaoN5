from django.shortcuts import render
import requests
import json
from .models import Comment
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.


def cmt_data_insert(fname, lname, email, mobile, address, product_id, product_name, price, comment):
    cmt_data = Comment(fname = fname, lname = lname, email = email, mobile = mobile, 
                address = address, product_id = product_id, product_name = product_name, price = price, comment = comment)
    cmt_data.save()
    return 1

# def post_info(product_id, uname, cmt):
#     cmt_dict = {}
#     url = 'http://127.0.0.1:8000/userinfo/'
#     cmt_dict['User Name'] = uname
#     data = json.dumps(cmt_dict)
#     headers = {'Content-Type': 'application/json'}
#     response = requests.post(url, data=data, headers=headers)
#     val1 = json.loads(response.content.decode('utf-8'))
#     cmt_dict['First Name'] = val1['data']['First Name']
#     cmt_dict['Last Name'] = val1['data']['Last Name']
#     cmt_dict['Email Id'] = val1['data']['Email Id']
#     cmt_dict['Mobile Number'] = data['mobile']
#     cmt_dict['Address'] = val1['data']['Address']

#     url2 = "http://127.0.0.1:3001/productinfo/"
#     d2 = {}
#     d2['Product Id'] = product_id
#     data2 = json.dumps(d2)
#     headers = {'Content-Type': 'application/json'}
#     response = requests.post(url, data=data2, headers=headers)
#     val2 = json.loads(response.content.decode('utf-8'))
#     cmt_dict['Product Id'] = product_id
#     cmt_dict['Product Name'] = val2['data']['Product Name']
#     cmt_dict['Price'] = val2['data']['Price']

#     cmt_dict['Comment'] = cmt
#     url = 'http://127.0.0.1:6000/post_comment/'
#     data = json.dumps(cmt_dict)
#     headers = {'Content-Type': 'application/json'}
#     response = requests.post(url, data=data, headers=headers)
#     api_resp = json.loads(response.content.decode('utf-8'))
#     return api_resp



@csrf_exempt
def post_comment(request):
    uname = request.POST.get("User Name")
    product_id = request.POST.get('Product id')
    comment = request.POST.get('Comment')
    resp = {}

    cmt_dict = {}

    url = 'http://127.0.0.1:8000/userinfo/'
    cmt_dict['User Name'] = uname
    data = json.dumps(cmt_dict)
    print('\ndata\n', data, '\n')
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=data, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    cmt_dict['First Name'] = val1['data']['First Name']
    cmt_dict['Last Name'] = val1['data']['Last Name']
    cmt_dict['Email Id'] = val1['data']['Email Id']
    cmt_dict['Mobile Number'] = val1['data']['Mobile Number']
    cmt_dict['Address'] = val1['data']['Address']

    url2 = "http://127.0.0.1:3001/productinfo/"
    d2 = {}
    d2['Product id'] = product_id
    data2 = json.dumps(d2)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url2, data=data2, headers=headers)
    val2 = json.loads(response.content.decode('utf-8'))
    cmt_dict['Product id'] = product_id
    cmt_dict['Product Name'] = val2['data']['Product Name']
    cmt_dict['Price'] = val2['data']['Price']
    
    fname = cmt_dict['First Name']
    lname = cmt_dict['Last Name']
    email = cmt_dict['Email Id']
    mobile = cmt_dict['Mobile Number']
    address = cmt_dict['Address']
    product_id = cmt_dict['Product id']
    product_name = cmt_dict['Product Name']
    price = cmt_dict['Price']

    respdata = cmt_data_insert(fname, lname, email, mobile, address, product_id, product_name, price, comment)
    if respdata:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'Post Comment Successfully'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Failed to Post Comment.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')     

  













    









    
