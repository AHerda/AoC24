import os

day=5
if not os.path.exists(f"data/day{day}"):
    os.system(f"bash src/get_data.sh {day}")

handle = open(f"data/day{day}", "r")
rules, updates = handle.read().split("\n\n")
handle.close()

rules = list(map(lambda pair: (int(pair.split("|")[0]), int(pair.split("|")[1])), rules.split("\n")))
updates = list(map(lambda update: list(map(int, update.split(","))), updates.split("\n")[:-1]))

rules_dict = dict()
for first, after in rules:
    if first not in rules_dict.keys():
        rules_dict[first] = []
    rules_dict[first].append(after)

result = 0

for update in updates:
    valid = True
    for i, page in enumerate(update):
        for j, previous_page in enumerate(update[:i]):
            if page in rules_dict.keys() and previous_page in rules_dict[page]:
                valid = False
                update.insert(j, update.pop(i))
                break
    if not valid:
        result += update[int((len(update) - 1) / 2)]

print(result)
