# QTimer
- The QTimer class provides a high-level programming interface for timers.


**Usage**
```c++
QTimer *timer = new QTimer(this);
connect(timer, &QTimer::timeout, this, &Foo::processOneThing);
timer->start();
```

### References
- [QTimer Class](https://doc.qt.io/qt-6/qtimer.html)