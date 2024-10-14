import sys
import os
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap
import random


class ImagePanel(QWidget):
    def __init__(self):
        super().__init__()

        # Get path to turn shorter paths
        current_path = os.getcwd()
        print(current_path)

        # Path to images
        image_path = os.path.join(current_path, 'windows_modules/images/')

        # Set up the QLabel to display images
        self.label = QLabel(self)
        # Set initial image
        self.label.setPixmap(QPixmap(image_path + "icon.png"))
        self.label.setScaledContents(True)  # Scale image to fit the label size

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Set up the QTimer to update the image every second (1000 ms)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change_image)
        self.timer.start(2000)

        # Image paths (change this to your actual images)
        self.images = [image_path+"mario.gif",
                       image_path+"icon.png", image_path+"python.png"]

    def change_image(self):
        # Pick a random image from the list
        new_image = random.choice(self.images)
        # Update the QLabel with the new image
        self.label.setPixmap(QPixmap(new_image))


# # Set up the QApplication and main window
# app = QApplication(sys.argv)
# window = ImagePanel()
# window.setWindowTitle("Image Panel")
# window.resize(400, 300)  # Adjust the size of the window
# window.show()

# # Run the application loop
# sys.exit(app.exec())
