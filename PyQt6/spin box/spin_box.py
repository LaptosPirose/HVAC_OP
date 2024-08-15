from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QSpinBox
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Frame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development -  QRadioButton")
        self.setGeometry(200, 200, 800, 580)
        self.setWindowIcon(QIcon('PyQt6/images/5968350.png'))
        self.setFont(QFont('Verdana', 16))

        self.label = QLabel("Lap Top Price", self)
        self.label.resize(500, 22)

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Text here!")
        self.line_edit.move(0, 60)
        self.line_edit.resize(400, 40)

        self.spin_box = QSpinBox(self)
        self.spin_box.move(0, 120)
        self.spin_box.setMaximum(10)
        self.spin_box.setWrapping(True)
        self.spin_box.valueChanged.connect(self.spin_box_change)

    def spin_box_change(self):
        print(f"Lap Top Price: ${self.spin_box.value()}")
        self.label.setText(f"Lap Top Price: ${self.spin_box.value() * 1000}")


app = QApplication(sys.argv)
window = Frame()

window.show()
sys.exit(app.exec())
