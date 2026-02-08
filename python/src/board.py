class Board():
    def __init__(self,fen=None):
        if fen:
            self.toPosition(fen)
        else:
            self.wb = 1|1<<48
            self.bb = 1<<6|1<<42
            self.blockers = 0
        self.stm = False 
        # False - White to move
        # True - Black to move

    def toPosition(self,fen):
        self.wb = 0
        self.bb = 0
        self.blockers = 0
        ptr = 0
        for f in fen:
            if f.isdigit():
                ptr += int(f)
            elif f=="x":
                self.wb |= 1<<ptr
                ptr += 1
            elif f=="o":
                self.bb |= 1<<ptr
                ptr += 1
            elif f=="-":
            	self.blockers |= 1<<ptr
            	ptr+=1
            elif f=="/":
                continue
            else:
                raise ValueError("FEN is malformed, aborting program.")
        if ptr > 49:
            raise ValueError("FEN is too long, aborting program.")

    def toFEN(self):
        fen = []
        for row in range(7):
            number = 0
            for col in range(7):
                mask = 1<<(row * 7 + col)
                if (self.wb&mask):
                    if number:
                        fen.append(str(number))
                        number = 0
                    fen.append("x")
                elif (self.bb&mask):
                    if number:
                        fen.append(str(number))
                        number = 0
                    fen.append("o")
                elif (self.blockers&mask):
                	if number:
                		fen.append(str(number))
                		number = 0
                	fen.append("-")
                else:
                    number += 1
            if number:
                fen.append(str(number))
                number = 0
            if (row+1)!=7:
                fen.append("/")
        return "".join(fen)
            
    def copyBoard(self):
            child = self.__new__(Board)
            child.wb = self.wb
            child.bb = self.bb
            child.blockers = self.blockers
            child.stm = self.stm
            return child
            
            
    def printBoard(self):
        table = [["." for _ in range(7)] for _ in range(7)]
        for row in range(7):
            for col in range(7):
                mask = 1<<(row*7+col)
                if (self.wb&mask)==0 and (self.bb&mask)==0 and (self.blockers&mask)==0:
                    continue
                elif (self.wb & mask and self.bb & mask):
                    raise ValueError("how? like actually, how? You got true on both? How do you expect me to print that dumbass")
                elif (self.wb&mask):
                    table[row][col] = "x"
                elif (self.bb&mask):
                    table[row][col] = "o"
                elif (self.blockers&mask):
                	table[row][col] = "-"
        for row in table:
            print(row)
            