# lesson 69 2020年5月25日 10:27:06-10:47:12
import sys
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

class DataLocationDemo(QWidget):
    def __init__(self):
        super(DataLocationDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("DataLocationDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(40)
        self.tableWidget.setColumnCount(4)
        layout.addWidget(self.tableWidget)
        for i in range(40):
            for j in range(4):
                self.itemContent = '(%d, %d)' %(i, j)
                self.tableWidget.setItem(i, j, QTableWidgetItem(self.itemContent))
        self.setLayout(layout)
        # 搜索满足条件的Cell
        # 不能写“01”
        self.text = '(24, 1)'
        # 或者字段匹配（只搜索第一个满足条件的）
        # self.text = '(24'
        # 字段匹配就要改为MatchStartsWitch
        self.items = self.tableWidget.findItems(self.text, QtCore.Qt.MatchExactly)
        if self.items:
            self.item = self.items[0]
            self.item.setBackground(QBrush(QColor(255, 255, 0)))
            self.item.setForeground(QBrush(QColor(255, 0, 255)))
            self.row = self.item.row()
            self.tableWidget.verticalScrollBar().setSliderPosition(self.row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DataLocationDemo()
    main.show()
    sys.exit(app.exec_())