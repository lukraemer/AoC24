def swap_position(list, index1, index2, space_file):
    # print(f"Swapping {index1} and {index2} with space {space_file}")
    list[index1], list[index2] = list[index2], space_file


def get_index_free(block, file):
    for i, e in enumerate(block):
        if isinstance(e, int) and e >= len(file):
            return i
    return -1


def do_step(block):
    for j, f in enumerate(block[::-1]):
        if isinstance(f, tuple):
            file = f[0] * f[1]
            index_file = block.index(f)
            i = get_index_free(block, file)
            # print(f"starting file:{file} at {index_file}, found index {i}")
            if i == -1 or i >= index_file:
                # print(f"found index not valid")
                continue
            e = block[i]
            space_left = e - len(file)
            # print(f"e:{e} space_left:{space_left}")
            swap_position(block, i, index_file, len(file))
            if space_left > 0:
                # print(f"Inserting {space_left} at {i + 1}")
                block.insert(i + 1, space_left)
            # print(f"Swapped {e} at {i} and {file} at {index_file}")
            # print(f"After swap and space insertion: {block}")
    return False


# function to combine integers in a list if they are adjacent
def combine_adjacent_integers(l):
    i = 0
    while i < len(l):
        if isinstance(l[i], int):
            j = i + 1
            sum = l[i]
            while j < len(l) and isinstance(l[j], int):
                sum += l[j]
                del l[j]
            l[i] = sum
        i += 1


f = open("../input", "r")

for line in f:
    splitted_line = list(map(int, list(line.strip())))

block = []
index = 0
for i, number in enumerate(splitted_line):
    if i % 2 == 0:
        block.append((str(index), number))
        index += 1
    else:
        if number != 0:
            block.append(number)


do_step(block)
combine_adjacent_integers(block)

# block_str = ""
# for e in block:
#    if isinstance(e, tuple):
#        block_str += e[0] * e[1]
#    else:
#        block_str += "." * e

print(block)

block_list = list()
for e in block:
    if isinstance(e, tuple):
        for i in range(e[1]):
            block_list.append(e[0])
    else:
        block_list.append(e)

print(block_list)

checksum = 0
i = 0
file_id = 0
for i, n in enumerate(block_list):
    if isinstance(n, str):
        print(f"Added {int(n)} * {file_id} = {checksum + int(n) * file_id}")
        checksum += int(n) * file_id
        file_id += 1
    else:
        file_id += n

print(f"Result Part 2: {checksum}")

f = open("../input").read()

# f="2333133121414131402"

outp = 0
data = []
free = []
idx = 0

d = 0
for i in f:
    if (d % 2) == 0:
        data.append([idx, int(i)])
    else:
        free.append([idx, int(i)])
    d += 1
    idx += int(i)

for i in range(len(data) - 1, -1, -1):
    for j in range(len(free)):
        if free[j][0] > data[i][0]:
            break
        if free[j][1] >= data[i][1]:
            data[i][0] = free[j][0]
            if free[j][1] == data[i][1]:
                free.pop(j)
            else:
                free[j][0] += data[i][1]
                free[j][1] -= data[i][1]
            break

for i in range(len(data)):
    outp += i * sum(range(data[i][0], data[i][0] + data[i][1]))
print(outp)
