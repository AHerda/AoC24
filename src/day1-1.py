import pandas as pd
import numpy as np
import os

day = 1
os.system(f"bash src/get_data.sh {day}")
data = pd.read_csv(f"data/zad0{day * 2 - 1}-0{day * 2}",
                   delimiter="   ",
                   names=["first", "second"],
                   engine="python")

first = data['first']
second = data['second']

first2 = np.sort(first)
second2 = np.sort(second)

diff = abs(first2 - second2)
print(sum(diff))
