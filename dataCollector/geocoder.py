# -*- coding: utf-8 -*-
#   Matthew Humphrey
#   10/30/2016
#   Adds longitude and latitude to the resource.json

import json
import codecs
import Provider
from geopy import geocoders
import pandas
providersRelAddress = '../data/resource.json'       #datafile address relative to this file

class geocoder:
    resourceList = None
    def __init__(self,providersFile):
        f = codecs.open(providersFile, 'r', 'utf-8')
        resourceList = json.load(f)
        f.close()
    #---------------------------------------------------
    # geocode(string, int)
    # purpose:append lat and lon to a number of providers
    #---------------------------------------------------
    def geocode (self, outFile, number=2):
        count = 0
        li = codecs.open('../data/resourceLatLon.json', 'a', 'utf-8')
        for resource in self.resourceList:
            try:
                g = geocoders.GoogleV3(api_key="AIzaSyBHJYku7O6cGgMNVL3nXo9dPB0EkgMVlXM")   #gmaps api key for ETSU Computing Dept. listed under styles@etsu.edu (Isaac Styles)
                place = g.geocode(resource['address'])      #place is not necessary
                #resource['latitude'] = lat
                #resource['longitude'] = lon
                #json.dump(resource,li)
                li.write(',\n')
            except:
                li.write('{}]]')
            if (count>=number):
                break
        li.close()