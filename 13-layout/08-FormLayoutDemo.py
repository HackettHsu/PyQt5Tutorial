# lesson 103 22:15:03-
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FormLayoutDemo(QWidget):
    def __init__(self):
        super(FormLayoutDemo, self).__init__()
        self.setWindowTitle("FormLayoutDemo")
        self.resize(500, 500)
        titleLabel = QLabel("标题")
        authorLabel = QLabel("作者")
        contentLabel = QLabel("内容")
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()
        layout = QFormLayout()
        layout.addRow(titleLabel, titleEdit)
        layout.addRow(authorLabel, authorEdit)
        layout.addRow(contentLabel, contentEdit)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = FormLayoutDemo()
    main.show()
    sys.exit(app.exec_())