# DragClip：拖拽和剪贴

1. [拖拽](00-DragDropDemo.py)

    接受者：

    1. *setAcceptDrops(True)*：必要：接受拖拽物

    2. *dragEnterEvent*：拖到上空时发生的事件

    3. *dropEvent*：放下时发生的事件

    发送者：

    1. *setDragEnabled(True)*：设置允许拖动

2. [剪切板](01-ClipBoardDemo.py)：通过剪贴板共享和传递数据

    用信号和槽设置方法，并利用*QApplication.clipboard()*方法获取剪切板对象