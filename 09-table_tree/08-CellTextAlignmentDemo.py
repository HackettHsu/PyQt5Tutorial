# lesson 72 2020年5月25日 11:41:44-11:46:42
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CellTextAlignmentDemo(QWidget):
    def __init__(self):
        super(CellTextAlignmentDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("CellTextAlignmentDemo")
        self.resize(500, 500)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['name', 'gendar', 'weight'])
        layout.addWidget(self.tableWidget)
        self.newItem = QTableWidgetItem('HackettHsu')
        # | 用于多项共存
        self.newItem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.tableWidget.setItem(0, 0, self.newItem)
        self.newItem = QTableWidgetItem('Male')
        # 中心对齐
        self.newItem.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, self.newItem)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CellTextAlignmentDemo()
    main.show()
    sys.exit(app.exec_())