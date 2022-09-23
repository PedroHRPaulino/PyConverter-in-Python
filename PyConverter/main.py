# IMPORTANDO AS BIBLIOTECAS
from frame import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PIL import Image
import sys
import os



# AQUI ESTAMOS CRIANDO UMA CLASSE MAIN WINDOW E HERDANDO AS PROPRIEDADES DO NOSSO ARQUIVO FRAME.PY(NOSSA JANELA)
class MainWindow(QMainWindow, Ui_MainWindow):
    # AQUI INICIAMOS COM O NOSSO MÉTODO CONSTRUTOR DA CLASSE, É AQUI QUE VAMOS COLOCAR OS ELEMENTOS E FUNÇÕES DE CADA UM)
    def __init__(self):
        super(MainWindow, self).__init__()  # AQUI ESTAMOS USANDO O METODO SUPER PARA HERDAR TUDO NA CLASSE MAIN WINDOW
        self.setupUi(self)  # AQUI ESTAMOS PUXANDO TODAS AS CONFIGURAÇÕES DE NOSSA JANELA
        self.setWindowTitle("PyConverter")  # AQUI ESTAMOS COLOCANDO O TITULO DE NOSSA JANELA
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)
        self.txt_oath.text()
        self.tiff.isChecked()
        self.png.isChecked()
        self.jpeg.isChecked()
        self.file = ''
        self.file2 = ''
        self.pushButton.clicked.connect(self.open)
        self.converter.clicked.connect(self.convert)

    def open(self):
        self.file, _ = QFileDialog.getOpenFileName(self, "Abrir um arquivo de imagen","Desktop\\","*.*")


        self.file = str(self.file)
        arquivo = open(self.file, "r")
        with arquivo:
            self.txt_oath.setText(self.file)

    def convert(self):
        if self.jpeg.isChecked() == True:
            path = self.txt_oath.text()
            img = Image.open(path).convert('RGB')
            img.save(path.replace("png", "jpg"))
        elif self.png.isChecked() == True:
            path = self.txt_oath.text()
            img = Image.open(path).convert('RGB')
            img.save(path.replace("jpg", "png"))
        elif self.tiff.isChecked() == True:
            path = self.txt_oath.text()
            img = Image.open(path).convert('RGB')
            img.save(path.replace("jpg", "tiff")) or img.save(path.replace("png", "tiff"))


if __name__ == "__main__":  # EXECUTE TODAS AS LINHAS ACIMA, MENOS OS ITENS DESCRITOS ABAIXO
    app = QApplication(sys.argv)  # APP DEFINIDO
    window = MainWindow()  # JANELA
    window.show()  # MOSTRAR JANELA
    app.exec_()  # EXECUTAR O APP