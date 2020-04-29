'''
单选控件
'''
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class QRadioButtonDemo(QtWidgets):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QRadioButton")
        layout = QHBoxLayout()
        self.button1 = QRadioButton("单选按钮1")
        # 默认状态
        self.button1.setChecked(True)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())