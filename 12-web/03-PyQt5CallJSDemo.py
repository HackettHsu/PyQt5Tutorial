# lesson 93
import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

os.chdir(sys.path[0])
class FileName(QWidget):
    def __init__(self):
        super(FileName, self).__init__()
        self.setWindowTitle("FileName")
        self.resize(500, 500)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.browser = QWebEngineView()
        url = os.getcwd() + '/t2.html'
        self.browser.load(QUrl.fromLocalFile(url))
        layout.addWidget(self.browser)
        self.button = QPushButton("Update Full Name")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.PyToJS)

    def PyToJS(self):
        self.value = 'Hello World'
        # Python -> JavaScript，并利用调用函数的方法实现JavaScript -> Python
        self.browser.page().runJavaScript('fullname("' + self.value +'");', self.JSToPy)

    def JSToPy(self, result):
        print(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = FileName()
    main.show()
    sys.exit(app.exec_())