# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui_0-02-2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtWebKit

try:
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

class Ui_MapWindow(object):
    def setupUi(self, MapWindow):
        MapWindow.setObjectName(_fromUtf8("MapWindow"))
        MapWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MapWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(10, 10, 781, 481))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))

        #Button for closing the app
        self.ExitProgramObj2 = QtGui.QPushButton(self.centralwidget)
        self.ExitProgramObj2.setGeometry(QtCore.QRect(660, 510, 111, 41))
        self.ExitProgramObj2.setObjectName(_fromUtf8("ExitProgramObj2"))
        self.ExitProgramObj.clicked.connect(self.close_application)

        #Button to go back? May remove
        self.BackToMainObj = QtGui.QPushButton(self.centralwidget)
        self.BackToMainObj.setGeometry(QtCore.QRect(520, 510, 111, 41))
        self.BackToMainObj.setObjectName(_fromUtf8("BackToMainObj"))


        MapWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MapWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMap_View_Vers_0_01 = QtGui.QMenu(self.menubar)
        self.menuMap_View_Vers_0_01.setObjectName(_fromUtf8("menuMap_View_Vers_0_01"))
        MapWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MapWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MapWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMap_View_Vers_0_01.menuAction())

        self.retranslateUi(MapWindow)
        QtCore.QMetaObject.connectSlotsByName(MapWindow)

    def retranslateUi(self, MapWindow):
        MapWindow.setWindowTitle(_translate("MapWindow", "MapWindow", None))
        self.ExitProgramObj2.setText(_translate("MapWindow", "Exit Program", None))
        self.BackToMainObj.setText(_translate("MapWindow", "Back to Menu", None))
        self.menuMap_View_Vers_0_01.setTitle(_translate("MapWindow", "Map View Vers. 0.01", None))

    def showMap(self):
        if __name__ == "__main__":
            import sys
            app = QtGui.QApplication(sys.argv)
            MapWindow = QtGui.QMainWindow()
            ui = Ui_MapWindow()
            ui.setupUi(MapWindow)
            MapWindow.show()
            sys.exit(app.exec_())




