# class for representaion of a 2D grid
class Grid:
    def __init__(self, map):
        self.map = map
        self.trailheads = {}

        self.width = len(self.map[0])
        self.height = len(self.map)

        for y in range(self.height):
            for x in range(self.width):
                if self.get_cell(x, y) == 0:
                    self.trailheads[(x, y)] = []
        self.score = 0
        for t in self.trailheads:
            self.score += self.do_step(t[0], t[1], 0, t[0], t[1])

    def get_cell(self, x, y):
        return self.map[y][x]

    def __str__(self):
        s = ""
        for i in range(len(self.map)):
            s = s + str(self.map[i]) + "\n"
        return s

    def get_representation(self):
        for y in range(self.height):
            for x in range(self.width):
                c = self.get_cell(x, y)
                print(c, end="")
            print()

    def get_N(self, x, y):
        if 0 <= x < self.width and 0 <= y - 1 < self.height:
            return self.get_cell(x, y - 1)
        else:
            return 0

    def get_S(self, x, y):
        if 0 <= x < self.width and 0 <= y + 1 < self.height:
            return self.get_cell(x, y + 1)
        else:
            return 0

    def get_E(self, x, y):
        if 0 <= x + 1 < self.width and 0 <= y < self.height:
            return self.get_cell(x + 1, y)
        else:
            return 0

    def get_W(self, x, y):
        if 0 <= x - 1 < self.width and 0 <= y < self.height:
            return self.get_cell(x - 1, y)
        else:
            return 0

    def do_step(self, x, y, n, x0, y0):
        # if n == 9 and not (x, y) in self.trailheads[(x0, y0)]:
        #    self.trailheads[(x0, y0)].append((x, y))
        #    return 1
        if n == 9:
            return 1
        score = 0
        if self.get_N(x, y) == n + 1:
            score += self.do_step(x, y - 1, n + 1, x0, y0)
        if self.get_S(x, y) == n + 1:
            score += self.do_step(x, y + 1, n + 1, x0, y0)
        if self.get_E(x, y) == n + 1:
            score += self.do_step(x + 1, y, n + 1, x0, y0)
        if self.get_W(x, y) == n + 1:
            score += self.do_step(x - 1, y, n + 1, x0, y0)
        # print(f"Do step from x:{x} y:{y} n:{n}  score:{score}")
        return score


f = open("../input", "r")

m = []

for line in f:
    splitted_line = list(map(int, line.strip()))  # map = list(line.strip())
    m.append(splitted_line)  # map.append(splitted_line)

grid = Grid(m)
print(grid.get_representation())
print(grid.trailheads)
print(len(grid.trailheads))

print(f"Result Part 1: {grid.score}")
