# QML Coding Conventions
- Recommended QML coding conventions

### QML Object Declarations
```QML
Rectangle {
    id: photo                                               // id on the first line makes it easy to find an object

    property bool thumbnail: false                          // property declarations
    property alias image: photoImage.source

    signal clicked                                          // signal declarations

    function doSomething(x)                                 // javascript functions
    {
        return x + photoImage.width
    }

    color: "gray"                                           // object properties
    x: 20                                                   // try to group related properties together
    y: 20
    height: 150
    width: {                                                // large bindings
        if (photoImage.width > 200) {
            photoImage.width;
        } else {
            200;
        }
    }

    states: [
        State {
            name: "selected"
            PropertyChanges { target: border; color: "red" }
        }
    ]

    transitions: [
        Transition {
            from: ""
            to: "selected"
            ColorAnimation { target: border; duration: 200 }
        }
    ]

    Rectangle {                                             // child objects
        id: border
        anchors.centerIn: parent; color: "white"

        Image {
            id: photoImage
            anchors.centerIn: parent
        }
    }
}
```

### Grouped Properties
- If using multiple properties from a group of properties, consider using group notation instead of dot notation if it improves readability.

```QML
// From this
Rectangle {
    anchors.left: parent.left; anchors.top: parent.top; anchors.right: parent.right; anchors.leftMargin: 20
}

Text {
    text: "hello"
    font.bold: true; font.italic: true; font.pixelSize: 20; font.capitalization: Font.AllUppercase
}

// to this
Rectangle {
    anchors { left: parent.left; top: parent.top; right: parent.right; leftMargin: 20 }
}

Text {
    text: "hello"
    font { bold: true; italic: true; pixelSize: 20; capitalization: Font.AllUppercase }
}
```

### Unqualified access
- In order to improve readability and performance always reference properties of parent components by their id explicitly:
```QML
Item {
    id: root

    property int rectangleWidth: 50

    Rectangle {
        width: root.rectangleWidth
    }
}
```