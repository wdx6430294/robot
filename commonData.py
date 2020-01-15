# -*- coding: utf-8 -*-

import time
import datetime
import random
import json
import types

def timestamp():

    timestamp = int(round(time.time() * 1000))

    return timestamp


def randNum(start, end):

    randNum = str(random.randint(start, end))

    return randNum

'''
Date format YYYYMMDD

'''
def date():

    timestamp=time.localtime()

    date=time.strftime('%Y%m%d', timestamp)

    return date


def modifyAppNum(data):


   Num=str(randNum(1,100))


   stamp=str(timestamp())


   APP_NUM="AUTO"+stamp+Num

   APP_DATE = date()


   if type(data) in types.StringTypes:

      modifyData=json.loads(data)


   else:
       
       modifyData=data

   modifyData["DATA"]["APP_NUM"]=APP_NUM

   print modifyData
   
   return modifyData


def modifyAppDate(data):


   APP_DATE = date()

   print APP_DATE

   if type(data) in types.StringTypes:
       

      modifyData=json.loads(data)


   else:
       
      modifyData=data

   modifyData["DATA"]["APP_DATE"]=APP_DATE

   print modifyData
   
   return modifyData


def RandomData(Variable):
    
    da=date()

    print da

    return unicode(str(Variable))+da+str(randNum(100,999))

    


if __name__ == "__main__":

    test=randNum(1,100)

    #timestamp()

    #modifyAppNum("{\"TIMESTAMP\":\"1234567890123\",\"NONCE\":\"a123456789\",\"SIGN\":\"f13c99f32c2765e891b5c1bca630a2b6\",\"ORG_NUM\":\"OG00000326\",\"DATA\":{\"FRD_PRODUCT_NUM\":\"AFP3000\",\"APP_PRODUCT_NUM\":\"A23\",\"TRANSFER_ORG_NUM\":\"TRA094\",\"APP_NUM\":\"TTV1234567890126\",\"APP_DATE\":\"20180701\"}}")

    #modifyAppDate("{\"TIMESTAMP\":\"1234567890123\",\"NONCE\":\"a123456789\",\"SIGN\":\"f13c99f32c2765e891b5c1bca630a2b6\",\"ORG_NUM\":\"OG00000326\",\"DATA\":{\"FRD_PRODUCT_NUM\":\"AFP3000\",\"APP_PRODUCT_NUM\":\"A23\",\"TRANSFER_ORG_NUM\":\"TRA094\",\"APP_NUM\":\"TTV1234567890126\",\"APP_DATE\":\"20180701\"}}")

    #test=RandomData("变量")

    print type(test)
