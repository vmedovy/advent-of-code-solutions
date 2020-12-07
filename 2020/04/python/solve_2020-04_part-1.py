from typing import List


def is_valid(passport_entry: List[str]) -> bool:
    fields = dict(e.split(':') for e in passport_entry)
    required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]
    return all(req_f in fields for req_f in required_fields)


with open('../input') as input_file:
    passports = [[]]
    for line in input_file:
        if line == '\n':
            passports.append([])
        else:
            passports[-1] += line.replace('\n', '').split()
    valid_passport_count = sum(is_valid(p) for p in passports)

print(f'There are {valid_passport_count} valid passport entries.')
