# -*- coding: utf-8 -*-
#   Jarred Wininger and Matthew Humphrey
#   09/16/2016
#   Reads stuff from the resource.json
 

import json
import codecs

#the file name will need to be changed to wherever you have it
f = codecs.open('../data/resource.json', 'r', 'utf-8')
resourceList = json.load(f)
f.close()

countDict = {}
nameDict = {}

for resource in resourceList:
    eli = resource['eligibility']
    name = resource['name']
    nameDict[eli] = name
    countDict[eli] = 0

for resource in resourceList:
    eli = resource['eligibility']
    countDict[eli] += 1

#the file name will need to be changed to wherever you want it to go
li = codecs.open('../text/listOfMultiEligibilities.txt', 'w', 'utf-8')
for eli in countDict:
    try:
        if countDict[eli] > 10:
            li.write(str(eli))
            li.write('\nCount: ')
            li.write(str(countDict[eli]))
            li.write('\n[')
            for na in nameDict:
                if na == eli:
                    li.write(nameDict[na])
            li.write(']\n\n')
    except UnicodeEncodeError:
        pprint(eli)
        li.write('Character encoding error.\n\n')
li.close()
