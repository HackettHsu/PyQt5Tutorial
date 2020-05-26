# lesson 80 2020年5月26日 16:41:37-17:08:17
import sys
from PyQt5.QtWidgets import *

class ModifyTreeDemo(QWidget):
    def __init__(self):
        super(ModifyTreeDemo, self).__init__()
        self.setWindowTitle("ModifyTreeDemo")
        self.resize(500, 500)
        operatorLayout = QHBoxLayout()
        self.addButton = QPushButton("ADD")
        self.updateButton = QPushButton("UPDATE")
        self.deleteButton = QPushButton("DELETE")
        operatorLayout.addWidget(self.addButton)
        operatorLayout.addWidget(self.updateButton)
        operatorLayout.addWidget(self.deleteButton)
        self.addButton.clicked.connect(self.addNode)
        self.updateButton.clicked.connect(self.updateNode)
        self.deleteButton.clicked.connect(self.deleteNode)
        self.treeWidget = QTreeWidget()
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setHeaderLabels(['Key', 'Value'])
        self.root = QTreeWidgetItem(self.treeWidget)
        self.root.setText(0, 'root')
        self.root.setText(1, '0')
        self.child1 = QTreeWidgetItem(self.root)
        self.child1.setText(0, 'child1')
        self.child1.setText(1, '1')
        self.child2 = QTreeWidgetItem(self.root)
        self.child2.setText(0, 'child2')
        self.child2.setText(1, '2')
        self.child3 = QTreeWidgetItem(self.child2)
        self.child3.setText(0, 'child3')
        self.child3.setText(1, '3')
        self.treeWidget.clicked.connect(self.onTreeClicked)
        mainLayout = QVBoxLayout()
        # 当需要多个layout嵌套时，子layout不能有(self)，父layout无所谓
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.treeWidget)
        self.setLayout(mainLayout)

    def onTreeClicked(self, index):
        self.item = self.treeWidget.currentItem()
        print(index.row())
        print(f'key: {self.item.text(0)}, value: {self.item.text(1)}')

    # 相当于动态的创建QTreeWidgetItem对象
    def addNode(self):
        print("Add root.")
        # 先获取当前节点
        item = self.treeWidget.currentItem()
        print(f"Current root: {item}")
        node = QTreeWidgetItem(item)
        node.setText(0, 'New Root.')
        node.setText(1, 'New Value.')

    def updateNode(self):
        print("Update root.")
        item = self.treeWidget.currentItem()
        item.setText(0, 'Update root.')
        item.setText(1, 'Value has been updated.')

    def deleteNode(self):
        print("Delete root.")
        item = self.treeWidget.currentItem()
        # 获取根节点的父节点（默认是不会获取的）
        root = self.treeWidget.invisibleRootItem()
        # 多选、含有子节点情况
        for item in self.treeWidget.selectedItems():
            # 或(or)语法
            (item.parent() or root).removeChild(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ModifyTreeDemo()
    main.show()
    sys.exit(app.exec_())