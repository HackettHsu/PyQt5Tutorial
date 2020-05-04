# *multithread*：多线程相关

用于同时完成多个任务

1. *QTimer*：定时器。可用于循环任务。如：

    1. [动态显示当前时间](00-ShowTimeDemo.py)。用到*QTimer()* 的 *\.start(刷新间隔（毫秒）)*和 *\.stop()*方法，实现循环执行任务。
    
    2. [让程序定时关闭](01-AutoCloseWindowDemo.py)。使用*QTimer.singleShot*方法，实现只执行一次的功能。

2. *QThread*：实现多线程。如：

    1. [计数器](02-CounterDemo.py)。步骤：

        1. 从*QThread*派生一个子类；

        2. 定义子类，如*run*，并在子类中创建一个（死）循环，`while True:`；

        3. 在循环中设定跳出方法，如`break`；

        4. 为防止循环执行过快导致显示效果不佳，要增加暂停语句，如：`self.sleep(1)`，单位：秒。