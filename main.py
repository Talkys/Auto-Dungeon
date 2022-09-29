from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import sys
from os import system
from PIL import Image
import numpy as np

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('mainwindow.ui',self)

        self.readytosave = False

        self.imagem = self.findChild(QtWidgets.QLabel, 'imagem')
        self.gridsize = self.findChild(QtWidgets.QSpinBox, 'size_input')
        self.dungeontype = self.findChild(QtWidgets.QComboBox, 'tipo_input')
        self.tiletype = self.findChild(QtWidgets.QComboBox, 'tile_input')
        self.generatebutton = self.findChild(QtWidgets.QPushButton, 'gerar_botao')
        self.savebutton = self.findChild(QtWidgets.QPushButton, 'salvar_botao')

        self.generatebutton.clicked.connect(self.generatePressed)
        self.savebutton.clicked.connect(self.savePressed)

        self.imagem.setText("No dungeon generated")

        self.show()

    def generatePressed(self):
        if self.verifyGenerate() == True:
            self.imagem.setText("Generating...")
            gridsize = self.gridsize.value()

            dungeontype = "D"
            tmp = self.dungeontype.currentIndex()
            dungeons = ["D","R","S"]
            dungeontype = dungeons[tmp]

            tilesize = "16"
            tileindex = 0
            tmp = self.tiletype.currentIndex()
            tiles = ["16","16", "16"]
            tilesize = tiles[tmp]
            tileindex = tmp

            generate(gridsize=gridsize, dungeontype=dungeontype, tilesize=tilesize, tileindex=tileindex)
            pixmap = QPixmap("/tmp/dungeon.png")
            self.imagem.setPixmap(pixmap.scaled(400,400))
            self.readytosave = True
        else:
            self.imagem.setText("Invalid")
    
    def savePressed(self):
        if self.readytosave == True:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_name, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","png (*.png);;All Files (*)", options=options)
            if file_name:
                print(file_name)
                system("cp /tmp/dungeon.png " + file_name)

    def verifyGenerate(self):
        if self.gridsize.value() <= 0:
            # print("1")
            return False
        if self.dungeontype.currentIndex() < 0:
            # print("2")
            return False
        if self.tiletype.currentIndex() < 0:
            # print("3")
            return False

        # print("Passei")

        return True

def generate(gridsize, dungeontype, tilesize, tileindex):

    system("./generatedungeon " + str(gridsize) + " " + dungeontype + " > dungeon")

    try:
        matrix_square = int(gridsize)
        tile_size = int(tilesize)
        input_file = "dungeon"
        output_file = "/tmp/dungeon.png"
    except:
        raise Exception("Problem parsing arguments")

    matrix_width = matrix_square
    matrix_height =  matrix_square

    image_width = matrix_width * tile_size
    image_height = matrix_height * tile_size

    matrix = np.loadtxt(input_file, usecols=range(matrix_square), dtype=int)

    #Importing all tiles
    tiles = [
        [
        "./tiles/black16.png",
        "./tiles/chao1601.png"
        ],
        [
        "./tiles/black16.png",
        "./tiles/chao1602.png"
        ],
        [
        "./tiles/black16.png",
        "./tiles/chao1603.png"
        ]
    ]
    
    black = Image.open(tiles[tileindex][0])
    chao = Image.open(tiles[tileindex][1])

    selectedtiles = []

    #Put the selected tile model on the working array
    selectedtiles.append(black)
    selectedtiles.append(chao)

    

    #for file in glob.glob("./tiles/*"):
     #   im = Image.open(file)
      #  tiles.append(im)

    output = Image.new('RGB', (image_width,image_height))

    for i in range(matrix_width):
        for j in range(matrix_height):
            x,y = i*tile_size,j*tile_size
            index = matrix[j][i]
            output.paste(selectedtiles[index],(x,y))

    output.save(output_file)
    system("rm dungeon")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()