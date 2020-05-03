# lesson 78 2020年5月3日 12:32:49-12:48:36 15:08:38-15:15:37
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BasicTreeWidgetDemo(QMainWindow):
    def __init__(self, parent = None):
        super(BasicTreeWidgetDemo, self).__init__()
        self.setWindowTitle("BasicTreeWidgetDemo")
        self.resize(500, 500)
        # 创建树控件
        self.treeWidget = QTreeWidget()
        # 为树控件指定列数
        self.treeWidget.setColumnCount(2)
        # 指定列标签（名称）
        self.treeWidget.setHeaderLabels(["标签1", "标签2", "标签3"])
        # 设置列宽（列0起x, 列0终x）
        self.treeWidget.setColumnWidth(0, 200)
        # 该组树控件默认展开
        self.treeWidget.expandAll()
        # 创建（根）节点并设置信息
        root = QTreeWidgetItem(self.treeWidget)
        # (所在列序号（从0开始）, 节点名称)
        # 通过所在列序号来确定设置的是该树控件的哪个节点的哪列
        root.setText(0, "根节点")
        root.setIcon(0, QIcon(QFileInfo(__file__).absolutePath() + "./images/test.ico"))
        # 添加子节点到根节点root
        child1 = QTreeWidgetItem(root)
        child1.setText(0, "子节点1")
        # 通过列序号控制内容显示位置
        child1.setText(1, "子节点1的数据")
        child1.setIcon(0, QIcon(QFileInfo(__file__).absolutePath() + "./images/test.ico"))
        # 添加复选框
        child1.setCheckState(0, Qt.Checked)
        # 继续嵌套
        child2 = QTreeWidgetItem(child1)
        child2.setText(2, "子节点1的子节点")
        # 将树控件放在布局正中间
        self.setCentralWidget(self.treeWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = BasicTreeWidgetDemo()
    main.show()
    sys.exit(app.exec_())