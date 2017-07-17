#-*- coding: utf-8 -*-

from __future__ import print_function
from builtins import input
import sys
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

with open('cfg.json', 'r') as cfgfile:
    cfgFilename = json.load(cfgfile)["SheetFile Name"]

def GetCredentials():
    credentialsjson = 'credentialKey.json'
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentialsjson, scope)
    gc = gspread.authorize(credentials)
    return gc

def OpenSheet(sheetname):
    return GetCredentials().open(cfgFilename).worksheet(sheetname)

def getAllSheetNames():
    sheetnames = list()
    worksheets = GetCredentials().open(cfgFilename).worksheets()
    for indsheet in worksheets:
        sheetnames.append(indsheet.title)
    return sheetnames

def make_sheet_with_firstrow(sheetname,firstrow):
    firstrow.insert(0, "TimeStamp")
    newsheet = GetCredentials().open(cfgFilename).add_worksheet(sheetname,1,len(firstrow))
    firstrowcells = newsheet.range(1,1,1,len(firstrow))
    for i in range(0,len(firstrow)):
        firstrowcells[i].value = firstrow[i]
    newsheet.update_cells(firstrowcells)

def Upload_dict(timestampstr,timestamp,location,inputdict):
    sheetlist = getAllSheetNames()
    for typekey in list(inputdict[list(inputdict.keys())[0]].keys()): #SUM
        sheetname = location + '_' + typekey
        if not sheetname in sheetlist:
            make_sheet_with_firstrow(sheetname,list(inputdict.keys()))
        ObjectSheet = OpenSheet(sheetname)
        row_dict = dict()
        for typekey2 in list(inputdict.keys()): #micrometer
            row_dict[ObjectSheet.find(typekey2).col] = inputdict[typekey2][typekey]
        #
        row_array = [None]*max(list(row_dict.keys()))
        #
        for col_index in list(row_dict.keys()):
            row_array[col_index-1] = row_dict[col_index]
        #
        row_array[ObjectSheet.find(timestampstr).col-1] = timestamp
        ObjectSheet.append_row(row_array)


if __name__ == "__main__":
    print("Test Google_Upload_Script")
    #print(getAllSheetNames())
    #print(OpenSheet('hello').range(1,1,1,5))
    print("end")
