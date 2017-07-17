from __future__ import print_function
from builtins import input
import sys
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

with open('cfg.json', 'r') as cfgfile:
    SheetFilename = json.load(cfgfile)["SheetFile Name"]

def GetCredentials():
    credentialsjson = 'credentialKey.json'
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentialsjson, scope)
    gc = gspread.authorize(credentials)
    return gc

def OpenSheet(Filename, Sheetname):
    gc = GetCredentials()
    return gc.open(Filename).worksheet(Sheetname)

def Upload_dict(timestampstr,timestamp,location,inputdict):
    for typekey in list(inputdict[list(inputdict.keys())[0]].keys()): #SUM
        ObjectSheet = OpenSheet(SheetFilename,location + '_' + typekey)
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
    #dustdata = {'0.1um': {'SUM': 5,'SIGMA': 3}, '0.3um': {'SUM': 10,'SIGMA': 6}, '5.0um': {'SUM': 15, 'SIGMA': 9}}
    #Upload_dict('TimeStamp', 'TIME', 'Inside',dustdata)
    #print("Testing GoogleUpload Script::")
    #print("Test Completed")
    print("Google_Upload_Script")
