#!/usr/bin/env python3

import sys

from PyQt5.QtCore import pyqtProperty, QObject, QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine

# Create the application instance.
app = QApplication(sys.argv)

# Create a QML engine.
engine = QQmlEngine()

# Create a component factory and load the QML script.
component = QQmlComponent(engine)
component.loadUrl(QUrl('main.qml'))

# get window
window = component.create()

window.show()

app.exec_()
