# lesson 70 2020年5月25日 11:19:20-11:26:22
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CellFontColorDemo(QWidget):
    def __init__(self):
        super(CellFontColorDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("CellFontColorDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        layout.addWidget(self.tableWidget)
        self.tableWidget.setHorizontalHeaderLabels(['name', 'gendar', 'weight'])
        self.newItem = QTableWidgetItem('HackettHsu')
        self.newItem.setFont(QFont('Hack', 16, QFont.Light))
        self.newItem.setBackground(QBrush(QColor(255, 0, 0)))
        # 前景色，可以理解为字体颜色
        self.newItem.setForeground(QBrush(QColor(0, 255, 0)))
        self.tableWidget.setItem(0, 0, self.newItem)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CellFontColorDemo()
    main.show()
    sys.exit(app.exec_())