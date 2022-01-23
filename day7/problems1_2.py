from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2021, day=7)

data = puzzle.input_data

### Part 1

crabs = np.fromiter(data.split(','), dtype=int)

fuel_use = 1000000

min = 0

for i in range(max(crabs)+1):
    loop_crab = crabs-i
    fuel_total = np.sum(np.absolute(loop_crab))
    if fuel_total < fuel_use:
        fuel_use = fuel_total
        min = i

print(min, fuel_use)

# puzzle.answer_a = fuel_use

### Part 2

fuel_calculator = lambda n: ((n*n) + n)/2

fuel_use = 10000000000

min = 0

for i in range(max(crabs)+1):
    loop_crab = crabs-i
    fuel_total = np.sum(fuel_calculator(np.absolute(loop_crab)))
    if fuel_total < fuel_use:
        fuel_use = fuel_total
        min = i

print(min, fuel_use)
