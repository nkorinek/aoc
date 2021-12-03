# Using new python module to get data, it's cool!
from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2021, day=3)

data = puzzle.input_data

data_list = data.split('\n')

data_np_list = [np.fromiter(binary, dtype=int) for binary in data_list]

arr = np.array(data_np_list)

majority = arr.shape[0]/2

sum_2d = arr.sum(axis=0)

binary_check = sum_2d>majority

gamma = ''.join(['1' if x else '0' for x in binary_check])
gamma_int = int(gamma, 2)

epsilon = ''.join(['0' if x else '1' for x in binary_check])
epsilon_int = int(epsilon, 2)

answer1 = gamma_int*epsilon_int

puzzle.answer_a = answer1
