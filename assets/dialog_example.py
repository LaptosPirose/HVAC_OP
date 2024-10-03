import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QAction


class SecondaryDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set dialog properties
        self.setWindowTitle("Secondary Screen")
        self.setGeometry(400, 400, 300, 200)

        # Create a label and a close button
        layout = QVBoxLayout()
        label = QLabel("This is a secondary screen (QDialog)", self)
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close)

        layout.addWidget(label)
        layout.addWidget(close_button)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set main window properties
        self.setWindowTitle("PyQt6 Main Window with Dialog Example")
        self.setGeometry(300, 300, 400, 300)

        # Create the menu bar
        menubar = self.menuBar()

        # Create File menu
        file_menu = menubar.addMenu("File")

        # Add an action to open the secondary dialog
        open_dialog_action = QAction("Open Secondary Screen", self)
        open_dialog_action.triggered.connect(self.open_dialog)
        file_menu.addAction(open_dialog_action)

        # Add an exit action
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def open_dialog(self):
        # Instantiate and show the dialog
        dialog = SecondaryDialog()
        dialog.exec()  # Modal dialog (blocks interaction with main window until closed)


# Main Application Loop
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
