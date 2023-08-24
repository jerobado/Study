# QML Object Attributes
- every QML object type has a defined set of attributes
- each instance of an object type is created with the set of attributes that have been defined for that object type

## Attributes in Object Declarations
- an _object declaration_ in a QML document defines a new type
- it also declares an object hierarchy that will be instantiated should an instance of that newly defined type be created

The set of QML object-type attributes types is as follows:
- id
- property
- signal
- signal handler
- method
- attached properties and attached signal handler
- enumeration

### Id Attribute
- every QML object type has exactly one _id_ attribute
- this attribute is provided by the language itself, and connot be redefined or overridden by any QML object type
- a value may be assigned to the _id_ attribute of an object instance to allow that object to be identified and referred to by other objects
- the `id` must begin with a lower-case letter or an underscore, and connot contain characters other than letters, numbers and underscores

**Example**
```QML
import QtQuick 2.0

Column {
    width: 200
    height: 200

    TextInput {
        id: sampleTextInput
        text: "Sugoi!"
    }

    Text {
        text: sampleTextInput.text
    }
}
```


# Resources
- [QML Object Attributes](https://doc.qt.io/qt-6/qtqml-syntax-objectattributes.html)