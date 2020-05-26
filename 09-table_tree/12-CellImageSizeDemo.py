# lesson 76 2020年5月26日 11:52:37-12:11:33
import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

os.chdir(sys.path[0])
class CellImageSizeDemo(QWidget):
    def __init__(self):
        super(CellImageSizeDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("CellImageSizeDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.tableWidget = QTableWidget()
        layout.addWidget(self.tableWidget)
        self.tableWidget.setIconSize(QSize(300, 300))
        self.tableWidget.setRowCount(4)
        # 让行高列宽与图片尺寸匹配
        for i in range(3):
            self.tableWidget.setColumnWidth(i, 300)
        for i in range(4):
            self.tableWidget.setRowHeight(i, 300)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['name', 'gendar', 'weight'])
        self.newItem = QTableWidgetItem('HackettHsu')
        self.tableWidget.setItem(0, 0, self.newItem)
        self.newItem = QTableWidgetItem('Male')
        self.tableWidget.setItem(0, 1, self.newItem)
        self.newItem = QTableWidgetItem('84')
        self.tableWidget.setItem(0, 2, self.newItem)
        self.newItem = QTableWidgetItem(QIcon('./images/罗小黑战记 电影原声带.bmp'), 'imagesizetest')
        self.tableWidget.setItem(1, 0, self.newItem)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CellImageSizeDemo()
    main.show()
    sys.exit(app.exec_())