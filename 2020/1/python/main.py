from itertools import combinations

TARGET_SUM = 2020

with open('../input') as input_file:
    data = list(map(int, input_file))

valid_combinations = ((x, y) for x, y in combinations(data, 2) if x + y == TARGET_SUM)
for x, y in valid_combinations:
    print(f'{x} * {y} = {x * y}')
