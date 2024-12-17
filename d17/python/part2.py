import re
import sys

regex = r"\d+"
if len(sys.argv) > 1:
    file_path = "../test_input2"
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


def run_program(program, combo, program_str):
    instruction_pointer = 0
    output = ""
    while instruction_pointer < len(program) and (
        output in program_str or output == ""
    ):
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
    return output[:-1]


def sim_program(num):
    tmp = (num % 8) ^ 3
    reg_c = num // (2**tmp)
    reg_c = reg_c ^ 6
    return (reg_c ^ (num % 8)) % 8


combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: 0, 5: 0, 6: 0}
program = []
with open(file_path, "r") as file:
    data = re.findall(regex, file.read())
    # combo[4] = int(data[0])
    combo[4] = 117440
    combo[5] = int(data[1])
    combo[6] = int(data[2])
    for d in data[3:]:
        program.append(int(d))

program_str = str(program)[1:-1].replace(" ", "")
print_program_state(combo[4], combo[5], combo[6], program)
print(run_program(program, combo, program_str))
print(program_str)
# i = 40781670
# while run_program(program, combo, program_str) != program_str:
#    print(i)
#    combo[4] = i
#    i += 1
# print(i - 1)
cands = [0]
for i in range(len(program) - 1, -1, -1):
    newCands = []
    for c in cands:
        for j in range(8):
            num = (c << 3) + j
            output = sim_program(num)
            if output == program[i]:
                newCands.append(num)
    cands = newCands
print(min(cands))
