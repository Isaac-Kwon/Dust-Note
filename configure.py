#-*- coding: utf-8 -*-

from __future__ import print_function

import sys,os
import json

#configuration main function's destinations

#configure things

#dataclasses : size of particles
#datatypes : SUM, SIGMA or etc
#Locations

if sys.version_info.major<3:
    print("Python version is too low, use over python 3")
    exit()

from builtins import input

def initialize():
    if not os.path.exists("cfg.json"):
        with open('cfg.json','w') as genfile:
            genjson = {"Locations": "none", "Type1": "none", "Type2": "none", "SheetFile Name": "none"}
            json.dump(genjson,genfile, ensure_ascii=False)

def configtypes(init_name,suffix,original):
    returnarray = list();
    print('Original Configuration data of %s' %(init_name))
    print(original)
    loop_number_str = input('number of %s: ' %init_name)
    if loop_number_str == '':
        return original
    else:
        loop_number = int(loop_number_str)
    for i in range(0,loop_number):
        returnarray.append(input('No.%d types? ' %(i+1))+suffix)
    return returnarray

def config_one(question, original):
    print('Original Configuration data of %s' %(question))
    print(original)
    temp_name = input(question+'?')
    if temp_name == '':
        return original
    else:
        return temp_name

if __name__ == "__main__":
    initialize()
    print("\n========================================")
    print("Dust Monitoring Script Configure")
    print("You can set Monitoring Location, ParticleSize, CollectingInformation, GoogleSpreadsheet\'s Filename\n")
    print("for all of Question, it will show original value of configure file, you can leave it at that or overwrite each configuration")
    print("At each question of NUMBERS just press RETURN to leave, put information to overwrite\n")
    with open('cfg.json', 'r') as infile:
        originaldic = json.load(infile)
    outputjson = dict()
    outputjson["Locations"] = configtypes('locations','', originaldic["Locations"])
    print('')
    outputjson["Type1"] = configtypes('particle types', 'um', originaldic["Type1"])
    print('')
    outputjson["Type2"] = configtypes('data types', '', originaldic["Type2"])
    print('')
    outputjson["SheetFile Name"] = config_one('SpreadSheet Name', originaldic["SheetFile Name"])
    print('')
    jsonString = json.dumps(outputjson, indent=4)
    print('')
    print(jsonString)
    # 문자열 출력
    #
    with open('cfg.json', 'w') as outfile:
        json.dump(outputjson, outfile, ensure_ascii=False)
