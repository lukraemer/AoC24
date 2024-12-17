import re
import sys

regex = r"\d+"
if len(sys.argv) > 1:
    file_path = "../test_input"
else:
    file_path = "../input"


def print_program_state(reg_a, reg_b, reg_c, program):
    print(f"reg_a: {reg_a}, reg_b: {reg_b}, reg_c: {reg_c}")
    print(f"program: {program}")


# Opcode 0, 6, 7
def adv(reg_a, operand):
    reg_a = reg_a // 2**operand
    return reg_a


# Opcode 1
def bxl(reg_b, operand):
    reg_b = reg_b ^ operand
    return reg_b


# Opcode 2
def bst(reg_b, operand):
    reg_b = operand % 8
    return reg_b


# Opcode 3
def jnz(reg_a, operand, instruction_pointer):
    if reg_a == 0:
        return instruction_pointer + 2
    instruction_pointer = operand
    return instruction_pointer


# Opcode 4
def bxc(reg_b, reg_c):
    reg_b = reg_b ^ reg_c
    return reg_b


# Opcode 5
def out(operand):
    return str(operand % 8)


combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: 0, 5: 0, 6: 0}
program = []
instruction_pointer = 0
with open(file_path, "r") as file:
    data = re.findall(regex, file.read())
    combo[4] = int(data[0])
    combo[5] = int(data[1])
    combo[6] = int(data[2])
    for d in data[3:]:
        program.append(int(d))

print_program_state(combo[4], combo[5], combo[6], program)

output = ""
while instruction_pointer < len(program):
    match program[instruction_pointer]:
        case 0:
            combo[4] = adv(combo[4], combo[program[instruction_pointer + 1]])
            instruction_pointer += 2
        case 1:
            combo[5] = bxl(combo[5], program[instruction_pointer + 1])
            instruction_pointer += 2
        case 2:
            combo[5] = bst(combo[5], combo[program[instruction_pointer + 1]])
            instruction_pointer += 2
        case 3:
            instruction_pointer = jnz(
                combo[4], program[instruction_pointer + 1], instruction_pointer
            )
        case 4:
            combo[5] = bxc(combo[5], combo[6])
            instruction_pointer += 2
        case 5:
            output += out(combo[program[instruction_pointer + 1]]) + ","
            instruction_pointer += 2
        case 6:
            combo[5] = adv(combo[4], combo[program[instruction_pointer + 1]])
            instruction_pointer += 2
        case 7:
            combo[6] = adv(combo[4], combo[program[instruction_pointer + 1]])
            instruction_pointer += 2
print(f"Program output: {output[:-1]}")
