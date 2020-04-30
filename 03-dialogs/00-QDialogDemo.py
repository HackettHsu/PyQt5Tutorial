# lesson 43
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QDialogDemo(QWidget):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QDialogDemo")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())