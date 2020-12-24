import itertools
import re
with open('prob16_input.txt', 'r') as f:
# with open('delete_me.txt', 'r') as f:
    rawdata = f.readlines()
your_ticket = False
nearby_tickets = False
nt = []
instruc = {}
full_range = set()
for line in rawdata:
    line = line.strip()
    if line == "":continue
    if line == "your ticket:":
        your_ticket = True
        continue
    if line == "nearby tickets:":
        nearby_tickets = True
        continue
    if your_ticket and not nearby_tickets:
        yt = [int(i) for i in line.split(",")]
        your_ticket = False
        continue
    if nearby_tickets:
        nt.append([int(i) for i in line.split(",")])
        continue
    name, nums = line.split(":")
    numbers = [int(i) for i in re.search("(\d+)-(\d+) or (\d+)-(\d+)", nums).groups()]
    instruc[name] = set(
        range(numbers[0], numbers[1]+1)
        ).union(set(range(numbers[2], numbers[3]+1))
        )
    full_range = full_range.union(instruc[name])

part1_ans = 0
good_tickets = [yt]
for ticket in nt:
    bad = False
    for num in ticket:
        if num not in full_range:
            part1_ans += num
            bad = True
    if not bad:
        good_tickets.append(ticket)

transposed = list(map(list, itertools.zip_longest(
    *good_tickets, fillvalue=None)))
    
print(f'Prob 16 Part 1: {part1_ans}')
part2_ans = ''
print(f'Prob 16 Part 2: {part2_ans}')
