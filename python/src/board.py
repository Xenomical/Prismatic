class Board():
    def __init__(self,fen=None,board_size=7):
        self.board_size = board_size
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
            elif f=="/":
                continue
            else:
                raise ValueError("FEN is malformed, aborting program.")
        if ptr > self.board_size*self.board_size:
            raise ValueError("FEN is too long, aborting program.")

    def toFEN(self):
        fen = []
        for row in range(self.board_size):
            number = 0
            for col in range(self.board_size):
                mask = 1<<(row * self.board_size + col)
                if (self.rb&mask):
                    if number:
                        fen.append(str(number))
                        number = 0
                    fen.append("x")
                elif (self.bb&mask):
                    if number:
                        fen.append(str(number))
                        number = 0
                    fen.append("o")
                else:
                    number += 1
            if number:
                fen.append(str(number))
                number = 0
            if (row+1)!=self.board_size:
                fen.append("/")
        return "".join(fen)
            
            
            
    def printBoard(self):
        table = [["." for _ in range(self.board_size)] for _ in range(self.board_size)]
        for row in range(self.board_size):
            for col in range(self.board_size):
                mask = 1<<(row*self.board_size+col)
                if (self.rb&mask)==0 and (self.bb&mask)==0: 
                    continue
                elif not (self.rb & mask or self.bb & mask):
                    raise ValueError("how? like actually, how? You got true on both? How do you expect me to print that dumbass")
                elif (self.rb&mask):
                    table[row][col] = "x"
                elif (self.bb&mask):
                    table[row][col] = "o"
        for row in table:
            print(row)

c = Board()
c.printBoard()
