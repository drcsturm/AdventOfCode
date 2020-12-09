import re
with open("prob8_input.txt", 'r') as f:
    rawdata = f.readlines()
last_line = len(rawdata) - 1

line = 0
acc = 0
executed_lines = []
jmp_nop_lines = []
while True:
    cmd, amt = rawdata[line].split(" ")
    executed_lines.append(line)
    if cmd == 'acc':
        line += 1
        acc += int(amt)
    elif cmd == 'jmp':
        if line not in jmp_nop_lines:
            jmp_nop_lines.append(line)
        line += int(amt)
    else:
        if line not in jmp_nop_lines:
            jmp_nop_lines.append(line)
        line += 1
    if line in executed_lines:
        break
print(f"Prob 8 Part 1: {acc}")

line = 0
acc = 0
executed_lines = []
for i in jmp_nop_lines:
    while True:
        cmd, amt = rawdata[line].split(" ")
        executed_lines.append(line)
        if i == line:
            if cmd == 'jmp':
                cmd = 'nop'
            else:
                cmd = 'jmp'
        if cmd == 'acc':
            line += 1
            acc += int(amt)
        elif cmd == 'jmp':
            line += int(amt)
        else:
            line += 1
        if line in executed_lines or line < 0:
            executed_lines = []
            line = 0
            acc = 0
            break
        if line == last_line:
            break
    if line == last_line:
        break
print(f"Prob 8 Part 2: {acc}")
