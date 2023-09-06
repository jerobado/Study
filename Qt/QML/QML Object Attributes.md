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

**Assigning Values to Property Attributes**

The value of a property of an object instance may be specified in two separate ways:
- a vlaue assignment on initialization
- an imperative value assignment

The syntax for assigning a value to a property on initialization is:
```
<propertyName> : <value>
```

An example of property value initialization:
```QML
import QtQuick 2.0

Rectangle {
    color: "red"
    property color nextColor: "blue" // combined property declaration and initialization
}
```

**Imperative Value Assignment**
- an imperative value assignment is where a property value (either static value or binding expression) is assigned to a property from imperative JavaScript code
- the syntax of an imperative value assignment is just the JavaScript assignment operator

**Example**
```QML
import QtQuick 2.0

Rectangle {
    id: rect
    Component.onCompleted: {
        rect.color = "red"
    }
}
```

**Static Values and Bindin Expression Values**

**Static**
- a constant value which does not depend on other properties

**Binding expression**
- a JavaScript expression which describes a property's relationship with other properties
- the variables in this expression are called the property's _dependencies_ 

**Example**
```QML
import QtQuick 2.0

Rectangle {
    // both of these are static value assignments on initialization
    width: 400
    height: 200

    Rectangle {
        // both of these are binding expression value assignments on initialization
        width: parent.width / 2
        height: parent.height
    }
}
```

**Type Safety**
- properties are type safe
- a property can only be assigned a value that matches the property type

For example, if a property is a real, and if you try to assign a string to it, you will get an error:
```QML
property int volume: "four"  // generates an error; the property's object will not be loaded
```

**Special Property Types**

**Object List Property Attributes**
- a `list` type can be assigned a list of QML object-type values

```QML
import QtQuick 2.0

Item {
    states: [
        State { name: "loading" },
        State { name: "running" },
        State { name: "stopped" }
    ]
}
```
If the list contains a single item, the square brackets may be omitted:
```QML
import QtQuick 2.0

Item {
    states: State { name: "running" }
}
```
An example of list property declaration follows:
```QML
import QtQuick 2.0

Rectangle {
    // declaration without initialization
    property list<Rectangle> siblingRects

    // declaration with initialization
    property list<Rectangle> childRects: [
        Rectangle { color: "red" },
        Rectangle { color: "blue"}
    ]
}
```

**Group Properties**
- in some cases, properties contain a logical group of sub-property attributes
- these sub-property attributes can be assigned to using either the dot notation or group notation

For example, the `Text` type has a font group property. Below, the first `Text` object initializes its font values using dot notation, while the second uses group notation:
```QML
Text {
    // dot notation
    font.pixelSize: 12
    font.b: true
}

Text {
    // group notation
    font { pixelSize: 12; b: true }
}
```

**Property Aliases**
- property aliases are properties which hold a reference to another property.
- unlike an ordinary property definition, which allocates a new, unique storage space for the property, a property alias connects the newly declared property (called the aliasing property) as a direct reference to an existing property (the aliased property)

For example, below is a Button type with a buttonText aliased property which is connected to the text object of the Text child:
```QML
// Button.qml
import QtQuick 2.0

Rectangle {
    property alias buttonText: textItem.text

    width: 100; height: 30; color: "yellow"

    Text { id: textItem }
}
```

The following code would create a Button with a defined text string for the child Text object:

```QML
Button { buttonText: "Click Me" }
```

Here, modifying `buttonText` directly modifies the textItem.text value; it does not change some other value that then updates textItem.text. If `buttonText` was not an alias, changing its value would not actually change the displayed text at all, as property bindings are not bi-directional: the `buttonText` value would have changed if textItem.text was changed, but not the other way around.

**Default Properties**
- an object definition can have a single _default_ property
- a default property is the property to which a value is assigned if an object is declared within another object's definition without declaraing it as a value for a particular property
- declaring a property with the optional `default` keyword marks it as the default property

**Example**
```QML
// MyLabel.qml
import QtQuick 2.0

Text {
    default property var someText

    text: "Hello, " + someText.text
}
```

**Required Properties**
- required property must be set when an instance of the object is created
- violation of this rule will result in QML applications not starting if it can be detected statically

**Example**
```QML
// ColorRectangle.qml
Rectangle {
    required color
}
```

**Read-Only Properties**
- read-only properties must be assigned a static value or a binding expression on initialization
- after a read-only property is initialized, you cannot change its static value or binding expression anymore

**Example**
```QML
Item {
    readonly property int someNumber: 10

    Component.onCompleted: someNumber = 20  // TypeError: Cannot assign to read-only property
}
```

### Signal Attributes
- a signal is a notification from an object that some event has occured
- for example, a property has changed, an animation has started or stopped, or when an image has been downloaded

**Example**
```QML
import QtQuick 2.0

Item {
    width: 100; height: 100

    MouseArea {
        anchors.fill: parent
        onClicked: {
            console.log("Click!")
        }
    }
}
```

### Signal Handler Attributes
- Signal handlers are a special sort of method attribute, where the method implementation is invoked by the QML engine whenever the associated signal is emitted.
- Adding a signal to an object definition in QML will automatically add an associated signal handler to the object definition, which has, by default, an empty implementation.
- Clients can provide an implementation, to implement program logic.

Consider the following SquareButton type, whose definition is provided in the SquareButton.qml file as shown below, with signals activated and deactivated:
```QML
// SquareButton.qml
Rectangle {
    id: root

    signal activated(xPosition: real, yPosition: real)
    signal deactivated

    property int side: 100
    width: side; height: side

    MouseArea {
        anchors.fill: parent
        onReleased: root.deactivated()
        onPressed: (mouse)=> root.activated(mouse.x, mouse.y)
    }
}
```

These signals could be received by any SquareButton objects in another QML file in the same directory, where implementations for the signal handlers are provided by the client:
```QML
// myapplication.qml
SquareButton {
    onDeactivated: console.log("Deactivated!")
    onActivated: (xPosition, yPosition)=> console.log("Activated at " + xPosition + "," + yPosition)
}
```

**Property Change Signal Handlers**
- Signal handlers for property change signal take the syntax form _on&lt;Property>Changed_ where _&lt;Property>_ is the name of the property, with the first letter capitalized.

```QML
import QtQuick 2.0

TextInput {
    text: "Change this!"

    onTextChanged: console.log("Text has changed to:", text)
}
```

# Resources
- [QML Object Attributes](https://doc.qt.io/qt-6/qtqml-syntax-objectattributes.html)