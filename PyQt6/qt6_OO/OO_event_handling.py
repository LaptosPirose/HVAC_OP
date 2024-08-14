from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont, QMovie, QPixmap

import sys
import os

current_path = os.getcwd()
path = os.path.join(current_path, 'PyQt6/images/')

print(current_path)
print(path)


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development - Event Handling")
        self.setGeometry(100, 100, 1200, 700)

        self.setWindowIcon(QIcon(path + '5968350.png'))

        # qlabel = QLabel(self)
        # qlabel.setText(f"Path added to project: {path}")
        # qlabel.setFont(QFont('Times New Roman', 18))
        # qlabel.setStyleSheet("color: red")

        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        btn1 = QPushButton('click Me To change Text')
        btn1.clicked.connect(self.clicked_event)
        self.label1 = QLabel("Default Text")

        hbox.addWidget(btn1)
        hbox.addWidget(self.label1)
        self.setLayout(hbox)

    def clicked_event(self):
        self.label1.setText('Button Clicked!')
        self.label1.setFont(QFont('Sans-serif', 20, QFont.Weight.ExtraBold))


app = QApplication(sys.argv)
window = Widget()

window.show()
sys.exit(app.exec())
