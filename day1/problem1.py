import os

file = open(os.path.join("day1", "input.csv"))

num = 10000
increase = 0

for line in file.readlines():
    new_num = int(line)
    if new_num > num:
        increase += 1
    num = new_num

print(increase)
