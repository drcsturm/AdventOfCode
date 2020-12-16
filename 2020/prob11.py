# with open('delete_me.txt', 'r') as f:
with open('prob11_input.txt', 'r') as f:
    rawdata = f.readlines()
    orig_grid = []
    for line in rawdata:
        orig_grid.append(line.strip()) # remove new line characters

xbound = [0, len(orig_grid)]
ybound = [0, len(orig_grid[0])]

def occupied(xy, grid):
    return grid[xy[0]][xy[1]] == "#"

def empty_seat(xy, grid):
    return grid[xy[0]][xy[1]] == "L"

def inbounds(xy):
    return xy[0] >= xbound[0] and xy[0] < xbound[1] and xy[1] >= ybound[0] and xy[1] < ybound[1]
    
def occupancy(x, y, grid, seat_view=1, max_neighbors=4):
    origx = x
    origy = y
    count = 0
    directions = [
        [-1, 0], # 12 oclock
        [-1, +1], # 1.5 oclock
        [0, +1], # 3 oclock
        [+1, +1], # 4.5 oclock
        [+1, 0], # 6 oclock
        [+1, -1], # 7.5 oclock
        [0, -1], # 9 oclock
        [-1, -1], # 10.5 oclock
    ]
    for direction in directions:
        view_count = 1
        x = origx
        y = origy
        while view_count <= seat_view:
            seat = [x+direction[0], y+direction[1]]
            if not inbounds(seat):
                break
            if empty_seat(seat, grid):
                break
            if occupied(seat, grid):
                count += 1
                break
            view_count += 1
            x, y = seat[0], seat[1]
    x = origx
    y = origy
    if grid[x][y] == "#":
        if count >= max_neighbors:
            return "L"
        else:
            return "#"
    if grid[x][y] == "L":
        if count > 0:
            return "L"
        else:
            return "#"
        
def grid_creator(grid, seat_view=1, max_neighbors=4):
    new_grid = []
    for x in range(xbound[0], xbound[1]):
        new_grid.append("")
        for y in range(ybound[0], ybound[1]):
            if grid[x][y] == ".":
                new_grid[x] += "."
            else:
                new_grid[x] += occupancy(x, y, grid, seat_view, max_neighbors)
    return new_grid

new_grid = ""
iterations = 0
seat_view = 1
max_neighbors = 4
grid = orig_grid
while True:
    new_grid = grid_creator(grid, seat_view, max_neighbors)
    iterations += 1
    if iterations > 500:
        break
    if new_grid != grid:
        grid = new_grid
    else:
        break

part1_ans = 0
for x in range(xbound[0], xbound[1]):
    for y in range(ybound[0], ybound[1]):
        if new_grid[x][y] == "#":
            part1_ans += 1
print(f'Prob 11 Part 1: {part1_ans} in {iterations} iterations')


new_grid = ""
iterations = 0
seat_view = 100
max_neighbors = 5
grid = orig_grid
while True:
    new_grid = grid_creator(grid, seat_view, max_neighbors)
    iterations += 1
    if iterations > 500:
        break
    if new_grid != grid:
        grid = new_grid
    else:
        break

part2_ans = 0
for x in range(xbound[0], xbound[1]):
    for y in range(ybound[0], ybound[1]):
        if new_grid[x][y] == "#":
            part2_ans += 1

print(f'Prob 11 Part 2: {part2_ans} in {iterations} iterations')
