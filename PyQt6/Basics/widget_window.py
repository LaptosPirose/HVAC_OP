import sys
from PySide6.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)
window = QWidget()

# Doesn't support status bar or menu bar

window.show()
sys.exit(app.exec())
