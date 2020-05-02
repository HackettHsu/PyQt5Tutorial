# lesson 60 2020年5月2日 21:46:19-22:10:38
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ToolbarDemo(QMainWindow):
    def __init__(self):
        super(ToolbarDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("ToolbarDemo")
        self.resize(500, 500)
        # 创建工具栏
        toolBar1 = self.addToolBar("Toolbar1")
        # 添加功能，图标不限制格式
        # QAction([图标,] （默认悬停时才显示的）名称, self)
        new = QAction(QIcon(QFileInfo(__file__).absolutePath() + \
            "./images/test.ico"), "new", self)
        toolBar1.addAction(new)
        # 调整显示状态，实现图标和提示文字同时显示。
        # 这是调整某个工具栏所有按钮
        # 一个工具栏中的显示形式是统一的
        # 默认模式ToolButtonFollowStyle，只显示图标，悬停显示文字
        # 还有只显示文字、文字和图标都显示，详见setToolButtonStyle
        toolBar1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolBar1.actionTriggered.connect(self.toolButtonPressed)

    def toolButtonPressed(self, action):
        print(f"按下的工具栏按钮是：{action.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ToolbarDemo()
    main.show()
    sys.exit(app.exec_())