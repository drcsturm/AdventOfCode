# with open('delete_me.txt', 'r') as f:
with open('prob12_input.txt', 'r') as f:
    rawdata = f.readlines()

degrees = {0:'E', 90:'N', 180:'W', 270:'S'}
facing = 0
loc = [0,0] #NS, EW
for line in rawdata:
    direc = line[0]
    num = int(line[1:])
    if direc == 'F':
        direc = degrees[facing]
    if direc == 'N':
        loc[0] += num
    elif direc == 'S':
        loc[0] -= num
    elif direc == 'E':
        loc[1] += num
    elif direc == 'W':
        loc[1] -= num
    elif direc == 'L':
        facing = (facing + num) %360
    elif direc == 'R':
        facing = (facing - num) %360

part1_ans = abs(loc[0]) + abs(loc[1])
part2_ans=''
print(f'Prob 12 Part 1: {part1_ans}')
print(f'Prob 12 Part 2: {part2_ans}')
