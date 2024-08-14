from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QIcon
import sys

app = QApplication(sys.argv)
window = QMainWindow()

window.setWindowTitle("Python")
window.setGeometry(200, 200, 800, 600)
window.setWindowIcon(QIcon('PyQt6/images/5968350.png'))

menu = window.menuBar().addMenu("File")

menu.addMenu("Menu Um")
menu.addMenu("Menu Dois")
menu.addSeparator()
menu.addMenu("Menu Três")
menu.addMenu("Menu Quatro")

file_menu = window.menuBar().addMenu("&File")
file_menu.addSection("&File")
file_menu.addSeparator()

label = QLabel("Teste de label", window)
label.setText("Teste de label__ ")
label.move(0, 22)

window.statusBar().showMessage("Python")

window.show()
sys.exit(app.exec())
