from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QPushButton, QLabel, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize

import sys
import os

current_path = os.getcwd()
path = os.path.join(current_path, 'PyQt6/images/')

print(current_path)
print(path)


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development - QPushButton")
        self.setGeometry(100, 100, 1200, 700)

        self.setWindowIcon(QIcon(path + '5968350.png'))

        qlabel = QLabel(self)
        qlabel.setText(f"Path added to project: {path}")
        qlabel.setFont(QFont('Times New Roman', 14))
        qlabel.setStyleSheet("color: red")

        # Populate screens with button
        self.create_buttons()

    def create_buttons(self):
        btn1 = QPushButton("Click Me", self)
        btn1.move(10, 40)

        btn2 = QPushButton(self)
        btn2.setText("Another Button")
        btn2.move(10, 80)
        btn2.setGeometry(10, 80, 400, 80)
        btn2.setFont(QFont('Sans-serif', 18, QFont.Weight.Bold))
        # btn2.setStyleSheet("background-color: lightgreen; color: white")
        # Set Icon
        btn2.setIcon(QIcon(path+'icon.png'))
        # Set Icon Size
        btn2.setIconSize(QSize(50, 50))

        menu = QMenu()
        menu.addAction("File")
        menu.addAction("Add")
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        menu.setFont(QFont('Arial',22))
        menu.setStyleSheet("background-color:lightgray")

        btn2.setMenu(menu)


app = QApplication(sys.argv)
window = Widget()

window.show()
sys.exit(app.exec())
