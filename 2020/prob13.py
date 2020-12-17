import math
with open('prob13_input.txt', 'r') as f:
# with open('delete_me.txt', 'r') as f:
    rawdata = f.readlines()

time = int(rawdata[0])
buses = [int(i) for i in rawdata[1].strip().split(",") if i != 'x']
wait = []
for bus in buses:
    minutes = bus - time % bus
    wait.append(minutes)
min_wait = min(wait)
part1_ans = buses[wait.index(min_wait)] * min_wait

busx = {int(j):i for i,j in enumerate(rawdata[1].strip().split(',')) if j != 'x'}
iteration = max(busx)
count = math.prod(busx.keys())
busex = {bus:ord-busx[iteration] for bus, ord in busx.items()}
dict = {}
while True:
    for bus, ord in busex.items():
        if (count + ord) % bus != 0:
            break
        dict[bus] = (count + ord) % bus
    if len(dict) == len(busex):
        print(count, dict)
        break
    if count < 1182922135469659:
        break
    count -= iteration
print(count, dict)

print(f'Prob 13 Part 1: {part1_ans}')
part2_ans = ''
print(f'Prob 13 Part 2: {part2_ans}')
