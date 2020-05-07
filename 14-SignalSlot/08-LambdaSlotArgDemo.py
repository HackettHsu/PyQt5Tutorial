# lesson 113 22:19:38-22:33:09
from PyQt5.QtWidgets import *
import sys

class lambdaSlotArgDemo(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LambdaSlotArgDemo")
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3")
        button1.clicked.connect(lambda: self.onButtonClick(10, 20))
        button2.clicked.connect(lambda: self.onButtonClick(40, -20))
        # 甚至可以直接用lambda写槽函数
        button3.clicked.connect(lambda: QMessageBox.information(self, "Button3", "Button3 is clicked."))
        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onButtonClick(self, m, n):
        print(m + n)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = lambdaSlotArgDemo()
    main.show()
    sys.exit(app.exec_())