import sys
import os
import time

# determine project root and add src to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from move import generateMoves
from make import makeMove, undoMove
from board import Board

correctValues = [1,16, 256, 6460, 155888, 4752668, 141865520, 5023479496, 176821532236]


def perft(board, depth):
	table = []
	if depth == 0:
		return 1
	
	nodes = 0
	bb = board.wb if not board.stm else board.bb
	blocked = board.wb | board.bb | board.blockers
	for move in generateMoves(bb, blocked):
		undo = makeMove(board,move)
		nodes += perft(board,depth-1)
		undoMove(board,undo)
		#print(f"Move: {move} - Nodes: {nodes}")
	return nodes
		
c = Board()

for d in range(0,6):
    start = time.perf_counter()
    nodes = perft(c, d)
    end = time.perf_counter()
    elapsed = end-start
    print(f"Depth {d}: {nodes} - {'OK' if nodes == correctValues[d] else 'WRONG'} - Time Elapsed: {elapsed}")
    