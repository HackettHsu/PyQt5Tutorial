# lesson 130 17:02:31-17:06:41
import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

os.chdir(sys.path[0])
class gifFileDemo(QWidget):
    def __init__(self):
        super(gifFileDemo, self).__init__()
        self.setWindowTitle("gifFileDemo")
        self.setFixedSize(200, 200)
        self.label = QLabel("", self)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie = QMovie("./images/0.gif")
        self.label.setMovie(self.movie)
        # 启动GIF
        self.movie.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = gifFileDemo()
    main.show()
    sys.exit(app.exec_())