# lesson 98 15:55:20-15:56:49
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class VBoxLayoutDemo(QWidget):
    def __init__(self):
        super(VBoxLayoutDemo, self).__init__()
        self.setWindowTitle("VBoxLayoutDemo")
        self.resize(500, 500)
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("按钮1"))
        layout.addWidget(QPushButton("按钮2"))
        layout.addWidget(QPushButton("按钮3"))
        layout.addWidget(QPushButton("按钮4"))
        layout.addWidget(QPushButton("按钮5"))
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = VBoxLayoutDemo()
    main.show()
    sys.exit(app.exec_())