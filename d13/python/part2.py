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


def find_lowest_token_part2(
    button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y
):
    # det(M) = 0 -> linear equation not solvable
    if button_a_x * button_b_y == button_b_x * button_a_y:
        return -1
    det = button_a_x * button_b_y - button_b_x * button_a_y
    button_count_a = (button_b_y * prize_x - button_b_x * prize_y) / det
    button_count_b = (button_a_x * prize_y - button_a_y * prize_x) / det
    if button_count_b.is_integer() and button_count_a.is_integer():
        return int(button_count_a) * 3 + int(button_count_b)
    return -1


def calculate_token(button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y):
    lowest_token = find_lowest_token(
        button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y, 0, 0
    )
    lowest_token_part2 = find_lowest_token_part2(
        button_a_x,
        button_a_y,
        button_b_x,
        button_b_y,
        prize_x + 10000000000000,
        prize_y + 10000000000000,
    )
    return lowest_token_part2


with open("../input", "r") as f:
    lines = f.read()
    matches = re.findall(pattern, lines, re.MULTILINE)
    matches = [tuple(map(int, match)) for match in matches]
    sum = 0
    for m in matches:
        res = calculate_token(*m)
        if res < 0:
            continue
        sum += res


print(f"Result Part 1: ", sum)
