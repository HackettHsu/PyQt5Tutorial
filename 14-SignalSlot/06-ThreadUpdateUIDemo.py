# lesson 111 18:15:08-18:30:24
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, time

class backendThread(QThread):
    update_date = pyqtSignal(str)
    
    # 创建运行线程池（主线程？）
    def run(self):
        while True:
            date = QDateTime.currentDateTime()
            currentTime = date.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currentTime))
            time.sleep(1)

class threadUpdateUI(QDialog):
    
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("ThreadUpateUIDemo")
        self.resize(500, 500)
        self.input = QLineEdit(self)
        self.input.resize(500, 500)
        self.initUI()

    def initUI(self):
        self.backend = backendThread()
        self.backend.update_date.connect(self.handleDisplay)
        # 启动线程
        self.backend.start()

    def handleDisplay(self, data):
        self.input.setText(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = threadUpdateUI()
    main.show()
    sys.exit(app.exec_())