# class for representaion of a 2D grid
class Grid:
    def __init__(self, map):
        self.map = map
        self.antennas = {}  # dict of key char to list of coords list(int,int)
        self.antinodes = set()
        self.width = len(self.map[0])
        self.height = len(self.map)
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == ".":
                    continue
                else:
                    if self.map[y][x] in self.antennas:
                        self.antennas[self.map[y][x]].append((x, y))
                    else:
                        self.antennas[self.map[y][x]] = [(x, y)]
        self.compute_antinodes()
        print(self.antinodes)

    def get_cell(self, x, y):
        return map[y][x]

    def __str__(self):
        s = ""
        for i in range(len(self.map)):
            s = s + str(self.map[i]) + "\n"
        return s

    def get_representation(self):
        for y in range(self.height):
            for x in range(self.width):
                c = "."
                for k, v in self.antennas.items():
                    for x1, y1 in v:
                        if x == x1 and y == y1:
                            c = k
                if (x, y) in self.antinodes:
                    if c == ".":
                        c = "#"
                    else:
                        c = "(" + c + ")"
                print(c, end="")
            print()

    def compute_antinodes(self):
        for k, v in self.antennas.items():
            for x, y in v:
                for x1, y1 in v:
                    if x1 == x and y1 == y:
                        continue
                    else:
                        dist_x = abs(x1 - x)
                        dist_y = abs(y1 - y)
                        if x1 > x and y1 > y:
                            self.antinodes.add(((x - dist_x, y - dist_y)))
                            self.antinodes.add(((x1 + dist_x, y1 + dist_y)))
                        elif x1 > x and y1 <= y:
                            self.antinodes.add(((x - dist_x, y + dist_y)))
                            self.antinodes.add(((x1 + dist_x, y1 - dist_y)))
                        elif x1 <= x and y1 > y:
                            self.antinodes.add(((x + dist_x, y - dist_y)))
                            self.antinodes.add(((x1 - dist_x, y1 + dist_y)))
                        else:
                            self.antinodes.add(((x + dist_x, y + dist_y)))
                            self.antinodes.add(((x1 - dist_x, y1 - dist_y)))

    # function to count the number of antinodes in bounds
    def count_antinodes_in_bounds(self):
        count = 0
        for a in self.antinodes:
            if a[0] >= 0 and a[0] < self.width and a[1] >= 0 and a[1] < self.height:
                count += 1
        return count


f = open("../input", "r")

map = []

for line in f:
    splitted_line = list(line.strip())
    map.append(splitted_line)

grid = Grid(map)
print(grid)
print(grid.get_representation())

print(f"Result Part 1: {grid.count_antinodes_in_bounds()}")
