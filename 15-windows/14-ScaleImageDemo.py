# lesson 132 17:43:04-17:47:47
import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

os.chdir(sys.path[0])
class ScaleImgaeDemo(QWidget):
    def __init__(self):
        super(ScaleImgaeDemo, self).__init__()
        self.setWindowTitle("ScaleImgaeDemo")
        self.resize(500, 500)
        img = QImage("./images/喵塔利亚.png")
        label1 = QLabel()
        label1.setFixedHeight(500)
        label1.setFixedWidth(500)
        # 宽，高，忽略比例，平滑缩放
        result = img.scaled(label1.width(), label1.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        label1.setPixmap(QPixmap.fromImage(result))
        layout = QVBoxLayout()
        layout.addWidget(label1)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ScaleImgaeDemo()
    main.show()
    sys.exit(app.exec_())