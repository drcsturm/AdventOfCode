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
print(f'Prob 13 Part 1: {part1_ans}')


# Checked 406629484067635 to 406114441067635 using 21/32 with 800 tries
# Checked 295730533867254 to 295151833867254 using 24/32 with 900 tries
# count = math.prod(busx.keys()) - math.ceil(math.prod(busx.keys())/iteration*21/32)*iteration
busx = {int(j):i for i,j in enumerate(rawdata[1].strip().split(',')) if j != 'x'}
count = math.prod(busx.keys())
# iteration = max(busx)
iteration = list(busx.keys())[0]
busex = {bus:ord-busx[iteration] for bus, ord in busx.items()}
xesub = sorted(busex, reverse=True)
dict = {}
start_num = count
busses = 1
for bus in xesub:
    print(start_num, iteration)
    for i in range(start_num, 0, -iteration):
        allgood = 0
        for b in xesub[:busses]:
            if (i + busex[b]) % b != 0:
                break
            allgood += 1
        if allgood == len(xesub[:busses]):
            iteration = math.prod(xesub[:busses])
            start_num = i
            busses += 1
            break



# print(start_num, iteration)
# for i in range(start_num, 0, -iteration):
#     if i%643 == 0 and (i+31)%433 == 0 and (i-10)%41==0:
#         print(i)
#         start_num = i
#         break
# iteration = 643*433*41
# print(start_num, iteration)
# for i in range(start_num, 0, -iteration):
#     if i%643 == 0 and (i+31)%433 == 0 and (i-10)%41==0 and (i+37)%37==0:
#         print(i)
#         start_num = i
#         break
# iteration = 643*433*41*37
# print(start_num, iteration)
# for i in range(start_num, 0, -iteration):
#     if i%643 == 0 and (i+31)%433 == 0 and (i-10)%41==0 and (i+37)%37==0:
#         print(i)
#         start_num = i
#         break
# print(start_num, iteration)

count = start_num
while True:
    for bus, ord in busex.items():
        if (count + ord) % bus != 0:
            break
        dict[bus] = (count + ord) % bus
    if len(dict) == len(busex):
        print(count, dict)
        break
    # if count < 1182922135469659:
    #     break
    count -= iteration
    i += 1
    if i%1000000 == 0:
        print(i, count)
    # print(count)
print(count, dict)

part2_ans = count
print(f'Prob 13 Part 2: {part2_ans}')
