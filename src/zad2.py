import pandas as pd
import numpy as np

data = pd.read_csv("data/zad1-2.csv")

first = data['first']
second = data['second']

unique, counts = np.unique(second, return_counts=True)
counts_dict = dict(zip(unique, counts))

score = 0
for number in first:
    if number in counts_dict.keys():
        score += number * counts_dict[number]

print(score)
