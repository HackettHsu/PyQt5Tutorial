# lesson 74 2020年5月26日 11:27:06-11:36:10
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CellSizeDemo(QWidget):
    def __init__(self):
        super(CellSizeDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("CellSizeDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.tableWidget = QTableWidget()
        layout.addWidget(self.tableWidget)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['name', 'gendar', 'weight'])
        # (第几行/列, 改成多少)
        self.tableWidget.setRowHeight(0 ,80)
        self.tableWidget.setColumnWidth(2, 180)
        self.newItem = QTableWidgetItem('HackettHsu')
        self.tableWidget.setItem(0, 0, self.newItem)
        self.newItem = QTableWidgetItem('Male')
        self.tableWidget.setItem(0, 1, self.newItem)
        self.newItem = QTableWidgetItem('84')
        self.tableWidget.setItem(0, 2, self.newItem)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CellSizeDemo()
    main.show()
    sys.exit(app.exec_())