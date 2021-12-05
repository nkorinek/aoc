from aocd.models import Puzzle
import numpy as np

def iterate_through_boards(list_of_boards, number, delete=False):
    for i, board in enumerate(list_of_boards):
        dotted_board = replace_correct_number(board, number)
        bingo_check = check_for_bingo(dotted_board, number)
        list_of_boards[i] = dotted_board
        if len(list_of_boards) == 1 and bingo_check:
            return(bingo_check)
        elif bingo_check:
            if delete:
                del list_of_boards[i]
            else:
                return(bingo_check)

def replace_correct_number(array, number):
    mask = ~(array == number)
    return(mask*array)

def check_for_bingo(array, number):
    bingo = False
    for i in list(range(5)):
        if not np.any(array[i]) or not np.any(array[:,i]):
            bingo = True
    if bingo:
        return(array.sum()*number)

puzzle = Puzzle(year=2021, day=4)

data = puzzle.input_data

boards = data.split('\n\n')

input = [int(i) for i in boards.pop(0).split(',')]

for i, board in enumerate(boards):
    boards[i] = np.array([nums.split() for nums in boards[i].split('\n')],
                         dtype=int)

for num in input:
    print("Checking {}".format(num))
    bingo_score1 = iterate_through_boards(boards, num)
    if bingo_score1:
        print("Bingo! Score: {}".format(bingo_score1))
        break

puzzle.answer_a = bingo_score1

print("Part 2!")

for num in input:
    print("Checking {}".format(num))
    bingo_score2 = iterate_through_boards(boards, num, delete=True)
    if len(boards) == 1:
        boards[0] = replace_correct_number(boards[0], num)
        if bingo_score2:
            print("Final Bingo! Score: {}".format(bingo_score2))
            break

puzzle.answer_b = bingo_score2
