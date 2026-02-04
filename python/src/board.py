class Board():
    def __init__(self,fen=None):
        if fen:
            self.toPosition(fen)
        else:
            self.rb = 1|1<<48
            self.bb = 1<<6|1<<42
        self.std = 1

    def toPosition(self,fen):
        self.rb = 0
        self.bb = 0
        ptr = 0
        for f in fen:
            if f.isdigit():
                ptr += int(f)
            elif f=="x":
                self.rb |= 1<<ptr
                ptr += 1
            elif f=="o":
                self.bb |= 1<<ptr
                ptr += 1
            else:
                raise NameError("FEN is malformed, aborting program")
    def printBoard(self,board_size=7):
        table = [["." for _ in range(board_size)] for _ in range(board_size)]
        for row in range(board_size):
            for col in range(board_size):
                mask = 1<<(row*board_size+col)
                if (self.rb&mask)==0 and (self.bb&mask)==0: 
                    print(f"Nothing detected at {row},{col}. Putting a '.' in there.")
                elif (self.rb&mask) and (self.bb&mask):
                    raise ValueError("how? like actually, how? You got true on both? How do you expect me to print that dumbass")
                elif (self.rb&mask):
                    table[row][col] = "x"
                    print(f"Red Bitboard at {row},{col}. Putting a 'x' in there.")
                elif (self.bb&mask):
                    table[row][col] = "o"
                    print(f"Blue Bitboard at {row},{col}. Putting a 'o' in there.")
        return table

c = Board()
print(c.printBoard())
