# lesson 108 11:18:26-11:35:42
from PyQt5.QtCore import *

class MultiSignal(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int)
    signal3 = pyqtSignal(int, str)
    signal4 = pyqtSignal(list)
    signal5 = pyqtSignal(dict)
    # 声明一个重载版本的信号，即两个中括号二选一
    signal6 = pyqtSignal([int, str], [str])
    def __init__(self):
        super(MultiSignal, self).__init__()
        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)
        # 重载形式绑定方法
        self.signal6[int, str].connect(self.signalCall6)
        self.signal6[str].connect(self.signalCall6Overload)
        self.signal1.emit()
        self.signal2.emit(10)
        self.signal3.emit(6, "Test")
        self.signal4.emit([1, 2, 3, 4, 5, 6])
        self.signal5.emit({"NAME": "HackettHsu", "AGE":22})
        # 重载形式关联方法
        self.signal6[str].emit("test6")
        self.signal6[int, str].emit(100, "test6-1")
    
    def signalCall1(self):
        print("signal1 emit")

    def signalCall2(self, val):
        print(f"singal2 emit, value: {val}")
    
    def signalCall3(self, val, text):
        print(f"signal3 emit, value: {val, text}")

    def signalCall4(self, val):
        print(f"signal4 emit, value: {val}")

    def signalCall5(self, val):
        print(f"signal5 emit, value: {val}")

    def signalCall6(self, val, text):
        print(f"signal6 emit, value: {val, text}")

    def signalCall6Overload(self, val):
        print(f"singal6 emit, value: {val}")

if __name__ == "__main__":
    multiSignal = MultiSignal()