# *SignalSlot*信号与槽

0. [基本](../00-SignalSlotDemo.py)

1. [自定义信号](../01-CustomSignalDemo.py)：自定义一个信号对象，*customSignal = pyqtSignal()*（继承自QObject），用*emit*触发。

2. [可以传递多个参数的信号](../02-MultiParameterSignalDemo.py)：*pyqtSignal()*括号中的内容控制发送参数类型和数量

3. [为类添加多个信号](../03-MultiSignalDemo.py)

4. [信号槽N对N连接与断开](../04-NNSignalDemo.py)

5. [为窗口类添加信号](../05-WinSignalDemo.py)：通过触发按钮的信号槽函数来关闭窗口

6. [多线程更新UI](../06-ThreadUpdateUIDemo.py)：在主线程更新UI。更新线程方法多种多样，用信号和槽来更新是推荐方法之一。

    理解：在两个线程中传递数据。用法：创建专用类继承*QThread*，在调用时使用 *.start()* 函数启动线程。

7. [信号和槽自动连接](../07-AutoSignalSlotDemo.py)：感觉没有更方便……

8. [使用lambda表达式为槽函数传递参数](../08-LambdaSlotArgDemo.py)

    Lambda表达式：匿名函数（简略函数？）。例如：

    ```python
    fun1 = lambda: print("Hello World")
    # 之后fun1就可以直接当函数调用了，如： 
    fun1()
    # 声明带有参数的函数：
    fun2 = lambda x, y: print(x, y)
    # 使用
    fun2("a", "b")
    ```

9. [用partial对象为槽函数传递参数](../09-PartialSlotArgDemo.py)

10. [override（覆盖）槽函数](../10-OverrideSlotDemo.py)：改变槽函数的行为，比如改变*clicked*。

11. 多窗口交互：目标：将数据和控件分离，实现降低强耦合。[不使用信号和槽](../11-MultiWindow1Demo.py)。[使用信号和槽](../12-MultiWindow2Demo.py)：文件中有较多笔记。关键思想：两个窗口交互，尽量不要互相访问控件（私有资源）而是应该访问信号，并指定与信号绑定的槽函数。这样，某一窗口的控件发生改变，但信号和槽不变，则另一窗口不需要修改。