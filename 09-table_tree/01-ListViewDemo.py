# lesson 65 2020年5月24日 20:45:18-20:51:50
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ListViewDemo(QWidget):
    def __init__(self):
        super(ListViewDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("ListViewDemo")
        self.resize(500, 500)
        layout = QVBoxLayout()
        self.listView = QListView()
        # 字符串列表模型
        self.listModel = QStringListModel()
        self.list = ['List1', 'List2', 'List3']
        # 将数据关联到数据模型中
        self.listModel.setStringList(self.list)
        self.listView.setModel(self.listModel)
        self.listView.doubleClicked.connect(self.doubleClicked)
        layout.addWidget(self.listView)
        self.setLayout(layout)

    def doubleClicked(self, item):
        QMessageBox.information(self, "QListView", "You've chosen: " + self.list[item.row()])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ListViewDemo()
    main.show()
    sys.exit(app.exec_())