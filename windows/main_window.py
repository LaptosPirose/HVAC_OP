import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QDialog
from PyQt6.QtWidgets import QMenu, QMessageBox, QPushButton, QVBoxLayout
from PyQt6.QtGui import QScreen, QFont, QIcon, QAction


class SecondaryDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set dialog properties
        self.setWindowTitle("Secondary Screen")
        # self.setGeometry(self.screen_width / 2 - 150,
        #                  self.screen_height / 2 - 100, 300, 200)
        self.setGeometry(400, 400, 300, 200)

        # Create a label and a close button
        label = QLabel("This is a secondary screen (QDialog)", self)
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(close_button)
        self.setLayout(layout)


class SecondaryDialog1(QDialog):
    def __init__(self):
        super().__init__()

        # Set dialog properties
        self.setWindowTitle("Secondary Screen")
        self.setGeometry(400, 400, 300, 200)

        # Create a label and a close button
        layout = QVBoxLayout()
        label = QLabel("This is a secondary screen (QDialog)", self)
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close)

        layout.addWidget(label)
        layout.addWidget(close_button)
        self.setLayout(layout)


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
        self.setFont(QFont("Arial", 11))

        # Generate menu
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")

        # Add an action to open the secondary dialog
        self.open_dialog_action = QAction("Open Secondary Screen", self)
        self.open_dialog_action.triggered.connect(self.open_secondary_screen)
        self.file_menu.addAction(self.open_dialog_action)

        # Add an action to open the secondary dialog
        self.open_dialog_action1 = QAction("Open Secondary Screen 1", self)
        self.open_dialog_action1.triggered.connect(self.open_dialog)
        self.file_menu.addAction(self.open_dialog_action1)

        self.text = "OP__HVAC OP__X!!"

        self.qlabel = QLabel(self)
        self.qlabel.setFixedSize(200, 22)  # width: 200, height: 22
        self.qlabel.move(5, 20)
        self.qlabel.setText(f"Posto: {self.text}")
        self.qlabel.setFont(QFont('Arial', 10))
        self.qlabel.setStyleSheet("color: blue")

    def open_secondary_screen(self):
        secondary_dialog = SecondaryDialog()
        secondary_dialog.exec()

    def open_dialog(self):
        # Instantiate and show the dialog
        dialog = SecondaryDialog1()
        dialog.exec()  # Modal dialog (blocks interaction with main window until closed)
