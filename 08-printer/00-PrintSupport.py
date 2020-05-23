# lesson 62 2020年5月23日 17:03:12-17:25:01
import sys
from PyQt5 import QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtWidgets import *

class PrintSupportDemo(QWidget):
    def __init__(self):
        super(PrintSupportDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("PrintSupportDemo")
        self.setGeometry(500, 200, 300, 300)
        self.button = QPushButton("打印QTextEdit控件中的内容", self)
        self.button.setGeometry(20, 20, 260, 30)
        self.editor = QTextEdit("...", self)
        self.editor.setGeometry(20, 60, 260, 200)
        self.button.clicked.connect(self.print)

    def print(self):
        # 打印机
        printer = QtPrintSupport.QPrinter()
        # 打印画布
        painter = QtGui.QPainter()
        # 将绘制目标重定向到打印机
        painter.begin(printer)
        screen = self.editor.grab()
        painter.drawPixmap(10, 10, screen)
        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = PrintSupportDemo()
    main.show()
    sys.exit(app.exec_())