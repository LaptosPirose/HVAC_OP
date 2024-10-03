import os
import sys
import random
import time

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QDialog
from PyQt6.QtWidgets import QMenu, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QScreen, QFont, QIcon, QAction, QPixmap
from PyQt6.QtCore import QTimer


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
