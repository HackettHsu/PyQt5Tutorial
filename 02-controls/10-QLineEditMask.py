'''
QLineEdit使用掩码功能
'''
from PyQt5.QtWidgets import *
import sys

class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("用掩码限制QLineEdit控件的输入")
        formLayout = QFormLayout()

        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenceLineEdit = QLineEdit()

        # 下面输入ip，“.”是直接显示的，“:_”表示没有输入时直接显示下划线
        # 0：数字非必须
        ipLineEdit.setInputMask("000.000.000.000;_")
        # H：十六进制且必须
        macLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        dateLineEdit.setInputMask("0000-00-00")
        # A：字母且必须；>：必须（自动转换为）大写
        # 用#表示没有输入的空间
        licenceLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        formLayout.addRow("数字掩码", ipLineEdit)
        formLayout.addRow("Mac掩码", macLineEdit)
        formLayout.addRow("日期掩码", dateLineEdit)
        formLayout.addRow("序列号掩码", licenceLineEdit)

        self.setLayout(formLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLineEditMask()
    main.show()
    sys.exit(app.exec_())