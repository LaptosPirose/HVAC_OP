import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QMessageBox
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle("PyQt6 Application Menu Example")
        self.setGeometry(300, 300, 400, 300)

        # Create the menu bar
        menubar = self.menuBar()

        # Create File menu and add actions
        file_menu = menubar.addMenu("File")

        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        file_menu.addSeparator()

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Create Help menu and add actions
        help_menu = menubar.addMenu("Help")

        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def new_file(self):
        QMessageBox.information(self, "New", "New File created!")

    def open_file(self):
        QMessageBox.information(self, "Open", "Opening file...")

    def save_file(self):
        QMessageBox.information(self, "Save", "Saving file...")

    def show_about(self):
        QMessageBox.information(
            self, "About", "This is a PyQt6 menu example application.")


# Main Application Loop
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
