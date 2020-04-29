'''
纯代码实现QLabel控件伙伴功能
注意：伙伴功能（热键）似乎只有Windows支持
'''
from PyQt5.QtWidgets import *
import sys

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("QLabel与伙伴控件")

        nameLabel = QLabel("&Name:", self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴控件
        # 伙伴控件直接利用&后的第一个字母
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel("&Password:", self)
        passwordLinEdit = QLineEdit(self)
        # 设置伙伴控件
        passwordLabel.setBuddy(passwordLinEdit)

        btnOK = QPushButton("&OK")
        btnCancel = QPushButton("&Cancel")

        # 栅格布局
        # 栅格布局名.addWidget(控件对象名， 行索引rowIndex, columnIndex, 占用行row， 占用列column)
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)
        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLinEdit, 1, 1, 1, 2)
        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())