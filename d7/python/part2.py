def check_calc(calc_result, calc_numbers, result):
    # print(f"Check {calc_result} with {calc_numbers}, result: {result}")
    if len(calc_numbers) == 0:
        return calc_result == result
    else:
        return (
            check_calc(calc_result, calc_numbers[1:], result * calc_numbers[0])
            or check_calc(calc_result, calc_numbers[1:], result + calc_numbers[0])
            or check_calc(
                calc_result, calc_numbers[1:], int(str(result) + str(calc_numbers[0]))
            )
        )


f = open("../input", "r")

calcs = list()

for line in f:
    calc_result = int(line.strip().split(":")[0])
    calc_numbers = list(map(int, line.strip().split(":")[1].strip().split(" ")))
    calcs.append((calc_result, calc_numbers))

print(calcs)

sum = 0
for c in calcs:
    if check_calc(c[0], c[1][1:], c[1][0]):
        print(c[0])
        sum += c[0]
print(f"Result Part 2: {sum}")
