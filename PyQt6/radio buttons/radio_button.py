from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QRadioButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Frame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development -  QRadioButton")
        self.setGeometry(200, 200, 800, 580)
        self.setWindowIcon(QIcon('PyQt6/images/5968350.png'))
        
        self.create_radio_button()
        
    def create_radio_button(self):
        hbox = QHBoxLayout()
        radio1 = QRadioButton("Option 1")
        radio1.clicked.connect(self.radio_button_checked)
        radio2 = QRadioButton("Option 2")
        radio2.toggled.connect(self.radio_button_checked)
        radio3 = QRadioButton("Option 3")
        radio4 = QRadioButton("Option 4")
        radio4.setChecked(True)
        
        hbox.addWidget(radio1)
        hbox.addWidget(radio2)
        hbox.addWidget(radio3)
        hbox.addWidget(radio4)
        
        self.label = QLabel("Python GUI Development", self)
        # label.move(20, 20)

        self.label2 = QLabel("New Label with different properties", self)
        # label2.move(20, 50)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.label2)
        vbox.addLayout(hbox)
        
        
        
        self.setLayout(vbox)

    def radio_button_checked(self):
        sender = self.sender()
        if sender.isChecked():
            print(f"Radio button {sender.text()} is checked")
            self.label.setText(f"Radio button {sender.text()} is checked")

app = QApplication(sys.argv)
window = Frame()

window.show()
sys.exit(app.exec())
