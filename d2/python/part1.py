f = open("../input", "r")

count_safe_lines = 0
least_difference = 1
most_difference = 3

def check_line(splitted_line: list[int]):
    safe = True
    increasing = False
    decreasing = False
    last_element = splitted_line[0]
    if splitted_line[0] - splitted_line[1] > 0:
        decreasing = True
    elif splitted_line[0] - splitted_line[1] < 0:
        increasing = True
    else:
        safe = False
    for e in splitted_line[1:]:
        if abs(last_element - e) <least_difference or abs(last_element - e) > most_difference:
            print("unsafe diff: ", splitted_line)
            print(f"{last_element}, {e}")
            safe = False
        if last_element - e < 0 and decreasing:
            print("unsafe dec: ", splitted_line)
            safe = False
        if last_element - e > 0 and increasing:
            print("unsafe inc: ", splitted_line)
            safe = False
        last_element = e
    return safe

for line in f:
    splitted_line =line.rstrip("\n").split(" ")
    splitted_line = [int(e) for e in splitted_line]
    #print(splitted_line)

    if check_line(splitted_line) :
        print("safe: ", splitted_line)
        count_safe_lines += 1

print(count_safe_lines)
