# lesson 112 18:31:15-18:33:06 22:07:20-22:18:42
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys

class AutoSignalSlotDemo(QWidget):
    
    def __init__(self):
        super(AutoSignalSlotDemo, self).__init__()
        self.okButton = QPushButton("ok", self)
        # 给按钮取个名字
        self.okButton.setObjectName("okButton")
        self.cancelButton = QPushButton("cancel")
        self.cancelButton.setObjectName("cancelButton")
        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        layout.addWidget(self.cancelButton)
        self.setLayout(layout)
        # 调用方法实现自动绑定
        QtCore.QMetaObject.connectSlotsByName(self)

    # 自动连接信号和槽开始
    # 将槽函数标注为槽
    # 函数命名规则为 on_发送者对象名称_发送信号（行为）名称(self, arg)
    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print("点击了ok按钮")

    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print("点击了cancel按钮")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = AutoSignalSlotDemo()
    main.show()
    sys.exit(app.exec_())