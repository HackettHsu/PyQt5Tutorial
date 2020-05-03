# lesson 83 2020年5月3日 17:23:49-17:41:18
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class StackedWidgetDemo(QWidget):
    def __init__(self):
        super(StackedWidgetDemo, self).__init__()
        self.setWindowTitle("StackedWidgetDemo")
        self.resize(500, 500)
        self.list = QListWidget()
        self.list.insertItems(3, ["联系方式", "个人信息", "教育程度"])
        # 创建用于绑定的堆栈
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stackUI1()
        self.stackUI2()
        # 创建堆栈窗口对象
        self.stack = QStackedWidget()
        # 将堆栈窗口对象添加到列表中
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        layout = QHBoxLayout()
        layout.addWidget(self.list)
        layout.addWidget(self.stack)
        self.setLayout(layout)
        # 为堆栈绑定UI页面，通过绑定列表变化操作
        self.list.currentRowChanged.connect(self.display)

    def stackUI1(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.stack1.setLayout(layout)
    
    def stackUI2(self):
        layout = QFormLayout()
        layout.addRow("测试", QLineEdit())
        self.stack2.setLayout(layout)

    # 通过索引控制切换
    def display(self, index):
        self.stack.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = StackedWidgetDemo()
    main.show()
    sys.exit(app.exec_())