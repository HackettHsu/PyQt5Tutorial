# lesson 77 2020年5月26日 14:15:57-14:30:43
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TableWidgetContextMenuDemo(QWidget):
    def __init__(self):
        super(TableWidgetContextMenuDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("TableWidgetContextMenuDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.tableWidget = QTableWidget()
        layout.addWidget(self.tableWidget)
        # 允许弹出菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # 用信号和槽设置弹出菜单的条件
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['name', 'gendar', 'weight'])
        self.newItem = QTableWidgetItem('HackettHsu')
        self.tableWidget.setItem(0, 0, self.newItem)
        self.newItem = QTableWidgetItem('Male')
        self.tableWidget.setItem(0, 1, self.newItem)
        self.newItem = QTableWidgetItem('84')
        self.tableWidget.setItem(0, 2, self.newItem)
    
    def generateMenu(self, position):
        # 打印弹出菜单的位置（获取当前鼠标的坐标）
        print(position)
        # 进行可用性限制：指定单元格才能弹出
        for i in self.tableWidget.selectionModel().selection().indexes():
            self.rowNum = i.row()
        # 选择行索引值小于二才能弹出菜单
        if self.rowNum < 2:
            self.menu = QMenu()
            self.item1 = self.menu.addAction('Menu1')
            self.item2 = self.menu.addAction('Menu2')
            self.item3 = self.menu.addAction('Menu3')
            # 将相对坐标转换为对于屏幕的绝对坐标
            self.screenPosition = self.tableWidget.mapToGlobal(position)
            print(self.screenPosition)
            # 被阻塞
            self.action = self.menu.exec(self.screenPosition)
            if self.action == self.item1:
                print('"Menu1" has been chosen in', \
                    self.tableWidget.item(self.rowNum, 0).text(), \
                        self.tableWidget.item(self.rowNum, 1).text(), \
                            self.tableWidget.item(self.rowNum, 2).text())
            elif self.action == self.item2:
                print('"Menu1" has been chosen in', \
                    self.tableWidget.item(self.rowNum, 0).text(), \
                        self.tableWidget.item(self.rowNum, 1).text(), \
                            self.tableWidget.item(self.rowNum, 2).text())
            elif self.action == self.item3:
                print('"Menu1" has been chosen in', \
                    self.tableWidget.item(self.rowNum, 0).text(), \
                        self.tableWidget.item(self.rowNum, 1).text(), \
                            self.tableWidget.item(self.rowNum, 2).text())
            else:
                return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TableWidgetContextMenuDemo()
    main.show()
    sys.exit(app.exec_())