# QStack
- `QStack<T>` is one of Qt's generic container classes.
- It implements a stack data structure for items of a same type.
- A stack is a last in, first out (LIFO) structure.
- Items are added to the top of the stack using `push()` and retrieved from the top using `pop()`.
- The `top()` function provides access to the topmost item without removing it.

#### Example
```c++
#include <QCoreApplication>
#include <QStack>


int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QStack<int> stack;
    //stack.resize(5);
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);
    stack.push(5);
    stack.push(6);

    qDebug() << "size:" << stack.size();

    // while(!stack.isEmpty())
    //     qDebug() << stack.pop();

    for(const auto &item : stack)
    {
        qDebug() << item;
    }

    if (stack.size() > 5)
        qDebug() << "stack exceeded";


    return a.exec();
}

```


### References
- [QStack Class](https://doc.qt.io/qt-6/qstack.html)