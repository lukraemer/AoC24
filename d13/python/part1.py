import re

pattern = r"""Button A: X[+=](\d+), Y[+=](\d+)\s*
Button B: X[+=](\d+), Y[+=](\d+)\s*
Prize: X[+=](\d+), Y[+=](\d+)"""


def find_lowest_token(
    button_a_x,
    button_a_y,
    button_b_x,
    button_b_y,
    prize_x,
    prize_y,
    button_a_press_count,
    button_b_press_count,
):
    results = set()
    for a in range(100):
        for b in range(100):
            calc_prize_x = a * button_a_x + b * button_b_x
            calc_prize_y = a * button_a_y + b * button_b_y
            if prize_x == calc_prize_x and prize_y == calc_prize_y:
                results.add(a * 3 + b)
    if len(results) == 0:
        return 0
    return min(results)


def calculate_token(button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y):
    lowest_token = find_lowest_token(
        button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y, 0, 0
    )
    print(lowest_token)
    return lowest_token


with open("../input", "r") as f:
    lines = f.read()
    matches = re.findall(pattern, lines, re.MULTILINE)
    matches = [tuple(map(int, match)) for match in matches]
    sum = 0
    for m in matches:
        sum += calculate_token(*m)


print(f"Result Part 1: ", sum)
