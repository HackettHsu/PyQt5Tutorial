# lesson 92 
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class InnerHTMLDemo(QMainWindow):
    def __init__(self):
        super(InnerHTMLDemo, self).__init__()
        self.setWindowTitle("InnerHTMLDemo")
        self.resize(500, 500)
        self.browser = QWebEngineView()
        self.browser.setHtml('''
<!DOCTYPE html>
<html lang = "en">
    <head>
        <meta charset = "UTF-8">
        <title>TEST</title>
    </head>
    <body>
        <h1>PyQt5 QtWebEngine Test</h1>
    </body>
</html>
        ''')
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = InnerHTMLDemo()
    main.show()
    sys.exit(app.exec_())