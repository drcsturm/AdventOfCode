with open("prob6_input.txt", 'r') as f:
    rawdata = f.readlines()

part1_count = 0
part2_count = 0
part2 = None
newdata = []
for line in rawdata:
    if line == "\n":
        part1_count += len(set(newdata))
        part2_count += len(part2)
        part2 = None
        newdata = []
        continue
    newdata += [i for i in line.strip()]
    if part2 is None:
        part2 = set([i for i in line.strip()])
    else:
        part2 = part2.intersection(set([i for i in line.strip()]))
print(f"Prob 6 Part 1: {part1_count}")
print(f"Prob 6 Part 2: {part2_count}")
