from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp # 正则表达式
import sys

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLineEdit校验器")

        # 创建表单布局
        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formLayout.addRow("整数类型", intLineEdit)
        formLayout.addRow("浮点类型", doubleLineEdit)
        formLayout.addRow("字母和数字", validatorLineEdit)

        intLineEdit.setPlaceholderText("整型")
        doubleLineEdit.setPlaceholderText("浮点型")
        validatorLineEdit.setPlaceholderText("字母和数字")

        # 整数校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)

        # 浮点校验器[-360, 360] 精度：小数点后两位
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360, 360)
        # 标准表示法：正常显示浮点数
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度：小数点后两位
        doubleValidator.setDecimals(2)

        # 字符和数字
        # 先创建正则表达式
        # +$表示至少有一个字符
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置校验器（链接校验器）
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())