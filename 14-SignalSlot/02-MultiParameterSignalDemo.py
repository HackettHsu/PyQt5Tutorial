# lesson 107 11:12:20-11:17:37
import sys 
from PyQt5.QtCore import *

class MyTypeSignal(QObject):
    sendmsg1 = pyqtSignal(object)
    # 发送三个参数的信号
    sendmsg2 = pyqtSignal(str, int, int)
    def run1(self):
        self.sendmsg1.emit("Hello PyQt5!")
    def run2(self):
        self.sendmsg2.emit("Signal2", 5, 6)

class MySlot(QObject):
    def get1(self, msg):
        print("信息：" + msg)
    def get2(self, msg, a, b):
        print(msg, a + b)

if __name__ == "__main__":
    send = MyTypeSignal()
    slot = MySlot()
    send.sendmsg1.connect(slot.get1)
    send.sendmsg2.connect(slot.get2)
    send.run1()
    send.run2()