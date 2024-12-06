import pandas as pd
import numpy as np
import os

day = 1
if not os.path.exists(f"data/day{day}"):
    os.system(f"bash src/get_data.sh {day}")
data = pd.read_csv(f"data/day{day}",
                   delimiter="   ",
                   names=["first", "second"],
                   engine="python")

first = data['first']
second = data['second']

unique, counts = np.unique(second, return_counts=True)
counts_dict = dict(zip(unique, counts))

score = 0
for number in first:
    if number in counts_dict.keys():
        score += number * counts_dict[number]

print(score)
