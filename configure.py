from __future__ import print_function
from builtins import input
import json

#configuration main function's destinations

#configure things

#dataclasses : size of particles
#datatypes : SUM, SIGMA or etc
#Locations

def configtypes(init_name,suffix):
    returnarray = list();
    loop_number = int(input('number of %s: ' %init_name))
    for i in range(0,loop_number):
        returnarray.append(input('No.%d types? ' %(i+1))+suffix)
    return returnarray

if __name__ == "__main__":
    outputjson = dict()
    outputjson["Locations"] = configtypes('locations','')
    print('')
    outputjson["Type1"] = configtypes('particle types', 'um')
    print('')
    outputjson["Type2"] = configtypes('data types', '')
    print('')
    outputjson["SheetFile Name"] = input('spreadsheet file\'s name?')
    print('')
    jsonString = json.dumps(outputjson, indent=4)
    print('')
    print(jsonString)
    # 문자열 출력
    #
    with open('cfg.json', 'w') as outfile:
        json.dump(outputjson, outfile, ensure_ascii=False)
