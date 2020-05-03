# lesson 85 2020年5月3日 17:54:48
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MultiWindowDemo(QMainWindow):
    # 统计当前已打开文件数量
    count = 0

    def __init__(self):
        super(MultiWindowDemo, self).__init__()
        self.setWindowTitle("MultiWindowDemo")
        self.resize(500, 500)
        # 创建一个能容纳多文件的控件区域
        self.mdi = QMdiArea()
        # 将控件加入主窗口
        self.setCentralWidget(self.mdi)
        # 一个能创建新文件的菜单栏按钮
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        # 设置多窗口显示方式。Cascade：层叠；Tiled：平铺
        file.addAction("Cascade")
        file.addAction("Tiled")
        file.triggered.connect(self.windowAction)

    def windowAction(self, action):
        if action.text() == "New":
            # 先计算总共有多少个打开的文件
            MultiWindowDemo.count += 1
            # 创建一个子窗口（文件）
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("New File" + str(MultiWindowDemo.count))
            # 将子窗口添加到主窗口
            self.mdi.addSubWindow(sub)
            sub.show()
        elif action.text() == "Cascade":
            self.mdi.cascadeSubWindows()
        elif action.text() == "Tiled":
            self.mdi.tileSubWindows()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MultiWindowDemo()
    main.show()
    sys.exit(app.exec_())