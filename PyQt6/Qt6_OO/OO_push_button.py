from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont, QMovie, QPixmap

import sys
import os

current_path = os.getcwd()
path = os.path.join(current_path, 'PyQt6/images/')

print(current_path)
print(path)


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Development - QPushButton")
        self.setGeometry(100, 100, 1200, 700)

        self.setWindowIcon(QIcon(path + 'icon.png'))

        qlabel = QLabel(self)
        qlabel.setText(f"Path added to project: {path}")
        qlabel.setStyleSheet("color: red")

        qlabel1 = QLabel(self)
        qlabel1.setNum(1866)
        qlabel1.move(0, 22)
        # Apaga o conteúdo da Label
        qlabel1.clear()

        pixmap = QPixmap(path + '5968350.png')
        qlabel_pixmap = QLabel(self)
        qlabel_pixmap.setPixmap(pixmap)
        qlabel_pixmap.move(0, 44)

        # Insert Movie
        # movie = QMovie(path+'mario.gif')

        # qlabel_movie = QLabel(self)
        # qlabel_movie.setMovie(movie)
        # qlabel_movie.move(0, 44)

        # movie.setSpeed(200)
        # movie.start()


app = QApplication(sys.argv)
window = Widget()

window.show()
sys.exit(app.exec())
