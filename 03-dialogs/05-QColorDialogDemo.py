# lessson 47 2020年4月30日 19:43:16-20:17:35
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QColorDialogDemo")
        layout = QVBoxLayout()
        self.colorButton1 = QPushButton("设置文字颜色")
        self.colorButton1.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton1)

        self.colorButton2 = QPushButton("设置文字的背景颜色")
        self.colorButton2.clicked.connect(self.getBackgroundColor)
        layout.addWidget(self.colorButton2)

        self.colorLabel1 = QLabel("Hello, 测试颜色会话")
        layout.addWidget(self.colorLabel1)

        self.setLayout(layout)

    def getColor(self):
        # getColor只有一个返回值，不再有ok
        # 这好像是弹出调色板的方法
        color= QColorDialog.getColor()
        # 控制文字颜色
        p = QPalette()
        # 设置窗口文字颜色为color 注意Window大写
        p.setColor(QPalette.WindowText, color)
        self.colorLabel1.setPalette(p)

    def getBackgroundColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)
        # 设置自动填充背景色
        self.colorLabel1.setAutoFillBackground(True)
        self.colorLabel1.setPalette(p)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())