import glob
from os import system
from turtle import width
from PIL import Image
import numpy as np
import sys

# arguments = program dimentions type tilesize outputfile


if len(sys.argv) != 5:
    raise Exception("Invalid arguments")

system("./generatedungeon " + sys.argv[1] + " " + sys.argv[2] + " > dungeon")

try:
    matrix_square = int(sys.argv[1])
    tile_size = int(sys.argv[3])
    input_file = "dungeon"
    output_file = sys.argv[4]
except:
    raise Exception("Problem parsing arguments")

matrix_width = matrix_square
matrix_height =  matrix_square

image_width = matrix_width * tile_size
image_height = matrix_height * tile_size



matrix = np.loadtxt(input_file, usecols=range(matrix_square), dtype=int)

tiles = []

for file in glob.glob("./tiles/*"):
    im = Image.open(file)
    tiles.append(im)

output = Image.new('RGB', (image_width,image_height))

for i in range(matrix_width):
    for j in range(matrix_height):
        x,y = i*tile_size,j*tile_size
        index = matrix[j][i]
        output.paste(tiles[index],(x,y))

output.save(output_file)
system("rm dungeon")

