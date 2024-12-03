import re


f = open("../input", "r")

finds = re.findall(r"(mul\(([0-9]+)\,([0-9]+)\))|(do\(\))|(don't\(\))", f.read())

do = True
sum = 0
for f in finds:
    if do and len(f[1])>0 and len(f[2])>0:
        sum += int(f[1])*int(f[2])
    if len(f[3])>0:
        do = True
    if len(f[4])>0:
        do = False
print(finds)
print(sum)
