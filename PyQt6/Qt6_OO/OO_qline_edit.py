from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QFrame, QPushButton, QLineEdit
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development - QLineEdit")
        self.setGeometry(200, 200, 800, 680)
        self.setWindowIcon(QIcon('PyQt6/images/5968350.png'))

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont('Arial', 18, QFont.Weight.Bold))
        line_edit.setGeometry(10, 10, 600, 50)
        line_edit.setPlaceholderText("Enter your text here...")
        
        # line_edit.setText("Enter your text")
        # line_edit.setEnabled(False)
        
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        


app = QApplication(sys.argv)
window = Widget()

window.show()
sys.exit(app.exec())
