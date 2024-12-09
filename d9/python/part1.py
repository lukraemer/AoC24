def swap_position(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]


def do_step(list):
    for i, e in enumerate(list[::-1]):
        if e != ".":
            index_last_element = len(list) - i - 1
            break
    for i, e in enumerate(list):
        if e == ".":
            index_first_free = i
            break
    if index_first_free > index_last_element:
        return False
    else:
        swap_position(list, index_first_free, index_last_element)
        return True


f = open("../test_input", "r")

for line in f:
    splitted_line = list(map(int, list(line.strip())))

print(splitted_line)

block = []
index = 0
for i, number in enumerate(splitted_line):
    if i % 2 == 0:
        for j in range(number):
            block.append(str(index))
        index += 1
    else:
        for j in range(number):
            block.append(".")

while do_step(block):
    pass

checksum = 0
for i, n in enumerate(block):
    if n == ".":
        break
    checksum += int(n) * i
print(block)


print(f"Result Part 1: {checksum}")
