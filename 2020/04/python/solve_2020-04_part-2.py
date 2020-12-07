from typing import List
import re


def is_valid_byr(value: str):
    try:
        byr = int(value)
        return 1920 <= byr <= 2002
    except ValueError:
        return False


def is_valid_iyr(value: str):
    try:
        iyr = int(value)
        return 2010 <= iyr <= 2020
    except ValueError:
        return False


def is_valid_eyr(value: str):
    try:
        byr = int(value)
        return 2020 <= byr <= 2030
    except ValueError:
        return False


def is_valid_hgt(value: str):
    if value.endswith('cm'):
        limits = (150, 193)
        value = value.replace('cm', '')
    elif value.endswith('in'):
        limits = (59, 76)
        value = value.replace('in', '')
    else:
        return False
    try:
        hgt = int(value)
        return limits[0] <= hgt <= limits[1]
    except ValueError:
        return False


def is_valid_hcl(value: str):
    return re.match(r'^#[0-9a-f]{6}$', value) is not None


def is_valid_ecl(value: str):
    return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def is_valid_pid(value: str):
    return re.match(r'^\d{9}$', value) is not None


def is_valid(passport_entry: List[str]) -> bool:
    fields = dict(e.split(':') for e in passport_entry)
    required_fields = {
        'byr': is_valid_byr,
        'iyr': is_valid_iyr,
        'eyr': is_valid_eyr,
        'hgt': is_valid_hgt,
        'hcl': is_valid_hcl,
        'ecl': is_valid_ecl,
        'pid': is_valid_pid
    }
    if not all(req_f in fields for req_f in required_fields):
        return False
    for field, value in fields.items():
        if field == 'cid':
            pass
        elif not required_fields[field](value):
            return False
    return True


with open('../input') as input_file:
    passports = [[]]
    for line in input_file:
        if line == '\n':
            passports.append([])
        else:
            passports[-1] += line.replace('\n', '').split()
    valid_passport_count = sum(is_valid(p) for p in passports)

print(f'There are {valid_passport_count} valid passport entries.')
