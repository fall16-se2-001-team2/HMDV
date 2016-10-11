#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from Provider import Provider
import folium
#from Parse import Parse

contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Resource Map Research Tool</title>
</head>
<body>
<h2>Workstation</h2>
</body>
</html>
'''

def main():
	providerCoords = Provider.toCoordinates("207 N. Boone St. Johnson City, TN 37604")		#test geocoding - print returned coordinates
	map = folium.Map(location=[36.3134,-82.3534])	#initialize map centered at JC
	'''The webscraper did not parse this particular provider's address correctly.'''
	folium.Marker(providerCoords, popup='ADRC (Aging, Disability, Resource Connections) - Johnson City').add_to(map)
	map.save('tempBrowseLocal.html')				#save the generated map to html
	import webbrowser, os.path
	webbrowser.open("file:///" + os.path.abspath('tempBrowseLocal.html'))  # path elaborated for Mac
	#sqlite_file = 'research.sqlite'     # name of the sqlite database file
	#cursor = initializeDB(sqlite_file)  #cursor is pointer to db connection
	#p = Provider.fromDB(cursor)         #p -> array of providers
	#queryDB(cursor)
	#browseLocal(contents)              #display webpage
	#cursor.close()

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