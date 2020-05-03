# lesson 84 2020年5月3日 17:44:14-
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DockWidgetDemo(QMainWindow):
    def __init__(self):
        super(DockWidgetDemo, self).__init__()
        self.setWindowTitle("DockWidgetDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        # 创建停靠控件
        self.item = QDockWidget("Dockable", self)
        self.list = QListWidget()
        self.list.addItems(["Item1", "Item2", "Item3"])
        # 将列表放入停靠控件
        self.item.setWidget(self.list)
        # 一个正常的控件
        self.setCentralWidget(QLineEdit())
        # 设置是否默认悬浮
        self.item.setFloating(True)
        # 将item设置为停靠控件并默认放置在窗口右侧
        self.addDockWidget(Qt.RightDockWidgetArea, self.item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DockWidgetDemo()
    main.show()
    sys.exit(app.exec_())