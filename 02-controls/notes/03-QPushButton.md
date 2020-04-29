# QPushButton 按钮控件

---

*QPushButton* 属于父类 *QAbstractButton*

*QAbstractButton* 常用子类：

1. *QPushButton*：最常用的按钮控件 [示例](../13-QPushButtonDemo.py)

2. *QRadioButton*：单选按钮控件：怎么实现多个单选按钮互相制约？只需要放在同一布局即可。 [示例](../14-QRadioButtonDemo.py)

3. *AToolButton*：工具条按钮控件

4. *QCheckBox*：多选按钮控件（复选框） （放在同一布局内实现相互制约） [示例](../15-QCheckBoxDemo.py)
    
    三种状态及表示（均用常量控制）：

    1. 未选中：0

    2. 半选中：1

        1. 设置是允许半选中方法：*setTristate(True)*

        2. 设置默认状态为半选中：*setCheckedState(Qt.PartiallyChecked)*。注意不要多括号

    3. 已选中：2

        设置默认状态为选中：*setChecked(True)*

5. *QComboBox*： 下拉列表控件 [示例](../16-QComboBoxDemo.py)

    1. 如何将列表项添加到QComboBox控件中：*addItem("ItemName")* 或 *addItems(['ItemName1', 'ItemName2'])* 注意是Item**s**

    2. 如何获取选中列表项。

6. *QSlider*：滑块控件 [示例](../17-QSliderDemo.py)

    水平*QSlider(Qt.Horizontal)*，垂直*QSlider(Qt.Vertical)*。

具体还有哪些可用子类详见*QtWidgets.pyi*的*QAbstractButton*类，子类命名非常好理解。