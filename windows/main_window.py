import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtWidgets import QMenu, QMessageBox, QA
from PyQt6.QtGui import QScreen, QFont, QIcon

# from PyQt6.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        # Get path to turn shorter paths
        current_path = os.getcwd()
        print(current_path)

        # Path to images
        image_path = os.path.join(current_path, 'windows/images/')
        print(image_path)

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
        self.setWindowIcon(QIcon(image_path + "python.png"))

        # Set the font size for the window
        self.setFont(QFont("Arial", 24))

        self.text = "OP__HVAC OP__X!!"

        self.qlabel = QLabel(self)
        self.qlabel.setFixedSize(200, 22)  # width: 200, height: 22
        self.qlabel.setText(f"Posto: {self.text}")
        self.qlabel.setFont(QFont('Arial', 10))
        self.qlabel.setStyleSheet("color: blue")
