# lesson 41
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("滑块控件演示")
        self.resize(500, 500)
        layout = QVBoxLayout()
        self.label = QLabel("泥嚎PyQt5")
        # 设置显示位置：居中显示
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.slider1 = QSlider(Qt.Horizontal)
        # 设置最小值最大值步长当前值
        self.slider1.setMinimum(12)
        self.slider1.setMaximum(48)
        self.slider1.setSingleStep(3)
        self.slider1.setValue(18)
        # 设置刻度位置
        # 刻度在下方
        self.slider1.setTickPosition(QSlider.TicksBelow)
        # 设置刻度的间隔
        self.slider1.setTickInterval(6)
        self.slider1.valueChanged.connect(self.valueChange)

        self.slider2 = QSlider(Qt.Vertical)
        self.slider2.setMinimum(12)
        self.slider2.setMaximum(48)
        self.slider2.setSingleStep(3)
        self.slider2.setValue(18)
        self.slider2.setTickPosition(QSlider.TicksRight)
        self.slider2.setTickInterval(6)
        self.slider2.valueChanged.connect(self.valueChange)
        layout.addWidget(self.slider2)

        layout.addWidget(self.slider1)
        self.setLayout(layout)

    def valueChange(self):
        # sender()：获得当前发送过来的信号
        print(f"当前值{self.sender().value()}")
        size = self.sender().value()
        self.label.setFont(QFont('OPPOSans L', size))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())