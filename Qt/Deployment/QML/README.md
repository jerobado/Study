# QML (Qt Modeling Language)
- is a declarative language that allows user interfaces to be described in terms of their visual components and how they interact and relate with one another
- is a user interface specification and programming language
- it allows developers and designers alike to create highly performant, fluidly animated and visually appealiling applications
- offers a higghly readable, declarative, JSON-like syntax with support for imperative JavaScript expression combined with dynamic propery bindings

```QML
// hello.qml

import QtQuick
import QtQuick.Controls

ApplicationWindow {
    width: 400
    height: 400
    visible: true

    Button {
        id: button
        text: "A Special Button"
        background: Rectangle {
            implicitWidth: 100
            implicitHeight: 40
            color: button.down ? "#d6d6d6" : "#f6f6f6"
            border.color: "#26282a"
            border.width: 1
            radius: 4
        }
    }
}
```

To run this file, use the QML Runtime Tool:
```cmd
qml hello.qml
```

# What is Qt Quick?
- is the standard library of QML types and functionality for QML
- it includes visual types, interactive types, animations, models and views, particle effects and shader effects

# Resources
- [QML Applications](https://doc.qt.io/qt-6/qmlapplications.html)
- [Prototyping with the QML Runtime Tool](https://doc.qt.io/qt-6/qtquick-qml-runtime.html)