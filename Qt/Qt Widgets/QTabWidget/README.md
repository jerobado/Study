# QTabWidget

### Example
```c++
QTabWidget *tabWidget;
tabWidget = new QTabWidget(this);

auto tabPageWidget = new QWidget();
tabWidget->addTab(tabPageWidget, "tab label");
```

Note
- always pass a new instance of `QWidget` when creating a new tab

### References
- [QTabWidget Class](https://doc.qt.io/qt-6/qtabwidget.html)