# lesson 110 16:42:49-16:50:01
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class WinSignalDemo(QWidget):
    button_clicked_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WinSignalDemo")
        self.resize(500, 500)
        button = QPushButton("关闭窗口", self)
        self.button_clicked_signal.connect(self.buttonClose)
        button.clicked.connect(self.buttonCilcked)

    # 按下按钮触发emit()方法来调用关联的信号
    def buttonCilcked(self):
        self.button_clicked_signal.emit()
    
    def buttonClose(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WinSignalDemo()
    main.show()
    sys.exit(app.exec_())