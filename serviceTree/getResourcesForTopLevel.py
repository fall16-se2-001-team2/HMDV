# -*- coding: utf-8 -*-
"""
@author: Matthew Humphrey
"""
#import requests
#import re
import json
import codecs
#from bs4 import BeautifulSoup

def main():
    inp = input("What is the name of the top level service you wish to search for?")
    res = getResourcesForTopLevel(inp)
    for r in res:
        print(r)

def getResourcesForTopLevel(fileName, topLevelService):          #just call this method, it returns a list
    f = codecs.open(fileName, 'r', 'utf-8')
    resourceList = json.load(f)
    f.close()

    resources = []

    for r in resourceList:
        if r["topLevelServices"].__contains__(topLevelService):
            resources.append(r)

    #k = codecs.open('../data/resourceOf#ServiceType#.json','w','utf-8')
    #k.write("[")
    #for t in topLevels:
    #    names["name"] = t
    #    json.dump(names,k)
    #    k.write(",\n")
    #k.write("]")
    return resources


if __name__ == "__main__":
    main()
