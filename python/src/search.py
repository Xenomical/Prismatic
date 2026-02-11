from move import generateMoves
from make import makeMove, undoMove
from evaluation import evaluate
from gameover import terminal

"""def orderMoves(move):
    score = 0
    score += (player.bit_count()-enemy.bit_count())*5
    score += 15 if not move[3] else 0
    return score"""

def negamax(board, depth):
    if depth == 0 or terminal(board):
        return evaluate(board), None

    bestScore = -float('inf')
    bestMove = None
    bb = board.wb if not board.stm else board.bb
    blocked = board.wb | board.bb | board.blockers
    allMoves = generateMoves(bb, blocked)

    if not allMoves:
        # Pass node: fix - update bestScore
        board.stm ^= 1
        score, _ = negamax(board, depth - 1)
        score = -score
        if score > bestScore:
            bestScore = score
            bestMove = None  # no move for pass
        board.stm ^= 1
    else:
        for move in allMoves:
            undo = makeMove(board, move)
            score, _ = negamax(board, depth - 1)  # fix - unpack properly
            score = -score
            undoMove(board, undo)
            if score > bestScore:
                bestScore = score
                bestMove = move

    return bestScore, bestMove

