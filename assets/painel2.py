import sys
import os
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap


class ImagePanel(QWidget):
    def __init__(self):
        super().__init__()

        # Get path to turn shorter paths
        current_path = os.getcwd()
        print(current_path)

        # Path to images
        image_path = os.path.join(current_path, 'windows/images/')

        # Criação do QLabel para exibir as imagens
        self.label = QLabel(self)
        # Escalar a imagem para preencher o QLabel
        self.label.setScaledContents(True)

        # Definindo uma lista de imagens (adicione os caminhos das suas imagens)
        self.images = [image_path+"mario.gif",
                       image_path+"icon.png", image_path+"python.png"]
        self.current_image_index = 0  # Índice da imagem atual

        # Carregue a primeira imagem
        self.update_image()

        # Layout para o painel
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Configurar o QTimer para alternar as imagens a cada 1 segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change_image)
        # A cada 1000 ms (1 segundo), a função `change_image` será chamada
        self.timer.start(1000)

    def update_image(self):
        """Atualiza a imagem exibida no QLabel"""
        pixmap = QPixmap(self.images[self.current_image_index])
        self.label.setPixmap(pixmap)

    def change_image(self):
        """Altera a imagem de forma sequencial"""
        # Avançar para a próxima imagem
        self.current_image_index = (
            self.current_image_index + 1) % len(self.images)
        self.update_image()


# Configurando a aplicação PyQt6
app = QApplication(sys.argv)
window = ImagePanel()
window.setWindowTitle("Painel de Imagens Sequenciais")
window.resize(400, 300)  # Tamanho da janela
window.show()

# Iniciar o loop de eventos da aplicação
sys.exit(app.exec())
