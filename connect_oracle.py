# -*- coding: utf-8 -*-
import cx_Oracle 

def connect(sql,key):

   conn=cx_Oracle.connect(key)    #连接数据库
   c=conn.cursor()                                                     
   x=c.execute(sql) 
   result=x.fetchone()
   c.close()                                            
   conn.close()
   return result

if __name__ == "__main__":

   test=connect('SELECT * FROM APPLICATION where app_id=\'eab942f5-9e2e-446e-9897-509575b89d92\'','sh_dectech/sh_dectech_test@166.188.20.49:1521/devdb')

   print test
