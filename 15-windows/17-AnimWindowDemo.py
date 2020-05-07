# lesson 135 18:21:59-18:33:44
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class AnimWindowDemo(QWidget):
    def __init__(self):
        super(AnimWindowDemo, self).__init__()
        self.setWindowTitle("AnimWindowDemo")
        self.OrigHeight = 50
        self.ChangeHeight = 150
        self.setGeometry(QRect(500, 400, 150, self.OrigHeight))
        self.button = QPushButton("展开", self)
        self.button.setGeometry(10, 10, 60, 35)
        self.button.clicked.connect(self.change)

    def change(self):
        currentHeight = self.height()
        if self.OrigHeight == currentHeight:
            startHeight = self.OrigHeight
            endHeight = self.ChangeHeight
            self.button.setText("收缩")
        else:
            startHeight = self.ChangeHeight
            endHeight = self.OrigHeight
            self.button.setText("展开")
        # 变化的动画
        self.animation = QPropertyAnimation(self, b'geometry')
        # 每500ms改变一次值(设置动画执行时长)
        self.animation.setDuration(500)
        # 设置开始值
        self.animation.setStartValue(QRect(500, 400, 150, startHeight))
        self.animation.setEndValue(QRect(500, 400, 150, endHeight))
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = AnimWindowDemo()
    main.show()
    sys.exit(app.exec_())