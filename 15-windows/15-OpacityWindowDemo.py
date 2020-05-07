# lesson 133 17:50:05-17:53:43
import sys 
from PyQt5.Qt import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("OpacityWindowDemo")
    window.setWindowOpacity(0.5)
    button = QPushButton("Button", window)
    window.resize(500, 500)
    window.show()
    sys.exit(app.exec_())