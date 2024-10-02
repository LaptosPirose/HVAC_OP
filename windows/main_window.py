import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QScreen, QFont, QIcon


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        # Get the screen object
        self.screen = app.primaryScreen()

        # Get the screen geometry
        self.screen_width = self.screen.size().width()
        self.screen_height = self.screen.size().height()

        # Configuring screen
        self.setGeometry(0, 0, self.screen_width, self.screen_height)
        self.setWindowTitle("HVAC OP__X!")
        print(f"Screen width: {
              self.screen_width} - Screen height: {self.screen_height}")
        # Set the window title
        self.setWindowTitle("HVAC OP__!")

        # Set the window icon
        self.setWindowIcon(QIcon("windows/images/python.png"))

        # Set the font size for the window
        self.setFont(QFont("Arial", 24))

        qlabel = QLabel(self)
        # qlabel.setText(f"Path added to project: {path}")
        qlabel.setText(f"Time")
        qlabel.setFont(QFont('Times New Roman', 18))
        qlabel.setStyleSheet("color: red")
