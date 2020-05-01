# Drawing API

PyQt5的基本绘图API：在窗口上绘制各种元素，主要有以下三种：

1. [*drawText*](../00-DrawTextDemo.py)：绘制文本

2. 各种图形：

    1. [点（以点绘图）](../01-DrawPointsDemo.py)

    2. [直线](../02-DrawMultiLineDemo.py)

    3. [其他图形](../03-DrawAllDemo.py)：其中含有

3. [**]：图像

基本流程：

1. 调用必要类*QPainter*

2. 创建实例 `painter = QPainter(self)`

3. 初始化 `painter.begin(self)`

4. 绘制内容 `painter.drawXXX()`

5. 结束 `painter.end()` 注意这里不需要*self*

注意：必须在*paintEvent*事件方法中绘制各种元素，因为该方法能在窗口尺寸发生改变时自动以极快速度重绘图像。