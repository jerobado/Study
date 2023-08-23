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

### Child Objects
- any object declaration can define child objects through nested object declarations
- any object declaration implicitly declares an object tree that may contain any number of child objects

**Example**

The `Rectanggle` object declaration below includes `Gradients` object declaration, which in turn contains two `GradientStop` declaration:

```QML
import QtQuick 2.0

Rectangle {
    width: 100
    height: 100

    gradient: Gradient {
        GradientStop { position: 0.0; color: "yellow" }
        GradientStop { position: 1.0; color: "green" }
    }
}
```

### Comments
The syntax for commenting in QML is similar to that of JavaScript:
- single line comment start with `//` and finish at the end of the line
- multiline comments start with `/*` and finish with `*/`
- comments are ignored by the engine when processing QML code

**Example**
```QML
Text {
    text: "Hello world!"    //a basic greeting
    /*
        We want this text to stand out from the rest so
        we give it a large size and different font.
     */
    font.family: "Helvetica"
    font.pointSize: 24
}
```


# Resources
- [QML Syntax Basics](https://doc.qt.io/qt-6/qtqml-syntax-basics.html)