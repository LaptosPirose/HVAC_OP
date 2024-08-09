from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QFrame
from PyQt6.QtGui import QIcon, QFont
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development")
        self.setGeometry(300, 300, 1200, 600)
        self.setWindowIcon(QIcon('PyQt6/images/5968350.png'))


        self.frame_direita = Frame_direito()
        self.setCentralWidget(self.frame_direita)

        self.frame_central = Frame()
        self.setCentralWidget(self.frame_central)

class Frame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development")
        self.setGeometry(200, 200, 800, 580)
        self.setWindowIcon(QIcon('PyQt6/images/5968350.png'))

        self.frame = QFrame(self)
        self.frame.setGeometry(10, 10, 800, 580)
        self.frame.setStyleSheet("background-color: #f0f0f0")

        label = QLabel("Python GUI Development", self.frame)
        label.move(20, 20)

        label2 = QLabel("New Label with different properties", self.frame)
        label2.move(20, 50)


class Frame_direito(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development")
        self.setGeometry(200, 200, 400, 580)
        self.setWindowIcon(QIcon('PyQt6/images/5968350.png'))

        self.frame = QFrame(self)
        self.frame.setGeometry(810, 10, 400, 580)
        self.frame.setStyleSheet("background-color: #f0f0f0")

        label = QLabel("Python GUI Development", self.frame)
        label.move(20, 20)

        label2 = QLabel("New Label with different properties", self.frame)
        label2.move(20, 50)


app = QApplication(sys.argv)
window = MainWindow()

window.show()
sys.exit(app.exec())
