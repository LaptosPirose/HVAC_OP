from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QPushButton, QLabel, QMenu, QGridLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize

import sys
import os

current_path = os.getcwd()
path = os.path.join(current_path, 'PyQt6/images/')


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development - QGridlayout")
        self.setGeometry(100, 100, 1200, 700)

        self.setWindowIcon(QIcon(path + '5968350.png'))

        qlabel = QLabel(self)
        qlabel.setText(f"Path added to project: {path}")
        qlabel.setFont(QFont('Times New Roman', 14))
        qlabel.setStyleSheet("color: red")

        grid = QGridLayout()

        btn1 = QPushButton('click One')
        btn2 = QPushButton('click Two')
        btn3 = QPushButton('click Three')
        btn4 = QPushButton('click Four')
        btn5 = QPushButton('click Five')
        btn6 = QPushButton('click Six')
        btn7 = QPushButton('click Seven')
        btn8 = QPushButton('click Eight')

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)

        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)

        self.setLayout(grid)


app = QApplication(sys.argv)
window = Widget()

window.show()
sys.exit(app.exec())
