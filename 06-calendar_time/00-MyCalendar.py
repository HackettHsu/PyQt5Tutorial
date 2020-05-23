# lesson 56 2020年5月23日 11:16:18-11:26:39
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyCalendarDemo(QWidget):
    def __init__(self):
        super(MyCalendarDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1900,1,1))
        self.cal.setMaximumDate(QDate(2900,1,1))
        # 以网格形式显示
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.cal.clicked.connect(self.showDate)
        self.setWindowTitle("MyCalendarDemo")
        self.resize(500, 500)
        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString("yyyy-MM-dd dddd"))
        self.label.move(20, 300)

    def showDate(self, date):
        self.label.setText(date.toString("yyyy-MM-dd dddd"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyCalendarDemo()
    main.show()
    sys.exit(app.exec_())