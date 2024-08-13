from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development - QVBoxLayout")
        self.setGeometry(200, 200, 800, 680)
        self.setWindowIcon(QIcon('PyQt6/images/5968350.png'))

        btn1 = QPushButton("Click One")
        btn2 = QPushButton("Click Two")
        btn3 = QPushButton("Click Three")
        btn4 = QPushButton("Click Four")

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        #vbox.addSpacing(120)
        vbox.addStretch(5)
        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Widget()

window.show()
sys.exit(app.exec())
