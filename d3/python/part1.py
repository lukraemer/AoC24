import re


f = open("../input", "r")

finds = re.findall(r"(mul\(([0-9]+)\,([0-9]+)\))", f.read())

sum = 0
for f in finds:
    sum += int(f[1])*int(f[2])


print(sum)
