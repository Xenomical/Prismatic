from move import generateMoves
from make import makeMove, undoMove
from evaluation import evaluate
from gameover import terminal

convert = [
    386,
    901,
    1802,
    3604,
    7208,
    14416,
    12320,
    49411,
    115335,
    230670,
    461340,
    922680,
    1845360,
    1577056,
    6324608,
    14762880,
    29525760,
    59051520,
    118103040,
    236206080,
    201863168,
    809549824,
    1889648640,
    3779297280,
    7558594560,
    15117189120,
    30234378240,
    25838485504,
    103622377472,
    241875025920,
    483750051840,
    967500103680,
    1935000207360,
    3870000414720,
    3307326144512,
    13263664316416,
    30960003317760,
    61920006635520,
    123840013271040,
    247680026542080,
    495360053084160,
    423337746497536,
    8899172237312,
    22230750724096,
    44461501448192,
    88923002896384,
    177846005792768,
    355692011585536,
    144036023238656
  ]

def orderMoves(moves,ebb):
    scoredMoves = []
    if not moves:
        return 0
    for move in moves:
        score = 15 if not move[2] else 0 #extra score for cloning
        score += ((ebb&convert(move[1]).bit_count())*5
        scoredMoves.append((move,score))
    scoredMoves.sort(key=lambda x: x[1], reverse=True)
    return [move for _,move in scoredMoves]

def negascout(board, depth, alpha, beta):
    if depth == 0 or terminal(board):
        return evaluate(board), None

    bestMove = None
    bestScore = -float('inf')
    bb = board.wb if not board.stm else board.bb
    ebb = board.wb if not board.stm else board.bb
    blocked = board.wb | board.bb | board.blockers
    allMoves = orderMoves(generateMoves(bb, blocked),ebb)

    if not allMoves:
        board.stm ^= 1
        score, _ = negascout(board, depth - 1,-beta,-alpha)
        score = -score
        if score > bestScore:
            bestScore = score
            bestMove = None
        board.stm ^= 1
    else:
        for move in allMoves:
            undo = makeMove(board, move)
            score, _ = negascout(board, depth - 1,-beta,-alpha)
            score = -score
            undoMove(board, undo)
            alpha = max(alpha,score)
            if score > bestScore:
                bestScore = score
                bestMove = move
            if alpha >= beta:
                break

    return bestScore, bestMove

def iterative(depth,board):
    for d in range(1,depth+1):
        bestEval,bestMove = negascout(board,d,-float('inf'),float('inf'))
    return bestEval, bestMove
