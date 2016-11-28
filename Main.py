#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------------------
#
# Name                     :Isaac Styles
# Department Name : Computer and Information Sciences
# File Name                :Main.py
# Purpose                  :Create a map of a general (top level) service, and approximate the number of people
#                            impacted by that service.
#
# Author			        : Team Pandas, github.com/fall16-se2-001-team2/HMDV
#                                   Product Owner: Isaac Styles (styles@etsu.edu
# Create Date	            : Sept 10, 2016
#
#-----------------------------------------------------------------------------------------------------------
#
# Modified Date	: Nov 27, 2016
# Modified By		: Isaac Styles
#
#-------------------------------------------------------------------------------------------------------------
#import sqlite3
import sys  #pyQt dependencies
from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
#from Parse import Parse        #for scripting
from ProviderList import ProviderList
from serviceTree import getTopLevelNames
from Map import Map

def main():
    #'''scripts to modify the resource file without producing a map.'''
    #Parser.parseCounties("data/counties_TN.json", "leaflet/counties-tn.js")    #parse the US Census geoJSON into one supported by leaflet
    #Geocoder.Geocoder.addLatLonJSON('data/resource.json','data/resourceLatLon3.json',10)   #manually add lat and lon to the resource file

    topLevels = getTopLevelNames.getTopLevelNames('serviceTree/servicetree.json')   #retrieve the general resource types for this dataset
    from MainWindow import start
    #userInput = start(topLevels)
    '''return the list of Provider objects offering a particular top level service, with lon and lat '''
    providersList = ProviderList('data/resourceLatLon.json',topLevels[0], 25, 1000)
    map = Map(topLevels[0])	                #initialize map with title of selected top level service
    for provider in providersList.providers:
        map.addProvider(provider.latitude, provider.longitude, 18,provider.getRadius(), str(provider))
    '''the following line is an example using pandas iterable arrays to place heat points in Folium'''
    #map.add_children(plugins.HeatMap([[providerCoords[0], providerCoords[1]] for name, row in morning_rush.iloc[:1000].iterrows()]))
    map.save('tempBrowseLocal.html')				                        #save the generated map to html
    import webbrowser, os.path
    webbrowser.open("file:///" + os.path.abspath('tempBrowseLocal.html'))   #display the map in the browser

    '''the following db code is the beginnings of a way to associate an output map with variables(radius, height), demographics files, and county boundaries.'''
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