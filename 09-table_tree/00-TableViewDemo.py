# lesson 64 2020年5月24日 20:33:01-20:43:38
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TableViewDemo(QWidget):
    def __init__(self):
        super(TableViewDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("TableViewDemo")
        self.resize(500, 500)
        # 先设置Model
        self.model = QStandardItemModel(4, 3)
        # 设置行标题
        self.model.setHorizontalHeaderLabels(['id', 'name', 'age'])
        self.tableView = QTableView(self)
        # 关联控件和数据模型
        self.tableView.setModel(self.model)
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)
        # 添加数据（按列）
        self.item1 = QStandardItem('00')
        self.item2 = QStandardItem('HackettHsu')
        self.item3 = QStandardItem('22')
        self.model.setItem(0, 0, self.item1)
        self.model.setItem(0, 1, self.item2)
        self.model.setItem(0, 2, self.item3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TableViewDemo()
    main.show()
    sys.exit(app.exec_())