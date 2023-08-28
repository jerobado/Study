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

### Property Attribute
- a property is an attribute of an object that can be assigned a static value or bound to a dynamic expression
- a property's value can be read by other objects
- generally, it can also be modified by another object, unless a particular QML type has explicitly disallowed this for a specific property

**Defining Property Attributes**
- property names must begin with a lower case letter and can only contain letters, numbers and underscores
- JavaScript reserved words are not valid property names
- `default`, `required`, and `readonly` keywords are optional, and modify the semantics of the property being declared

**Syntax**
```
[default] [required] [readonly] property <propertyType> <propertyName>
```

Declaring a custom property name **implicitly** creates a value-change _signal_ for that property, as well as an associated _signal handler_ called `on<PropertyName>Changed`, where `<PropertyName>` is the name of the property with the first letter capitalized.

**Example**
```QML
Rectangle {
    property color previousColor
    property color nextColor
    onNextColorChanged: console.log("The next color will be " + nextColor.toString())
}
```

**Valid Types in Custom Property Definitions**
- any of the QML Value Types aside from the enumeration types can be used as custom property types

**Example**
```QML
// These are all valid property declarations
Item {
    property int someNumber
    property string someString
    property url someUrl
}
```
Note: enumaration values are simply whole number values and can be referred to wth the int type instead

The `var` value type is a generic placeholder type that can hold any type of value, includin lists and objects:
```QML
property var someNumber: 1.5
property var someString: "abc"
property var someBool: true
property var someList: [1, 2, "three", "four"]
property var someObject: Rectangle { width: 100; height: 100; color: "red" }
```

Additionally, any QML object type can be used as a property type. For example:
```QML
property Item someItem
property Rectanle someRectangle
```
This applies to custom QML types as well. If a QML type was defined in a file named `ColorfulButton.qml` (in a directory which was then imported by the client), then a property of type `ColorfulButton` would also be valid.

# Resources
- [QML Object Attributes](https://doc.qt.io/qt-6/qtqml-syntax-objectattributes.html)