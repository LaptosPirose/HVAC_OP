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
        
    
    

app = QApplication(sys.argv)
window = Frame()

window.show()
sys.exit(app.exec())
