from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QRadioButton, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Frame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development -  QRadioButton")
        self.setGeometry(200, 200, 800, 580)
        self.setWindowIcon(QIcon('PyQt6/images/5968350.png'))

        label = QLabel("Python GUI Development", self)
        label.move(20, 20)

        label2 = QLabel("New Label with different properties", self)
        label2.move(20, 50)
        
        self.create_radio_button()
        
    def create_radio_button(self):
        hbox = QHBoxLayout()
        radio1 = QRadioButton("Option 1")
        radio2 = QRadioButton("Option 2")
        radio3 = QRadioButton("Option 3")
        radio4 = QRadioButton("Option 4")
        radio4.setChecked(True)
        
        hbox.addWidget(radio1)
        hbox.addWidget(radio2)
        hbox.addWidget(radio3)
        hbox.addWidget(radio4)
        
        self.setLayout(hbox)


app = QApplication(sys.argv)
window = Frame()

window.show()
sys.exit(app.exec())
