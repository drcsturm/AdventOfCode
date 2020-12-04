with open("prob1_input.txt") as f:
    numbers = [int(i.strip()) for i in f.readlines()]
for i in numbers:
    for j in numbers:
        for k in numbers:
            if k + i + j == 2020:
                print(i,j, k, k*i*j)
