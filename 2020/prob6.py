with open("prob6_input.txt", 'r') as f:
    rawdata = f.readlines()

part1 = 0
newdata = []
for line in rawdata:
    if line == "\n":
        part1 += len(set(newdata))
        newdata = []
        continue
    newdata += [i for i in line.strip()]
print(f"Prob 6 Part 1: {part1}")
