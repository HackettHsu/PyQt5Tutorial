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

    3. 已选中：2

具体还有哪些可用子类详见*QtWidgets.pyi*的*QAbstractButton*类，子类命名非常好理解。