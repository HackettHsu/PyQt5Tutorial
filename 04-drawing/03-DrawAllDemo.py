# lesson 52 2020年5月1日 20:35:54-21:12:34
# 绘制各种图形
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QDrawAllDemo(QWidget):
    def __init__(self):
        super(QDrawAllDemo, self).__init__()
        self.setWindowTitle("QDrawAllDemo")
        self.resize(600, 600)
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        # 定义一个区域QRect(起始点（左上角）坐标, 宽度，高度)
        rect = QRect(0, 10, 100, 100)
        # 绘制弧drawArc(确定一个矩形的区域（可以用rect，或者四个参数的形式）, 起始角度a（单位°）, 结束角度（单位alen）)
        # 四个参数形式为：起始x， 起始y，结束（距离起始）x，结束（距离起始）y
        # 后两个参数可以理解成区域的长和宽
        # 结束角度alen：1alen = 1/16°
        # 等于说结束角度应该是要求的角度*16
        painter.drawArc(rect, 0, 50* 16)
        # 用弧绘制圆
        painter.setPen(Qt.red)
        painter.drawArc(120, 10, 100, 100, 0, 360* 16)
        # 带弦的弧（弧的起止点有直线连接）
        # 参数类似
        painter.drawChord(0, 120, 100, 100, 12, 130*16)
        # 扇形 参数类似
        painter.drawPie(0, 240, 100, 100, 12, 130*16)
        # 椭圆 参数就只需要区域四个了
        painter.drawEllipse(120, 120, 150, 100)
        # 多边形（多个点）
        point1 = QPoint(140, 380)
        point2 = QPoint(270, 420)
        point3 = QPoint(290, 512)
        point4 = QPoint(290, 588)
        point5 = QPoint(200, 533)
        # 创建多边形对象
        polygon = QPolygon([point1, point2, point3, point4, point5])
        painter.drawPolygon(polygon)
        # 图像
        image = QImage(QFileInfo(__file__).absolutePath() + './images/罗小黑战记 电影原声带.bmp')
        rect = QRect(10, 400, image.width() / 3, image.height() / 3)
        painter.drawImage(rect, image)
        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QDrawAllDemo()
    main.show()
    sys.exit(app.exec_())