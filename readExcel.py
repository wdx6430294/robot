# -*- coding: utf-8 -*-

import xlrd


def getTestData(host,path,sheetName,caseNo):

    
    excelFile=xlrd.open_workbook(path)
    
    table = excelFile.sheet_by_name(sheetName)
    
    nrows = table.nrows



    apiPath=table.cell(0,1).value
    url="http://" +host + apiPath
    headers=table.cell(1,1).value
    method=table.cell(2,1).value


    nRow=table.nrows
    nCol=table.ncols
    caseNo=int(caseNo)

    
    caseNum=nRow-4
    
    
    dict_params={}
    for i in range(nCol):
        dict_params[table.cell(3, i).value] = table.cell(caseNo+3, i).value


    caseNo = dict_params.pop("caseNo")
    caseName = dict_params.pop("caseName")
    requestBody = dict_params.pop("requestBody")
    expectedCode = dict_params.pop("expectedCode")
    expectedResult = dict_params.pop("expectedResult")

    

    return url,headers,method,caseNo,caseName,requestBody,expectedCode,expectedResult,caseNum

if __name__ =="__main__":

 getTestData("166.188.20.105","testdata/test.xlsx","AFP3010","1")
