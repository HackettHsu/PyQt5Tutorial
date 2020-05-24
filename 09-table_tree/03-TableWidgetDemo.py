# lesson 67 2020年5月24日 22:10:26-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.setWindowTitle("TableWidgetDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        # 设置水平列表名称
        self.tableWidget.setHorizontalHeaderLabels(['name', 'age', 'born-place'])
        self.tableWidget.setVerticalHeaderLabels(['a', 'b'])
        # 创建tableWidgetItem
        self.nameItem = QTableWidgetItem("HackettHsu")
        self.tableWidget.setItem(0, 0, self.nameItem)
        self.ageItem = QTableWidgetItem("22")
        self.tableWidget.setItem(0, 1, self.ageItem)
        self.born_placeItem = QTableWidgetItem("Shanghai")
        self.tableWidget.setItem(0, 2, self.born_placeItem)
        # 禁用编辑功能
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 整行选中
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 自适应调整行列大小
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        # 显示/隐藏表头
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        # 显示/隐藏表格线
        self.tableWidget.setShowGrid(False)
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TableWidgetDemo()
    main.show()
    sys.exit(app.exec_())