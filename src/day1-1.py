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

first2 = np.sort(first)
second2 = np.sort(second)

diff = abs(first2 - second2)
print(sum(diff))
