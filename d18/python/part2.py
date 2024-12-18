from collections import defaultdict
import sys
import heapq

f = open("../input", "r").read()


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
            return True

        for neighbor in get_neighbors(current, cells):
            if neighbor in visited:
                continue
            if neighbor not in cost or cost[neighbor] > current_cost + 1:
                cost[neighbor] = current_cost + 1
                heapq.heappush(unvisited, (current_cost + 1, neighbor))

    return False


height, width = 6, 6
height, width = 70, 70
cells = set()
start = (0, 0)
end = (width, height)
for y in range(height + 1):
    for x in range(width + 1):
        cells.add((x, y))
for line in f.split("\n"):
    if line == "":
        continue
    x, y = list(map(int, line.strip().split(",")))
    if ((x, y)) in cells:
        cells.remove((x, y))
    found = dijkstra(cells, start, end)
    if not found:
        print(f"No path found after inserting {x}, {y}")
        sys.exit(0)

# print(f"Result Part 1: {grid.get_sum_gps_coordinates_boxes()}")
