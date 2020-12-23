import re
with open('prob14_input.txt', 'r') as f:
# with open('delete_me.txt', 'r') as f:
    rawdata = f.readlines()

def decimal_to_binary(n):
    return f"{int(bin(n).replace('0b', '')):036}"

def process(val, mask):
    binary = decimal_to_binary(val)
    for i, m in enumerate(mask):
        if m != "X":
            binary = f"{binary[:i]}{m}{binary[i+1:]}"
    # convert back to decimal
    return int(binary, 2)

mem = {}
for i ,line in enumerate(rawdata):
    var, val = line.split(" = ")
    val = val.strip()
    if var.startswith('mask'):
        mask = val
    else:
        key = re.search('\d+', var).group()
        mem[key] = process(int(val), mask)

part1_ans = 0
for k, v in mem.items():
    part1_ans += v

print(f'Prob 14 Part 1: {part1_ans}')
part2_ans = ''
print(f'Prob 14 Part 2: {part2_ans}')
