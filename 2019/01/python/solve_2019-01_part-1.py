def calc_fuel_per_module(mass: int):
    return mass // 3 - 2


with open('../input') as input_file:
    input_data = tuple(map(int, input_file))

print(f'The solution is {sum(map(calc_fuel_per_module, input_data))}')
