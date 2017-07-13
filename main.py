from __future__ import print_function
import os
import datetime


import inputinform

locations = ["Outside", "Buffer Room", "ALICIA Table", "HIC Table"]
dataclasses = ["PM2.5", "PM10"]

def goscriptup():
    print("\033[A                             \033[A")



########################################################################
##datatable Initialize

datatable = dict()
for i in range(0,len(dataclasses)):
    datatable.update({dataclasses[i]:{"Value" : 0.0, "Sigma" :0.0}})

########################################################################
print('===================================')
print('Dust Monitoring Data Sending Script')

#timeseq = ['Year', 'Month', 'Day', 'Hour', 'Minute']
#ntimeseq = len(timeseq)
print('date? \n(blank if realtime)')

input_time1 = raw_input('Year: ')
if input_time1 == '':
    input_time = datetime.datetime.now()
else:
    input_time = inputinform.input_time_rt_update(int(input_time1))

goscriptup()
print("Time : %s" %input_time)

########################################################################
print('')
print('Location?')
for i in range(0,len(locations)):
    print("%d: %s" %(i+1,locations[i]))

loc2 = raw_input('')
loc = int(loc2)-1

goscriptup()
print('Location: %s' %locations[int(loc)])

print('')

dustdata = inputinform.input_dust(["PM2.5", "PM10"], ["SUM", "SIGMA"])



