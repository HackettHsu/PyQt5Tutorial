# lesson 105 22:51:52-
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SignalSlotDemo(QWidget):
    def __init__(self):
        super(SignalSlotDemo, self).__init__()
        self.initUI()

    def onClick(self):
        self.btn.setText("信号已经发出")
        self.btn.setStyleSheet("QPushButton(max-width:200px;min:200px)")
        
    def initUI(self):
        self.setWindowTitle("SignalSlotDemo")
        self.resize(500, 500)
        self.btn = QPushButton("我的按钮", self)
        self.btn.clicked.connect(self.onClick)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = SignalSlotDemo()
    main.show()
    sys.exit(app.exec_())