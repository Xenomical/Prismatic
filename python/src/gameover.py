def terminal(board):
    blocked = board.wb | board.bb | board.blockers
    if not board.stm:
        player = board.wb
        enemy = board.bb
    else:
        player = board.bb
        enemy = board.wb
    if player==0:
        return 1
    elif enemy==0:
        return 2
    elif blocked == ((1 << 49) - 1):
        if player.bit_count()>enemy.bit_count():
            return 2
        else:
            return 1
    else:
        return 0
