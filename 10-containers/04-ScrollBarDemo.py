# lesson 86 2020年5月3日 20:53:30-21:14:01
# 1. 用三个滚动条控件控制文字颜色变化
# 2. 用一个滚动条控件控制控件位置变化
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ScrollBarDemo(QWidget):
    def __init__(self):
        super(ScrollBarDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("ScrollBarDemo")
        self.setGeometry(200, 200, 500, 500)
        layout = QHBoxLayout()
        self.label1 = QLabel("拖动滚动条改变文本颜色")
        layout.addWidget(self.label1)
        # 创建三个滚动条控件，颜色[0,255]
        self.scrollBar1 = QScrollBar()
        self.scrollBar1.setMaximum(255)
        self.scrollBar1.sliderMoved.connect(self.sliderMoved1)
        self.scrollBar2 = QScrollBar()
        self.scrollBar2.setMaximum(255)
        self.scrollBar2.sliderMoved.connect(self.sliderMoved1)
        self.scrollBar3 = QScrollBar()
        self.scrollBar3.setMaximum(255)
        self.scrollBar3.sliderMoved.connect(self.sliderMoved1)
        self.scrollBar4 = QScrollBar()
        self.scrollBar4.sliderMoved.connect(self.sliderMoved2)
        layout.addWidget(self.scrollBar1)
        layout.addWidget(self.scrollBar2)
        layout.addWidget(self.scrollBar3)
        layout.addWidget(self.scrollBar4)
        self.setLayout(layout)
        # 保存当前layout坐标(?)
        self.y = self.label1.pos().y()

    def sliderMoved1(self):
        print(self.scrollBar1.value(), self.scrollBar2.value(), self.scrollBar3.value())
        # 实现调色板功能
        palette = QPalette()
        color = QColor(self.scrollBar1.value(), self.scrollBar2.value(), self.scrollBar3.value(), 255)
        palette.setColor(QPalette.Foreground, color)
        self.label1.setPalette(palette)

    # 实现移动位置功能
    def sliderMoved2(self):
        self.label1.move(self.label1.x(), self.y + self.scrollBar4.value())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ScrollBarDemo()
    main.show()
    sys.exit(app.exec_())