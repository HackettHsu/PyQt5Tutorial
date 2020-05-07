# lesson 127 16:51:44-16:58:18
# 成不了，不知道是不是图片的问题
import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

os.chdir(sys.path[0])
class AbnormityWindowDemo(QWidget):
    def __init__(self):
        super(AbnormityWindowDemo, self).__init__()
        self.setWindowTitle("AbnormityWindowDemo")
        self.pix = QBitmap('./images/喵塔利亚.png')
        self.resize(self.pix.size())
        self.setMask(self.pix)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), QPixmap("./images/dropdown.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = AbnormityWindowDemo()
    main.show()
    sys.exit(app.exec_())