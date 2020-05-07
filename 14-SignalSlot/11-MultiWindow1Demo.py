# lesson 116 15:12:13-15:36:13 说的有问题没解决
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# 一个显示日期的对话框款模块，自创的
from DateDialog import DateDialog

class MultiWindow1Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MultiWindow1Demo")
        self.resize(500, 500)
        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton("弹出对话框1")
        self.button1.clicked.connect(self.onButton1Click)
        self.button2 = QPushButton("弹出对话框2")
        self.button2.clicked.connect(self.onButton2Click)
        layout = QGridLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def onButton1Click(self):
        dialog = DateDialog()
        result = dialog.exec()
        date = dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        # 销毁
        dialog.destroy()
    
    # 使用静态方法，不需要再访问DateDialog中的控件了
    def onButton2Click():
        date, time, result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        if result == QDialog.Accepted:
            print("请点击确认按钮")
        else:
            print("单击取消按钮")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MultiWindow1Demo()
    main.show()
    sys.exit(app.exec_())