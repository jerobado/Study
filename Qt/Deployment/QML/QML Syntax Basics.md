# QML Syntax Basics

### Import Statements
- a QML document may have one or more imports at the top of the file
- an import can be any one of:
    - a versioned namespace into which types have been registered (e.g., by a plugin)
    - a relative directory which contains type-definitions as QML documents
    - a JavaScript file

**Example**
```QML
import QtQuick 2.0
import QtQuick.LocalStorage 2.0 as Database
import "../privateComponents"
import "somefile.js" as Script
```

### Object Declarations
- syntactically, a block of QML code defines a tree of QML objects to be created
- objects are defined using _object declarations_ that describe the type of object to be created as well as the attributes that are given to the object
- each object may also declare child objects using nested object declarations
- an object declarations consists of the name of its object type, followed by a set of curly braces
- all attributes and child object ar then declared within these braces

**Example**
```QML
Rectangle {
    width: 100
    height: 100
    color: "green"
}
```


# Resources
- [QML Syntax Basics](https://doc.qt.io/qt-6/qtqml-syntax-basics.html)