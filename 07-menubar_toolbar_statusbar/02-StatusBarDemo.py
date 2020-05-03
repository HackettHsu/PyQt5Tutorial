# lesson 61 2020年5月3日 12:10:22-12:18:54
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class StatusBarDemo(QMainWindow):
    def __init__(self):
        super(StatusBarDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("StatusBarDemo")
        self.resize(500, 500)
        menuBar = self.menuBar()
        file = menuBar.addMenu("File")
        file.addAction("Show")
        file.triggered.connect(self.processTrigger)
        # 在正中间加个输入控件
        self.setCentralWidget(QTextEdit())
        # 创建状态栏
        self.statusBar = QStatusBar()
        # 设置状态栏
        self.setStatusBar(self.statusBar)

    def processTrigger(self, action):
        if action.text() == "Show":
            # 5000参数：显示5000毫秒后自动关闭
            self.statusBar.showMessage(action.text() + "菜单被点击了", 5000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = StatusBarDemo()
    main.show()
    sys.exit(app.exec_())