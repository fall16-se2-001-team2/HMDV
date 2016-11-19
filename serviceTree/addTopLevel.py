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

names = {}
secondLevels = {}
topLevels = {}
resourceTops = {}
i = 0

for l in serviceList:
    names[l["name"]] = i
    i += 1

for r in resourceList:
    for s in r["services"]:
        if s != "Not Found":
            try:
                resourceTops = serviceList[names[s]]["topLevelName"]
            except KeyError:
                resourceTops = "Target Demographics"
    r["topLevelServices"] = resourceTops

k = codecs.open('../data/resourceWithTopLevelName.json','w','utf-8')
k.write("[")
for r in resourceList:
    json.dump(r,k)
    k.write(",")
k.write("]")

