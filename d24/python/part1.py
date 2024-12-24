wires = {}
gates = []
with open("../input") as file:
    w, g = file.read().split("\n\n")
    for wire in w.split("\n"):
        wires[wire.split(" ")[0][:-1]] = True if wire.split(" ")[1] == "1" else False
    for gate in g.split("\n"):
        if gate == "":
            continue
        w1, op, w2, _, out = gate.split(" ")
        gates.append((w1, op, w2, out))
while len(gates) > 0:
    for gate in gates:
        w1, op, w2, out = gate
        match op:
            case "AND":
                if w1 in wires.keys() and w2 in wires.keys():
                    wires[out] = wires[w1] & wires[w2]
                    gates.remove(gate)
            case "OR":
                if w1 in wires and wires[w1]:
                    wires[out] = True
                    gates.remove(gate)
                elif w2 in wires and wires[w2]:
                    wires[out] = True
                    gates.remove(gate)
                elif w1 in wires and w2 in wires:
                    if not wires[w1] and not wires[w2]:
                        wires[out] = False
                        gates.remove(gate)
            case "XOR":
                if w1 in wires and w2 in wires:
                    wires[out] = wires[w1] ^ wires[w2]
                    gates.remove(gate)
binary = ""
for wire in sorted(wires, reverse=True):
    if wire.startswith("z"):
        binary += "1" if wires[wire] else "0"
        print(wire, wires[wire])
print(int(binary, 2))
