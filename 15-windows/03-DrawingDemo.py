# lesson 121 11:08:21-
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DrawingDemo(QWidget):
    def __init__(self, parent = None):
        super(DrawingDemo, self).__init__()
        self.setWindowTitle("DrawingDemo")
        self.resize(500, 500)
        self.pix = QPixmap(500, 500)
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        # 画布背景色为白色
        self.pix.fill(Qt.white)

    def paintEvent(self, event):
        pp = QPainter(self.pix)
        # 根据光标前后两个位置绘制直线
        pp.drawLine(self.lastPoint, self.endPoint)
        # 让前一个坐标值等于后一个坐标值，即可实现画出连续的线
        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

    # 这个mouseXxEvent是PyQt自带的？
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # pos：获得坐标（像素点）
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            # update方法会重新调用最开始的函数
            # 会不断重复pointEvent来实现划极短的直线？
            self.update()

    # 鼠标左键释放
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # 进行重新绘制
            self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DrawingDemo()
    main.show()
    sys.exit(app.exec_())