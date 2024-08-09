import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


app = QApplication(sys.argv)
window = QMainWindow()

# Creating a Menu Bar
window.menuBar().addMenu("Menu")

# Setting screen size
window.setGeometry(200, 200, 800, 600)

# Setting window title
window.setWindowTitle("Python GUI Development")

# Creating a status bar
window.statusBar().showMessage("QtWidgets")

window.show()
sys.exit(app.exec())
