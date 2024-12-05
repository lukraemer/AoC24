import math


def check_update(update, rules) -> bool:
    print(f"Checking {update}")
    printed_pages = set()
    for u in update:
        valid_page = True
        if u not in rules:
            print(f"{u} not in {rules}")
        else:
            for e in rules[u]:
                if e not in printed_pages and e in update:
                    valid_page = False
        if valid_page:
            printed_pages.add(u)
        else:
            return False
    return True


def apply_rule(update, rules):
    printed_pages = set()
    for u in update:
        if u not in rules:
            print(f"{u} not in {rules}")
            printed_pages.add(u)
            continue
        for e in rules[u]:
            print(
                f"searching for u:{u} e:{e} in {rules[u]} with printed_pages:{printed_pages}"
            )
            if e not in printed_pages and e in update:
                print(f"replace {u} with {e}")
                a, b = update.index(u), update.index(e)
                update[b], update[a] = update[a], update[b]
                return update
        printed_pages.add(u)
    return update


f = open("../input", "r")

rules_over = False
rules = {}
updates = []
sum_correct = 0
sum_incorrect = 0
for line in f:
    if line == "\n":
        rules_over = True
        continue
    if not rules_over:
        splitted_line = line.strip().split("|")
        before_page, after_page = list(map(int, splitted_line))
        if after_page in rules:
            rules[after_page].append(before_page)
        else:
            rules[after_page] = [before_page]
    else:
        splitted_line = line.strip().split(",")
        update = list(map(int, splitted_line))
        updates.append(update)

        if check_update(update, rules):
            sum_correct += update[math.floor(len(update) / 2)]
            print(f"Check of {update} succesful")
        else:
            u = update
            while not check_update(u, rules):
                u = apply_rule(u, rules)
            print(f"Check of {u} succesful")
            sum_incorrect += u[math.floor(len(u) / 2)]


# print(rules)
# print(updates)
print("Result Part 1: ", sum_correct)
print("Result Part 2: ", sum_incorrect)
