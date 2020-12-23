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


# get a dictionary of the bas number and offset time
busx = {int(j):i for i,j in enumerate(rawdata[1].strip().split(',')) if j != 'x'}
# the start_num starts at the highest possible value of all the busses multipled together
start_num = math.prod(busx.keys())
# start with the first bus in the list
iteration = list(busx.keys())[0]
# change the offset based on which bus centered around.
# ex: If using max bus then make it's offset 0 and all others adjusted down
busex = {bus:ord-busx[iteration] for bus, ord in busx.items()}
# get a list of the busses. I sorted in reverse so the largest number is first
xesub = sorted(busex, reverse=True)
dict = {}
busses = 1
for bus in xesub:
    print(start_num, iteration)
    for i in range(start_num, 0, -iteration):
        # work backwards from highest number
        allgood = 0
        for b in xesub[:busses]:
            # go through the busses checking one at a time
            # and adding a bus on the next main loop
            if (i + busex[b]) % b != 0:
                # modulus not met so break and check next iteration
                break
            allgood += 1
        if allgood == len(xesub[:busses]):
            # all busses in the list worked so
            # the iteration is now the product of the working busses
            iteration = math.prod(xesub[:busses])
            # we start at the last good number
            start_num = i
            busses += 1
            break

## WRITTEN OUT LOOPS FOR CLARITY
# print(start_num, iteration)
# for i in range(start_num, 0, -iteration):
#     if i%643 == 0 and (i+31)%433 == 0 and (i-10)%41==0:
#         print(i)
#         start_num = i
#         break
# iteration = 643*433*41
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

# count = start_num
# while True:
#     for bus, ord in busex.items():
#         if (count + ord) % bus != 0:
#             break
#         dict[bus] = (count + ord) % bus
#     if len(dict) == len(busex):
#         print(count, dict)
#         break
#     # if count < 1182922135469659:
#     #     break
#     count -= iteration
#     i += 1
#     if i%1000000 == 0:
#         print(i, count)
#     # print(count)
# print(count, dict)

part2_ans = start_num
print(f'Prob 13 Part 2: {part2_ans}')
