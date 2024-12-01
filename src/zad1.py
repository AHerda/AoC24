import pandas as pd
import numpy as np

data = pd.read_csv("data/zad1-2.csv")

first = data['first']
second = data['second']

first2 = np.sort(first)
second2 = np.sort(second)

diff = abs(first2 - second2)
print(sum(diff))
