# lesson 75 2020年5月26日 11:48:32-11:52:05
import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

os.chdir(sys.path[0])
class CellImageTextDemo(QWidget):
    def __init__(self):
        super(CellImageTextDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("CellImageTextDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.tableWidget = QTableWidget()
        layout.addWidget(self.tableWidget)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['name', 'gendar', 'weight'])
        self.newItem = QTableWidgetItem('HackettHsu')
        self.tableWidget.setItem(0, 0, self.newItem)
        self.newItem = QTableWidgetItem('Male')
        self.tableWidget.setItem(0, 1, self.newItem)
        self.newItem = QTableWidgetItem('84')
        self.tableWidget.setItem(0, 2, self.newItem)
        self.newItem = QTableWidgetItem(QIcon('./images/罗小黑战记 电影原声带.bmp'), 'imagetest')
        self.tableWidget.setItem(1, 0, self.newItem)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CellImageTextDemo()
    main.show()
    sys.exit(app.exec_())