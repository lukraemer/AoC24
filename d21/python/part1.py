import heapq
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


def sort_commands_numeric(commands):
    groups = {"^": [], "v": [], "<": [], ">": []}
    for c in commands:
        groups[c].append(c)
    sorted_commands = groups["^"] + groups[">"] + groups["v"] + groups["<"]
    return sorted_commands


def sort_commands_directional(commands):
    groups = {"^": [], "v": [], "<": [], ">": []}
    for c in commands:
        groups[c].append(c)
    sorted_commands = groups["v"] + groups[">"] + groups["^"] + groups["<"]
    return sorted_commands


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


def get_code_numeric_keypad(numeric_code):
    keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
    start = numeric_keypad["A"]
    commands = []
    for n in numeric_code:
        n = numeric_keypad[n]
        commands.extend(dijkstra(keypad, start, n))
        start = n
    print(numeric_code)
    print("".join(commands))
    return commands


def get_code_directional_keypad(directional_code):
    keypad = [[None, "^", "A"], ["<", "v", ">"]]
    start = directional_keypad["A"]
    commands = []
    for n in directional_code:
        n = directional_keypad[n]
        commands.extend(dijkstra(keypad, start, n))
        start = n
    print(directional_code)
    print("".join(commands))
    return commands


def get_code(codes):
    start = "A"
    commands = ""
    for c in codes:
        commands += moves.moves[(start, c)]
        start = c
    return commands


with open("../input") as file:
    codes = file.read().splitlines()
    sum = 0
    for code in list(map(list, codes)):
        # for code in input.strip().splitlines():
        # n_code = get_code_numeric_keypad(code)
        # d_code = get_code_directional_keypad(n_code)
        # d_code = get_code_directional_keypad(d_code)
        n_code = get_code(code)
        d_code = get_code(get_code(n_code))
        res = len(d_code) * int("".join(code[:-1]))
        print(f"Result: {res} for code {''.join(code)} with length {len(d_code)}")
        print(f"Code: {d_code}")
        sum += res
    print(sum)
