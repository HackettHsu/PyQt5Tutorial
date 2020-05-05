# lesson 109 16:27:33-16:36:35
from PyQt5.QtCore import *

class NNSignalDemo(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int)

    def __init__(self):
        super(NNSignalDemo, self).__init__()
        # N<->1，谁先关联谁先调用
        self.signal1.connect(self.call1)
        self.signal1.connect(self.call1_1)
        self.signal1.emit()
        # 1<->N，Signal2虽然参数没有用，但必须写
        self.signal2.connect(self.signal1)
        self.signal2.emit(2)
        self.signal1.disconnect(self.call1)
        self.signal1.disconnect(self.call1_1)
        self.signal2.disconnect(self.signal1)
        self.signal1.connect(self.call1)
        self.signal2.connect(self.call2)
        self.signal1.emit()
        self.signal2.emit(2)

    def call1(self):
        print("call1 emit")

    def call1_1(self):
        print("call1_1 emit")
    
    def call2(self, val):
        print("call2 emit, value:", val)

if __name__ == "__main__":
    nnSignal = NNSignalDemo()
