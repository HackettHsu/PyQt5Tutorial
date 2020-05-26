'''
1. 普通按钮
2. 按钮显示图像
3. 按钮支持开关（两种状态）
'''
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButton Demo")
        self.resize(400, 300)
        # 垂直布局
        layout = QVBoxLayout()
        self.button1 = QPushButton("第1个按钮")
        # 设置文本
        self.button1.setText("First Button")
        # 复选功能实现
        self.button1.setCheckable(True)
        # 实现视觉效果上的复选（按钮状态）
        self.button1.toggle()
        self.button1.clicked.connect(lambda: self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)
        layout.addWidget(self.button1)

        self.button2 = QPushButton("图像按钮")
        self.button2.setIcon(QIcon(QPixmap(QFileInfo(__file__).absolutePath() + './images/test.ico')))
        self.button2.clicked.connect(lambda: self.whichButton(self.button2))
        layout.addWidget(self.button2)

        self.button3 = QPushButton("不可用的按钮")
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton("&MyButton")
        # 设为默认按钮。一个窗口只能有一个默认
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda: self.whichButton(self.button4))
        layout.addWidget(self.button4)
        self.setLayout(layout)
    # 实现判断是否按按钮的方法
    # 1. 用isChecked判断
    def buttonState(self):
        if self.button1.isChecked():
            print("按钮1已被选中")
        else:
            print("按钮1未被选中")
    # 2. 用槽函数，通过是否传参数来判断，如下
    # 但传的参数只能是布尔型
    # 所以要用lambda表达式来写connect，如上文首次出现connect的语句
    def whichButton(self, btn):
        print(f"被单击的按钮是<{btn.text()}>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())