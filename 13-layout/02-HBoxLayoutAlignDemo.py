# lesson 97 15:46:04-15:54:19
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class HBoxLayoutAlignDemo(QWidget):
    def __init__(self):
        super(HBoxLayoutAlignDemo, self).__init__()
        self.setWindowTitle("HBoxLayoutDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        # 左对齐和顶对齐
        layout.addWidget(QPushButton("按钮1"), 2, Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(QPushButton("按钮2"), 2, Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(QPushButton("按钮3"), 1, Qt.AlignLeft | Qt.AlignTop)
        # 左对齐底对齐
        layout.addWidget(QPushButton("按钮4"), 2, Qt.AlignLeft | Qt.AlignBottom)
        layout.addWidget(QPushButton("按钮5"), 3, Qt.AlignRight | Qt.AlignBottom)
        # 设置控件（锁定）间距
        layout.setSpacing(40)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = HBoxLayoutAlignDemo()
    main.show()
    sys.exit(app.exec_())