import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QDialog
from PyQt6.QtWidgets import QMenu, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QScreen, QFont, QIcon, QAction


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
        self.open_dialog_action = QAction("Configure PLC IP", self)
        self.open_dialog_action.triggered.connect(
            self.open_configura_ip)
        self.file_menu.addAction(self.open_dialog_action)

        # Add an action to open the secondary dialog
        self.open_dialog_action1 = QAction("Configure Número do Posto", self)
        self.open_dialog_action1.triggered.connect(self.open_configura_posto)
        self.file_menu.addAction(self.open_dialog_action1)

        self.text = "OP__HVAC OP__X!!"

        self.qlabel = QLabel(self)
        self.qlabel.setFixedSize(200, 22)  # width: 200, height: 22
        self.qlabel.move(5, 20)
        self.qlabel.setText(f"Posto: {self.text}")
        self.qlabel.setFont(QFont('Arial', 10))
        self.qlabel.setStyleSheet("color: blue")

    def open_configura_ip(self):
        secondary_dialog = SecondaryDialog(
            self.screen_width, self.screen_height, "Configurações", "Configura IP do PLC com o qual aaplicação vai comunicar.")
        secondary_dialog.exec()
        print(
            f"Largura da tela -> {self.screen_width} Altura -> {self.screen_height}")

    def open_configura_posto(self):
        secondary_dialog = SecondaryDialog(
            self.screen_width, self.screen_height, "Configurações", "Configura número do posto.")
        secondary_dialog.exec()
        print(
            f"Largura da tela -> {self.screen_width} Altura -> {self.screen_height}")


class SecondaryDialog(QDialog):
    def __init__(self, width, height, text_title, text_label):
        super().__init__()

        # Set dialog properties
        self.text_title = text_title
        self.text_label = text_label

        self.box_x = 100
        self.box_y = 100
        self.box_width = int(width / 2) - 400
        self.box_height = int(height / 2) - 400

        self.setWindowTitle(f"{self.text_title}")
        self.setGeometry(10, 10, self.box_width, self.box_height)

        # Create a label and a close button
        label = QLabel(
            f"{text_label}", self)
        label.setFixedWidth(self.box_width-50)
        # self.setStyleSheet(
        # "QPushButton{background-color : green} QLabel{background-color : yellow} QDialog{background-color : lightgray}")

        label.move(self.box_x - 50, self.box_y-100)

        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close)
        ok_button = QPushButton("Ok", self)

        layout = QHBoxLayout()
        # layout.addWidget(label)
        layout.addWidget(close_button)
        layout.addWidget(ok_button)
        self.setLayout(layout)
