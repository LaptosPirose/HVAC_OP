from windows_modules.main_window import MainWindow
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QScreen

# Create application window
app = QApplication(sys.argv)
window = MainWindow(app)


window.show()
sys.exit(app.exec())
