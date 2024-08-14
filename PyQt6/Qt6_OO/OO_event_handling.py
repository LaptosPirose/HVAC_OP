from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
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

        self.setWindowIcon(QIcon(path + 'icon.png'))

        qlabel = QLabel(self)
        qlabel.setText(f"Path added to project: {path}")
        qlabel.setFont(QFont('Times New Roman', 18))
        qlabel.setStyleSheet("color: red")


app = QApplication(sys.argv)
window = Widget()

window.show()
sys.exit(app.exec())
