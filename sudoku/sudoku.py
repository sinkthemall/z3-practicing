from z3 import * 
import time 


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

if solver.check() == sat:
    print("solution found")
    M = solver.model()
    for i in range(9):
        for j in range(9):
            print(f"{M[sudokuboard[i][j]]}", end = " ")
        print("")
else:
    print("No solution")