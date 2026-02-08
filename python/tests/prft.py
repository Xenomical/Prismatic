import sys
import os

# determine project root and add src to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from move import generateMoves
from make import makeMove
from board import Board

correctValues = [1,16, 256, 6460, 155888, 4752668, 141865520, 5023479496, 176821532236]


def perft(board, depth):
	if depth == 0:
		return 1
	
	nodes = 0
	for move in generateMoves(board.wb if not board.stm else board.bb,board.wb|board.bb|board.blockers):
		child = board.copyBoard()
		makeMove(child, move)
		nodes += perft(child, depth-1)
		
	return nodes
		
for d in range(4):
    c = Board()  # starting position
    nodes = perft(c, d)
    print(f"Depth {d}: {nodes} - {'OK' if nodes == correctValues[d] else 'WRONG'} - correct Nodes - {correctValues[d]}")
