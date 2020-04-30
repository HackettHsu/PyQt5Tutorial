# lesson 49 2020年4月30日 22:34:10-22:52:52
# 在窗口上绘制文本
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DrawTextDemo(QWidget):
    def __init__(self):
        super(DrawTextDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("DrawTextDemo")
        self.resize(500, 500)
        self.text = "DrawTextDemo测试文字"
    
    # 创建paintEvent方法
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        # 设置画笔（颜色）
        painter.setPen(QColor(150, 3, 5))
        # 设置字体
        painter.setFont(QFont("Hack", 18))
        # painter.drawText(可绘图区域, 位置, 文字内容)
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)
        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DrawTextDemo()
    main.show()
    sys.exit(app.exec_())