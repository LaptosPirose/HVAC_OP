# Imported from PyQt6 site

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
def **init**(self):
super().**init**()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))



if **name** == "**main**":
app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

# Simple main window

import sys
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()

window.statusBar().showMessage("QtWidgets")

window.show()
sys.exit(app.exec())

# Simple Widget window

import sys
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()

## Doesn't support status bar or menu bar

window.show()
sys.exit(app.exec())

# Dialog Window

## Also does not support menu bar or status bar and sometimes doesn't show maximize or minimize buttons
import sys
from PySide6.QtWidgets import QApplication, QDialog

app = QApplication(sys.argv)
window = QDialog()


window.show()
sys.exit(app.exec())
