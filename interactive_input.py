#-*- coding: utf-8 -*-
from __future__ import print_function

from builtins import input

import sys
import time
import datetime


def goscriptup():
    print("\033[A                             \033[A \r")

def input_time_rt_update(yearm):
    inputtime = datetime.datetime(2000,1,1,0,0)
    print('%s' %inputtime)
    #
    inputtime = inputtime.replace(year=yearm)###int(input("Year?: ")))
    goscriptup()
    goscriptup()
    #
    print('%s' %inputtime)
    #
    inputtime = inputtime.replace(month=int(input("Month?: ")))
    goscriptup()
    goscriptup()
    #
    print('%s' %inputtime)
    #
    inputtime = inputtime.replace(day=int(input("Day?: ")))
    goscriptup()
    goscriptup()
    #
    print('%s' %inputtime)
    #
    inputtime = inputtime.replace(hour=int(input("Hour?: ")))
    goscriptup()
    goscriptup()
    #
    print('%s' %inputtime)
    #
    inputtime = inputtime.replace(minute=int(input("Minute?: ")))
    goscriptup()
    goscriptup()
    #
    print('%s' %inputtime)
    #
    return inputtime

def printdict(dicta):
    print('index\t',end='')
    for key in list(dicta[list(dicta.keys())[0]].keys()):
        print('|%s\t' %key,end='')
    print('')
    #
    for key in list(dicta.keys()):
        print('%s\t' %key,end='')
        for key2 in list(dicta[list(dicta.keys())[0]].keys()):
            print('|%s\t' %dicta[key][key2],end='')
        print('')


def input_dust(dataclasses, datatypes):
    datadict = dict()
    for i in range(0,len(dataclasses)):
        datadict[dataclasses[i]] = dict();
        for j in range(0,len(datatypes)):
            print('%s of %s'%(datatypes[j], dataclasses[i]))
            datadict[dataclasses[i]][datatypes[j]] = int(input(" :"))
            goscriptup()
            goscriptup()
    printdict(datadict)
    return datadict

if __name__ == "__main__":
    #    diction testdata
    #    diction = {'PM2.5': {'SUM': 2, 'SIGMA': 3}, 'PM10': {'SUM': 4, 'SIGMA': 5}}
    print("")
