import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from move import generateMoves

def perft():
    nodes = len(generateMoves(1|1<<48,(1|1<<48|1<<6|1<<42)))
    correct = True if nodes==16 else False
    if correct:
        print(f"Nodes: {nodes} - Test Succeded")
    else:
        print(f"Nodes: {nodes} - Test Failed")

perft()