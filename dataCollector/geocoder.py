# -*- coding: utf-8 -*-
#   Matthew Humphrey / Isaac Styles
#   10/30/2016
#   Adds longitude and latitude to the resource.json

import json
import codecs
#import Provider
from geopy import geocoders
#import pandas

class Geocoder:
    def __init__(self):
        self.g = geocoders.GoogleV3(api_key="AIzaSyBHJYku7O6cGgMNVL3nXo9dPB0EkgMVlXM")  # gmaps api key for ETSU Computing Dept. listed under styles@etsu.edu (Isaac Styles)

    #---------------------------------------------------
    # geocode(string, int)
    # purpose:append lat and lon to a provider class
    #---------------------------------------------------
    def geocode (self, provider):
        #li = codecs.open('../data/resourceLatLon2.json', 'w', 'utf-8')
        #li.write('[')
        #for resource in self.resourceList:
        #try:

        place, (lat, lon) = self.g.geocode(provider.address)      #place is not necessary
        return lat, lon
        #json.dump(resource,li)
        #li.write(',\n')
        #except:
        #     break   #remove succeeding line
        #      li.write('{}]]')
        #   if count>=number:
        #     break
        #li.close()
    '''addLatLonJSON is a script to add lat and lon to a whole JSON file.'''
    @staticmethod
    def addLatLonJSON(source, dest, max=2):
        g = geocoders.GoogleV3(api_key="AIzaSyBHJYku7O6cGgMNVL3nXo9dPB0EkgMVlXM")  # gmaps api key for ETSU Computing Dept. listed under styles@etsu.edu (Isaac Styles)
        with codecs.open(source, 'r', 'utf-8') as inf:
            resourceList = json.load(inf)
        li = codecs.open(dest, 'w', 'utf-8')
        li.write('[')
        count = 0
        for resource in resourceList:
            place, (lat, lon) = g.geocode(resource["address"])      #place is not necessary
            resource['latitude'] = lat
            resource['longitude'] = lon
            json.dump(resource,li)
            count += 1
            if count == len(resourceList) or count == max:
                break
            li.write(',\n')
        li.write(']')
        li.close()