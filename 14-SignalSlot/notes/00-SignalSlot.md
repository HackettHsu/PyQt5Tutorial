# *SignalSlot*信号与槽

0. [基本](../00-SignalSlotDemo.py)

1. [自定义信号](../01-CustomSignalDemo.py)：自定义一个信号对象，*customSignal = pyqtSignal()*（继承自QObject），用*emit*触发。

2. [可以传递多个参数的信号](../02-MultiParameterSignalDemo.py)：*pyqtSignal()*括号中的内容控制发送参数类型和数量

3. [为类添加多个信号](../03-MultiSignalDemo.py)

4. [信号槽N对N连接与断开](../04-NNSignalDemo.py)

5. [为窗口类添加信号](../05-WinSignalDemo.py)：通过触发按钮的信号槽函数来关闭窗口