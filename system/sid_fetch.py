from __future__ import division
import urllib2

__author__ = 'azoi'

import wx
import csv
import os
import sys
import time
import requests
import wx.calendar as cal
import operator


strurl="https://kito.azoi.com//accounts/login/"
header = {
    "content-type": "application/x-www-form-urlencoded"
}
payload = {
    "client_id": "7vRYL8F5kQarIlqpaRZwOCHjr6Cl45",
    "grant_type": "password",
    "username": "hardik@azoi.com",
    "password": "RnD#123456"
    #"dev_id": "aBaBaBaBaBaBaBaBaBaBaBaBaBaBaBaB"
}

r=requests.post(strurl, headers=header, data=payload)
rJson = r.json()
print rJson
access_token = rJson['results']['access_token']

# sid="562f5a7aa6d73d558ca75a39"


# strurl="https://kito.azoi.com//api/test-jig/v1/charger/test-fixture/?charger_test_fixture_id="+str(sid)


# r=requests.get(strurl, headers={"Authorization":"Bearer "+access_token})
# data = r.json()
# print "data",data

# data1 = data['results']['charger_test_fixture']

# print "data1",data1

sid="56fcaa20a6d73d6b8d69e183"

strurl="https://kito.azoi.com//api/test-jig/v1/data/?testjig_data_id="+str(sid)
            
r=requests.get(strurl, headers={"Authorization":"Bearer "+access_token})
data = r.json()
data1 = data['results']['testjig_data']

print "data1  ", data1


#"https://kito.azoi.com//api/test-jig/v1/pcba_test_log/from_ts=2016-01-19T00:00:00Z&to_ts=2016-01-28T23:59:59Z"


