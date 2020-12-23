import re
with open('prob14_input.txt', 'r') as f:
# with open('delete_me.txt', 'r') as f:
    rawdata = f.readlines()

def decimal_to_binary(n, pad=36):
    return f"{int(bin(n).replace('0b', '')):0{pad}}"

def process1(val, mask):
    binary = decimal_to_binary(val)
    for i, m in enumerate(mask):
        if m != "X":
            binary = f"{binary[:i]}{m}{binary[i+1:]}"
    # convert back to decimal
    return int(binary, 2)

def process2(val, mask):
    binary = decimal_to_binary(val)
    for i, m in enumerate(mask):
        if m != "0":
            binary = f"{binary[:i]}{m}{binary[i+1:]}"
    xs = binary.count('X')
    permutations = []
    for x in range(2**xs):
        bin_str = decimal_to_binary(x, pad=xs)
        perm = ''
        for i, s in zip(bin_str + ' ', binary.split("X")):
            perm += s + i
        permutations.append(int(perm.strip(), 2))
    return permutations
    
mem1 = {}
mem2 = {}
for i ,line in enumerate(rawdata):
    var, val = line.split(" = ")
    val = val.strip()
    if var.startswith('mask'):
        mask = val
    else:
        val = int(val)
        key = int(re.search('\d+', var).group())
        mem1[key] = process1(val, mask)
        for p in process2(key, mask):
            mem2[p] = val

part1_ans = 0
for k, v in mem1.items():
    part1_ans += v

part2_ans = 0
for k, v in mem2.items():
    part2_ans += v

print(f'Prob 14 Part 1: {part1_ans}')
print(f'Prob 14 Part 2: {part2_ans}')
