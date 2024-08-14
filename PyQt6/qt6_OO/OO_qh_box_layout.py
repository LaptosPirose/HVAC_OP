from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development - QHBoxLayout")
        self.setGeometry(200, 200, 800, 680)
        self.setWindowIcon(QIcon('PyQt6/images/5968350.png'))

        btn1 = QPushButton("Click One")
        btn2 = QPushButton("Click Two")
        btn3 = QPushButton("Click Three")
        btn4 = QPushButton("Click Four")

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        #hbox.addSpacing(120)
        hbox.addStretch(5)
        self.setLayout(hbox)


app = QApplication(sys.argv)
window = Widget()

window.show()
sys.exit(app.exec())
