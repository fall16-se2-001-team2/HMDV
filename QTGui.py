import sys

from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl

class GUI:
    app = QApplication(sys.argv)

    browser = QWebView()
    browser.load(QUrl("tempBrowseLocal.html"))
    browser.show()

    app.exec_()