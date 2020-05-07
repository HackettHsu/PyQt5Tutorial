# lesson 117
# 主要使用内置信号和自定义信号
# 这个倒是没问题
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from NewDateDialog import NewDateDialog

class MultiWindow2(QWidget):
    
    def __init__(self, parent = None):
        super(MultiWindow2, self).__init__(parent)
        self.resize(500, 500)
        self.setWindowTitle("MultiWindow2")
        self.open_btn = QPushButton("获取时间")
        self.lineEdit_inner = QLineEdit(self)
        self.lineEdit_emit = QLineEdit(self)
        self.open_btn.clicked.connect(self.openDialog)
        self.lineEdit_inner.setText("接收子窗口内置信号的时间")
        self.lineEdit_emit.setText("接收子窗口自定义信号的时间")
        layout = QGridLayout()
        layout.addWidget(self.lineEdit_inner)
        layout.addWidget(self.lineEdit_emit)
        layout.addWidget(self.open_btn)
        self.setLayout(layout)

    def openDialog(self):
        dialog = NewDateDialog(self)
        # 连接子窗口的内置信号与主窗口的槽函数
        dialog.datetime_inner.dateTimeChanged.connect(self.deal_inner_slot)
        # 自定义信号的槽函数
        # 这个槽函数是在New文件中定义的
        # 子窗口数据发生变化即触发此槽函数
        # 推荐这个方法：尽量不要再一个窗口中访问另一窗口的控件（私有资源）太多
        # 而这种方法可看就只访问了另一窗口的一个自定义信号
        # 想想信号最关键的作用：与外界交互
        dialog.Signal_OneParameter.connect(self.deal_emit_slot)
        dialog.show()
    
    def deal_inner_slot(self, date):
        self.lineEdit_inner.setText(date.toString())

    def deal_emit_slot(self, dateStr):
        self.lineEdit_emit.setText(dateStr)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MultiWindow2()
    main.show()
    sys.exit(app.exec_())