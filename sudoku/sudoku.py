from z3 import * 
OKGREEN = '\033[92m'
ENDC = '\033[0m'


solver = Solver()    

sudokuboard = [[Int(f"a_{i}_{j}") for j in range(9)] for i in range(9)]

for i in range(9):
    solver.add(Distinct(sudokuboard[i]))

for i in range(9):
    solver.add(Distinct([sudokuboard[row][i] for row in range(9)]))


for i in range(3):
    for j in range(3):
        arr = []
        for row in range(i * 3, (i +  1) * 3):
            for col in range(j * 3, (j + 1) * 3):
                arr.append(sudokuboard[row][col])
        solver.add(Distinct(arr))
for i in range(9):
    for j in range(9):
        solver.add(sudokuboard[i][j] >=1)
        solver.add(sudokuboard[i][j] <=9)

# Input from file instead of stdin, this way its more easy to do
f = open("./sudoku/sudokugrid.txt", "r")
original_sudokuboard = [[0 for i in range(9)] for j in range(9)]
cnt = 0
for line in f.readlines():
    for i in range(9):
        # print(line[i], end = ' ')
        
        if line[i] != ".":
            solver.add(sudokuboard[cnt][i] == int(line[i]))
            original_sudokuboard[cnt][i] = int(line[i])
    cnt += 1
    # print('')

f.close()

if solver.check() == sat:
    print("solution found")
    M = solver.model()
    for i in range(9):
        for j in range(9):
            if original_sudokuboard[i][j] == 0:
                print(OKGREEN + f"{M[sudokuboard[i][j]]}" + ENDC, end = " ")
            else:
                print(f"{M[sudokuboard[i][j]]}", end = " ")
        print("")
else:
    print("No solution")