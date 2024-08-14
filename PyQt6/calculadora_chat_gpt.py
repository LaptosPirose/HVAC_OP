import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuração da janela principal
        self.setWindowTitle('Calculadora')
        self.setGeometry(100, 100, 300, 400)

        # Layout da interface
        grid = QGridLayout()
        self.setLayout(grid)

        # Display da calculadora
        self.display = QLineEdit()
        grid.addWidget(self.display, 0, 0, 1, 4)

        # Botões
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '←',
            '1', '2', '3', '-', '',
            '0', '.', '=', '+', ''
        ]

        positions = [(i, j) for i in range(1, 6) for j in range(4)]

        for position, button_text in zip(positions, buttons):
            if button_text == '':
                continue
            button = QPushButton(button_text)
            button.clicked.connect(self.on_click)
            grid.addWidget(button, *position)

    def on_click(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.display.clear()
        elif text == '←':
            current_text = self.display.text()
            self.display.setText(current_text[:-1])
        elif text == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception:
                self.display.setText('Erro')
        else:
            current_text = self.display.text()
            new_text = current_text + text
            self.display.setText(new_text)

def main():
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

