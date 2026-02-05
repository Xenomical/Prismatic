from board import Board
from move import generateMoves

BOARD_SIZE = int(input("What should be the size of the board?\n"))

FEN = input("Input the beginning FEN position (or none, then this will default to the 7x7 normal pos")

board = Board(FEN)