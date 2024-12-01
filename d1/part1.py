f = open("input", "r")

l1 = list()
l2 = list()

for line in f:
    splitted_line =line.split("   ")
    l1.append(int(splitted_line[0]))
    l2.append(int(splitted_line[1].rstrip("\n")))

    l1 = sorted(l1)
    l2 = sorted(l2)

sum_distance = 0
for i, x in enumerate(l1):
    sum_distance += abs(l1[i] - l2[i])
    
print(f"Result Part 1: ", sum_distance)

