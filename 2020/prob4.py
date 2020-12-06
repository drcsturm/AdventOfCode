import re

with open("prob4_input.txt", 'r') as f:
    rawdata = f.readlines()
fullset = set(["byr","iyr","eyr","hgt","hcl","ecl","pid"])
valid_count = 0
valid_data = []
newdata = {}
for line in rawdata:
    if line == "\n":
        if len(fullset.difference(newdata.keys())) == 0:
            valid_count += 1
            valid_data.append(newdata)
        newdata = {}
        continue
    newdata.update({kv.split(":")[0].lower():kv.split(":")[1] for kv in line.strip().split(" ")})
print(f"Prob 4 Part 1: {valid_count} Valid")

def yr(v, min, max):
    try:
        v = int(v)
    except:
        return False
    if v >= min and v <= max:
        return True
    return False

def hgt(v):
    g = re.search("(\d+)(\w*)", v).groups()
    h = int(g[0])
    if g[1] == "":
        return False
    elif g[1] == "in" and h >= 59 and h <= 76:
        return True
    elif g[1] == "cm" and h >= 150 and h <= 193:
        return True
    else:
        return False

def hcl(v):
    if re.search("#[0-9a-f]{6,6}", v):
        return True
    else:
        return False

def ecl(v):
    if v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth",]:
        return True
    else:
        return False

def pid(v):
    if re.search("[0-9]{9,9}", v) and len(v) == 9:
        return True
    else:
        return False

valid_count = 0
for d in valid_data:
    if (yr(d['byr'], 1920, 2002) and
        yr(d['iyr'], 2010, 2020) and
        yr(d['eyr'], 2020, 2030) and
        hgt(d['hgt']) and
        hcl(d['hcl']) and
        ecl(d['ecl']) and
        pid(d['pid'])
        ):
        valid_count += 1
print(f"Prob 4 Part 2: {valid_count} Valid")
