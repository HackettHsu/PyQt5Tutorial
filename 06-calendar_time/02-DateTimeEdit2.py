# lesson 57 2020年5月23日 11:26:53-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DateTimeEdit1(QWidget):
    def __init__(self):
        super(DateTimeEdit1, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("DateTimeEdit1")
        self.resize(500, 500)
        layout = QVBoxLayout()
        dateTimeEdit1 = QDateTimeEdit()
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(365))
        dateTimeEdit1.dateChanged.connect(self.onDateChanged)
        dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)
        self.dateTimeEdit = dateTimeEdit1
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
        # 设置为下拉修改日期
        dateTimeEdit2.setCalendarPopup(True)
        dateEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())
        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")
        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:ss")
        self.button = QPushButton("获取日期和时间")
        self.button.clicked.connect(self.onButtonClick)
        layout.addWidget(dateTimeEdit1)
        layout.addWidget(dateTimeEdit2)
        layout.addWidget(dateEdit)
        layout.addWidget(timeEdit)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def onDateChanged(self, date):
        print(date)
    
    def onTimeChanged(self, time):
        print(time)

    def onDateTimeChanged(self, dateTime):
        print(dateTime)

    def onButtonClick(self):
        dateTime = self.dateTimeEdit.dateTime()
        print(dateTime)
        print(self.dateTimeEdit.maximumDate())
        print(self.dateTimeEdit.maximumDateTime())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DateTimeEdit1()
    main.show()
    sys.exit(app.exec_())