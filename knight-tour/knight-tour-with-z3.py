from z3 import *
from random import randint 

WARNING = '\033[93m'
OKGREEN = '\033[92m'
ENDC = '\033[0m'

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, 2, 1, 1, 2, -2, -1]

def print_board(boardsize, trc):
    for i in range(boardsize):
        print("|".join(f"{trc.index((i, j)):>2}" for j in range(boardsize)))

# implementation for nxn chessboard
# solving() can solve for both open tour and close tour. Currently, I am lazy to implement auto close tour solver, 
# so just read my code to know how to do it

def solving(boardsize, start, end):
    global dx, dy
    # IDEA: 
    # Create an arr[], arr[i], with i - position on chess board (but in 1 dimension)
    # arr[i] : the order when knight move to position i
    # adding constrain to each cell arr[i] (arr[j] = arr[i] + 1, with j to i by moving knight)
    in_board = lambda x, y: (x >=0 and x<boardsize) and (y >=0 and y<boardsize)
    solver = Solver()
    arr = [Int(f"x{i}") for i in range(boardsize ** 2)]
    solver.add(Distinct(arr))
    for i in range(boardsize ** 2):
        solver.add(0<=arr[i])
        solver.add(arr[i] < boardsize ** 2)

    def in_one_of(x, ls):
        cond = BoolVal(False)
        for i in ls:
            cond = Or(cond, i == x)
        return cond 
    
    #define random startpoint, as arr[startpoint] = 0
    # startx = randint(0, 7)
    # starty = randint(0, 7)
    # solver.add(arr[startx * 8 + starty] == 0)
    solver.add(arr[start] == 0)
    solver.add(arr[end] == boardsize ** 2 - 1)
    for idx in range(0, boardsize ** 2):
        if idx == start:
            continue

        x = idx // boardsize
        y = idx % boardsize
        tmp = []
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_board(nx, ny):
                tmp.append(arr[nx * boardsize + ny])
    
        solver.add(in_one_of(arr[idx] - 1, tmp))

    if solver.check() == sat:
        print(OKGREEN + "FOUND solution" + ENDC)
        # print(solver.model())
        tr = [None for i in range(boardsize * boardsize)]
        s = solver.model()
        for i in range(boardsize):
            for j in range(boardsize):
                tr[s[arr[i * boardsize + j]].as_long()] = (i, j)
        print_board(boardsize, tr)
    else:
        print(WARNING + "NO soulution found" + ENDC)
        # raise Exception()


solving(8, 2 * 8 + 6, 7 * 8 + 2)