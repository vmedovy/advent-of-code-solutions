from functools import reduce
from itertools import combinations

TARGET_SUM = 2020

with open('../input') as input_file:
    data = tuple(map(int, input_file))

for num_count in (2, 3):
    valid_combinations = (c for c in combinations(data, num_count) if sum(c) == TARGET_SUM)
    for combination in valid_combinations:
        print(f'{" * ".join(tuple(map(str, combination)))} = {reduce(lambda x, y: x * y, combination)}')
