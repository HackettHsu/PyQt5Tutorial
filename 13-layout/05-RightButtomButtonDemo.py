# lesson 100 16:10:56-未记录结束时间
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class RightButtomButtonDemo(QWidget):
    def __init__(self):
        super(RightButtomButtonDemo, self).__init__()
        self.setWindowTitle("RightButtomButtonDemo")
        self.resize(500, 500)
        layout1 = QHBoxLayout()
        okButton = QPushButton("确定")
        cancelButton = QPushButton("取消")
        layout1.addStretch(1)
        layout1.addWidget(okButton)
        layout1.addWidget(cancelButton)
        layout2 = QVBoxLayout()
        layout2.addStretch(0)
        layout2.addWidget(QPushButton("按钮1"))
        layout2.addWidget(QPushButton("按钮2"))
        layout2.addWidget(QPushButton("按钮3"))
        layout2.addStretch(1)
        # 布局套布局
        layout2.addLayout(layout1)
        self.setLayout(layout2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = RightButtomButtonDemo()
    main.show()
    sys.exit(app.exec_())