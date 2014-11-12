import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1

ApplicationWindow {
    property int margin: 18
    property int inner_spacing: 9
    property int contentHeight: 120

    width: 400
    minimumWidth: 400

    // property alias password : passwordField.text
    // property alias email    : emailField.text

    property Component firstStep : Column {
        spacing: inner_spacing
        GridLayout {
            id: credentialsLayout
            columns: 2
            anchors.left:  parent.left
            anchors.right: parent.right
            rowSpacing:    inner_spacing
            columnSpacing: inner_spacing

            Label {
                text: "E-Mail:"
                anchors.baseline: emailField.baseline
            }
            TextField {
                id: emailField
                Layout.fillWidth: true
                placeholderText: "pfadi@pbs.ch"
                width: 40
            }

            Label {
                text: "Passwort:"
                anchors.baseline: passwordField.baseline
            }
            TextField {
                id: passwordField
                Layout.fillWidth: true
                echoMode: TextInput.Password
            }
        }

        Button {
            id: loginButton
            text: "Login"
            isDefault: true
            anchors.horizontalCenter: parent.horizontalCenter

            onClicked: stackView.push({item: secondStep})

            BusyIndicator {
                anchors.right: parent.left
                anchors.rightMargin: inner_spacing
                anchors.verticalCenter: parent.verticalCenter

                height: parent.height * 0.6
                width: height
            }
        }
    }

    property Component secondStep : Column {
        spacing: inner_spacing
        RowLayout {
            anchors.left:  parent.left
            anchors.right: parent.right

            Label {
                text: "Gruppe:"
                anchors.baseline: groupComboBox.baseline
            }
            ComboBox {
                id: groupComboBox
                Layout.fillWidth: true
                model: ["Abteilung Stern", "Abteilung Chuuz"]
            }
        }

        Button {
            id: printButton
            text: "Drucken"
            isDefault: true
            anchors.horizontalCenter: parent.horizontalCenter

            BusyIndicator {
                anchors.right: parent.left
                anchors.rightMargin: inner_spacing
                anchors.verticalCenter: parent.verticalCenter

                height: parent.height * 0.6
                width: height
            }
        }
    }

    StackView {
        anchors.fill: parent
        anchors.margins: margin

        id: stackView
        initialItem: { item: firstStep }

        delegate: StackViewDelegate {
            function transitionFinished(properties)
            {
                properties.exitItem.y = -contentHeight;
            }

            pushTransition: StackViewTransition {
                PropertyAnimation {
                    target: enterItem
                    property: "y"
                    from: +contentHeight
                    to: 0
                }
                PropertyAnimation {
                    target: exitItem
                    property: "y"
                    from: 0
                    to: -contentHeight
                }
            }
        }
    }
}

