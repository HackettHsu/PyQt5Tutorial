# lesson 68 2020年5月25日 10:14:54-10:23:28
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PlaceControlInCellDemo(QWidget):
    def __init__(self):
        super(PlaceControlInCellDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("PlaceControlInCellDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        layout.addWidget(self.tableWidget)
        self.tableWidget.setHorizontalHeaderLabels(['name', 'gendar', 'weight'])
        self.textItem = QTableWidgetItem('HacketHsu')
        self.tableWidget.setItem(0, 0, self.textItem)
        self.combox = QComboBox()
        self.combox.addItems(['Male', 'Female'])
        self.combox.setStyleSheet("QComboBox{margin: 3px}")
        self.tableWidget.setCellWidget(0, 1, self.combox)
        self.modifyButton = QPushButton("Modify")
        # 默认按下状态
        self.modifyButton.setDown(True)
        self.modifyButton.setStyleSheet("QPushButton{margin: 3px}")
        self.tableWidget.setCellWidget(0, 2, self.modifyButton)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = PlaceControlInCellDemo()
    main.show()
    sys.exit(app.exec_())