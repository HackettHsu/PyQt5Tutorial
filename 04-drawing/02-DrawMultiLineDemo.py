# lesson 51 2020年5月1日 18:22:18-18:44:36
# 绘制不同类型的直线
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QDrawMultiLineDemo(QWidget):
    def __init__(self):
        super(QDrawMultiLineDemo, self).__init__()
        self.setWindowTitle("设置笔的样式")
        self.resize(500, 500)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        # QPen(颜色, 粗细, 线类型（默认实线）)
        pen = QPen(Qt.blue, 3, Qt.SolidLine)
        # 设置绘图时用哪支笔
        painter.setPen(pen)
        # drawLine(开始点x, 开始点y, 长度, 结束点y)
        painter.drawLine(20, 40, 250, 40)
        # 只改变线类型，这次为虚线
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)
        # -..
        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)
        # 点（窄虚线）
        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)
        # 自定义
        pen.setStyle(Qt.CustomDashLine)
        # [实线长度, 空白长度]
        pen.setDashPattern([1, 4, 5, 4])
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)
        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QDrawMultiLineDemo()
    main.show()
    sys.exit(app.exec_())