#!/usr/bin/python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------------------- 
#
# Name                     :Matthew Humphrey
# Department Name : Computer and Information Sciences
# File Name                :Geocoder.py
# Purpose                  :query google maps api with an address, and return latitude and longitude
#
# Author			        : Isaac Styles, styles@etsu.edu
# Create Date	            : 10/30/2016
#
#-----------------------------------------------------------------------------------------------------------
#
# Modified Date	: Nov 27, 2016
# Modified By		: Isaac Styles
#
#-------------------------------------------------------------------------------------------------------------
import json
import codecs
from geopy import geocoders

class Geocoder:
    api_key="AIzaSyBHJYku7O6cGgMNVL3nXo9dPB0EkgMVlXM" # gmaps api key for ETSU Computing Dept. listed under styles@etsu.edu (Isaac Styles)
    def __init__(self):
        self.g = geocoders.GoogleV3(api_key=Geocoder.api_key)

    #---------------------------------------------------
    # geocode(string, int)
    # purpose:append lat and lon to a provider class
    #---------------------------------------------------
    def geocode (self, address):
        place, (lat, lon) = self.g.geocode(address)      #returns tuple:(place, lat, lon)
        return lat, lon
    '''addLatLonJSON is a script to add lat and lon to a whole JSON file.'''
    @staticmethod
    def addLatLonJSON(source, dest, max=2):
        g = geocoders.GoogleV3(api_key=Geocoder.api_key)  # gmaps api key for ETSU Computing Dept. listed under styles@etsu.edu (Isaac Styles)
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