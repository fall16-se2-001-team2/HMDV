# -*- coding: utf-8 -*-
#   Matthew Humphrey
#   10/30/2016
#   Adds longitude and latitude to the resource.json

import json
import codecs
import Provider
import pandas

#the file name will need to be changed to wherever you have it
f = codecs.open('../data/resource.json', 'r', 'utf-8')
resourceList = json.load(f)
f.close()

#the file name will need to be changed to wherever you want it to go
li = codecs.open('../data/resourceLatLon.json', 'a', 'utf-8')
for resource in resourceList:
    try:
        latlon = Provider.Provider.toCoordinates(resource['address'])
        resource['latitude'] = latlon[0]
        resource['longitude'] = latlon[1]
        json.dump(resource,li)
        li.write(',\n')
    except:
        li.write('{}]]')
li.close()
