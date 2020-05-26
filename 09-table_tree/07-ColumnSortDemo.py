# lesson 71 2020年5月25日 11:28:22-11:39:37
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ColumnSortDemo(QWidget):
    def __init__(self):
        super(ColumnSortDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("ColumnSortDemo")
        self.resize(500, 500)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['name', 'gendar', 'weight'])
        layout.addWidget(self.tableWidget)
        self.newItem = QTableWidgetItem('HackettHsu')
        self.tableWidget.setItem(0, 0, self.newItem)
        self.newItem = QTableWidgetItem('Male')
        self.tableWidget.setItem(0, 1, self.newItem)
        self.newItem =QTableWidgetItem('80')
        self.tableWidget.setItem(0, 2, self.newItem)
        
        self.newItem = QTableWidgetItem('Hackett')
        self.tableWidget.setItem(1, 0, self.newItem)
        self.newItem = QTableWidgetItem('Male')
        self.tableWidget.setItem(1, 1, self.newItem)
        self.newItem =QTableWidgetItem('75')
        self.tableWidget.setItem(1, 2, self.newItem)
        
        self.newItem = QTableWidgetItem('Hsu')
        self.tableWidget.setItem(2, 0, self.newItem)
        self.newItem = QTableWidgetItem('Male')
        self.tableWidget.setItem(2, 1, self.newItem)
        self.newItem =QTableWidgetItem('70')
        self.tableWidget.setItem(2, 2, self.newItem)
        self.sortButton = QPushButton("Sort the Data")
        self.sortButton.clicked.connect(self.order)
        layout.addWidget(self.sortButton)
        # 设置默认排序类型
        self.orderType = Qt.DescendingOrder
    
    def order(self):
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder
        # 控制排序的列和排序类型
        self.tableWidget.sortItems(2, self.orderType)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ColumnSortDemo()
    main.show()
    sys.exit(app.exec_())