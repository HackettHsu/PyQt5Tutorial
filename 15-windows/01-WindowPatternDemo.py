# lesson 119 10:14:05-10:23:16
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class WindowPatternDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WindowPatternDemo")
        self.resize(500, 500)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # 设置窗口名字
        self.setObjectName("MainWindow")
        # Qt样式语言，借鉴了很多css
        # 不知为何总要绝对路径
        self.setStyleSheet("#MainWindow{border-image:url(d:/Users/Hackett Hsu/Documents/Study-And-Work/Coding/Python/Study/PyQt5Tutorial/15-windows/images/罗小黑战记 电影原声带.bmp);}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WindowPatternDemo()
    main.show()
    sys.exit(app.exec_())