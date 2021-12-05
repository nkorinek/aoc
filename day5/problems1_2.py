from aocd.models import Puzzle
import numpy as np
import sys
import os

np.set_printoptions(threshold=sys.maxsize)

def coord_extractor(coordinates):
    return [[int(j) for j in i.split(',')] for i in coordinates.split(' -> ')]

def min_max_finder(pair):
    return(pair.min(), pair.max())

def coord_legibility_helper(coordinate_pair):
    return coord[0,0], coord[1,0], coord[0,1], coord[1,1]

def line_maker(coordinates, direction):
    if direction == "horizontal":
        pos = coordinates[:,1]
        min, max = min_max_finder(pos)
        return [[coordinates[0,0], i] for i in list(range(min, max+1))]
    elif direction == "vertical":
        pos = coordinates[:,0]
        min, max = min_max_finder(pos)
        return [[i, coordinates[0,1]] for i in list(range(min, max+1))]

def map_marker(line_coords, zeros_map):
    for coord in line_coords:
        zeros_map[coord[0], coord[1]] += 1

puzzle = Puzzle(year=2021, day=5)

data = puzzle.input_data

coords = np.array([coord_extractor(coord) for coord in data.split('\n')])

size = coords.max() + 1

map = np.zeros((size, size))

for coord in coords:
    x1, x2, y1, y2 = coord_legibility_helper(coord)
    if x1 == x2:
        map_marker(line_maker(coord, "horizontal"), map)
    elif y1 == y2:
        map_marker(line_maker(coord, "vertical"), map)

answer_a = (map >= 2).sum()

puzzle.answer_a = answer_a

### PART 2

def diagonal_helper(coordinates, column):
    coord = coordinates[:,column]
    min, max = min_max_finder(coord)
    line_list = list(range(min, max+1))
    if coord[0] != min:
        line_list.reverse()
    return line_list

def diagonal_line_maker(coordinates):
    x_line_coords = diagonal_helper(coordinates, 0)
    y_line_coords = diagonal_helper(coordinates, 1)
    return list(zip(x_line_coords, y_line_coords))

for coord in coords:
    x1, x2, y1, y2 = coord_legibility_helper(coord)
    if abs(x1-x2) == abs(y1-y2):
        map_marker(diagonal_line_maker(coord), map)

answer_b = (map>=2).sum()

puzzle.answer_b = answer_b
