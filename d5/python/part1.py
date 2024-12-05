import math


def check_update(update, rules) -> bool:
    print(f"Checking {update}")
    printed_pages = set()
    for u in update:
        valid_page = True
        for e in rules[u]:
            if e not in printed_pages and e in update:
                print(f"page {u}")
                print(f"broke on {e}")
                print(f"because {rules[u]}")
                valid_page = False
        if valid_page:
            printed_pages.add(u)
            print(f"added {u}")
        else:
            return False
    return True


f = open("../input", "r")

rules_over = False
rules = {}
updates = []
sum = 0
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
            sum += update[math.floor(len(update) / 2)]


# print(rules)
# print(updates)
print("Result Part 1: ", sum)
