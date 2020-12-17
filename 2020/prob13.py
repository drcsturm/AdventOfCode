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

busex = [i for i in rawdata[1].strip().split(",")]
count = 99999999999992#int(busex[0])
dict = {}
while True:
    for i, bus in enumerate(busex[1:]):
        if bus == 'x':continue
        if int(bus) - count % int(bus) - (i+1) != 0:
            break
        dict[int(bus)] = int(bus) - count % int(bus) - (i+1)
    if len(dict) == len(buses) - 1:
        print(count, dict)
        break
    if count > 99999999999992 * 2:
        break
    count += int(busex[0])
print(count, dict)

print(f'Prob 13 Part 1: {part1_ans}')
part2_ans = ''
print(f'Prob 13 Part 2: {part2_ans}')
