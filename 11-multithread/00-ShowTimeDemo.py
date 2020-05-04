# lesson 87 动态显示当前时间 22:32:22-忘记登记时间了
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ShowTimeDemo(QWidget):
    def __init__(self):
        super(ShowTimeDemo, self).__init__()
        self.setWindowTitle("ShowTimeDemo")
        self.resize(200, 100)
        self.label = QLabel("显示当前时间")
        self.startButton = QPushButton("开始")
        self.endButton = QPushButton("停止")
        layout = QGridLayout()
        self.timer = QTimer()
        # timeout：一种信号，根据时间，每x秒发送一次信号
        self.timer.timeout.connect(self.showTime)
        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startButton, 1, 0)
        layout.addWidget(self.endButton, 1, 1)
        self.startButton.clicked.connect(self.startTimer)
        self.endButton.clicked.connect(self.endTimer)
        self.setLayout(layout)
    
    def showTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label.setText(timeDisplay)

    def startTimer(self):
        # 开始显示时间，参数指定时间间隔1000ms
        # start：QTimer方法
        self.timer.start(1000)
        # 开始后开始按钮失效
        self.startButton.setEnabled(False)
        self.endButton.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startButton.setEnabled(True)
        self.endButton.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ShowTimeDemo()
    main.show()
    sys.exit(app.exec_())