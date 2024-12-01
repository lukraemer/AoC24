f = open("input", "r")

l1 = list()
l2 = list()

d = dict()

for line in f:
    splitted_line =line.split("   ")
    l1.append(int(splitted_line[0]))
    l2_element =int(splitted_line[1].rstrip("\n")) 
    l2.append(l2_element)

    if l2_element in d:
        d[l2_element] += 1
    else:
        d[l2_element] = 1

print(d)

score = 0

for x in l1:
    if x in d:
        count = d[x]
        score += x * count
    
print(f"Result Part 2: ",score )

