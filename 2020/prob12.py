# with open('delete_me.txt', 'r') as f:
with open('prob12_input.txt', 'r') as f:
    rawdata = f.readlines()

def rotate_wp(rotate):
    temp0 = wp[0]
    temp1 = wp[1]
    if rotate == 180:
        wp[0] *= -1
        wp[1] *= -1
    if rotate == 90:
        wp[0] = temp1
        wp[1] = -1 * temp0
    if rotate == 270:
        wp[0] = -1 * temp1
        wp[1] = temp0

degrees = {0:'E', 90:'N', 180:'W', 270:'S'}
facing = 0
loc1 = [0,0] #[+N(-S), +E(-W)]
loc2 = [0,0] #[+N(-S), +E(-W)]
wp = [1, 10] #[+N(-S), +E(-W)]
for line in rawdata:
    direc = line[0]
    orig_direc = line[0]
    num = int(line[1:])
    if direc == 'F':
        direc = degrees[facing]
        loc2[0] += wp[0] * num
        loc2[1] += wp[1] * num
    if direc == 'N':
        loc1[0] += num
    if direc == 'S':
        loc1[0] -= num
    if direc == 'E':
        loc1[1] += num
    if direc == 'W':
        loc1[1] -= num
    if direc == 'L':
        rotate_wp(num % 360)
        facing = (facing + num) %360
    if direc == 'R':
        rotate_wp(-num % 360)
        facing = (facing - num) %360
    if orig_direc == 'N':
        wp[0] += num
    if orig_direc == 'S':
        wp[0] -= num
    if orig_direc == 'E':
        wp[1] += num
    if orig_direc == 'W':
        wp[1] -= num

part1_ans = abs(loc1[0]) + abs(loc1[1])
print(f'Prob 12 Part 1: {part1_ans}')
part2_ans = abs(loc2[0]) + abs(loc2[1])
print(f'Prob 12 Part 2: {part2_ans}')
