# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui_0-02-1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from MapWindow import Ui_MapWindow

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(792, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #button to exit program
        self.ExitProgramObj = QtGui.QPushButton(self.centralwidget)
        self.ExitProgramObj.setGeometry(QtCore.QRect(660, 510, 111, 41))
        self.ExitProgramObj.setObjectName(_fromUtf8("ExitProgramObj"))
        self.ExitProgramObj.clicked.connect(self.close_application)

        #List window
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(380, 10, 401, 481))
        self.listView.setObjectName(_fromUtf8("listView"))

        #Instruction Text Browser
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 341, 131))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        #Radius Input from user
        self.RadiusEntry1Obj = QtGui.QLineEdit(self.centralwidget)
        self.RadiusEntry1Obj.setGeometry(QtCore.QRect(460, 30, 113, 20))
        self.RadiusEntry1Obj.setObjectName(_fromUtf8("RadiusEntry1Obj"))

        #Sizing
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 20, 91, 31))
        self.label.setObjectName(_fromUtf8("label"))

        #button to generate map
        self.GenerateMapObj = QtGui.QPushButton(self.centralwidget)
        self.GenerateMapObj.setGeometry(QtCore.QRect(660, 440, 111, 41))
        self.GenerateMapObj.setObjectName(_fromUtf8("GenerateMapObj"))
        self.GenerateMapObj.clicked.connect(self.handleOpenMap)

        #Spacing/ Layerin
        self.listView.raise_()
        self.ExitProgramObj.raise_()
        self.textBrowser.raise_()
        self.RadiusEntry1Obj.raise_()
        self.label.raise_()
        self.GenerateMapObj.raise_()

        #unused
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMap_View_Vers_0_01 = QtGui.QMenu(self.menubar)
        self.menuMap_View_Vers_0_01.setObjectName(_fromUtf8("menuMap_View_Vers_0_01"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMap_View_Vers_0_01.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ExitProgramObj.setText(_translate("MainWindow", "Exit Program", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Team Pandas Map Creator<br /><br />In order to use the Heat Map Creator, Enter a radius on the right and click &quot;Generate Map.&quot;</span></p></body></html>", None))
        self.RadiusEntry1Obj.setText(_translate("MainWindow", "0", None))
        self.label.setText(_translate("MainWindow", "Radius", None))
        self.GenerateMapObj.setText(_translate("MainWindow", "Generate Map", None))
        self.menuMap_View_Vers_0_01.setTitle(_translate("MainWindow", "Map View Vers. 0.01", None))


    #attempting to define Button handler classes to open Gui_0_02-2 as seen http://stackoverflow.com/questions/27567208/how-do-i-open-sub-window-after-i-click-on-button-on-main-screen-in-pyqt4

    def handleOpenMap(self):
        Ui_MapWindow.showMap(self)



    def close_application(self):
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

