# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui_0-01.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(838, 556)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(440, 500, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.MapView = QtWebKit.QWebView(Dialog)
        self.MapView.setGeometry(QtCore.QRect(10, 40, 701, 371))

        #Absolute file path to use for now, make sure to escape backslahes
        self.MapView.setUrl(QtCore.QUrl(("tempBrowseLocal.html")))
        self.MapView.setObjectName(_fromUtf8("MapView"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridFrame = QtGui.QFrame(Dialog)
        self.gridFrame.setGeometry(QtCore.QRect(720, 40, 111, 231))
        self.gridFrame.setObjectName(_fromUtf8("gridFrame"))
        self.gridLayout = QtGui.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBox_3 = QtGui.QCheckBox(self.gridFrame)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout.addWidget(self.checkBox_3, 4, 0, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.gridFrame)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 2, 0, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.gridFrame)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout.addWidget(self.checkBox_4, 1, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.gridFrame)
        self.checkBox.setMinimumSize(QtCore.QSize(61, 41))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1)
        self.gridFrame.raise_()
        self.buttonBox.raise_()
        self.MapView.raise_()
        self.textEdit.raise_()

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Current Map</span></p></body></html>", None))
        self.checkBox_3.setText(_translate("Dialog", "State Lines", None))
        self.checkBox_2.setText(_translate("Dialog", "Bus Routes", None))
        self.checkBox_4.setText(_translate("Dialog", "Populations", None))
        self.checkBox.setText(_translate("Dialog", "Counties", None))

from PyQt4 import QtWebKit


import sys
app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
