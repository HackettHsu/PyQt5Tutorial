# lesson 66 2020年5月24日 21:42:46-21:51:50
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ListWidgetDemo(QMainWindow):
    def __init__(self):
        super(ListWidgetDemo, self).__init__()
        self.setWindowTitle("ListWidgetDemo")
        self.resize(500, 500)
        self.listWidget = QListWidget()
        self.listWidget.resize(300, 20)
        self.listWidget.addItem('item1')
        self.listWidget.addItems(['item2', 'item3', 'item5', 'item4'])
        self.setCentralWidget(self.listWidget)
        self.listWidget.itemDoubleClicked.connect(self.doubleClicked)

    def doubleClicked(self, index):
        QMessageBox.information(self, 'QListWidget', "You've chosen: " +\
            self.listWidget.item(self.listWidget.row(index)).text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ListWidgetDemo()
    main.show()
    sys.exit(app.exec_())