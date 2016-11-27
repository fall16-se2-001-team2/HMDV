#!/usr/bin/python
# -*- coding: utf-8 -*-
#import sqlite3
import sys  #pyQt dependencies
from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
#from Parse import Parse        #for scripting
#import Gui
#import json
#import codecs
from ProviderList import ProviderList
from serviceTree import getTopLevelNames
from Map import Map

def main():
    #Parser.parseCounties("data/counties_TN.json", "leaflet/counties-tn.js")
    #Geocoder.Geocoder.addLatLonJSON('data/resource.json','data/resourceLatLon3.json',10)

    topLevels = getTopLevelNames.getTopLevelNames('serviceTree/servicetree.json')

    providersList = ProviderList('data/resourceLatLon.json',topLevels[0], 25, 1000)

    map = Map()	#initialize map centered at JC

    for provider in providersList.providers:
        map.addProvider(provider.latitude, provider.longitude, 18,provider.getRadius(), str(provider))

    #folium.Marker(providerCoords, popup='ADRC (Aging, Disability, Resource Connections) - Johnson City').add_to(map)


    '''the following line is an example using pandas iterable arrays to place heat points in Folium'''
    #map.add_children(plugins.HeatMap([[providerCoords[0], providerCoords[1]] for name, row in morning_rush.iloc[:1000].iterrows()]))
    map.save('tempBrowseLocal.html')				#save the generated map to html
    import webbrowser, os.path
    webbrowser.open("file:///" + os.path.abspath('tempBrowseLocal.html'))  # path elaborated for Mac
    #sqlite_file = 'research.sqlite'     # name of the sqlite database file
    #cursor = initializeDB(sqlite_file)  #cursor is pointer to db connection
    #p = Provider.fromDB(cursor)         #p -> array of providers
    #queryDB(cursor)
    #browseLocal(contents)              #display webpage
    #cursor.close()

    #c = Curve()
    #from PopConstraint import PopConstraint
    #PopConstraint.ageConstraint("children from 8-14 years old")

    #pyqt GUI stuff starts here

    #end pyqt GUI stuff
#------------------------------------------------------------
#initializeDB(string)
#Purpose: Connect to the database file and return the cursor
#------------------------------------------------------------

def initializeDB(sqlite_file):
    conn = sqlite3.connect(sqlite_file)
    return conn.cursor()

#------------------------------------------------------------
#strToFile(string, string)
#Purpose:Write a file with the given name and the given text.
#------------------------------------------------------------
def strToFile(text, filename):
    output = open(filename,"w")
    output.write(text)
    output.close()

# ------------------------------------------------------------
# browseLocal(string, string)
# Purpose:Write a file with the given name and the given text.
#	depreciated because map_osm.save writes the entire html file
#-------------------------------------------------------------
def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    #Start your webbrowser on a local file containing the text with given filename
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac

# ------------------------------------------------------------
# queryDB(cursor)
# Purpose:use a cursor to query SQLite and return all rows
# ------------------------------------------------------------
def queryDB(cursor):
    table_name = 'resource'
    #id_column = 'rid'
    cursor.execute('SELECT * FROM {tn}'. \
				   format(tn=table_name))
    all_rows = cursor.fetchall()
    print('1):', all_rows)
    return all_rows

main()	#run the program