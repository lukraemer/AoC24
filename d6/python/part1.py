# class for representaion of a 2D grid
class Grid:
    def __init__(self, map):
        self.map = map
        self.obs = list((int, int))
        self.already_visited_cells = set((int, int))
        self.guard = (0, 0, "N")
        self.width = len(self.map[0])
        self.height = len(self.map)
        for y in range(self.height):
            for x in range(self.width):
                if self.get_cell(x, y) == ".":
                    continue
                elif self.get_cell(x, y) == "#":
                    self.obs.append((x, y))
                elif self.get_cell(x, y) == "^":
                    self.guard = (x, y, "N")

    def get_cell(self, x, y):
        return map[y][x]

    def __str__(self):
        s = ""
        for i in range(len(self.map)):
            s = s + str(self.map[i]) + "\n"
        return s

    def get_guard_representation(self):
        if self.guard[2] == "N":
            return "^"
        if self.guard[2] == "S":
            return "v"
        if self.guard[2] == "E":
            return ">"  #
        if self.guard[2] == "W":
            return "<"

    def get_representation(self):
        for y in range(self.height):
            for x in range(self.width):
                c = ""
                if (x, y) in self.obs:
                    c = "#"
                elif x == self.guard[0] and y == self.guard[1]:
                    c = self.get_guard_representation()
                elif (x, y) in self.already_visited_cells:
                    c = "X"
                else:
                    c = "."
                print(c, end="")
            print()

    def rotate(self):
        if self.guard[2] == "N":
            self.guard = (self.guard[0], self.guard[1], "E")
            return
        if self.guard[2] == "E":
            self.guard = (self.guard[0], self.guard[1], "S")
            return
        if self.guard[2] == "S":
            self.guard = (self.guard[0], self.guard[1], "W")
            return
        if self.guard[2] == "W":
            self.guard = (self.guard[0], self.guard[1], "N")
            return

    def walk(self):
        dir = self.guard[2]
        next_cell = (0, 0)
        if dir == "N":
            next_cell = (self.guard[0], self.guard[1] - 1)
        if dir == "S":
            next_cell = (self.guard[0], self.guard[1] + 1)
        if dir == "E":
            next_cell = (self.guard[0] + 1, self.guard[1])
        if dir == "W":
            next_cell = (self.guard[0] - 1, self.guard[1])

        if (
            next_cell[0] < 0
            or next_cell[0] >= self.width
            or next_cell[1] < 0
            or next_cell[1] >= self.height
        ):
            return False

        if (next_cell[0], next_cell[1]) in self.obs:
            self.rotate()
            return True
        self.already_visited_cells.add((self.guard[0], self.guard[1]))
        self.guard = (next_cell[0], next_cell[1], dir)
        return True

    def get_count_already_visited_cells(self):
        return len(self.already_visited_cells)


f = open("../input", "r")

map = []

for line in f:
    splitted_line = list(line.strip())
    map.append(splitted_line)

grid = Grid(map)
print(grid.get_representation())
while grid.walk():
    pass

res = grid.get_count_already_visited_cells()
print(f"Result Part 1: {res}")
