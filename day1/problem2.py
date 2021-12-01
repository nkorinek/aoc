import numpy as np
import os

file = open(os.path.join("day1", "input.csv"))

num = 10000
increase = 0
numbers = []

for line in file.readlines():
    numbers.append(int(line))

array = np.array(numbers)

three_avg = list(np.convolve(array,np.ones(3,dtype=int),'valid'))

for new_num in three_avg:
    if new_num > num:
        increase += 1
    num = new_num

print(increase)
