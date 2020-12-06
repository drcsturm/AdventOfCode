with open("prob5_input.txt", 'r') as f:
    rawdata = f.readlines()

def seat_location(line):
    line = line.strip()
    r = [0, 127]
    c = [0, 7]
    for l in line:
        if l == "F":
            r[1] -= (r[1] - r[0] + 1) / 2
        if l == "B":
            r[0] += (r[1] - r[0] + 1) / 2
        if l == "L":
            c[1] -= (c[1] - c[0] + 1) / 2
        if l == "R":
            c[0] += (c[1] - c[0] + 1) / 2
    # return r[0], c[0]
    return int(r[0] * 8 + c[0])

min_seat = 99999
max_seat = 0
data = []
for line in rawdata:
    seat = seat_location(line)
    data.append(seat)
    min_seat = min(min_seat, seat)
    max_seat = max(max_seat, seat)
all_seats = set(range(min_seat, max_seat))
print(f"Prob 5 Part 1: {max_seat}")
print(f"Prob 5 Part 2: {list(all_seats.difference(data))[0]}")
