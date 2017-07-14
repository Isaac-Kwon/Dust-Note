from __future__ import print_function
import os
import sys
import datetime
import json
from builtins import input

#Input Argument
#python main.py timestamp(0 or YYYY.MM.DD_HH:MM) locationNo 0.3um 0.5um 5um

#sys.argv[0] #TimeStamp or Realtime Parameter
#sys.argv[1] #first Value
#sys.argv[2] #second Value
#sys.argv[3] #third Value

with open('cfg.json', 'r') as cfgfile:
    cfgdata = json.load(cfgfile)



########################################################################
#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])

if sys.argv[1] == '0':
    TimeStamp = datetime.datetime.now()
else:
    TimeStamp = datetime.datetime.strptime(sys.argv[1],'%Y.%m.%d_%H:%M')

dustdata = dict()

if len(cfgdata["Locations"])==1:
    k = 2
else:
    k = 3

for i in range(0,len(cfgdata['Type1'])):
    dustdata[cfgdata['Type1'][i]] = dict()
    for j in range(0,len(cfgdata['Type2'])):
        dustdata[cfgdata['Type1'][i]][cfgdata['Type2'][j]] = int(sys.argv[k])

print(dustdata)
