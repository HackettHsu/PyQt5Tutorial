# lesson 44
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QMessageBox案例")
        self.resize(300, 400)
        layout = QVBoxLayout()
        # 要加self，否则无法实现功能
        self.button1 = QPushButton(self)
        self.button1.setText("显示关于对话框")
        self.button1.clicked.connect(self.showDialog)
        layout.addWidget(self.button1)
        
        self.button2 = QPushButton(self)
        self.button2.setText("显示消息对话框")

        self.setLayout(layout)

    def showDialog(self):
        # 千万别忘记sender()这个接受信号数据的方法！
        text = self.sender().text()
        if text == "显示关于对话框":
            QMessageBox.about(self, "关于", "这是一个关于对话框")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.show()
    sys.exit(app.exec_())