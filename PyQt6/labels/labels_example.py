from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Development")
        self.setGeometry(300, 100, 1200, 600)
        self.setWindowIcon(QIcon('PyQt6/5968350.png'))

        label = QLabel("Python GUI Development", self)

        label1 = QLabel(self)
        label1.setText("New Label with different properties")
        label1.move(0, 18)
        label1.clear()

        label2 = QLabel(self)
        label2.setText("New Label with different properties 3rd line")
        label2.setFont(QFont("Verdana", 14))
        label2.setStyleSheet("color:red; font-weight:bold")
        label2.move(0, 36)

        label3 = QLabel(str(20), self)
        label3.setNum(154)
        label3.move(0, 64)


app = QApplication(sys.argv)
window = Window()


window.show()
sys.exit(app.exec())
