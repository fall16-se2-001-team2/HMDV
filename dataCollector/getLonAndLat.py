# -*- coding: utf-8 -*-
#   Matthew Humphrey
#   10/30/2016
#   Adds longitude and latitude to the resource.json

import json
import codecs
import Provider
from geopy import geocoders
import pandas

#the file name will need to be changed to wherever you have it
f = codecs.open('../data/resource.json', 'r', 'utf-8')
resourceList = json.load(f)
f.close()

#the file name will need to be changed to wherever you want it to go
li = codecs.open('../data/resourceLatLon.json', 'a', 'utf-8')
for resource in resourceList:
    try:
        latlon = addressToCoordinates(resource['address'])
        from geopy import geocoders

        g = geocoders.GoogleV3(api_key="AIzaSyBHJYku7O6cGgMNVL3nXo9dPB0EkgMVlXM")
        place, (lat, lng) = g.geocode(address)      #place is not necessary
        resource['latitude'] = lat
        resource['longitude'] = lon
        json.dump(resource,li)
        li.write(',\n')
    except:
        li.write('{}]]')
li.close()