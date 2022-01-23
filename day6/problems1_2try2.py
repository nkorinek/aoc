from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2021, day=6)

data = puzzle.input_data

lanternfish = np.fromiter(data.split(','), dtype=int)

# Code borrowed from here: https://zonito.medium.com/lantern-fish-day-6-advent-of-code-2021-python-solution-4444387a8380

days = [0] * 9
# Update the current numbers
for fish in lanternfish:
    days[fish] += 1

for i in range(256):
    today = i % len(days)    # Add new babies
    days[(today + 7) % len(days)] += days[today]

print('Total lanternfish after 256 days: {}'.format(sum(days)))
