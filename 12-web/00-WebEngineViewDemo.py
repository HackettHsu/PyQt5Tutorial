# lesson 90 2020年5月27日 22:57:48 完成
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class WebEngineViewDemo(QMainWindow):
    def __init__(self):
        super(WebEngineViewDemo, self).__init__()
        self.setWindowTitle("WebEngineViewDemo")
        self.resize(500, 500)
        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://hacketthsu.github.io/'))
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WebEngineViewDemo()
    main.show()
    sys.exit(app.exec_())