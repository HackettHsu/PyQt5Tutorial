# lesson 114 22:44:52-22:49:31
from PyQt5.QtWidgets import *
import sys 
from functools import partial
class PartialSlotArgDemo(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LambdaSlotArgDemo")
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        x = 5
        y = 105
        # partial(self.要传入的参数, arg1, arg2)
        button1.clicked.connect(partial(self.onButtonClick, 10, 20))
        button2.clicked.connect(partial(self.onButtonClick, x, y))
        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onButtonClick(self, m, n):
        print(m + n)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = PartialSlotArgDemo()
    main.show()
    sys.exit(app.exec_())