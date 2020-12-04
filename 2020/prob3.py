with open("prob3_input.txt") as f:
# with open("delete_me.txt") as f:
    inputlines = f.readlines()
product = 1
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
for slope in slopes:
    hits = ""
    line_count = 1
    for i, line in enumerate(inputlines):
        if i == 0:continue
        if i % slope[1] != 0:continue
        line = line.strip()
        hits += line[(line_count * slope[0]) % len(line)]
        line_count += 1
    trees = hits.count("#")
    product *= trees
print(product)