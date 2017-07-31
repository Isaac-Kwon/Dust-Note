#-*- coding: utf-8 -*-
from __future__ import print_function
import os
import sys
import datetime
import json
from builtins import input
import google_upload

#Input Argument
#python main.py timestamp(0 or YYYY.MM.DD_HH:MM) locationNo 0.3um 0.5um 5um

#or

#python main.py --help
#or
#python main.py -h

#sys.argv[0] #TimeStamp or Realtime Parameter
#sys.argv[1] #first Value
#sys.argv[2] #second Value
#sys.argv[3] #third Value

with open('cfg.json', 'r') as cfgfile:
    cfgdata = json.load(cfgfile)

if len(sys.argv) == 1:
    print('')
    print('if you help to use program, do \"python main.py --help\" or \"python main.py -help\"\n RUN IN INTERACTIVE MODE\n')
    os.system('python3 main_interactive.py')
    exit()

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("HELP DISPLAY for Input Parameter")
    print("python main.py timestamp(0 or YYYY-MM-DD HH:MM) ", end='')
    if len(cfgdata["Locations"])!=1:
        print('LocationNumber ', end='')
    for i in range(0,len(cfgdata['Type1'])):
        for j in range(0,len(cfgdata['Type2'])):
            print(cfgdata['Type2'][j]+'of'+cfgdata['Type1'][i], end=' ')
    print('')
    if len(cfgdata["Locations"])!=1:
        print('\nlocation numbers')
        locationind = 1
        for location in list(cfgdata["Locations"]):
            print("%d: %s" %(locationind, location))
            locationind = locationind + 1
    exit()

########################################################################

if sys.argv[1] == '0':
    TimeStamp = datetime.datetime.now()#.strftime('%Y/%m/%d-%H:%M')
else:
    TimeStamp = datetime.datetime.strptime(sys.argv[1],'%Y-%m-%d %H:%M')

dustdata = dict()

if len(cfgdata["Locations"])==1:
    k = 2
    location = cfgdata["Locations"][0]
else:
    k = 3
    location = cfgdata["Locations"][int(sys.argv[2])]

for i in range(0,len(cfgdata['Type1'])):
    dustdata[cfgdata['Type1'][i]] = dict()
    for j in range(0,len(cfgdata['Type2'])):
        dustdata[cfgdata['Type1'][i]][cfgdata['Type2'][j]] = int(sys.argv[k])
        k = k+1

google_upload.Upload_dict('TimeStamp', TimeStamp.strftime('%Y-%m-%d %H:%M'), location, dustdata)
