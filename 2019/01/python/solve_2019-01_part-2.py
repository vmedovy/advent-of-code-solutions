def calc_fuel(mass: int):
    return mass // 3 - 2


def calc_total_fuel_per_module(module_mass: int):
    fuel_amounts = [calc_fuel(module_mass)]
    while fuel_amounts[-1] > 0:
        fuel_amounts.append(calc_fuel(fuel_amounts[-1]))
 
    return sum(fuel_amounts[:-1])


with open('../input') as input_file:
    input_data = tuple(map(int, input_file))

print(f'The solution is {sum(map(calc_total_fuel_per_module, input_data))}')
