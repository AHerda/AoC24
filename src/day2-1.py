import os

day=2
os.system(f"bash src/get_data.sh {day}")

handle = open(f"data/zad0{day*2-1}-0{day * 2}", "r")
reports = list(map(lambda x: list(map(int, x.split(" "))), handle.read().split("\n")[:-1]))
handle.close()

def safe(report: list) -> bool:
    return all([0 < report[i + 1] - report[i] < 4 for i in range(len(report) - 1)]) \
        or all([0 > report[i + 1] - report[i] > -4 for i in range(len(report) - 1)])

print(sum([1 if safe(report) else 0 for report in reports]))