# lesson 96 15:29:31-15:34:04
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class HBoxLayoutDemo(QWidget):
    def __init__(self):
        super(HBoxLayoutDemo, self).__init__()
        self.setWindowTitle("HBoxLayoutDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        layout.addWidget(QPushButton("按钮1"))
        layout.addWidget(QPushButton("按钮2"))
        layout.addWidget(QPushButton("按钮3"))
        layout.addWidget(QPushButton("按钮4"))
        layout.addWidget(QPushButton("按钮5"))
        # 设置控件（锁定）间距
        layout.setSpacing(40)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = HBoxLayoutDemo()
    main.show()
    sys.exit(app.exec_())