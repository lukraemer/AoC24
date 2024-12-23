from collections import defaultdict

connections = defaultdict(list)
with open("../input") as file:
    for line in file.readlines():
        pc1, pc2 = line.strip().split("-")
        connections[pc1].append(pc2)
        connections[pc2].append(pc1)

sets_of_connected_pcs = set()
for pc1, list_pcs in connections.items():
    pcs_to_add = [pc1]
    pcs_to_check = list_pcs.copy()
    while pcs_to_check:
        pc = pcs_to_check.pop()
        if pc not in pcs_to_add and all(pc in connections[pc2] for pc2 in pcs_to_add):
            pcs_to_add.append(pc)
            pcs_to_check.extend(connections[pc])
    sets_of_connected_pcs.add(tuple(sorted(pcs_to_add)))
longest = " "
for e in sets_of_connected_pcs:
    if len(e) > len(longest):
        longest = e
print(",".join(longest))
