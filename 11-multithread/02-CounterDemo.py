# lesson 89 11:17:07-11:38:15
# 首次涉及自定义信号和槽
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

sec = 0

# 工作线程
class WorkThread(QThread):
    # 自定义信号和槽（声明为自定义信号）
    timer = pyqtSignal() # 每隔一秒发送一次信号
    end = pyqtSignal() # 技术完成后发送一次信号
    def run(self):
        while True:
            self.sleep(1) # 休眠一秒
            if sec == 5:
                # 发送（调用）end信号
                self.end.emit()
                break
            self.timer.emit() # 发送timer信号(自定义信号和槽)

class ConuterDemo(QWidget):
    def __init__(self):
        super(ConuterDemo, self).__init__()
        self.setWindowTitle("ConuterDemo")
        self.resize(500, 500)
        layout = QVBoxLayout()
        self.lcdNumber = QLCDNumber()
        layout.addWidget(self.lcdNumber)
        button = QPushButton("开始计数")
        layout.addWidget(button)
        self.workThread = WorkThread()
        # 绑定自定义的信号和槽
        self.workThread.timer.connect(self.countTime)
        self.workThread.end.connect(self.end)
        button.clicked.connect(self.work)
        self.setLayout(layout)

    def countTime(self):
        # sec为全局变量，要事先声明
        global sec
        sec += 1
        self.lcdNumber.display(sec)

    def end(self):
        QMessageBox.information(self, "消息", "计数终止", QMessageBox.Ok)

    def work(self):
        self.workThread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ConuterDemo()
    main.show()
    sys.exit(app.exec_())