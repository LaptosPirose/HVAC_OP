### Python QT6 Guide

#### Create a new simple screen

3 tipos de window - Main Window - app window - Dialogo - interações curtas - Widget - Para uso com interfaces como teclado, mouse e etc.

O código abaixo cria uma Widget:

    from PyQt6.QtWidgets import QApplication, QWidget
    import sys

    app = QApplication(sys.argv)
    window = QWidget()
    window.show()

    sys.exit(app.exec())

Criar uma Main Window:

    from PyQt6.QtWidgets import QApplication, QMainWindow
    import sys

    app = QApplication(sys.argv)
    window = QMainWindow()

    window.show()
    window.statusBar().showMessage("Hello Python!")

    sys.exit(app.exec())

    "Note que existe uma Main Window com status bar. A status bar é usada somente em Main Window.

Criando uma Main Window com menu simples e status bar
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

    # Instance of QApplication
    app = QApplication(sys.argv)
    # Instance of window
    window = QMainWindow()

    window.statusBar().showMessage("Hello Python!")
    window.menuBar().addMenu('File')


    window.show()
    sys.exit(app.exec())

Criando uma tela Dialog.

    from PyQt6.QtWidgets import QApplication, QDialog
    import sys

    # Instance of QApplication
    app = QApplication(sys.argv)
    # Instance of window
    window = QDialog()

    # window.statusBar().showMessage("Hello Python!")
    # window.menuBar().addMenu('File')


    window.show()
    sys.exit(app.exec())

    Note que a parte de status bar e menu bar estão comentadas, porque não é possível
    inserir uma status bar ou menu bar numa Dialog

    