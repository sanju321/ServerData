import requests
import os
import sys
import csv
def get_firmware_token():
    f = open("data_pcba_4_to_23_02_2016.csv",'w')
    csv_writer = csv.writer(f)
    strurl="https://kito.azoi.com//accounts/login/"#main server
    #strurl="https://qa-azync.azoi.com//accounts/login/"#qa server
    header = {
        "content-type": "application/x-www-form-urlencoded"
    }
    payload = {
        
        "client_id": "7vRYL8F5kQarIlqpaRZwOCHjr6Cl45",#main server
        #"client_id":"EGigJKKoiSLvGShq8XPFqTOyWRdmQo",#qa server
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
    
    start_date_url="2016-02-04T00:00:00Z"
    end_date_url="2016-02-23T23:59:59Z"

    
    strurl="https://kito.azoi.com//api/test-jig/v1/pcba_test_log/?from_ts="+start_date_url+"&to_ts="+end_date_url+"&filter=_id"#main server
    
    #strurl="https://qa-azync.azoi.com//api/test-jig/v1/pcba_test_log/?from_ts="+start_date_url+"&to_ts="+end_date_url+"&filter=_id"#qa server
    r1=requests.get(strurl, headers={"Authorization":"Bearer "+access_token})
    rJson1 = r1.json()
    print "rJson1------------------------------------------------------------------------", rJson1
    dct = rJson1['results']['pcba_test_log']
    print "dct---------------------------------------------------------------------------",dct
    cnt=0

    first = True
    new_list=[]
    fw=open("./pcb_server_data_4_to_23_02_2016.txt","w")
    for d in dct:
        try:
            cnt+=1
            sid = d['pcba_test_log_id']
            strurl="https://kito.azoi.com//api/test-jig/v1/pcba_test_log/?pcba_test_log_id="+str(sid)#main server
            
            #strurl="https://qa-azync.azoi.com//api/test-jig/v1/pcba_test_log/?pcba_test_log_id="+str(sid)#qa server
            r=requests.get(strurl, headers={"Authorization":"Bearer "+access_token})
            data = r.json()
            #print "data ----------------------------------------",cnt ,"   ",data
            data1=data["results"]["pcba_test_log"]
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

            print "row ",cnt,"   ",data["results"]["pcba_test_log"],"sid  ",sid
            fw.write("row "+str(cnt)+"   "+str(data["results"]["pcba_test_log"])+"sid  "+str(sid)+"\n")
        except:
            new_list.append(sid)

    for n in new_list:
        try:
            cnt+=1
            sid = n
            strurl="https://kito.azoi.com//api/test-jig/v1/pcba_test_log/?pcba_test_log_id="+str(sid)#main server
            
            #strurl="https://qa-azync.azoi.com//api/test-jig/v1/pcba_test_log/?pcba_test_log_id="+str(sid)#qa server
            r=requests.get(strurl, headers={"Authorization":"Bearer "+access_token})
            data = r.json()
            #print "data ----------------------------------------",cnt ,"   ",data
            data1=data["results"]["pcba_test_log"]
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
            print "row ",cnt,"   ",data["results"]["pcba_test_log"],"sid  ",sid
            fw.write("row "+str(cnt)+"   "+str(data["results"]["pcba_test_log"])+"sid  "+str(sid)+"\n")
        except:
            print "problem in fetching"
    fw.close()

get_firmware_token()