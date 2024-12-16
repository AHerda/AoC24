import os

day = 7
if not os.path.exists(f"data/day{day}"):
    os.system(f"bash src/get_data.sh {day}")

handle = open(f"data/day{day}", "r")
equations = list(map(lambda row: (int(row.split(":")[0]), list(map(int, row.split(":")[1][1:].split(" ")))), handle.read().split("\n")[:-1]))
handle.close()

def can_be_unconcantenated(a, b):
    lvl = 10
    while lvl <= b:
        lvl *= 10
    if a % lvl == b:
        return True
    return False

def unconcantenate(a, b):
    lvl = 10
    while lvl <= b:
        lvl *= 10
    a -= b
    a /= lvl
    return a

def test(equation):
    result = equation[0]
    numbers = equation[1]
    if len(numbers) == 0:
        if result == 0:
            return True
        else:
            return False
    return test((result / numbers[-1], numbers[:-1])) or test((result - numbers[-1], numbers[:-1])) or (test((unconcantenate(result, numbers[-1]), numbers[:-1])) if can_be_unconcantenated(result, numbers[-1]) else False)


print(sum(map(lambda x: x[0], filter(test, equations.copy()))))
