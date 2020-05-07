# lesson 115 22:49:47-22:54:48
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class OverrideSlotDemo(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OverrideSlotDemo")
        
    # 例如，“按下任意键”中添加自己的槽
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Alt:
            self.setWindowTitle("Key 'Alt' is pressed.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = OverrideSlotDemo()
    main.show()
    sys.exit(app.exec_())