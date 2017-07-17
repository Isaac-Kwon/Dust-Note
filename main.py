from __future__ import print_function
import os
import sys
import datetime
import json
from builtins import input
import google_upload

#Input Argument
#python main.py timestamp(0 or YYYY.MM.DD_HH:MM) locationNo 0.3um 0.5um 5um

#sys.argv[0] #TimeStamp or Realtime Parameter
#sys.argv[1] #first Value
#sys.argv[2] #second Value
#sys.argv[3] #third Value

with open('cfg.json', 'r') as cfgfile:
    cfgdata = json.load(cfgfile)



########################################################################

if sys.argv[1] == '0':
    TimeStamp = datetime.datetime.now()#.strftime('%Y/%m/%d-%H:%M')
else:
    TimeStamp = datetime.datetime.strptime(sys.argv[1],'%Y/%m/%d-%H:%M')

dustdata = dict()

if len(cfgdata["Locations"])==1:
    k = 2
    location = cfgdata["Locations"][0]
else:
    k = 3
    location = cfgdata["Locations"][sys.argv[2]]

for i in range(0,len(cfgdata['Type1'])):
    dustdata[cfgdata['Type1'][i]] = dict()
    for j in range(0,len(cfgdata['Type2'])):
        dustdata[cfgdata['Type1'][i]][cfgdata['Type2'][j]] = int(sys.argv[k])
        k = k+1

google_upload.Upload_dict('TimeStamp', TimeStamp.strftime('%Y/%m/%d-%H:%M'), location, dustdata)
