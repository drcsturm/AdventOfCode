with open("prob9_input.txt", 'r') as f:
    rawdata = f.readlines()
for i, line in enumerate(rawdata[25:]):
    line = int(line)
    prev_nums = [int(i) for i in rawdata[i:i+25]]
    found = False
    for num in prev_nums:
        val = int(line) - int(num)
        if val in prev_nums and val != line:
            found = True
            break
    if not found:
        break
part1 = line
print(f"Prob 9 Part 1: {part1}")

found = False
for i, line in enumerate(rawdata):
    line = int(line)
    mini = 9999999999999999
    maxi = 0
    total = 0
    j = 0
    while True:
        total += int(rawdata[i+j])
        mini = min(mini, int(rawdata[i+j]))
        maxi = max(maxi, int(rawdata[i+j]))
        if total > part1:
            break
        if total == part1:
            found = True
            break
        j += 1
    if found:
        break
print(f"Prob 9 Part 2: {mini + maxi}")
