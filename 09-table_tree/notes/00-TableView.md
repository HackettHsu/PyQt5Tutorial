# 表格显示

[显示二维表数据](../00-TableViewDemo.py)：数据源：Model。要创建控件实例QTableView和数据源实例Model并两者关联。*MVC*形式：Model Viewer Controller。*MVC*的目的：将后端数据和前端页面的耦合度降低。

[显示列表数据](../01-ListViewDemo.py)

[扩展的列表控件](../02-ListWidgetDemo.py)：*QListView*的子类，精细化了一些功能。*QListWidget*支持非*MVC*模式。可以直接添加数据项。

[扩展的表格控件](../03-TableWidgetDemo.py)：同样是个子类。每一个Cell（单元格）是一个QTableWidget。