// Run using the QML Runtime tool
// qml sample.qml

import QtQuick

Rectangle {
    width: 200
    height: 100
    color: "green"

    Text {
        anchors.centerIn: parent
        text: "Ola!"
    }
}