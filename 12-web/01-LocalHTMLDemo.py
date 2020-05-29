# lesson 91
import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

os.chdir(sys.path[0])
class LocalHTMLDemo(QMainWindow):
    def __init__(self):
        super(LocalHTMLDemo, self).__init__()
        self.setWindowTitle("LocalHTMLDemo")
        self.resize(500, 500)
        url = os.getcwd() + '/index.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = LocalHTMLDemo()
    main.show()
    sys.exit(app.exec_())