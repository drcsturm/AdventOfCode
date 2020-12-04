import re

# part 1
valid_count = 0
with open("prob2_input.txt", 'r') as f:
    for line in f:
        line = line.strip()
        groups = re.search("(\d+)-(\d+) (\w): (\w+)", line).groups()
        minval = int(groups[0])
        maxval = int(groups[1])
        letter = groups[2]
        word = groups[3]
        l_count = 0
        for l in word:
            if l == letter:
                l_count += 1
        if l_count >= minval and l_count <= maxval:
            valid_count += 1
print(valid_count)

# part 2
valid_count = 0
with open("prob2_input.txt", 'r') as f:
    for line in f:
        line = line.strip()
        groups = re.search("(\d+)-(\d+) (\w): (\w+)", line).groups()
        minval = int(groups[0])
        maxval = int(groups[1])
        letter = groups[2]
        word = groups[3]
        if word[minval - 1] == letter and word[maxval - 1] == letter:
            continue
        if word[minval - 1] == letter or word[maxval - 1] == letter:
            valid_count += 1
print(valid_count)
