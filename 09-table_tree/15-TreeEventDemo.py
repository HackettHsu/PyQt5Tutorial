# lesson 79 2020年5月26日 16:30:29-16:41:13
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TreeEventDemo(QMainWindow):
    def __init__(self):
        super(TreeEventDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("TreeEventDemo")
        self.resize(500, 500)
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
        self.setCentralWidget(self.treeWidget)
        self.treeWidget.clicked.connect(self.onTreeClicked)

    def onTreeClicked(self, index):
        self.item = self.treeWidget.currentItem()
        print(index.row())
        print(f'key: {self.item.text(0)}, value: {self.item.text(1)}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TreeEventDemo()
    main.show()
    sys.exit(app.exec_())