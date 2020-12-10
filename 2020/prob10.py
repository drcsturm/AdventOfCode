import pandas as pd
with open("prob10_input.txt", 'r') as f:
    rawdata = f.readlines()
nums = [int(i) for i in rawdata]
nums_sorted = sorted(nums)
df = pd.DataFrame({'n':nums_sorted})
df['differ'] = df.n.diff()
count1 = len(df[df.differ == 1]) + 1
count3 = len(df[df.differ == 3]) + 1
print(f"Prob 10 Part 1: {count1 * count3}")
