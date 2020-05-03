# lesson 82 2020年5月3日 16:52:44-17:05:57 17:20:29-
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TabWidgetDemo(QTabWidget):
    def __init__(self):
        super(TabWidgetDemo, self).__init__()
        self.setWindowTitle("TabWidgetDemo")
        self.resize(500, 500)
        # 创建三个页面用于绑定选项卡
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        # 绑定选项卡
        self.addTab(self.tab1, "选项卡1")
        self.addTab(self.tab2, "选项卡2")
        self.addTab(self.tab3, "选项卡3")

        self.tab1UI()
    
    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        # 改变选项卡名称
        self.setTabText(0, "联系方式")
        # 绑定设计的UI和对应选项卡
        self.tab1.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TabWidgetDemo()
    main.show()
    sys.exit(app.exec_())