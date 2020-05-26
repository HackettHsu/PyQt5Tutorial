# 表格显示

[显示二维表数据](../00-TableViewDemo.py)：数据源：Model。要创建控件实例QTableView和数据源实例Model并两者关联。*MVC*形式：Model Viewer Controller。*MVC*的目的：将后端数据和前端页面的耦合度降低。

[显示列表数据](../01-ListViewDemo.py)

[扩展的列表控件](../02-ListWidgetDemo.py)：*QListView*的子类，精细化了一些功能。*QListWidget*支持非*MVC*模式。可以直接添加数据项。

[扩展的表格控件](../03-TableWidgetDemo.py)：同样是个子类。每一个Cell（单元格）是一个QTableWidget。

[在单元格中放置控件](../04-PlaceControlInCellDemo.py)：将控件放到单元格中：使用*setCellWidget*。将文本放入单元格中：使用*setItem*。

[在表格中搜索Cell和行定位](../05-DataLocationDemo.py)：搜索和查找。
    1. 数据的搜索：*findItems*查找所有满足条件的单元格，返回为list。
    2. 搜索结果不为空，定位单元格所在行：*setSliderPosition(row)*。

[设置单元格字体和颜色](../06-CellFontColorDemo.py)

[按列排序](../07-ColumnSortDemo.py):*sortItems(columnIndex, orderType)*
    1. 按哪一列排序；
    2. 排序类型：升序降序。

[设置单元格文本对齐方式](../08-CellTextAlignmentDemo.py)：使用*setTextAlignment*。

[合并单元格](../09-SpanDemo.py)：多项项合并为一个；或者可以理解为去掉分割线？使用*setSpan(row, col, 合并行数, 合并列数)*

[设置单元格尺寸](../10-CellSizeDemo.py)：*setColumnWidth*和*setRowHeight*。

[在单元格实现图文混排的效果](../11-CellImageTextDemo.py)

[改变单元格中图片的尺寸](../12-CellImageSizeDemo.py)：*QTableWidget.setIconSize(QSize(width, height))*

[在表格中显示上下文菜单](../13-TableWidgetContextMenuDemo.py)：指定单元格单击鼠标右键会弹出内容。
    1. 如何弹出菜单：*QMenu.exec_(相对于屏幕的坐标系)*
    2. 如何在满足条件情况下弹出菜单

[树控件（QTreeWidget）的基本用法](../14-BasicTreeWidgetDemo.py)

[为树结点添加响应事件](../15-TreeEventDemo.py)

[添加、修改和删除树控件中的节点](../16-ModifyTreeDemo.py)

[QTreeView控件与系统定制模式](../17-TreeViewDemo.py)