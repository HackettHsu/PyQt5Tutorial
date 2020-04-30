# lesson 44
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QMessageBoxDemo(QMainWindow
):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QMessageBox案例")
        self.resize(300, 400)
        layout = QVBoxLayout()
        self.button1 = QPushButton(self)
        self.button1.setText("显示关于对话框")
        self.button1.clicked.connect(self.showDialog)
        self.setLayout(layout)

    def 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.show()
    sys.exit(app.exec_())