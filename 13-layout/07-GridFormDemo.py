# lesson 102 22:08:29-22:13:48
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class GirdFormDemo(QWidget):
    def __init__(self):
        super(GirdFormDemo, self).__init__()
        self.setWindowTitle("GirdFormDemo")
        self.resize(500, 500)
        titleLabel = QLabel("标题")
        authorLabel = QLabel("作者")
        contentLabel = QLabel("内容")
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()
        layout = QGridLayout()
        # 设置默认间隔
        layout.setSpacing(10)
        layout.addWidget(titleLabel, 1, 0)
        layout.addWidget(titleEdit, 1, 1)
        layout.addWidget(authorLabel, 2, 0)
        layout.addWidget(authorEdit, 2, 1)
        layout.addWidget(contentLabel, 3, 0)
        # 单独还设置个大小，占5行1列
        layout.addWidget(contentEdit, 3, 1, 5, 1)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = GirdFormDemo()
    main.show()
    sys.exit(app.exec_())