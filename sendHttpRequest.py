# -*- coding: utf-8 -*-

import requests
import os
import readExcel as r
import json
import commonData as co
import types

def send_HttpRequest(url, data=None, headers=None, method=None):

 
    if method=="get":
        
        response=requests.get(url,verify=False)
       
    elif method=="post"and headers.find("json")>=0:

        if type(data) in types.StringTypes:
          
           postbody=json.loads(data)
        
           response=requests.post(url,None,postbody,verify=False)

        else:

           response=requests.post(url,None,data,verify=False)
           

    else:

        headers=json.loads(headers)

        response=requests.post(url,data,None,headers=headers,verify=False)
        
    responseCode = str(response.status_code)
    
    content = response.content.decode("utf-8")

    return responseCode,content



if __name__ =="__main__":
    
  testdata=r.getTestData("166.188.20.105","/testpython/11/test.xlsx","AFP3010","1")
  
  requestBody=testdata[5]

  requestBody=co.modifyAppNum(requestBody)

  requestBody=co.modifyAppDate(requestBody)
  
  print "111111", type(requestBody)
  
  #re=json.loads(requestBody)

  print type(requestBody)

  #print type(re)
  
  response=send_HttpRequest("http://166.188.20.102:8080/antifraud/api/v4/application",requestBody,"{\"Content-Type\": \"application/json\"}","post")
  #response=send_HttpRequest("http://166.188.20.25/cpcs/api/v2/channel/4002",requestBody,"{\"Content-Type\": \"application/x-www-form-urlencoded\"}","post")

  #response=send_HttpRequest("https://dev.suanhua.org/cpcs/api/v2/channel/4002",requestBody,"{\"Content-Type\": \"application/x-www-form-urlencoded\"}","get")

  print "".join(response)



