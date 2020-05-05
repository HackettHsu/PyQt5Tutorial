# lesson 106 10:48:29-10:54:09
import sys 
from PyQt5.QtCore import *

class MyTypeSignal(QObject):
    # 定义一个自定义信号
    sendmsg = pyqtSignal(object)
    def run(self):
        # 触发信号
        self.sendmsg.emit("Hello PyQt5!")

class MySlot(QObject):
    def get(self, msg):
        print("信息：" + msg)

if __name__ == "__main__":
    send = MyTypeSignal()
    slot = MySlot()
    # 信号类中的信号方法绑定到槽类的槽方法
    send.sendmsg.connect(slot.get)
    send.run()
    # 断开连接
    send.sendmsg.disconnect(slot.get)
    send.run()