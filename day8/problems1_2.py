import numpy as np
import pandas as pd
import os

# Manually inputting data, aocd didn't work for this data
### Part 1

col_names = ["col" + str(i) for i in list(range(15))]

letters = pd.read_csv(os.path.join("day8", "input.txt"), names = col_names, sep=' ')

output_letters = letters[col_names[11:]].to_numpy()

strlen = np.vectorize(len)

strlens = strlen(output_letters)

_, counts = np.unique(strlens, return_counts = True)

nums = counts[0] + counts[1] + counts[2] + counts[5]

print(nums)

### Part 2 read this page to get some ideas (borrowed a lot of code from) https://zonito.medium.com/seven-segment-search-day-8-advent-of-code-2021-21e5bc965005

output_letters = letters[col_names[11:]]

input_letters = letters[col_names[:10]]

decodinator = {2:1, 4:4, 3:7, 7:8}

def word_descrambler(word):
    return ''.join(sorted(word))

def answermaker(letters, answers):
    for word in letters:
        word = word_descrambler(word)
        if word not in answers:
            for word in letters:
                word = word_descrambler(word)
                if len(word) in decodinator:
                    answers[decodinator[len(word)]] = word
            for word in letters:
                word = word_descrambler(word)
                if len(word) == 6 and not all(char in word for char in answers[1]):
                    answers[6] = word
            for word in letters:
                word = word_descrambler(word)
                if len(word) == 6 and word not in answers.values() and not all(char in word for char in answers[4]):
                    answers[0] = word
            for word in letters:
                word = word_descrambler(word)
                if len(word) == 6 and word not in answers.values():
                    answers[9] = word
            for word in letters:
                word = word_descrambler(word)
                if len(word) == 5 and all(char in word for char in answers[1]):
                    answers[3] = word
            for word in letters:
                word = word_descrambler(word)
                if len(word) == 5 and all(char in answers[6] for char in word):
                    answers[5] = word
            for word in letters:
                word = word_descrambler(word)
                if len(word) == 5 and word not in answers.values():
                    answers[2] = word
    return(answers)

# I coded the decodinatorifier and the answer_getterifier when I was tired so I don't think it's very effecient

def answer_getterifier(num, answer):
    for key, value in answer.items():
         if sorted(num) == sorted(value):
             return str(key)

def decodinatorifier(outputs, answers):
    num_list = []
    for i in outputs:
        for char in i:
            num_list.append(answer_getterifier(char, answers))
    number = int(''.join(num_list))
    return(number)

outputs = []

for index, row in input_letters.iterrows():
    answers = answermaker(row.values, {})
    answers = answermaker(output_letters.iloc[index], answers)
    outputs.append(decodinatorifier(output_letters.iloc[[index]].values, answers))

output_array = np.array(outputs)

print(output_array.sum())
