def check_calc(calc_result, calc_numbers):
    if len(calc_numbers) == 1:
        return calc_numbers[0] == calc_result
    else:
        return check_calc(
            calc_result / calc_numbers[-1], calc_numbers[:-1]
        ) or check_calc(calc_result - calc_numbers[-1], calc_numbers[:-1])


f = open("../input", "r")

calcs = list()

for line in f:
    calc_result = int(line.strip().split(":")[0])
    calc_numbers = list(map(int, line.strip().split(":")[1].strip().split(" ")))
    calcs.append((calc_result, calc_numbers))

print(calcs)

sum = 0
for c in calcs:
    if check_calc(c[0], c[1]):
        sum += c[0]
print(f"Result Part 1: {sum}")
