#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------------------
#
# Name                     :Isaac Styles
# Department Name : Computer and Information Sciences
# File Name                :ProviderList.py
# Purpose                  :encapsulate a list of providers, ensuring that they contain lat, lon,
#                            and topLevelService. If a unique radius is defined, ru is set.
#                               It also does the conversion from miles to degrees.
# Author			        : Isaac Styles, styles@etsu.edu
# Create Date	            : Sept 28, 2016
#
#-----------------------------------------------------------------------------------------------------------
#
# Modified Date	: Nov 27, 2016
# Modified By		: Isaac Styles
#
#-------------------------------------------------------------------------------------------------------------
import codecs
import json
from Provider import Provider
from serviceTree import AddTopLevel
from dataCollector import Geocoder

class ProviderList:
    providers = []
    def __init__(self, fileName, topLevelService, defaultRadiusInMiles, count=-1):  # if count isn't specified then import all providers
        g = Geocoder.Geocoder()
        t = AddTopLevel.AddTopLevel()
        with codecs.open(fileName, 'r', 'utf-8') as f:
            providersData = json.load(f)
        for tally, providerObj in enumerate(providersData):
            provider = Provider(providerObj)
            if len(provider.topLevelServices) == 0:  # if topLevelServices not in json file
                tls = t.addToProvider(provider)
                provider.topLevelServices = tls
            if not topLevelService in provider.topLevelServices:  # if this provider doesn't have the particular topLevelService, don't append it
                continue
            if provider.longitude is None:  # if coords not in json file
                latlon = g.geocode(provider.address)
                provider.setLatLon(latlon[0], latlon[1])



            if provider.getRadius() == None:
                provider.ru = float(defaultRadiusInMiles) / 69.0      #convert to degrees. there are approximately 69 miles in 1 degree latitude.
            self.providers.append(provider)
            tally += 1
            if tally == count:
                break

