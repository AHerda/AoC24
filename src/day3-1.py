import re
import os

day=3
os.system(f"bash src/get_data.sh {day}")

handle = open(f"data/zad0{day*2-1}-0{day * 2}", "r")
pairs = re.findall("mul\((\d|\d\d|\d\d\d),(\d|\d\d|\d\d\d)\)", handle.read())
handle.close()

print(sum(map(lambda pair: int(pair[0]) * int(pair[1]), pairs)))
