from collections import defaultdict

connections = defaultdict(list)
with open("../input") as file:
    for line in file.readlines():
        pc1, pc2 = line.strip().split("-")
        connections[pc1].append(pc2)
        connections[pc2].append(pc1)

sets_of_3 = set()
for pc1, list_pcs in connections.items():
    for pc2 in list_pcs:
        for pc3 in connections[pc2]:
            if pc1 in connections[pc3]:
                if pc1.startswith("t") or pc2.startswith("t") or pc3.startswith("t"):
                    sets_of_3.add(tuple(sorted([pc1, pc2, pc3])))
print(sets_of_3)
print(len(sets_of_3))
