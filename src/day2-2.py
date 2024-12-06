import os

day=2
if not os.path.exists(f"data/day{day}"):
    os.system(f"bash src/get_data.sh {day}")

handle = open(f"data/day{day}", "r")
reports = list(map(lambda x: list(map(int, x.split(" "))), handle.read().split("\n")[:-1]))
handle.close()

def safe(report: list, dampner_used: bool) -> bool:
    if all([0 < report[i + 1] - report[i] < 4 for i in range(len(report) - 1)]) \
        or all([0 > report[i + 1] - report[i] > -4 for i in range(len(report) - 1)]):
        return True
    elif dampner_used:
        return False

    asc = False if report[0] - report[1] > 0 else True

    if 2 < len(report):
        asc2 = False if report[1] - report[2] > 0 else True
        if asc2 != asc:
            rep = report.copy()
            del rep[0]
            if safe(rep, True):
                return True

    for i in range(len(report) - 1):
        if (not asc and report[i + 1] - report[i] not in range(-1, -4, -1)) \
            or (asc and report[i + 1] - report[i] not in range(1, 4)):
            rep1 = report.copy()
            rep2 = report.copy()
            del rep1[i]
            del rep2[i+1]
            return safe(rep1, True) or safe(rep2, True)
    print("wrong!!!!!")

print(sum([1 if safe(report.copy(), False) else 0 for report in reports]))
