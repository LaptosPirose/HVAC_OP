from PyQt6.QtWidgets import QDialog, QApplication
import sys

app = QApplication(sys.argv)
window = QDialog()

"""
    Status bar not permitted
"""
    
window.show()
sys.exit(app.exec())
