# lesson 50 2020年5月1日 17:39:46-18:04:04
# 用像素点绘制正弦曲线
# 范围：两个周期[-2π, 2π] 方法：drawPoint(x, y)

# math用来求值
import sys, math
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QDrawPointDemo(QWidget):
    def __init__(self):
        super(QDrawPointDemo, self).__init__()
        self.setWindowTitle("QDrawPointDemo")
        self.resize(500, 500)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        # 获得窗口尺寸
        size = self.size()
        # 图像精细度1000
        for i in range(0, 999):
            # 相当于-2π，具体之后解释。size.width()画面宽度
            # 具体数学问题可以自己思考，设计自己的计算式
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50)+ size.height() / 2.0
            # painter.drawPoint(点的坐标轴)
            painter.drawPoint(x, y)
        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QDrawPointDemo()
    main.show()
    sys.exit(app.exec_())