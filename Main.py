#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------------------
#
# Name                     :Isaac Styles and Ryan Meades
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
# Modified Date	: Nov 28, 2016
# Modified By		: Isaac Styles
#
#-------------------------------------------------------------------------------------------------------------
#import sqlite3                 #for history
#from Parse import Parse        #for scripting
from ProviderList import ProviderList
from serviceTree import getTopLevelNames
from Map import Map
defaultHeight = 18          #constant declaring the default height of provider, out of 100
def main():
    '''retrieve the general resource types for this particular dataset. NOTE this doesn't change with the resource file.
        The serviceTree scripts would have to build another tree to conform to another dataset.'''
    topLevels = getTopLevelNames.getTopLevelNames('serviceTree/servicetree.json')
    QtGui, Ui_MainWindow = gui()


    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, topLevels)
    MainWindow.show()
    sys.exit(app.exec_())
    #app.exec_()

#-------------------------------------------------------------
# gui()
# purpose: accept a user inputted top level service and radius
#-------------------------------------------------------------
def gui():
    from PyQt4 import QtCore, QtGui
    import sys
    try:                        #the following code is for potential translation to other languages, and is QT generated
        _fromUtf8 = QtCore.QString.fromUtf8
    except AttributeError:
        def _fromUtf8(s):
            return s
    try:
        _encoding = QtGui.QApplication.UnicodeUTF8

        def _translate(context, text, disambig):
            return QtGui.QApplication.translate(context, text, disambig, _encoding)
    except AttributeError:
        def _translate(context, text, disambig):
            return QtGui.QApplication.translate(context, text, disambig)

    # ------------------------------------------------------------
    # UI_MainWindow
    # purpose: display the main GUI window
    # ------------------------------------------------------------
    class Ui_MainWindow(object):
        def setupUi(self, MainWindow, topLevels):
            MainWindow.setObjectName(_fromUtf8("MainWindow"))
            MainWindow.resize(792, 600)
            self.centralwidget = QtGui.QWidget(MainWindow)
            self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

            # button to exit program
            self.ExitProgramObj = QtGui.QPushButton(self.centralwidget)
            self.ExitProgramObj.setGeometry(QtCore.QRect(660, 510, 111, 41))
            self.ExitProgramObj.setObjectName(_fromUtf8("ExitProgramObj"))
            self.ExitProgramObj.clicked.connect(self.close_application)

            # List window
            self.listView = QtGui.QListView(self.centralwidget)
            self.listView.setGeometry(QtCore.QRect(380, 10, 401, 481))
            self.listView.setObjectName(_fromUtf8("listView"))

            # Instruction Text Browser
            self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
            self.textBrowser.setGeometry(QtCore.QRect(20, 10, 341, 350))
            self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

            # Radius Input from user
            self.RadiusEntry1Obj = QtGui.QLineEdit(self.centralwidget)
            self.RadiusEntry1Obj.setGeometry(QtCore.QRect(460, 30, 113, 20))
            self.RadiusEntry1Obj.setObjectName(_fromUtf8("RadiusEntry1Obj"))

            # Space for Dropdown List
            self.dropDownList = QtGui.QComboBox(MainWindow)
            self.dropDownList.setGeometry(QtCore.QRect(460, 75, 270, 20))
            self.dropDownList.addItems(topLevels)

            # Sizing
            self.label = QtGui.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(390, 20, 91, 31))
            self.label.setObjectName(_fromUtf8("label"))

            # button to generate map
            self.GenerateMapObj = QtGui.QPushButton(self.centralwidget)
            self.GenerateMapObj.setGeometry(QtCore.QRect(660, 440, 111, 41))
            self.GenerateMapObj.setObjectName(_fromUtf8("GenerateMapObj"))
            self.GenerateMapObj.clicked.connect(self.handleOpenMap)

            # Spacing/ Layerin
            self.listView.raise_()
            self.ExitProgramObj.raise_()
            self.textBrowser.raise_()
            self.RadiusEntry1Obj.raise_()
            self.dropDownList.raise_()
            self.label.raise_()
            self.GenerateMapObj.raise_()

            # unused
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtGui.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 21))
            self.menubar.setObjectName(_fromUtf8("menubar"))
            self.menuMap_View_Vers_0_01 = QtGui.QMenu(self.menubar)
            self.menuMap_View_Vers_0_01.setObjectName(_fromUtf8("Service Map Generator v.1.0"))
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtGui.QStatusBar(MainWindow)
            self.statusbar.setObjectName(_fromUtf8("statusbar"))
            MainWindow.setStatusBar(self.statusbar)
            self.menubar.addAction(self.menuMap_View_Vers_0_01.menuAction())

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ------------------------------------------------------------
        # handleOpenMap()
        # purpose: listener that produces a map once triggered
        # ------------------------------------------------------------
        def handleOpenMap(self):
            produceMap(self.dropDownList.currentText(), self.RadiusEntry1Obj.text())
        # ------------------------------------------------------------
        # retranslateUi()
        # purpose: modifies the GUI objects once they're created
        # ------------------------------------------------------------
        def retranslateUi(self, MainWindow):
            MainWindow.setWindowTitle(_translate("MainWindow", "ETSU Social Services Mapper", None))
            self.ExitProgramObj.setText(_translate("MainWindow", "Exit", None))
            self.textBrowser.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">ETSU Social Work Department<br /><br /></p><p>To generate a map, enter a default radius and select the type of service. Click &quot;Generate Map&quot; to continue.</span></p><p><img src=panda.jpg>Team Pandas</p></body></html>",
                                                None))
            self.RadiusEntry1Obj.setText(_translate("MainWindow", "25", None))
            self.label.setText(_translate("MainWindow", "Radius (mi.)", None))
            self.GenerateMapObj.setText(_translate("MainWindow", "Generate Map", None))
            self.menuMap_View_Vers_0_01.setTitle(_translate("MainWindow", "Map Maker v.1.0", None))

        def close_application(self):
            sys.exit()

    return QtGui, Ui_MainWindow
#------------------------------------------------------------
# produceMap(string, string)
# purpose: take user input and produce a corresponding map
#------------------------------------------------------------
def produceMap(topLevel, radius):
    '''scripts to modify the resource file without producing a map. included for performance reasons during testing'''
    # Parser.parseCounties("data/counties_TN.json", "leaflet/counties-tn.js")    #parse the US Census geoJSON into one supported by leaflet
    # Geocoder.Geocoder.addLatLonJSON('data/resource.json','data/resourceLatLon3.json',10)   #manually add lat and lon to the resource file for 10 providers

    #from MainWindow import Ui_MainWindow
    '''return the list of Provider objects offering a particular top level service, with lon and lat, up to 1000 providers '''
    providersList = ProviderList('data/resourceLatLon.json', topLevel, radius, 1000)
    map = Map(topLevel)  # initialize map with title of selected top level service
    for provider in providersList.providers:
        map.addProvider(provider.latitude, provider.longitude, defaultHeight, provider.getRadius(), str(provider))
    '''the following line is an example using pandas iterable arrays to place heat points in Folium'''
    # map.add_children(plugins.HeatMap([[providerCoords[0], providerCoords[1]] for name, row in morning_rush.iloc[:1000].iterrows()]))
    map.save('tempBrowseLocal.html')  # save the generated map to html
    import webbrowser, os.path
    webbrowser.open("file:///" + os.path.abspath('tempBrowseLocal.html'))  # display the map in the browser

    '''the following db code is the beginnings of a way to associate an output map with variables(radius, height), demographics files, and county boundaries.'''
    # sqlite_file = 'research.sqlite'     # name of the sqlite database file
    # cursor = initializeDB(sqlite_file)  #cursor is pointer to db connection
    # p = Provider.fromDB(cursor)         #p -> array of providers
    # queryDB(cursor)
    # browseLocal(contents)              #display webpage
    # cursor.close()
    '''this code tests the age constraint parser, which is incomplete'''
    # from PopConstraint import PopConstraint
    # PopConstraint.ageConstraint("children from 8-14 years old")


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