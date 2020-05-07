# lesson 120 10:25:53-10:38:02
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class WindowMaxMinDemo(QWidget):
    def __init__(self):
        super(WindowMaxMinDemo, self).__init__()
        self.setWindowTitle("WindowMaxMinDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        maxButton1 = QPushButton("设置窗口最大化：方法1")
        maxButton1.clicked.connect(self.maximized1)
        layout.addWidget(maxButton1)
        maxButton2 = QPushButton("设置窗口最大化：方法2")
        # 信号链接到PyQt自带的最大化方法
        maxButton2.clicked.connect(self.showMaximized)
        layout.addWidget(maxButton2)
        minButton = QPushButton("设置窗口最小化")
        minButton.clicked.connect(self.showMinimized)
        layout.addWidget(minButton)
        self.setLayout(layout)
    
    # 最大化（全屏）最小化方法1:修改窗口尺寸
    def maximized1(self):
        # 先获得可用尺寸
        desktop = QApplication.desktop()
        rect = desktop.availableGeometry()
        self.setGeometry(rect)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WindowMaxMinDemo()
    main.show()
    sys.exit(app.exec_())