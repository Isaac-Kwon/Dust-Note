import sys
import time
import datetime
#from __future__ import print_function

def goscriptup():
    print "\033[A                             \033[A \r"

def input_time_rt_update(yearm):
    inputtime = datetime.datetime(2000,01,01,00,00)
    print inputtime
    #
    inputtime = inputtime.replace(year=yearm)###int(raw_input("Year?: ")))
    goscriptup()
    goscriptup()
    #
    print inputtime
    #
    inputtime = inputtime.replace(month=int(raw_input("Month?: ")))
    goscriptup()
    goscriptup()
    #
    print inputtime
    #
    inputtime = inputtime.replace(day=int(raw_input("Day?: ")))
    goscriptup()
    goscriptup()
    #
    print inputtime
    #
    inputtime = inputtime.replace(hour=int(raw_input("Hour?: ")))
    goscriptup()
    goscriptup()
    #
    print inputtime
    #
    inputtime = inputtime.replace(minute=int(raw_input("Minute?: ")))
    goscriptup()
    goscriptup()
    #
    print inputtime
    #
    return inputtime

def printdict(dict):
    print 'index', '\t',
    for key in dict.keys():
        print '|', key, ' \t',
    print ''
    #
    for key in dict.keys():
        print key, '\t',
        for key2 in dict[dict.keys()[0]].keys():
            print '|', dict[key][key2], '\t\t',
        print '\n',


def input_dust(dataclasses, datatypes):
    datadict = dict()
    for i in range(0,len(dataclasses)):
        datadict[dataclasses[i]] = dict();
        for j in range(0,len(datatypes)):
            print datatypes[j], 'of', dataclasses[i]
            datadict[dataclasses[i]][datatypes[j]] = int(raw_input(" :"))
            goscriptup()
            goscriptup()
    printdict(datadict)
    return datadict


if __name__ == "__main__":
    print ""
    #diction = input_dust(["PM2.5", "PM10"], ["SUM", "SIGMA"])
