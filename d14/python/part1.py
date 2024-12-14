from collections import Counter
from math import ceil, floor


class Robot:
    def __init__(self, pos_x, pos_y, v_x, v_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = v_x
        self.v_y = v_y

    def get_pos(self):
        return self.pos_x, self.pos_y

    def get_vel(self):
        return self.v_x, self.v_y

    def __repr__(self):
        return f"Robot({self.pos_x}, {self.pos_y}, {self.v_x}, {self.v_y})"


width = 101
# width = 11
height = 103
# height = 7
seconds = 100
with open("../input", "r") as f:
    robots = list()
    for line in f.readlines():
        pos_x, pos_y = list(
            map(int, line.strip().split(" ")[0].split("=")[1].split(","))
        )
        v_x, v_y = list(map(int, line.strip().split(" ")[1].split("=")[1].split(",")))
        robots.append(Robot(pos_x, pos_y, v_x, v_y))

    for i in range(seconds):
        for r in robots:
            pos_x, pos_y = r.get_pos()
            v_x, v_y = r.get_vel()
            new_x = (pos_x + v_x + width) % width
            new_y = (pos_y + v_y + height) % height
            r.pos_x = new_x
            r.pos_y = new_y

    positions = list()
    quadrants = [0, 0, 0, 0]
    for r in robots:
        pos_x, pos_y = r.get_pos()
        positions.append((pos_x, pos_y))
        middle_x = floor(width / 2)
        middle_y = floor(height / 2)
        if pos_x < middle_x:
            if pos_y < middle_y:
                quadrants[0] += 1
            elif pos_y > middle_y:
                quadrants[1] += 1
        elif pos_x > middle_x:
            if pos_y < middle_y:
                quadrants[2] += 1
            elif pos_y > middle_y:
                quadrants[3] += 1

    counter = Counter(positions)
    for y in range(height):
        for x in range(width):
            if (x, y) in positions:
                print(counter[(x, y)], end="")
            else:
                print(".", end="")
        print()
    print(quadrants)

    print(f"Result part 1: {quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]}")
