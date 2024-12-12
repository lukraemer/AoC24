from collections import defaultdict


# class for representaion of a 2D grid
class Grid:
    def __init__(self, map):
        self.map = map
        # Dict of areas with areacode key:(arealiteral , number) value: set of all cells in the area
        self.areas = defaultdict(set)
        self.already_visited = set()

        self.width = len(self.map[0])
        self.height = len(self.map)
        i = 0
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) not in self.already_visited:
                    self.bfd(x, y, i)
                    i += 1

    def bfd(self, x, y, n):
        if (x, y) not in self.already_visited:
            self.already_visited.add((x, y))
            self.areas[(self.get_cell(x, y), n)].add((x, y))
            if self.get_N(x, y) == self.get_cell(x, y):
                self.bfd(x, y - 1, n)
            if self.get_S(x, y) == self.get_cell(x, y):
                self.bfd(x, y + 1, n)
            if self.get_E(x, y) == self.get_cell(x, y):
                self.bfd(x + 1, y, n)
            if self.get_W(x, y) == self.get_cell(x, y):
                self.bfd(x - 1, y, n)

    def get_count_fences(self, area_cells):
        count = 0
        for e in area_cells:
            x, y = e
            if self.get_N(x, y) != self.get_cell(x, y):
                count += 1
            if self.get_S(x, y) != self.get_cell(x, y):
                count += 1
            if self.get_E(x, y) != self.get_cell(x, y):
                count += 1
            if self.get_W(x, y) != self.get_cell(x, y):
                count += 1
        return count

    def get_price(self):
        price = 0
        for k in self.areas:
            v = self.areas[k]
            price += len(v) * self.get_count_fences(v)
            print(f"Area {k}: {len(v)} cells, {self.get_count_fences(v)} fences")
        return price

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

    def get_corners(self, x, y):
        count = 0
        if self.get_N(x, y) != self.get_cell(x, y):
            if self.get_E(x, y) != self.get_cell(x, y):
                count += 1
            if self.get_W(x, y) != self.get_cell(x, y):
                count += 1
        if self.get_S(x, y) != self.get_cell(x, y):
            if self.get_E(x, y) != self.get_cell(x, y):
                count += 1
            if self.get_W(x, y) != self.get_cell(x, y):
                count += 1
        return count

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


f = open("../input", "r")

m = []

for line in f:
    splitted_line = list(line.strip())  # map = list(line.strip())
    m.append(splitted_line)  # map.append(splitted_line)

grid = Grid(m)
print(grid)
print(grid.get_representation())
print(grid.areas)
print(len(grid.areas))
print(f"Result Part 1: {grid.get_price()}")
