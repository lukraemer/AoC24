from functools import cache


@cache
def get_len_i(i):
    return len(str(i))


@cache
def mult(x):
    return x * 2024


@cache
def get_splitted_digits(value):
    len_stone_value = get_len_i(value)
    left_digits = int(str(value)[: len_stone_value // 2])
    right_digits = int(str(value)[len_stone_value // 2 :])
    return left_digits, right_digits


@cache
def do_blink(stone, times):
    if times == 0:
        return 1
    if stone == 0:
        return do_blink(1, times - 1)
    if get_len_i(stone) % 2 == 0:
        left, right = get_splitted_digits(stone)
        return do_blink(left, times - 1) + do_blink(right, times - 1)
    return do_blink(mult(stone), times - 1)


with open("../input") as f:
    stones = list(map(int, f.read().strip().split("\n")[0].split(" ")))
    # print(stones)
    count = 0
    for s in stones:
        count += do_blink(s, 75)

    print(f"Result Part 2: {count}")
