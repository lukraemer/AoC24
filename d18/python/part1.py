from collections import defaultdict
import math

f = open("../input", "r").read()

height, width = 6, 6
height, width = 70, 70
num_checked_bytes = 1024
cells = set()
for y in range(height + 1):
    for x in range(width + 1):
        cells.add((x, y))
lines = f.split("\n")
for i in range(num_checked_bytes):
    line = lines[i]
    print(line)
    x, y = list(map(int, line.strip().split(",")))
    if ((x, y)) in cells:
        cells.remove((x, y))


def print_grid(cells):
    for y in range(height + 1):
        for x in range(width + 1):
            if (x, y) not in cells:
                print("#", end="")
            else:
                print(".", end="")
        print()


def get_neighbors(cell, cells):
    x, y = cell
    s = set()
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        n = (x + d[0], y + d[1])
        if n in cells:
            s.add(n)
    return s


def dijkstra(cells, start, end):
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

        if current == end and current_cost < best_cost:
            best_end = current
            best_cost = current_cost

        unvisited.remove(current)

        if best_end and all(cost[x] >= best_cost for x in unvisited):
            break

        for neighbor in get_neighbors(current, cells):
            if neighbor not in unvisited:
                continue

            new_cost = current_cost + 1

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
end = (width, height)
path, cost = dijkstra(cells, start, end)
print(path)
print(cost)
# print(f"Result Part 1: {grid.get_sum_gps_coordinates_boxes()}")
