from windows_modules.secondary_window import SecondaryDialog
import os
import sys
import time
import datetime

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QDialog
from PyQt6.QtWidgets import QMenu, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QScreen, QFont, QIcon, QAction, QPixmap
from PyQt6.QtCore import QTimer


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        update_time_rate = 1000
        images_update_rate = 3000

        # Get path to turn shorter paths
        current_path = os.getcwd()
        print(current_path)

        # Path to images
        image_path = os.path.join(current_path, 'windows_modules/images/')
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
        self.file_menu = self.menu_bar.addMenu("Configurações")

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

        self.label_posto = QLabel(self)
        self.label_posto.setFixedSize(200, 22)  # width: 200, height: 22
        self.label_posto.move(5, 20)
        self.label_posto.setText(f"Posto: {self.text}")
        self.label_posto.setFont(QFont('Arial', 10))
        self.label_posto.setStyleSheet("color: blue")

        self.datetime_text = datetime.datetime.now()

        self.label_datetime = QLabel(self)
        self.label_datetime.setFixedSize(200, 22)  # width: 200, height: 22
        self.label_datetime.move(5, 40)
        self.label_datetime.setText(f"Data e Hora: {self.datetime_text}")
        self.label_datetime.setFont(QFont('Arial', 10))
        self.label_datetime.setStyleSheet("color: blue")

        # Set up the QLabel to display images

        self.label_panel = QLabel(self)
        # Scale image to fit the label size
        self.label_panel.setScaledContents(True)
        # Move panel to center
        self.label_panel.move(80, 80)
        # Set panel size
        self.label_panel.setFixedSize(1000, 800)  # width: 100, height: 100
        # Define first imagem to display
        pixmap = QPixmap(image_path+"python.png")
        self.label_panel.setPixmap(pixmap)

        # Image paths (change this to your actual images)
        self.images = [image_path+"mario.gif",
                       image_path+"icon.png", image_path+"python.png"]
        self.current_image_index = 0  # Índice da imagem atual

        # Configurar o QTimer para alternar as imagens a cada 1 segundo
        self.timer_datetime = QTimer(self)
        self.timer_datetime.timeout.connect(self.update_time)
        # A cada 1000 ms (1 segundo), a função `change_image` e `update_time` serão chamadas
        self.timer_datetime.start(update_time_rate)

        self.timer_update_images = QTimer(self)
        self.timer_update_images.timeout.connect(self.change_image)
        self.timer_update_images.start(images_update_rate)

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

    def update_image(self):
        """Atualiza a imagem exibida no QLabel"""
        pixmap = QPixmap(self.images[self.current_image_index])
        self.label_panel.setPixmap(pixmap)

    def change_image(self):
        """Altera a imagem de forma sequencial"""
        # Avançar para a próxima imagem
        self.current_image_index = (
            self.current_image_index + 1) % len(self.images)
        print(self.current_image_index)
        self.update_image()

    def update_time(self):
        self.datetime_text = datetime.datetime.now()
        self.label_datetime.setText(f"Data e Hora: {self.datetime_text}")
