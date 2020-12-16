from datetime import datetime
import requests
import sys

def get_input(prob_num, year=2020):
    response = requests.get(f"https://adventofcode.com/{year}/day/{prob_num}/input")
    with open(f"prob{prob_num}_input.txt", 'w') as f:
        f.write(response.text)

def set_up_prob(prob_num):
    with open(f"prob{prob_num}.py", 'w') as f:
        f.write(f"with open('prob{prob_num}_input.txt', 'r') as f:\n")
        f.write(f"    rawdata = f.readlines()\n")
        f.write(f"\n")
        f.write(f"part1_ans=''\n")
        f.write(f"part2_ans=''\n")
        f.write(f"print(f'Prob {prob_num} Part 1: {{part1_ans}}')\n")
        f.write(f"print(f'Prob {prob_num} Part 2: {{part2_ans}}')\n")

if __name__ == "__main__":
    prob_num = 0
    if len(sys.argv) > 1:
        prob_num = sys.argv[1]
    # get_input(prob_num, year=datetime.now().year)
    set_up_prob(prob_num)
