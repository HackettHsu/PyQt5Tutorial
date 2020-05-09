# lesson 134 17:54:12-18:11:02
import sys, os
from PyQt5.QtWidgets import *
from CommandHelper import CommandHelper

os.chdir(sys.path[0])
class MainWindow(QMainWindow):
    
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.resize(500, 500)
        self.setWindowTitle("LoadQSSFileDemo")
        button = QPushButton()
        button.setText("Load QSS File.")
        button.setToolTip("ToopTip Text")
        layout = QVBoxLayout()
        layout.addWidget(button)
        button.clicked.connect(self.onClick)
        widget = QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(layout)

    def onClick(self):
        styleFile = "./style.qss"
        qssStyle = CommandHelper.readQSS(styleFile)
        win.setStyleSheet(qssStyle)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())