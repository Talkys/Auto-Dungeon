# Auto Dungeon

This is a simple project that generates random dungeon maps for tabletop rpgs, or for regular crpgs. This helps you save some time with level desing by generating various types of dungeons.

## Features

It supports 3 types of dungeons. Dense, Regular and Sparse. You can specify a size too, but the generation is always a square, as the random generator works better on sqaures by providing better designs.

You can change the tiles on the tiles folder too, but remember to use the same resolution for your dungeon tiles.

## Usage

You need to run the program by: python3 maplot.py (squaresize) (type) (tilesize) (outputfile)

A simple example: python3 maplot.py 50 D 16 dungeon.png