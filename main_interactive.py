from __future__ import print_function
import os
import datetime
from builtins import input
import json

import interactive_input
import google_upload

def goscriptup():
    print("\033[A                             \033[A")

with open('cfg.json', 'r') as cfgfile:
    cfgdata = json.load(cfgfile)

#print(cfgdata)
#print(cfgdata["Locations"])

locations = cfgdata["Locations"]
dataclasses = cfgdata["Type1"]
datatypes = cfgdata["Type2"]

########################################################################
print('===================================')
print('Dust Monitoring Data Sending Script')

#timeseq = ['Year', 'Month', 'Day', 'Hour', 'Minute']
#ntimeseq = len(timeseq)
print('date? \n(blank if realtime)')

input_time1 = input('Year: ')
if input_time1 == '':
    input_time = datetime.datetime.now()
else:
    input_time = interactive_input.input_time_rt_update(int(input_time1))

goscriptup()
print("Time : %s" %input_time)

########################################################################
print('')
print('Location?')
for i in range(0,len(locations)):
    print("%d: %s" %(i+1,locations[i]))

loc2 = input('')
loc = int(loc2)-1

goscriptup()
print('Location: %s' %locations[int(loc)])

print('')

dustdata = interactive_input.input_dust(dataclasses, datatypes)
#print(dustdata)

print('\nSending Data to Google')
google_upload.Upload_dict('TimeStamp', input_time.strftime('%Y/%m/%d-%H:%M'), locations[loc], dustdata)
goscriptup()
print('Google Data Transfer Completed')


