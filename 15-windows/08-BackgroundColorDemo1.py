# lesson 126-1-1
from  PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setObjectName("MainWindow")
window.setStyleSheet("#MainWindow{background-color : blue}")
window.show()
sys.exit(app.exec_())