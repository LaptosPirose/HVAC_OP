import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python GUI Development!")
        self.setGeometry(100, 10, 800, 600)
        self.setFixedWidth(800)
        self.setFixedHeight(600)

        self.setStyleSheet("background-color:green")
        self.setWindowOpacity(0.3)

        # self.setWindowIcon(QIcon('PyQt6/5968350.png'))
        self.setWindowIcon(QIcon('PyQt6/images/icon.png'))


app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec())
