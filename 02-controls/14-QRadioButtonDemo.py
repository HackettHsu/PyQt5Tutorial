'''
单选控件
'''
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QRadioButton")
        layout = QHBoxLayout()
        self.button1 = QRadioButton("单选按钮1")
        # 默认状态，True为默认勾选
        self.button1.setChecked(True)
        # toggled：状态
        self.button1.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)
        self.button2 = QRadioButton("单选按钮2")
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def buttonState(self):
        # 用sender接收信号函数传来的数据
        radioButton = self.sender()
        if radioButton.isChecked() is True:
            print(f"< {radioButton.text()} > 被选中")
        else:
            print(f"< {radioButton.text()} > 被取消选中状态")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())