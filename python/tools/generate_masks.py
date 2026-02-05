def generate_clone_masks(board_size=7):
    board = board_size*board_size
    masks = [0]*board
    for sq in range(board):
        x,y = divmod(sq,board_size)
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                if dx==0 and dy==0:
                    continue
                nx,ny = x+dx,y+dy
                if 0<=nx<board_size and 0<=ny<board_size:
                    masks[sq] |= 1<<(nx*board_size+ny)
    return masks

def generate_jump_masks(board_size=7):
    board = board_size*board_size
    masks = [0]*board
    for sq in range(board):
        row,col = divmod(sq,board_size)
        for dr in (-2,-1,0,1,2):
            for dc in (-2,-1,0,1,2):
                if max(abs(dr),abs(dc))<2:
                    continue
                nr,nc = row+dr,col+dc
                if 0<=nr<board_size and 0<=nc<board_size:
                    masks[sq] |= 1<<(nr*board_size+nc)
    return masks

if __name__ == "__main__":
    import json
    data = {
        "clone": generate_clone_masks(),
        "jump": generate_jump_masks()
    }
    with open("masks.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Masks precalculated and saved to masks.json :D")
