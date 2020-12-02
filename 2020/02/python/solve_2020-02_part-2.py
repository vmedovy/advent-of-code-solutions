import re
from dataclasses import dataclass
from typing import Tuple


@dataclass()
class PasswordEntry:
    positions: Tuple[int]
    letter: str
    password: str

    @staticmethod
    def from_entry(e: str):
        position_1, position_2, letter, password = [i for i in re.split(r'[ \-:\n]', e) if i]
        return PasswordEntry(tuple(int(p) for p in (position_1, position_2)), letter, password)

    def is_valid(self):
        is_count = sum(1 for p in self.positions if self.password[p - 1] == self.letter)
        return is_count == 1


with open('../input') as input_file:
    entries = tuple(PasswordEntry.from_entry(e) for e in input_file)

print(f'The number of valid password entries is {sum(e.is_valid() for e in entries)}.')
