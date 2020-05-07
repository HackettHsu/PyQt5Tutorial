# lesson 126-2-1
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

app = QApplication(sys.argv)
window = QMainWindow()
palette = QPalette()
palette.setColor(QPalette.Background, Qt.cyan)
window.setPalette(palette)
window.show()
sys.exit(app.exec_())