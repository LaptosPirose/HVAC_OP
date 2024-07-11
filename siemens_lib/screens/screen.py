from PyQt6.QtWidgets import QApplication, QWidget
import sys


class WidgetWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 800, 1000, 800)
        self.setWindowTitle("Widgets")


app = QApplication(sys.argv)
widget = WidgetWindow()
widget.show()
sys.exit(app.exec())
