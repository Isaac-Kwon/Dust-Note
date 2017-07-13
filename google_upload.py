from __future__ import print_function
from builtins import input
import gspread
from oauth2client.service_account import ServiceAccountCredentials

print('upload sequence start')

def GetCredentials():
    credentialsjson = 'credentialKey.json'
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentialsjson, scope)
    gc = gspread.authorize(credentials)
    return gc

def OpenSheet(Filename, Sheetname):
    gc = GetCredentials()
    return gc.open(Filename).worksheet(Sheetname)

if __name__ == "__main__":
    print("")
