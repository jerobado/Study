# QList
- `QList<T>` is one of Qt's generic container classes.
- It stores its items in adjacent memory locations and provides fast index-based access.
- `QVector<T>` used to be a different class in Qt 5, but is now a simple alias to QList.

### Example
```c++
QList<int> integerList;
QList<QString> stringList;
```
QList stores its items in an array of continuous memory. Typically, lists are created with an initial size. For example, the following code constructs a QList with 200 elements:

```c++
QList<QString> list(200);
```

### References
- [QList Class](https://doc.qt.io/qt-6/qlist.html#details)