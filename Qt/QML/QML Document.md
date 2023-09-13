# QML Document
- a QML document is a string which conforms to QML document syntax
- a document defines a QML object type
- a document is generally loaded from a `.qml` file stored either locally or remotely, but can be constructed manually in code


## Defining Object Types Through QML Documents

In the following example, the client developer defines a Button type with a document in a file:

```CML
// Button.qml
import QtQuick 2.0

Rectangle {
    width: 100; height: 100
    color: "red"

    MouseArea {
        anchors.fill: parent
        onClicked: console.log("Button clicked!")
    }
}
```

The Button type can then be used in an application:

```QML
// application.qml
import QtQuick 2.0

Column {
    Button { width: 50; height: 50 }
    Button { x: 50; width: 100; height: 50; color: "blue" }
    Button { width: 50; height: 50; radius: 8 }
}
```