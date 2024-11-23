from windows_modules.secondary_window import SecondaryDialog
import os
import sys
import time
import datetime

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QDialog
from PyQt6.QtWidgets import QMenu, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QScreen, QFont, QIcon, QAction, QPixmap
from PyQt6.QtCore import QTimer


class SetMainWindow():
    def __init__(self, window, app):
        # Get the screen geometry
        self.screen = app.primaryScreen()

        self.screen_width = self.screen.size().width()
        self.screen_height = self.screen.size().height()

        # Configuring screen
        self.setGeometry(0, 0, self.screen_width, self.screen_height)
        self.setWindowTitle("HVAC OP__X!")
        print(f"Screen width: {
              self.screen_width} - Screen height: {self.screen_height}")
        # Set the window title
        self.setWindowTitle("HVAC OP__!")
