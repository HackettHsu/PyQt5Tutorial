# lesson 101 21:50:45-22:05:47
# 利用栅格布局和循环实现简单计算器UI
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CalcDemo(QWidget):
    def __init__(self):
        super(CalcDemo, self).__init__()
        self.setWindowTitle("CalcDemo")
        self.resize(500, 500)
        layout = QGridLayout()
        self.setLayout(layout)
        # 用列表定义UI文本。注意观察例子的格式。
        names = ["Cls", "Back", "", "Close",
                "7", "8", "9", "/",
                "4", "5", "6", "*",
                "1", "2", "3", "-",
                "0", ".", "=", "+"]
        # 利用循环生成坐标，填入按钮
        # 这也是一种快速生成list的方法，值得学习
        positions = [(i, j) for i in range(5) for j in range(4)]
        # 用zip函数返回一个可迭代的对象，将生成的位置和文本拼接在一起，并产生按钮
        # 注意position和name是两个新变量，同时position是元组，而addWidget不接受元组，所以需要拆开
        for position, name in zip(positions, names):
            if name == "":
                continue
            button = QPushButton(name)
            # 元组快速拆解好方法！在前面加*
            layout.addWidget(button, *position)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CalcDemo()
    main.show()
    sys.exit(app.exec_())