# lesson 126-1-2 
import sys,os
from PyQt5.QtWidgets import *

# 解决Windows环境下VsCode设置相对路径失败的方法
os.chdir(sys.path[0])
app = QApplication(sys.argv)
window = QMainWindow()
window.setObjectName("MainWindow")
window.setStyleSheet("#MainWindow{border-image:url(images/罗小黑战记 电影原声带.bmp)}")
window.showMaximized()
sys.exit(app.exec_())