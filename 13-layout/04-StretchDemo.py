# lesson 99 15:58:29-16:08:00
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class StretchDemo(QWidget):
    def __init__(self):
        super(StretchDemo, self).__init__()
        self.setWindowTitle("StretchDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        button1 = QPushButton(self)
        button2 = QPushButton(self)
        button3 = QPushButton(self)
        button1.setText("按钮1")
        button2.setText("按钮2")
        button3.setText("按钮3")
        # addWidget会搜索addStretch来确定间距
        # 搜索addStretch值是搜索上文最近者
        layout.addStretch(1)
        layout.addWidget(button1)
        layout.addStretch(0)
        layout.addWidget(button2)
        layout.addStretch(2)
        layout.addWidget(button3)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = StretchDemo()
    main.show()
    sys.exit(app.exec_())