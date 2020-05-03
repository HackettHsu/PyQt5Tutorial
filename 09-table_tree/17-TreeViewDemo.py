# lesson 81 2020年5月3日 16:14:12-16:39:41
# 本次演示要实现类似于列表显示磁盘文件的功能
# 用到了QDirModel控件来帮助实现
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # QDirModel已被QFileSystemModel淘汰
    # 相比于QDirModel，QFileSystemModel需要单独添加layout
    model = QDirModel()
    tree = QTreeView()
    tree.setModel(model)
    tree.setWindowTitle("TreeViewDemo")
    tree.resize(600, 600)
    tree.show()
    sys.exit(app.exec_())