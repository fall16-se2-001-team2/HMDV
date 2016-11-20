# -*- coding: utf-8 -*-
"""
@author: Matthew Humphrey
"""
import requests
import re
import json
import codecs
from bs4 import BeautifulSoup

f = codecs.open('../data/resource.json', 'r', 'utf-8')
resourceList = json.load(f)
f.close()

d = codecs.open('servicetree.json', 'r', 'utf-8')
serviceList = json.load(d)
d.close()

k = codecs.open('../data/resource.json','w','utf-8')
k.write("[")

names = {}
secondLevels = {}
topLevels = {}
newRe = {}
newResourceList = []
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
    json.dump(r,k)
    k.write(",")
    k.write("\n")
k.write("]")
k.close()

