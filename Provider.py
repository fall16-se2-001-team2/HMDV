#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------------------
#
# Name                     :Isaac Styles
# Department Name : Computer and Information Sciences
# File Name                :Provider.py
# Purpose                  :store and parse a service provider from a JSON resource file.
#                            output an html formatted string of name, services, phone, and # of people impacted.
#
# Author			        : Isaac Styles, styles@etsu.edu
# Create Date	            : Sept 14, 2016
#
#-----------------------------------------------------------------------------------------------------------
#
# Modified Date	: Nov 27, 2016
# Modified By		: Isaac Styles
#
#-------------------------------------------------------------------------------------------------------------
class Provider:
    #parsed attributes
    name = ""
    address = ""
    eligibility = ""
    #desc = ""
    phone = ""
    isShelter = False                   #boolean identifying if the provider offers shelter
    #calculated attributes
    longitude = None
    latitude = None
    numOfPeople = 0                     #calculated number of people close and eligible for services
    #h = 100                            #the relative height of the provider; type int(0,100)
    ru = 0.0                            #unique radius. NOTE this is in DEGREES
    #fu = 0.0                           #unique fade (0-1] from provider
    services = []                       #low level services offered
    topLevelServices = []               #general categories of services determined by serviceTree
    isMobile = False                    #boolean identifying if the provider offers mobile service. True indicates 0 fade for service area. *NOT IMPLEMENTED*
    jsonObj = None                      #data structure so the program can output the completed resource file *PROGRAM DOESN'T OUTPUT JSON FILE*
    #regions = []                       #list of pointers to regions impacted by this provider
    #population = []                    #list of population constraints
    #-----------------------------------
    # Provider(jsonObj)
    # Purpose: initialize from JSON file
    #-----------------------------------
    def __init__(self,jsonObj):
        self.jsonObj = jsonObj
        self.name = jsonObj["name"]
        self.address = jsonObj["address"]
        self.eligibility = jsonObj["eligibility"]
        self.services = jsonObj["services"]
        #self.desc = jsonObj["description"]
        self.phone = jsonObj["phone"]
        if jsonObj["shelter"] == "Yes":
            self.isShelter = True
        if "topLevelServices" in jsonObj:
            self.topLevelServices = jsonObj["topLevelServices"]
        if "longitude" in jsonObj:      #check to see if previously geocoded
            self.longitude = jsonObj["longitude"]
            self.latitude = jsonObj["latitude"]
        if "ru" in jsonObj:             #check for unique radius in resource file
            self.ru = float(jsonObj["ru"])
    # ------------------------------------------------------------
    # Provider(string, string, string, string, string, string, string, float, float, bool)
    # Purpose: initialize a provider with minimal information
    # -------------------------------------------------------------
    """def __init__(self, name, address, eligibility, defaultRadius, multiplier, isMobile=False):
        self.rd = defaultRadius * multiplier         #the provider's default radius is the product of resourceType's radius and the resource's multiplier
        self.address = address
        #self.address2 = address2
        self.name = name
        self.eligibility = eligibility
        self.isMobile = isMobile"""
    # ------------------------------------------------------------
    # Provider(string, string, string, string, string, string, string, bool, float, float)
    # Purpose:initialize a provider with a unique radius and fade
    # -------------------------------------------------------------
    """def __init__(self, name, address, eligibility, isMobile, radius, fade):
        self.address = address
        self.name = name
        self.eligibility = eligibility
        self.isMobile = isMobile
        self.ru = radius                # optional parameters unique radius and fade
        self.fu = fade"""

    def setLatLon (self, lat, lon):
        self.latitude = lat
        self.longitude = lon

    def getRadius (self):
        if self.ru > 0:     # if unique radius defined, return that
            return self.ru
        else:
            return None


    def __str__(self):
        serv = ""
        for i,s in enumerate(self.services):
            i += 1
            serv += s
            if i == len(self.services):
                break
            else:
                serv += ", "
        return "<h3>"+ self.name + "</h3><p>Services: "+serv+"</p><p>Phone:" + self.phone + "</p>"