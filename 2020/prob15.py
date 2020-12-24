starting_numbers = [15,12,0,14,3,1]
def game(turns, numbers):
    dict = {}
    prev = numbers[-1]
    for i, n in enumerate(numbers):
        dict[n] = {'a': 0, 'b': i + 1}
    for turn in range(len(numbers) + 1, turns + 1):
        a = dict[prev]['a']
        b = dict[prev]['b']
        if a == 0:
            dict[0]['a'] = dict[0]['b']
            dict[0]['b'] = turn
            prev = 0
            continue
        prev = b - a
        if dict.get(prev, -1) == -1:
            dict[prev] = {'a': 0, 'b': turn}
        dict[prev]['a'] = dict[prev]['b']
        dict[prev]['b'] = turn
    return prev, dict

part1_ans, dict = game(2020, starting_numbers)
print(f'Prob 15 Part 1: {part1_ans}')
part2_ans, dict = game(30000000, starting_numbers)
print(f'Prob 15 Part 2: {part2_ans}')
