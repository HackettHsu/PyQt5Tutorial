# lesson 126-2-2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, os

os.chdir(sys.path[0])
app = QApplication(sys.argv)
window = QMainWindow()
palette = QPalette()
# 设置笔刷
palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/罗小黑战记 电影原声带.bmp")))
window.setPalette(palette)
window.show()
sys.exit(app.exec_())