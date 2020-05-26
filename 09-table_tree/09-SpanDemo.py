# lesson 73 2020年5月25日 18:01:14-18:06:08
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SpanDemo(QWidget):
    def __init__(self):
        super(SpanDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("SpanDemo")
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
        self.tableWidget.setSpan(0, 0, 3, 1)
        self.newItem = QTableWidgetItem('Male')
        self.tableWidget.setItem(0, 1, self.newItem)
        self.tableWidget.setSpan(0, 1, 2, 1)
        self.newItem = QTableWidgetItem('83')
        self.tableWidget.setItem(0, 2, self.newItem)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = SpanDemo()
    main.show()
    sys.exit(app.exec_())