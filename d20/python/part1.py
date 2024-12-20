from collections import defaultdict
from collections import Counter
import sys
import heapq

f = open("../input", "r").read()


def print_grid(cells):
    for y in range(height):
        for x in range(width):
            if (x, y) not in cells:
                print("#", end="")
            else:
                print(".", end="")
        print()


def get_neighbor_cells(cell, cells):
    x, y = cell
    s = set()
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        n = (x + d[0], y + d[1])
        if n in cells:
            s.add(n)
    return s


def get_neighbors(cell):
    x, y = cell
    s = set()
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        n = (x + d[0], y + d[1])
        if 0 <= n[0] < width and 0 <= n[1] < height:
            s.add(n)
    return s


def dijkstra(cells, start, end):
    unvisited = [(0, start)]
    heapq.heapify(unvisited)
    visited = set()
    cost = {start: 0}
    while unvisited:
        current_cost, current = heapq.heappop(unvisited)
        if current in visited:
            continue
        visited.add(current)
        if current == end:
            break

        for neighbor in get_neighbor_cells(current, cells):
            if neighbor in visited:
                continue
            if neighbor not in cost or cost[neighbor] > current_cost + 1:
                cost[neighbor] = current_cost + 1
                heapq.heappush(unvisited, (current_cost + 1, neighbor))

    return cost[end]


cells = set()
start = (0, 0)
end = (0, 0)
lines = f.strip().split("\n")
height = len(lines)
width = len(lines[0])
checked_cheats = {}
for y in range(height):
    for x in range(width):
        if lines[y][x] == "#":
            continue
        cells.add((x, y))
        if lines[y][x] == "S":
            start = (x, y)
        if lines[y][x] == "E":
            end = (x, y)
print_grid(cells)
original_cost = dijkstra(cells, start, end)
for y in range(height):
    for x in range(width):
        for n in get_neighbors((x, y)):
            print(f"Checking {n}")
            if (n) not in checked_cheats.keys():
                if (x, y) not in cells:
                    continue
                if n in cells:
                    continue
                tmp_cells = cells.copy()
                tmp_cells.add(n)
                new_cost = dijkstra(tmp_cells, start, end)
                cheat_cost = original_cost - new_cost
                checked_cheats[n] = cheat_cost

print(checked_cheats)
count = sum(1 for v in checked_cheats.values() if v >= 100)

# for _, v in checked_cheats.items():

print(f"Result Part 1: {count}")
