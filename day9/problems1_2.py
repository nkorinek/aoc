import numpy as np
import os

data = np.genfromtxt(os.path.join('day9', 'input.txt'), dtype=str)

elevation_map = np.array([np.fromiter(nums, dtype=int) for nums in data])

rows, columns = np.shape(elevation_map)

### Part 1

def check_center(ypositions, xpositions, y, x):
    num = elevation_map[y, x]
    for yposes in ypositions:
        if yposes != 0:
            if num >= elevation_map[y+yposes, x]:
                return False
    for xposes in xpositions:
        if xposes != 0:
            if num >= elevation_map[y, x+xposes]:
                return False
    return True


total = 0

for y in range(rows):
    ypos, yneg = 1, -1
    if y == 0:
        yneg = 0
    elif y == rows-1:
        ypos = 0
    for x in range(columns):
        xpos, xneg = 1, -1
        if x == 0:
            xneg = 0
        elif x == columns-1:
            xpos = 0
        if check_center(ypositions=[ypos, yneg], xpositions=[xpos, xneg], y=y, x=x):
            total += elevation_map[y, x]+1
print(total)

## Part 2

# ...recursion is the answer maybe?

ele_copy = elevation_map

def basin_filler(arr, starty, startx, fill):
    try:
        val = arr[starty, startx]
        if val < 9:
            arr[starty, startx] = fill
            new_starts = [[starty+1, startx], [starty-1, startx],
                          [starty, startx+1], [starty, startx-1]]
            for start in new_starts:
                if all(pos >= 0 for pos in start):
                    basin_filler(arr, start[0], start[1], fill)
        else:
            return
    except IndexError:
        return

fill_val = 100

for y in range(rows):
    for x in range(columns):
        if ele_copy[y,x] < 9:
            basin_filler(ele_copy, y, x, fill_val)
            fill_val += 1

nums, counts = np.unique(ele_copy, return_counts = True)

largest_areas = sorted(counts)[-4:-1]

print(np.prod(largest_areas))
