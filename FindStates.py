#Created by:    Jarred Wininger/ Matthew Humphrey
#Date:          October 9, 2016

import json
import os
from pprint import pprint

#opens the countylines file downloaded from http://eric.clst.org/Stuff/USGeoJSON
with open('countylines.json') as countylines:
    countydata = json.load(countylines)

#goes through each county and checks if it is Tennessee (state number 47)
#if it matches, it pulls the name, GEO_ID (which is used in census files) and its
#geometry array.
# To change which state it looks for, find the state number in the json file and replace it
# in the if statement
for record in countydata['features']:
    if(int(record['properties']['STATE']) == 47):
        # write to dictionary
        countyData = {
            'name': record['properties']['NAME'],
            'GEO_ID': record['properties']['GEO_ID'],
            'geometry': record['geometry']
            }

        # append to json file
        # to use, change the first open parameter with location of JSON
        with open('Counties_TN.json', 'a') as f:
            json.dump(countyData, f)
            f.write(os.linesep)

