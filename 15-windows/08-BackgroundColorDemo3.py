# lesson 126-3-1
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("BackgroundColorDemo3")
    
    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setBrush(Qt.green)
        painter.drawRect(self.rect())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Winform()
    window.show()
    sys.exit(app.exec_())