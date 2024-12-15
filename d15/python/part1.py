from collections import defaultdict


# class for representaion of a 2D grid
class Grid:
    def __init__(self, map):
        self.map = map
        self.walls = list()
        self.robot = (0, 0)
        self.boxes = list()

        self.width = len(self.map[0])
        self.height = len(self.map)
        for y in range(self.height):
            for x in range(self.width):
                match self.get_cell(x, y):
                    case "#":
                        self.walls.append((x, y))
                    case "O":
                        self.boxes.append((x, y))
                    case "@":
                        self.robot = (x, y)

    def get_cell(self, x, y):
        return self.map[y][x]

    def __str__(self):
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.robot:
                    c = "@"
                elif (x, y) in self.walls:
                    c = "#"
                elif (x, y) in self.boxes:
                    c = "O"
                else:
                    c = "."
                s = s + c
            s += "\n"
        return s

    def get_representation(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.robot:
                    c = "@"
                elif (x, y) in self.walls:
                    c = "#"
                elif (x, y) in self.boxes:
                    c = "O"
                else:
                    c = "."
                print(c, end="")
            print()

    def go_north(self):
        found_free = False
        (x, y) = self.robot
        (x, y) = (x, y - 1)
        while (x, y) not in self.walls and not found_free:
            # Check if not in boxes and not a wall -> free field
            if (x, y) not in self.boxes:
                found_free = True
                break
            (x, y) = (x, y - 1)
        if found_free:
            self.robot = (self.robot[0], self.robot[1] - 1)
            (x, y) = self.robot
            new_boxes = []
            while (x, y) in self.boxes and (x, y - 1) not in self.walls:
                new_boxes.append((x, y - 1))
                del self.boxes[self.boxes.index((x, y))]
                (x, y) = (x, y - 1)
            self.boxes.extend(new_boxes)

    def go_east(self):
        found_free = False
        (x, y) = self.robot
        (x, y) = (x + 1, y)
        while (x, y) not in self.walls and not found_free:
            # Check if not in boxes and not a wall -> free field
            if (x, y) not in self.boxes:
                found_free = True
                break
            (x, y) = (x + 1, y)
        if found_free:
            self.robot = (self.robot[0] + 1, self.robot[1])
            (x, y) = self.robot
            new_boxes = []
            while (x, y) in self.boxes and (x + 1, y) not in self.walls:
                new_boxes.append((x + 1, y))
                del self.boxes[self.boxes.index((x, y))]
                (x, y) = (x + 1, y)
            self.boxes.extend(new_boxes)

    def go_south(self):
        found_free = False
        (x, y) = self.robot
        (x, y) = (x, y + 1)
        while (x, y) not in self.walls and not found_free:
            # Check if not in boxes and not a wall -> free field
            if (x, y) not in self.boxes:
                found_free = True
                break
            (x, y) = (x, y + 1)
        if found_free:
            self.robot = (self.robot[0], self.robot[1] + 1)
            (x, y) = self.robot
            new_boxes = []
            while (x, y) in self.boxes and (x, y + 1) not in self.walls:
                new_boxes.append((x, y + 1))
                del self.boxes[self.boxes.index((x, y))]
                (x, y) = (x, y + 1)
            self.boxes.extend(new_boxes)

    def go_west(self):
        found_free = False
        (x, y) = self.robot
        (x, y) = (x - 1, y)
        while (x, y) not in self.walls and not found_free:
            # Check if not in boxes and not a wall -> free field
            if (x, y) not in self.boxes:
                found_free = True
                break
            (x, y) = (x - 1, y)
        if found_free:
            self.robot = (self.robot[0] - 1, self.robot[1])
            (x, y) = self.robot
            new_boxes = []
            while (x, y) in self.boxes and (x - 1, y) not in self.walls:
                new_boxes.append((x - 1, y))
                del self.boxes[self.boxes.index((x, y))]
                (x, y) = (x - 1, y)
            self.boxes.extend(new_boxes)

    def do_step(self, c):
        match c:
            case "<":
                self.go_west()
            case ">":
                self.go_east()
            case "^":
                self.go_north()
            case "v":
                self.go_south()

    def get_sum_gps_coordinates_boxes(self):
        sum = 0
        for b in self.boxes:
            sum += b[0] + b[1] * 100
        return sum


f = open("../input", "r").read()

matrix, commands = f.split("\n\n")

print(matrix)

m = []
c = []
for line in matrix.split("\n"):
    splitted_line = line.strip()  # map = list(line.strip()
    m.append(splitted_line)  # map.append(splitted_line)
for line in commands:
    c.extend(line.strip())

print("Commands")
print(c)
grid = Grid(m)
print(grid)
for command in c:
    grid.do_step(command)
# print(grid.get_representation())
print(f"Result Part 1: {grid.get_sum_gps_coordinates_boxes()}")
