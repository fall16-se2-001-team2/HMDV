# -*- coding: utf-8 -*-
"""
@author: Matthew Humphrey, Isaac Styles
"""
#import requests
import re
import json
import codecs
#from bs4 import BeautifulSoup


class AddTopLevel:
    def __init__(self):
        d = codecs.open('serviceTree/servicetree.json', 'r', 'utf-8')
        self.serviceList = json.load(d)
        d.close()
        self.names = {}
        i = 0
        for l in self.serviceList:
            self.names[l["name"]] = i
            i += 1

    def addToProvider(self, p):
        resourceTops = []
        for s in p.services:
            if s != "Not Found":
                try:
                    if not resourceTops.__contains__(self.serviceList[self.names[s]]["topLevelName"]):
                        resourceTops.append(self.serviceList[self.names[s]]["topLevelName"])
                except KeyError:
                    if not resourceTops.__contains__("Target Demographics"):
                        resourceTops.append("Target Demographics")
        if resourceTops.__len__() == 0:
            resourceTops.append("Not Found")
        return resourceTops
    '''addToJSON is a script to read a JSON file and add topLevelService to all records.'''
    @staticmethod
    def addToJSON(source, dest):

        f = codecs.open(source, 'r', 'utf-8')
        resourceList = json.load(f)
        f.close()

        d = codecs.open('serviceTree/servicetree.json', 'r', 'utf-8')
        serviceList = json.load(d)
        d.close()

        k = codecs.open(dest, 'w', 'utf-8')
        k.write("[")

        names = {}
        resourceTops = []
        i = 0

        for l in serviceList:
            names[l["name"]] = i
            i += 1

        for r in resourceList:
            resourceTops.clear()
            for s in r["services"]:
                if s != "Not Found":
                    try:
                        if not resourceTops.__contains__(serviceList[names[s]]["topLevelName"]):
                            resourceTops.append(serviceList[names[s]]["topLevelName"])
                    except KeyError:
                        if not resourceTops.__contains__("Target Demographics"):
                            resourceTops.append("Target Demographics")
            if resourceTops.__len__() == 0:
                resourceTops.append("Not Found")
            r["topLevelServices"] = resourceTops
            json.dump(r, k)
            k.write(",")
            k.write("\n")
        k.write("]")
        k.close()