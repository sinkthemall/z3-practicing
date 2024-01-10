from z3 import * 
import random 
# from math import sum 


# Z3 does not use strategy like divide subset, so when increase to 30, it takes really long to find the solution

nsize = 25
def generate_test(n_size : int ):
    N = n_size 
    val = [random.randint(0, 10000000000) for i in range(N)]
    subset = [random.randint(0, 1) for i in range(N)]
    subsetsum = sum([i * j for i, j in zip(subset, val)])
    return ((val, subsetsum), subset)


public, private = generate_test(nsize)
knapsack, subsetsum = public 

solver = Solver()
x = [BitVec(f"a_{i}", 1) for i in range(nsize)]


total = 0
for i in range(nsize):
    total = Sum(total, If(x[i] == 1, knapsack[i], 0))

solver.add(total == subsetsum)

if solver.check() == sat:
    print("Solution found")
    for i in range(nsize):
        print(f" Solver answer: {solver.model()[x[i]]}, Solution answer: {private[i]}")

else:
    print("No solution")
