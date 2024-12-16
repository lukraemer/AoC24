from collections import defaultdict
import math

f = open("../input", "r").read()

m = []
for line in f.split("\n"):
    splitted_line = line.strip()  # map = list(line.strip()
    if line != "":
        m.append(splitted_line)  # map.append(splitted_line)


def get_neighbors(cell, cells):
    x, y, z = cell
    s = set()
    for d, valid_z in [((1, 0), 2), ((0, 1), 3), ((-1, 0), 4), ((0, -1), 1)]:
        n = (x + d[0], y + d[1], z)
        if n in cells and z == valid_z:
            s.add(n)

    # Add layer transitions
    for new_z in range(1, 5):
        if new_z != z:
            n = (x, y, new_z)
            if n in cells:
                s.add(n)
    return s


def dijkstra(cells, start, ends):
    cost = defaultdict(lambda: math.inf)
    prev = defaultdict(lambda: None)
    cost[start] = 0
    unvisited = set(cells)
    best_end = None
    best_cost = math.inf

    while unvisited:
        current = min(unvisited, key=lambda x: cost[x])
        current_cost = cost[current]

        if current_cost == math.inf:
            break

        if current in ends and current_cost < best_cost:
            best_end = current
            best_cost = current_cost

        unvisited.remove(current)

        if best_end and all(cost[x] >= best_cost for x in unvisited):
            break

        for neighbor in get_neighbors(current, cells):
            if neighbor not in unvisited:
                continue

            transition_cost = 1000 if neighbor[2] != current[2] else 1
            new_cost = current_cost + transition_cost

            if new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                prev[neighbor] = current

    path = []
    current = best_end
    while current is not None:
        path.append(current)
        current = prev[current]

    return path[::-1], best_cost


start = (0, 0)
ends = set()
cells = set()
for y in range(len(m)):
    for x in range(len(m[y])):
        if m[y][x] == "S":
            start = (x, y, 2)
            cells.add((x, y, 1))
            cells.add((x, y, 2))
            cells.add((x, y, 3))
            cells.add((x, y, 4))
        elif m[y][x] == "E":
            ends.add((x, y, 1))
            ends.add((x, y, 2))
            ends.add((x, y, 3))
            ends.add((x, y, 4))
            cells.add((x, y, 1))
            cells.add((x, y, 2))
            cells.add((x, y, 3))
            cells.add((x, y, 4))
        elif m[y][x] == ".":
            cells.add((x, y, 1))
            cells.add((x, y, 2))
            cells.add((x, y, 3))
            cells.add((x, y, 4))

path, cost = dijkstra(cells, start, ends)
print(path)
print(cost)
# print(f"Result Part 1: {grid.get_sum_gps_coordinates_boxes()}")
