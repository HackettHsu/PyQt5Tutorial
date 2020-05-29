# lesson 94
# 按视频来还是出问题
# 最后发现是少了MySharedObject.py
# 但MySharedObject.py中又不包含QWebChannel……
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MySharedObject  import MySharedObject
from PyQt5.QtWebChannel import  QWebChannel
from factorial import *
import sys, os

# 创建传输到JavaScript的对象
channel = QWebChannel()
factorial = Factorial()
os.chdir(sys.path[0])
class PyFactorialDemo(QWidget):
    def __init__(self):
        super(PyFactorialDemo, self).__init__()
        self.setWindowTitle("PyFactorialDemo")
        self.resize(500, 500)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(os.getcwd() + './t3.html'))
        self.layout.addWidget(self.browser)
        channel.registerObject("obj", factorial)
        self.browser.page().setWebChannel(channel)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = PyFactorialDemo()
    main.show()
    sys.exit(app.exec_())