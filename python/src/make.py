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

def makeMove(board, move):
	undo = (board.wb,board.bb,board.stm)
	from_sq = move[0]
	to_sq = move[1]
	is_jump = move[2]
	if not board.stm:
		player = board.wb
		enemy = board.bb
	else:
		player = board.bb
		enemy = board.wb
		
	if is_jump:
		player ^= 1<<from_sq
		
	player |= 1<<to_sq
	
	captured = enemy & convert[to_sq]
	player |= captured
	enemy &= ~captured # probably wrong.
	
	if not board.stm:
		board.wb = player
		board.bb = enemy
	else:
		board.bb = player
		board.wb = enemy
	board.stm = not board.stm
	return undo
	
def undoMove(board, undo):
    board.wb, board.bb, board.stm = undo