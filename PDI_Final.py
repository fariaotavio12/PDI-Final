# PyQt5 - Criando interfaces gráficas com Python
import os
import shutil
import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget, QMessageBox, QFileDialog
from PyQt5.QtCore import QSize


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_main_window() # chamado ao método
        self.initUI()

    # vai configurar a janela para conseguirmos aplicar o grid
    def setup_main_window(self):
        self.x = 640
        self.y = 480
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Trnasformaçoes de Imagens - Processamento Digital de Imagens")
        self.wid = QWidget(self) # vai receber o grid
        self.setCentralWidget(self.wid) # coloca a variável que vai receber o grid e o coloca no centro da jenaela
        self.layout = QGridLayout() # cria o layout para aplicar dentro da variável wid
        self.wid.setLayout(self.layout) # aplica o layout no grid


    def initUI(self):
        # Criar os widgets (Label, Button, Text, Image)
        #barra de menu
        self.barrademenu = self.menuBar()
        #criar os menus
        self.menuarquivo = self.barrademenu.addMenu("&Arquivo")
        self.menuimagens = self.barrademenu.addMenu("&Imagens")
        self.menusobre = self.barrademenu.addMenu("&Sobre")

        #criar as actions
        self.opcaoabrir = self.menuarquivo.addAction("&Abrir")
        self.opcaoabrir.triggered.connect(self.open_file)
        self.opcaoabrir.setShortcut("Ctrl+A")
        self.opcaoabrir.setCheckable(True)
        self.opcaoabrir.setChecked(False)
        self.menuarquivo.addSeparator()
        self.salvarcomo = self.menuarquivo.addAction("&Salvar Como")
        self.salvarcomo.triggered.connect(self.salvarImagemComo)
        self.salvarcomo.setShortcut("Ctrl+S")


        self.menuarquivo.addSeparator()

        self.opcaofechar = self.menuarquivo.addAction("&Fechar")
        self.opcaofechar.setShortcut("Ctrl+X")
        self.opcaofechar.triggered.connect(self.close)

        #imagens
        self.Colorida = self.menuimagens.addMenu("Transformaçoes Colorida")
        self.transformacaoNegativo = self.Colorida.addAction("Transformaçao Negativo")
        self.transformacaoNegativo.setShortcut("Ctrl+N+E")
        self.transformacaoNegativo.triggered.connect(self.transform_NegativoColorida)
        self.transformacaoGama = self.Colorida.addAction("Transformaçao Gama")
        self.transformacaoGama.setShortcut("Ctrl+E")
        self.transformacaoGama.triggered.connect(self.transform_CorrecaoGamaColorida)
        self.menuimagens.addSeparator()
        self.transformacaoLog = self.Colorida.addAction("Transformaçao Logaritima")
        self.transformacaoLog.setShortcut("Ctrl+W")
        self.transformacaoLog.triggered.connect(self.transform_LogColorida)
        self.menuimagens.addSeparator()
        self.transformacaoSharpen = self.Colorida.addAction("Transformaçao Sharpen")
        self.transformacaoSharpen.setShortcut("Ctrl+W")
        self.transformacaoSharpen.triggered.connect(self.transform_SharpenColorida)
        self.menuimagens.addSeparator()
        self.transformacaoMediana = self.Colorida.addAction("Transformaçao Mediana")
        self.transformacaoMediana.setShortcut("Ctrl+T")
        self.transformacaoMediana.triggered.connect(self.transform_MedianaColorida)
        self.menuimagens.addSeparator()
        self.transformacaoGaussiano = self.Colorida.addAction("Transformaçao Gaussiano")
        self.transformacaoGaussiano.setShortcut("Ctrl+T")
        self.transformacaoGaussiano.triggered.connect(self.transform_GaussianoColorida)
        self.menuimagens.addSeparator()
        self.transformacaoSobel = self.Colorida.addAction("Transformaçao Sobel")
        self.transformacaoSobel.setShortcut("Ctrl+T")
        self.transformacaoSobel.triggered.connect(self.transform_SobelColorida)
        self.menuimagens.addSeparator()
        self.transformacaoBorda = self.Colorida.addAction("Transformaçao Detecçao de Bordas")
        self.transformacaoBorda.setShortcut("Ctrl+T")
        """self.transformacaoBorda.triggered.connect(self.transform_Borda)"""
        self.menuimagens.addSeparator()
        self.transformacaoColoridaParaCinza = self.Colorida.addAction("Transformaçao Colorida Para Cinza")
        self.transformacaoColoridaParaCinza.setShortcut("Ctrl+T")
        self.transformacaoColoridaParaCinza.triggered.connect(self.transform_ConverterCinza)
        self.menuimagens.addSeparator()
        self.transformacaoColoridaParaPreto = self.Colorida.addAction("Transformaçao Colorida Para Preto e Branco")
        self.transformacaoColoridaParaPreto.setShortcut("Ctrl+T")
        """self.transformacaoColoridaParaPreto.triggered.connect(self.transform_ColoridaParaPretoBranco)"""
        self.menuimagens.addSeparator()
        self.transformacaoR = self.Colorida.addAction("Transformaçao RGB -R-")
        self.transformacaoR.setShortcut("Ctrl+T")
        self.transformacaoR.triggered.connect(self.transform_R)
        self.menuimagens.addSeparator()
        self.transformacaoRG = self.Colorida.addAction("Transformaçao RGB -G-")
        self.transformacaoRG.setShortcut("Ctrl+T")
        self.transformacaoRG.triggered.connect(self.transform_G)
        self.menuimagens.addSeparator()
        self.transformacaoRGB = self.Colorida.addAction("Transformaçao RGB -B-")
        self.transformacaoRGB.setShortcut("Ctrl+T")
        self.transformacaoRGB.triggered.connect(self.transform_B)
        self.menuimagens.addSeparator()
        self.transformacaoColoridaPreto = self.Colorida.addAction("Transformaçao Colorida Para Preto")
        self.transformacaoColoridaPreto.setShortcut("Ctrl+T")
        self.transformacaoColoridaPreto.triggered.connect(self.transform_ColoridaPraPreto)
        self.menuimagens.addSeparator()

        self.Cinza = self.menuimagens.addMenu("Transformaçoes Cinza")

        self.transformacaoNegativo = self.Cinza.addAction("Transformaçao Negativo")
        self.transformacaoNegativo.setShortcut("Ctrl+N+E")
        self.transformacaoNegativo.triggered.connect(self.transform_NegativoCinza)
        self.menuimagens.addSeparator()
        self.transformacaoGama = self.Cinza.addAction("Transformaçao Gama")
        self.transformacaoGama.setShortcut("Ctrl+E")
        self.transformacaoGama.triggered.connect(self.transform_CorrecaoGama)
        self.menuimagens.addSeparator()
        self.transformacaoLog = self.Cinza.addAction("Transformaçao Logaritima")
        self.transformacaoLog.setShortcut("Ctrl+W")
        self.transformacaoLog.triggered.connect(self.transform_Log)
        self.menuimagens.addSeparator()
        self.transformacaoSharpen = self.Cinza.addAction("Transformaçao Sharpen")
        self.transformacaoSharpen.setShortcut("Ctrl+W")
        self.transformacaoSharpen.triggered.connect(self.transform_Sharpen)
        self.menuimagens.addSeparator()
        self.transformacaoMediana = self.Cinza.addAction("Transformaçao Mediana")
        self.transformacaoMediana.setShortcut("Ctrl+T")
        self.transformacaoMediana.triggered.connect(self.transform_Mediana)
        self.menuimagens.addSeparator()
        self.transformacaoGaussiano = self.Cinza.addAction("Transformaçao Gaussiano")
        self.transformacaoGaussiano.setShortcut("Ctrl+T")
        self.transformacaoGaussiano.triggered.connect(self.transform_Gaussiano)
        self.menuimagens.addSeparator()
        self.transformacaoSobel = self.Cinza.addAction("Transformaçao Sobel")
        self.transformacaoSobel.setShortcut("Ctrl+T")
        self.transformacaoSobel.triggered.connect(self.transform_Sobel)
        self.menuimagens.addSeparator()
        self.transformacaoBorda = self.Cinza.addAction("Transformaçao Detecçao de Bordas")
        self.transformacaoBorda.setShortcut("Ctrl+T")
        """self.transformacaoBorda.triggered.connect(self.transform_Borda)
        self.menuimagens.addSeparator()"""

        self.menuimagens.addSeparator()
        self.Binaria = self.menuimagens.addMenu("Transformaçoes Binaria")

        self.transformacaoErosao = self.Binaria.addAction("Transformaçao Erosao")
        self.transformacaoErosao.setShortcut("Ctrl+T")
        self.transformacaoErosao.triggered.connect(self.transform_Erosao)
        self.menuimagens.addSeparator()
        self.transformacaoDilatacao = self.Binaria.addAction("Transformaçao Dilatacao")
        self.transformacaoDilatacao.setShortcut("Ctrl+T")
        self.transformacaoDilatacao.triggered.connect(self.transform_Dilatacao)
        self.menuimagens.addSeparator()
        self.transformacaoAbertura = self.Binaria.addAction("Transformaçao Abertura")
        self.transformacaoAbertura.setShortcut("Ctrl+T")
        self.transformacaoAbertura.triggered.connect(self.transform_Abertura)
        self.menuimagens.addSeparator()
        self.transformacaoFechamento = self.Binaria.addAction("Transformaçao Fechamento")
        self.transformacaoFechamento.setShortcut("Ctrl+T")
        self.transformacaoFechamento.triggered.connect(self.transform_Fechamento)
        self.menuimagens.addSeparator()
        self.transformacaoBordaBinaria = self.Binaria.addAction("Transformaçao Detecçao De Borda")
        self.transformacaoBordaBinaria.setShortcut("Ctrl+T")
        """self.transformacaoBordaBinaria.triggered.connect(self.transform_BordaBinaria)
        self.menuimagens.addSeparator()"""


        #sobre
        self.sobre1 = self.menusobre.addAction("&Sobre...")
        self.sobre1.setShortcut("Ctrl+Y")
        self.sobre1.triggered.connect(self.menssagem)
        self.menusobre.addSeparator()
        self.apagar = self.menusobre.addAction("Detalhes da Imagem")
        self.apagar.setShortcut("Ctrl+U")
        self.apagar.triggered.connect(self.exibe_mensagem2)

        self.barradestatus = self.statusBar()
        self.barradestatus.showMessage("Oi ,Bem-vindo ao meu software!",3000)


        # Criando um QLabel para texto
        self.texto = QLabel("Obrigado por utilizar", self)
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)


        # Criando um botão
        
        # Criando uma imagem(QLabel)
        self.imagem1 = QLabel(self)
        self.endereco1 = 'Impala_67.ppm'
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

        self.imagem2 = QLabel(self)
        self.endereco2 = 'Impala_67.ppm'
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

        # Organizando os widgets dentro do GridLayout
        self.layout.addWidget(self.texto, 0, 0, 1, 2)
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        
        self.layout.setRowStretch(0, 0)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 0)
        self.endImagemOriginal = ''
        self.imagemResultado = QLabel()
        self.endImagemResultado = ''

    # Métodos para ações dos botões
    def open_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption="Open Image",
                                                            directory=QtCore.QDir.currentPath(),
                                                            filter='All files(*.*);;Imagens(*.ppm; *.pgm; *.pbm)',
                                                            initialFilter='Imagens(*.ppm; *.pgm; *.pbm)')
        print(fileName)
        if fileName != '':
            self.endereco1 = fileName
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
            self.imagem1.setPixmap(self.pixmap1)

    #Colorida 
    def transform_NegativoColorida(self):
        self.entrada = self.endereco1
        self.saida = 'images/NegativoColorida.ppm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/colorida/negativo.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Colorida()
      

    def transform_CorrecaoGamaColorida(self):

        self.entrada = self.endereco1
        self.saida = 'images/GamaColorida.ppm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/colorida/CorrecaoGama.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle("ERRO!")
            self.msg.setText("Somente arquivos PPM")
            self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.msg.exec_()  # exibir a caixa de mensagens, ou caixa de diálogo
            self.reply = self.msg.clickedButton()

    def transform_LogColorida(self):
        self.entrada = self.endereco1
        self.saida = 'images/LogColorida.ppm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/colorida/TransformacaoLogaritmica.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Colorida()
    def transform_SharpenColorida(self):
        self.entrada = self.endereco1
        self.saida = 'images/SharpenColorida.ppm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/colorida/Sharpen.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Colorida()

    def transform_MedianaColorida(self):
        self.entrada = self.endereco1
        self.saida = 'images/MedianaColorida.ppm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/colorida/mediana.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Colorida()

    def transform_GaussianoColorida(self):
        self.entrada = self.endereco1
        self.saida = 'images/GaussianoColorida.ppm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/colorida/Gaussiano3x3.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Colorida()

    def transform_SobelColorida(self):
        self.entrada = self.endereco1
        self.saida = 'images/SobelColorida.ppm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/Colorida/sobel.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Colorida()

    def transform_R(self):
        self.entrada = self.endereco1
        self.saida = 'images/RGB-RColorida.ppm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/colorida/CamadaR.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Colorida()
    def transform_G(self):
        self.entrada = self.endereco1
        self.saida = 'images/RGB-G.ppm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/colorida/CamadaG.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Colorida()
    def transform_ConverterCinza(self):
        self.entrada = self.endereco1
        self.saida = 'images/ConvertCinza.pgm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/colorida/ColoridaPraCinza.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Colorida()
    def transform_B(self):
        self.entrada = self.endereco1
        self.saida = 'images/RGB-B.ppm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/colorida/CamadaB.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Colorida()

    def transform_ColoridaPraPreto(self):
        self.entrada = self.endereco1
        self.saida = 'images/coloridaPraPreto.pbm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/colorida/ParaPreto.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Colorida()

    #Cinza
    def transform_NegativoCinza(self):
        self.entrada = self.endereco1
        self.saida = 'images/NegativoCinza.pgm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'pgm'):
            self.script = 'filtrosDeTransformacao/escalaCinza/negativo.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Cinza()


    
    def transform_CorrecaoGama(self):
        self.entrada = self.endereco1
        self.saida = 'images/GamaCinza.pgm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'pgm'):
            self.script = 'filtrosDeTransformacao/escalaCinza/CorrecaoGama.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Cinza()


   
    def transform_Log(self):
        self.entrada = self.endereco1
        self.saida = 'images/LogNegativo.pgm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'pgm'):
            self.script = 'filtrosDeTransformacao/escalaCinza/TransformacaoLogaritmica.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Cinza()
    

    def transform_Sharpen(self):
        self.entrada = self.endereco1
        self.saida = 'images/SharpenCinza.pgm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'pgm'):
            self.script = 'filtrosDeTransformacao/escalaCinza/Sharpen.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Cinza()
    
    def transform_Mediana(self):
        self.entrada = self.endereco1
        self.saida = 'images/MedianaCinza.pgm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'pgm'):
            self.script = 'filtrosDeTransformacao/escalaCinza/mediana.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Cinza()
    
    def transform_Gaussiano(self):
        self.entrada = self.endereco1
        self.saida = 'images/GaussianoCinza.pgm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'pgm'):
            self.script = 'filtrosDeTransformacao/escalaCinza/Gaussiano3x3.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Cinza()
    
    def transform_Sobel(self):
        self.entrada = self.endereco1
        self.saida = 'images/SobelCinza.pgm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'pgm'):
            self.script = 'filtrosDeTransformacao/escalaCinza/Sobel.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Cinza()
    """def transform_DeteccaoBordaColorida(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfNegativo.ppm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/colorida/Sharpen.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle("ERRO!")
            self.msg.setText("Somente arquivos PPM")
            self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.msg.exec_()  # exibir a caixa de mensagens, ou caixa de diálogo
            self.reply = self.msg.clickedButton()"""

    """def transform_DeteccaoBorda(self):
            self.entrada = self.endereco1
            self.saida = 'images/transfNegativo.pgm'
            self.string = self.endereco1
            self.parts = self.string.rpartition('.')
            print(self.parts)

            if (self.parts[2] == 'pgm'):
                self.script = 'filtrosDeTransformacao/escalaCinza/Sharpen.py'
                self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
                print(self.program)
                subprocess.run(self.program, shell=True)
                self.endereco2 = self.saida
                self.pixmap2 = QtGui.QPixmap(self.endereco2)
                self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
                self.imagem2.setPixmap(self.pixmap2)

            else:
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Information)
                self.msg.setWindowTitle("ERRO!")
                self.msg.setText("Somente arquivos PGM")
                self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                self.msg.exec_()  # exibir a caixa de mensagens, ou caixa de diálogo
                self.reply = self.msg.clickedButton()"""

    def transform_EscalaCinza(self):
        self.entrada = self.endereco1
        self.saida = 'images/ColoridoPraCinza.ppm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'ppm'):
            self.script = 'filtrosDeTransformacao/colorida/ConverterEscalaDeCinza.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Colorida()
    def transform_Erosao(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfErosao.pbm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'pbm'):
            self.script = 'filtrosDeTransformacao/pretoBranco/Erosao.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Preto()
    def transform_Dilatacao(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfDilatacao.pbm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'pbm'):
            self.script = 'filtrosDeTransformacao/pretoBranco/Dilatacao.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Preto()
    def transform_Abertura(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfAbertura.pbm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'pbm'):
            self.script = 'filtrosDeTransformacao/pretoBranco/Abertura.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Preto()
    def transform_Fechamento(self):
        self.entrada = self.endereco1
        self.saida = 'images/transfFechamento.pbm'
        self.string = self.endereco1
        self.parts = self.string.rpartition('.')
        print(self.parts)

        if (self.parts[2] == 'pbm'):
            self.script = 'filtrosDeTransformacao/pretoBranco/Fechamento.py'
            self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        else:
            self.menssagem_Preto()


    def apagar_mensagem(self):
        self.barradestatus.clearMessage()

    def exibe_mensagem2(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Desenvolvido por Otavio Faria")
        self.msg.setWindowTitle("Informações da Imagem")
     

        self.entrada = open(self.endereco1, "r+")
        self.saida = open("balao.pgm", "w+")
        self.linha = self.entrada.readline() #P2
        self.linha2 = self.entrada.readline() #Comentário
        self.linha1 = self.entrada.readline() #Dimensões
        self.dimensoes = self.linha1.split()
        self.largura = self.dimensoes[0]
        self.altura = self.dimensoes[1]


        self.string = self.endereco1
        self.parts = self.string.rpartition('/')
        self.parts2 = self.string.rpartition('.')
        print(self.string)
        print(self.parts)

        self.msg.setDetailedText("Nome: " + self.parts[2] + "\n" + "Extensão do Arquivo: " + self.parts2[2] + "\n" + "Comentario : " + self.linha2 + "\n" + "Largura : " +  self.largura + "\n" + "Altura: " +  self.altura)
        

        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec_()# exibir a caixa de mensagens, ou caixa de diálogo
        self.reply = self.msg.clickedButton()
        self.barradestatus.showMessage("Foi clicado o botao: " + self.reply.text())


    def menssagem(self):
       self.msg = QMessageBox()
       self.msg.setIcon(QMessageBox.Information)
       self.msg.setText("Desenvolvido por Otavio Faria")
       self.msg.setWindowTitle("Sobre")
       self.msg.setInformativeText("Canapolis,05 de Agosto de 2020 ")
       self.msg.setDetailedText("https://youtu.be/tXbv-BzgG18")
       self.msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
       self.msg.exec_()
       self.reply = self.msg.clickedButton()
       self.barradestatus.showMessage("Foi clicado o botão:" + str(self.reply.text()))

       if self.reply.text() == "OK":
          print('Apertou OK')
       if self.reply.text() == "Cancel":
          print('Apertou Cancel')

    def menssagem_Colorida(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("ERRO!")
        self.msg.setText("Somente arquivos PPM")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec_()  # exibir a caixa de mensagens, ou caixa de diálogo
        self.reply = self.msg.clickedButton()
    def menssagem_Cinza(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("ERRO!")
        self.msg.setText("Somente arquivos PGM")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec_()  # exibir a caixa de mensagens, ou caixa de diálogo
        self.reply = self.msg.clickedButton()

    def menssagem_Preto(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("ERRO!")
        self.msg.setText("Somente arquivos PBM")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec_()  # exibir a caixa de mensagens, ou caixa de diálogo
        self.reply = self.msg.clickedButton()


    def salvarImagemComo(self):

        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, caption='salvar_arquivo',
                                                            directory=QtCore.QDir.currentPath(),
                                                            filter='Images (*.ppm; *.pgm; *.pbm)',
                                                            initialFilter='Images (*.pgm)')

        print(fileName)

        if fileName != '':
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(
                300, 300, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

            shutil.copyfile(self.endereco2, fileName)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
