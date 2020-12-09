import re

with open("prob7_input.txt", 'r') as f:
    rawdata = f.readlines()

data1 = {}
data2 = {}
for line in rawdata:
    array1 = re.sub("\d*", "", line).replace("bags", "bag").replace("contain", "").replace(",", "").replace(".", "").strip().split("bag")
    array1 = [i.strip() for i in array1[:-1]]
    data1[array1[0]] = array1[1:]
    array2 = line.replace("bags", "bag").replace("contain", "").replace(",", "").replace(".", "").strip().split("bag")
    array2 = [re.search("(\d*) ?([A-Za-z ]+)", i.strip()).groups() for i in array2[:-1]]
    data2[array2[0][1]] = array2[1:] # data[bag] = [('#', bag2), ('#', bag3) ...]

target = 'shiny gold'
def find_bag(bag):
    if bag == 'no other':
        return False
    if target in bag or target in data1[bag]:
        return True
    for b in data1[bag]:
        if find_bag(b):
            return True
        
part1_count = 0
for k, v in data1.items():
    if k == target:continue
    if find_bag(k):
        part1_count += 1
print(f"Prob 7 Part 1: {part1_count}")

def count_bag(bags):
    count = 1
    for bag in data2[bags[1]]:
        if bag[1] != 'no other':
            count += int(bag[0]) * count_bag(bag)
    return count
    
part2_count = 0
for bag in data2[target]:
    if bag[1] != 'no other':
        part2_count += int(bag[0]) * count_bag(bag)
print(f"Prob 7 Part 2: {part2_count}")
        