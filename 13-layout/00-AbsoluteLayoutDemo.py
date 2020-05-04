# lesson 95 15:17:09-15:19:40
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class AbsoluteLayoutDemo(QWidget):
    def __init__(self):
        super(AbsoluteLayoutDemo, self).__init__()
        self.setWindowTitle("AbsoluteLayoutDemo")
        self.resize(500, 500)
        self.label1 = QLabel("Welcome", self)
        self.label1.move(15, 20)
        self.label2 = QLabel("Study", self)
        self.label2.move(65, 70)
        self.label3 = QLabel("PyQt5", self)
        self.label3.move(115, 120)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = AbsoluteLayoutDemo()
    main.show()
    sys.exit(app.exec_())