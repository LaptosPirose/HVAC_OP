from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QCheckBox, QHBoxLayout, QVBoxLayout, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Frame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development -  QCheckBox")
        self.setGeometry(200, 200, 800, 580)
        self.setWindowIcon(QIcon('PyQt6/images/5968350.png'))

        menu = QMenu("Python")

        self.check1 = QCheckBox(self)
        self.check1.setText("Option 1")
        self.check1.setIcon(QIcon('PyQt6/images/icon.png'))
        self.check1.setIconSize(QSize(60, 60))

        self.check2 = QCheckBox(self)
        self.check2.setText("Option 2")
        self.check2.setIcon(QIcon('PyQt6/images/python.png'))
        self.check2.setIconSize(QSize(60, 60))

        self.check3 = QCheckBox(self)
        self.check3.setText("Option 3")

        self.hbox = QHBoxLayout(self)
        self.hbox.addWidget(self.check1)
        self.hbox.addWidget(self.check2)
        self.hbox.addWidget(self.check3)

        self.setLayout(self.hbox)


app = QApplication(sys.argv)
window = Frame()

window.show()
sys.exit(app.exec())
