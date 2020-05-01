# lesson 53 2020年5月1日 21:13:35-21:24:20
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FillRectDemo(QWidget):
    def __init__(self):
        super(FillRectDemo, self).__init__()
        self.setWindowTitle("FillRectDemo")
        self.resize(300, 600)
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        # 创建画刷对象
        brush1 = QBrush(Qt.SolidPattern)
        # 设置画刷对象
        painter.setBrush(brush1)
        painter.drawRect(10, 15, 90, 60)
        # 不同的填充模式DensenX X = [1, 7]，各有效果，就是点点越来越密集
        brush2 = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush2)
        painter.drawRect(130, 15, 90, 60)
        # 横隔儿
        brush3 = QBrush(Qt.HorPattern)
        painter.setBrush(brush3)
        painter.drawRect(130, 75, 90, 60)
        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = FillRectDemo()
    main.show()
    sys.exit(app.exec_())