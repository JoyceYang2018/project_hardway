#coding:utf-8

from nose.tools import *
# import sys
# sys.path.append('/home/yang/python/project_hardway/gothonweb')
from bin.game import app
from tests.tools import assert_response

def test_index():
    resp = app.request('/')
    assert_response(resp,status='404')


    resp = app.request('/hello')
    assert_response(resp)

    resp = app.request('/hello',method ='POST')
    assert_response(resp,contains='Nobody')

    data = {'name':'Zed','greet':'Hola'}
    resp = app.request('/hello',method='POST',data=data)
    assert_response(resp,contains='Zed')