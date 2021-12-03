from aocd.models import Puzzle
import numpy as np
import pandas as pd

def filter(df, values):
    for column in df.columns:
        sum = df[column].sum()
        len = df.shape[0]
        if len == 1:
            break
        majority = len/2
        if sum < majority:
            df = df[df[column] == values[0]]
        else:
            df = df[df[column] == values[1]]
    return df

puzzle = Puzzle(year=2021, day=3)

data = puzzle.input_data

data_list = data.split('\n')

data_np_list = [np.fromiter(binary, dtype=int) for binary in data_list]

headers = ["col" + str(i) for i in range(12)]

df = pd.DataFrame(
        data_np_list,
        columns=headers
)

o2_df, co2_df = df.copy(), df.copy()

o2_df = filter(o2_df, (1, 0))
co2_df = filter(co2_df, (0, 1))

o2_value = ''.join(o2_df.values.astype(str)[0])
o2_int = int(o2_value, 2)

co2_value = ''.join(co2_df.values.astype(str)[0])
co2_int = int(co2_value, 2)

answer2 = o2_int * co2_int

puzzle.answer_b = answer2
