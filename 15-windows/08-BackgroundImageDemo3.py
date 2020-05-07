# lesson 126-3-1
import sys, os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

os.chdir(sys.path[0])

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("BackgroundImageDemo3")

    # 直接event也成
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("./images/罗小黑战记 电影原声带.bmp")
        painter.drawPixmap(self.rect(), pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Winform()
    window.show()
    sys.exit(app.exec_())