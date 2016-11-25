#!/usr/bin/python
# -*- coding: utf-8 -*-
#import sqlite3
import sys  #qtPy dependencies
from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from Provider import Provider
import folium      #tag for removal
from folium import plugins     #tag for removal
#from Parse import Parse
#import Curve
#import Gui
import json
import codecs
from dataCollector import Geocoder
from ProviderList import ProviderList
from serviceTree import AddTopLevel
from HeatLayer import HeatLayer
from Map import Map

def main():
    #Parser.parseCounties("data/counties_TN.json", "leaflet/counties-tn.js")
    #Geocoder.Geocoder.addLatLonJSON('data/resource.json','data/resourceLatLon3.json',10)
    providersList = ProviderList('data/resourceLatLon.json',3)
    g = Geocoder.Geocoder()
    t = AddTopLevel.AddTopLevel()
    for provider in providersList.providers:
        if provider.longitude is None:  #if coords not in json file
            latlon = g.geocode(provider)
            provider.setLatLon (latlon[0], latlon[1])
        if len(provider.topLevelServices) == 0: #if topLevelServices not in json file
            tls = t.addToProvider(provider)
            provider.topLevelServices = tls
    map = Map([36.3134,-82.3534])	#initialize map centered at JC

    for provider in providersList.providers:
        folium.Marker([provider.latitude,provider.longitude], popup=str(provider)).add_to(map)
        #map.add_child(plugins.HeatMap([[provider.latitude,provider.longitude, 1]]))
    '''The webscraper did not parse this particular provider's address correctly. line 95 in resource.json'''
    #providerCoords = g.geocode(Provider("Name","207 N. Boone St. Johnson City, TN 37604","eligStr",False,1.0,1.0))		#test geocoding
    #folium.Marker(providerCoords, popup='ADRC (Aging, Disability, Resource Connections) - Johnson City').add_to(map)


    '''the following line is an example to place heat points for all providers from pandas'''
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