keys = []
locks = []
with open("../input") as file:
    elements = file.read().strip().split("\n\n")
    for e in elements:
        e = e.split("\n")
        sums = [-1, -1, -1, -1, -1]
        for i in range(len(e)):
            for j in range(len(e[i])):
                if e[i][j] == "#":
                    sums[j] += 1
            print(sums)
            # e is lock
        if e[0] == "#####":
            locks.append(sums)
        else:
            keys.append(sums)
print(keys)
print(locks)
count_fitting_combs = 0
for k in keys:
    for l in locks:
        fit = True
        for i in range(len(k)):
            if k[i] + l[i] > 5:
                fit = False
                break
        if fit:
            count_fitting_combs += 1
print(count_fitting_combs)
