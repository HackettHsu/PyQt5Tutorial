# lesson 123 14:58:15-15:04:38
import sys 
from PyQt5.QtWidgets import *

class QSSSelectorDemo(QWidget):
    def __init__(self):
        super(QSSSelectorDemo, self).__init__()
        self.setWindowTitle("QSSSelectorDemo")
        self.resize(500, 500)
        button1 = QPushButton("Button1")
        button1.setProperty("buttonName", "button1")
        button2 = QPushButton("Button2")
        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QSSSelectorDemo()
    # 给控件设置属性进行区分
    qssStyle = '''
        QPushButton[buttonName = button1]{ background-color : pink; color : 
        blue; height: 120; font-size : 30px}
    '''
    main.setStyleSheet(qssStyle)
    main.show()
    sys.exit(app.exec_())