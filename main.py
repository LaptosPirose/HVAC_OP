import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QScreen


from windows_modules.main_window import MainWindow

# Create application window
app = QApplication(sys.argv)
window = MainWindow(app)


window.show()
sys.exit(app.exec())
