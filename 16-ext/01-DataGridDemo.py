# lesson 139
import sys, os
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

os.chdir(sys.path[0])
def initialzieModel(model):
    model.setTable('people')
    # 设置数据更新策略
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, Qt.Horizontal, 'ID')
    model.setHeaderData(1, Qt.Horizontal, 'Name')
    model.setHeaderData(2, Qt.Horizontal, 'Address')

def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def findrow(index):
    derlow = index.row()
    # print(f"del row = {str(derlow)}")

def addRow():
    ret = model.insertRows(model.rowCount(), 1)
    # print(f'InsertRow = {str(ret)}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./db/database.db')
    # 装载数据的模型
    model = QSqlTableModel()
    derlow = -1
    initialzieModel(model)
    view = createView("Display DB", model)
    view.clicked.connect(findrow)
    dialog = QDialog()
    layout = QVBoxLayout()
    layout.addWidget(view)
    addButton = QPushButton("Add a row")
    addButton.clicked.connect(addRow)
    delButton = QPushButton("Del a row")
    delButton.clicked.connect(lambda : model.removeRow(view.currentIndex().row()))
    layout.addWidget(addButton)
    layout.addWidget(delButton)
    dialog.setLayout(layout)
    dialog.setWindowTitle("DataGridDemo")
    dialog.resize(500, 400)
    dialog.show()
    sys.exit(app.exec_())