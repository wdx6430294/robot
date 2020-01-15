# encoding: utf-8
import readExcel as read
import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

import re

caseNo = 1
conn = cx_Oracle.connect('sh_nl_dev/YUpNMlCA33@166.188.20.49:1521/devdb')  # 连接数据库
c = conn.cursor()

for caseNo in range(1, 513):

    result = read.getTestData("temp.xlsx", "Sheet1", caseNo)
    CONFIG_ID = result[0]
    RULE = result[1]
    INFO_CHARACTER = result[2]
    INFO_CHARACTER_DEGREE = result[3]
    BUSINESS_SOURCE = result[4]
    FILTER_MODULE = result[5]

    sql = "SELECT ID_NUM,ID_MD5,CUST_NAME,PHONE,PHONE_MD5,ORGIN_CASE_NO FROM STAT_USER_LIST2_CS where " + RULE + " order by ID_NUM"
    strsql = sql.encode('UTF-8')
    x = c.execute(strsql)
    sqlresult = x.fetchall()

    LenoldResult=len(sqlresult)
    print LenoldResult

    if sqlresult is None:
        print "此规则无数据", CONFIG_ID
    elif FILTER_MODULE == "FILTER_ID":
        sqlperson = "SELECT IDCARD,IDCARDMD5,NAME,ORGINCASENO,INFOCHARACTER,INFOCHARACTERDEGREE,BUSINESSSOURCE FROM TBLPERSONBLACKLIST where configid=" + "\'" + CONFIG_ID + "\'" + "order by IDCARD"
        checkstrsql = sqlperson.encode('UTF-8')
        x = c.execute(checkstrsql)
        checkresult = x.fetchall()
        Lencheckresult=len(checkresult)
        if Lencheckresult==LenoldResult:
          CONFIG_PERSON_NUM_SUCCESS = 0
          CONFIG_PERSON_NUM_FAIL = 0
          t=0
          for t in range(0,Lencheckresult):
              checkresultperson=checkresult[t]
              result_2=sqlresult[t]
              if result_2[0] == checkresultperson[0] and result_2[1] == checkresultperson[1] and result_2[2] == checkresultperson[2] and \
                 result_2[5] == checkresultperson[3] and INFO_CHARACTER == checkresultperson[4] and INFO_CHARACTER_DEGREE == \
                 checkresultperson[5] and BUSINESS_SOURCE == checkresultperson[6]:
                 CONFIG_PERSON_NUM_SUCCESS = CONFIG_PERSON_NUM_SUCCESS + 1
                 print "比对成功", CONFIG_ID
                 print "比对成功条数", CONFIG_PERSON_NUM_SUCCESS
              else:
                 CONFIG_PERSON_NUM_FAIL = CONFIG_PERSON_NUM_FAIL + 1
                 print "比对失败", CONFIG_ID
                 print "比对失败条数", CONFIG_PERSON_NUM_FAIL
        else:
             print "原始表与结果表条数不匹配：",CONFIG_ID
             print "原始表条数：",LenoldResult
             print "结果表条数：",Lencheckresult
    elif FILTER_MODULE == "FILTER_PHONE":
        sqlmobile = "SELECT IDCARD,IDCARDMD5,NAME,MOBILENUM,MOBILENUMMD5,ORGINCASENO,INFOCHARACTER,INFOCHARACTERDEGREE,BUSINESSSOURCE FROM TBLMOBILENUMBLACKLIST where configid=" + "\'" + CONFIG_ID + "\'" + "order by IDCARD"
        checkstrsqlmobile = sqlmobile.encode('UTF-8')
        x = c.execute(checkstrsqlmobile)
        checkresultmobile = x.fetchall()
        Lencheckresultmobile=len(checkresultmobile)
        if Lencheckresultmobile == LenoldResult:
           CONFIG_MOBILE_NUM_SUCCESS = 0
           CONFIG_MOBILE_NUM_FAIL = 0
           m=0
           for m in  range(0,Lencheckresultmobile):
             mobilecheck=checkresultmobile[m]
             result_1=sqlresult[m]
             if result_1[0] == mobilecheck[0] and result_1[1] == mobilecheck[1] and result_1[2] == mobilecheck[2] and result_1[3] == mobilecheck[3] and result_1[4] == mobilecheck[4] \
                     and result_1[5] == mobilecheck[5] and INFO_CHARACTER == mobilecheck[6] \
                     and INFO_CHARACTER_DEGREE == mobilecheck[7] \
                     and BUSINESS_SOURCE == mobilecheck[8]:
                CONFIG_MOBILE_NUM_SUCCESS = CONFIG_MOBILE_NUM_SUCCESS + 1
                print "比对成功", CONFIG_ID
                print "比对成功条数", CONFIG_MOBILE_NUM_SUCCESS
             else:
                CONFIG_MOBILE_NUM_FAIL = CONFIG_MOBILE_NUM_FAIL + 1
                print "比对失败", CONFIG_ID
                print "比对失败条数", CONFIG_MOBILE_NUM_FAIL
        else:
             print "原始表与结果表条数不匹配：",CONFIG_ID
             print "原始表条数：",LenoldResult
             print "结果表条数：",Lencheckresultmobile
    else:
        print "不符合规则", CONFIG_ID
c.close()
conn.close()
