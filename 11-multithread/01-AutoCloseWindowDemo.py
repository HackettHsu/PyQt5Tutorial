# lesson 88 11:05:23-11:16:24
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("<font color = red size = 140><b>五秒后自动关闭</b></font>")
    # 隐藏窗口标题栏等
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()
    QTimer.singleShot(5000, app.quit)
    sys.exit(app.exec_())