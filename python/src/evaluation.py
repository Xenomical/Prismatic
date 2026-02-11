from move import generateMoves
from gameover import terminal

def evaluate(board):
    blockers = board.wb|board.bb|board.blockers
    if not board.stm:
        player = board.wb
        enemy = board.bb
    else:
        player = board.bb
        enemy = board.wb
    if terminal(board) == 1:
        return -float('inf')
    elif terminal(board) ==2:
        return float('inf')
    xScore = player.bit_count()-enemy.bit_count()
    movementScore = len(generateMoves(player,blockers))-len(generateMoves(enemy,blockers))
    return xScore+movementScore
    
