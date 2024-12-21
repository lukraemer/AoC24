import heapq
from functools import cache
import moves

numeric_keypad = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}
numeric_keypad_rev = {
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    (0, 1): "4",
    (1, 1): "5",
    (2, 1): "6",
    (0, 2): "1",
    (1, 2): "2",
    (2, 2): "3",
    (1, 3): "0",
    (2, 3): "A",
}
directional_keypad = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}

paths_numeric = {}


def get_neighbors(cell, keypad):
    height = len(keypad)
    width = len(keypad[0])
    x, y = cell
    s = set()
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        n = (x + d[0], y + d[1])
        if 0 <= n[0] < width and 0 <= n[1] < height and keypad[n[1]][n[0]] is not None:
            s.add(n)
    return s


def dijkstra(cells, start, end):
    unvisited = [(0, start)]
    heapq.heapify(unvisited)
    visited = set()
    cost = {start: 0}
    prev = {}
    while unvisited:
        current_cost, current_cell = heapq.heappop(unvisited)
        if current_cell in visited:
            continue
        visited.add(current_cell)
        if current_cell == end:
            break
        for neighbor in get_neighbors(current_cell, cells):
            if neighbor in visited:
                continue
            if neighbor not in cost or cost[neighbor] > current_cost + 1:
                cost[neighbor] = current_cost + 1
                prev[neighbor] = current_cell
                heapq.heappush(unvisited, (current_cost + 1, neighbor))
    path = [end]
    commands = []
    current = end
    while current != start:
        match (current[0] - prev[current][0], current[1] - prev[current][1]):
            case (1, 0):
                commands.append(">")
            case (-1, 0):
                commands.append("<")
            case (0, 1):
                commands.append("v")
            case (0, -1):
                commands.append("^")
        current = prev[current]
        path.append(current)
    return (commands) + ["A"]


@cache
def get_code(codes, depth):
    if depth > 20:
        print(f"Getting code for {codes} with depth {depth}")
    if depth == 0:
        return len(codes)
    len_commands = 0
    start = "A"
    for c in codes:
        len_commands += get_code(moves.moves[(start, c)], depth - 1)
        start = c
    return len_commands


num_directional_keypads = 25
with open("../input") as file:
    codes = file.read().splitlines()
    sum = 0
    for code in list(codes):
        print(f"Working on Code: {''.join(code)}")
        res = get_code(code, num_directional_keypads + 1)
        res = res * int("".join(code[:-1]))
        print(f"Result: {res} for code {''.join(code)} with length {res}")
        sum += res
    print(sum)
