# 为 lesson 116 制作的一个自创模块
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# 显示一个日历对话框
class DateDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("DateDialog")
        layout = QVBoxLayout()
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime)
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        # 连接到Ok按钮
        buttons.accepted.connect(self.accept)
        # 连接到Cancel按钮
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        self.setLayout(layout)

    def dateTime(self):
        return self.datetime.dateTime()

    # 用静态方法获取对话框
    @staticmethod
    def getDateTime(parent = None):
        dialog = DateDialog(parent)
        result = dialog.exec()
        date = dialog.dateTime()
        return (date.date(), date.time(), result == QDialog.Accepted)