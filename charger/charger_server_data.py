import requests
import os
import sys
import csv
def get_firmware_token():


    f = open("data_charger_4_to_23_02_2015.csv",'w')
    csv_writer = csv.writer(f)

    strurl="https://kito.azoi.com//accounts/login/" #for main server
    #strurl="https://qa-azync.azoi.com//accounts/login/"  #for qa server
    header = {
        "content-type": "application/x-www-form-urlencoded"
    }
    payload = {
        
        "client_id": "7vRYL8F5kQarIlqpaRZwOCHjr6Cl45",#for main server
        #"client_id":"EGigJKKoiSLvGShq8XPFqTOyWRdmQo",#for qa server
        "grant_type": "password",
        "username": "hardik@azoi.com",
        "password": "RnD#123456"
        #"dev_id": "aBaBaBaBaBaBaBaBaBaBaBaBaBaBaBaB"
    }

    print "getting access_token"
    r=requests.post(strurl, headers=header, data=payload)
    rJson = r.json()
    print rJson
    access_token = rJson['results']['access_token']
    
    start_date_url="2016-02-4T00:00:00Z"
    end_date_url="2016-02-23T23:59:59Z"


    strurl="https://kito.azoi.com//api/test-jig/v1/charger/test-fixture/?from_ts="+start_date_url+"&to_ts="+end_date_url+"&filter=_id"#for main server
    #strurl="https://qa-azync.azoi.com//api/test-jig/v1/charger/test-fixture/?from_ts="+start_date_url+"&to_ts="+end_date_url+"&filter=_id"#for qa server
    r1=requests.get(strurl, headers={"Authorization":"Bearer "+access_token})
    rJson1 = r1.json()
    print "rJson1------------------------------------------------------------------------", rJson1
    dct = rJson1['results']['charger_test_fixture']
    print "dct---------------------------------------------------------------------------",dct

    
    cnt=0
    first = True
    new_list=[]
    fw=open("./charger_server_data_4_to_23_02_2015.txt","w")
    for d in dct:
        try:
            cnt+=1
            sid = d['charger_test_fixture_id']
            
            strurl="https://kito.azoi.com//api/test-jig/v1/charger/test-fixture/?charger_test_fixture_id="+str(sid)#for main server
            
            #strurl="https://qa-azync.azoi.com//api/test-jig/v1/charger/test-fixture/?charger_test_fixture_id="+str(sid)#for qa server
            r=requests.get(strurl, headers={"Authorization":"Bearer "+access_token})
            data = r.json()
            #print "data ----------------------------------------",cnt ,"   ",data
            data1 = data['results']['charger_test_fixture']
            if first:
                first = False
                key_list = ['sid']
                for key in data1.keys():
                    key_list.append(key)
                csv_writer.writerow(key_list)

            data_l = [str(sid)]
            for key in data1.keys():
                data_l.append(data1[key])
            csv_writer.writerow(data_l)
            f.flush()
            print "row ",cnt,"   ",data["results"]["charger_test_fixture"],"sid  ",sid
            fw.write("row "+str(cnt)+"   "+str(data["results"]["charger_test_fixture"])+"sid  "+str(sid)+"\n")
        except:
            new_list.append(sid)

    for n in new_list:
        try:
            cnt+=1
            sid = n
            strurl="https://kito.azoi.com//api/test-jig/v1/charger/test-fixture/?charger_test_fixture_id="+str(sid)#for main server
            
            #strurl="https://qa-azync.azoi.com//api/test-jig/v1/charger/test-fixture/?charger_test_fixture_id="+str(sid)#for qa server
            r=requests.get(strurl, headers={"Authorization":"Bearer "+access_token})
            data = r.json()
            data1 = data['results']['charger_test_fixture']
            if first:
                first = False
                key_list = ['sid']
                for key in data1.keys():
                    key_list.append(key)
                csv_writer.writerow(key_list)

            data_l = [str(sid)]
            for key in data1.keys():
                data_l.append(data1[key])
            csv_writer.writerow(data_l)
            f.flush()
            #print "data ----------------------------------------",cnt ,"   ",data
            print "row ",cnt,"   ",data["results"]["charger_test_fixture"],"sid  ",sid
            fw.write("row "+str(cnt)+"   "+str(data["results"]["charger_test_fixture"])+"sid  "+str(sid)+"\n")
        except:
            print "problem in fetch"

    fw.close()

get_firmware_token()