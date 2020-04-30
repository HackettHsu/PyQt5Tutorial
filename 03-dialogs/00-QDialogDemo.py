# lesson 43
import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QDialog案例")
        self.resize(300, 200)

        self.button = QPushButton(self)
        self.button.setText("弹出对话框")
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)

    # 在这里写Dialog
    # 相当于一个新的 __init__
    def showDialog(self):
        dialog  = QDialog()
        # 在Dialog中放置一个新按钮
        button = QPushButton("确定", dialog)
        # dialog.close 方法 ：关闭对话框
        button.clicked.connect(dialog.close)
        button.move(50, 50)
        dialog.setWindowTitle("对话框")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())