from z3 import *

chessboardsize = 10
solver = Solver()


def rowcheck(bitvecs, row):
    # This constraint ensures exactly one bit is set in the bit vector
    return Sum([If(Extract(i, i, bitvecs[row]) == 1, 1, 0) for i in range(chessboardsize)]) == 1

# def rowcheck(bitvecs, row ):
#     condi = BoolVal("False")
#     for i in range(chessboardsize):
#         condi  = Or(condi, bitvecs[row] == BitVecVal(1<<i, chessboardsize))
#     return condi

# def columncheckall(bitvecs):
#     condi
#     for i in range(chessboardsize):


def columncheck(bitvecs, col):
    count =  0
    for i in range(chessboardsize):
        count += If(Extract(col, col, bitvecs[i]) == 1, 1, 0)
    return count == 1

def L_diagonalcheck(bitvecs, x, y): # x, y is the start index , should be on the top left 
    count = 0 
    while x < chessboardsize and y < chessboardsize:
        count = Sum( If(Extract(y ,y , bitvecs[x]) ==1, 1, 0), count)
        x += 1
        y += 1 
    return count <= 1 

def R_diagonalcheck(bitvecs, x, y): # x, y is the start index , should be on the top right
    count =0 
    while x < chessboardsize and  y >=0 :
        count = Sum( If(Extract(y, y, bitvecs[x]) == 1, 1, 0), count)
        x += 1
        y -= 1
    return count <= 1 


state = [BitVec(f"Row{i}", chessboardsize) for i in range(chessboardsize)]


#row
# for i in range(chessboardsize):
#     sum = BoolVal("False")
#     for j in range(chessboardsize):
#         sum = Or(sum, state[i] == (1<<j))
#     solver.add(sum)

for row in range(chessboardsize):
    solver.add(rowcheck(state, row))

#col
for i in range(chessboardsize):
    solver.add(columncheck(state, i))


#left diagonal
for i in range(1, chessboardsize):
    solver.add(L_diagonalcheck(state, i, 0))
for i in range(0, chessboardsize):
    solver.add(L_diagonalcheck(state, 0, i))


# #right diagonal
for i in range(1, chessboardsize):
    solver.add(R_diagonalcheck(state, i, chessboardsize - 1))

for i in range(chessboardsize):
    solver.add(R_diagonalcheck(state, 0, i))

# col = [Int(f"c{i}") for i in range(chessboardsize)]



if solver.check() == sat:
    print("FOUND solution")
    for i in range(chessboardsize):
        print(bin(int(solver.model()[state[i]].as_long()))[2:].zfill(chessboardsize))
else:
    print("NO solution found")
