# lesson 59 2020年5月2日 21:23:50-21:46:27
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# QMainWindow方法中才有menubar
class MenuDemo(QMainWindow):
    def __init__(self):
        super(MenuDemo, self).__init__()
        self.setWindowTitle("MenuDemo")
        self.resize(500, 500)
        # 创建菜单栏
        bar = self.menuBar()
        # 为菜单栏添加内容,默认先创建的在上面
        file = bar.addMenu("文件")
        # 为“文件”菜单栏添加“新建”按钮
        file.addAction("新建")
        # 创建“保存”按钮
        save = QAction("保存", self)
        # 为“保存”按钮创建快捷键
        save.setShortcut("Ctrl + S")
        # 真正实现功能还是要借助信号和槽
        save.triggered.connect(self.process)
        # 将“保存”按钮添加进“文件”
        file.addAction(save)
        # 在“文件”中添加有子菜单的“Edit”按钮
        edit = file.addMenu("Edit")
        # 为“Edit”添加按钮
        edit.addAction("copy")
        edit.addAction("paste")
        quit = QAction("Quit", self)
        file.addAction(quit)

    def process(self):
        print(self.sender().text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MenuDemo()
    main.show()
    sys.exit(app.exec_())