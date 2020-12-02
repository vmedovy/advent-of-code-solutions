import re
from dataclasses import dataclass


@dataclass()
class PasswordEntry:
    min_count: int
    max_count: int
    letter: str
    password: str

    @staticmethod
    def from_entry(e: str):
        min_count, max_count, letter, password = [i for i in re.split(r'[ \-:\n]', e) if i]
        return PasswordEntry(int(min_count), int(max_count), letter, password)

    def is_valid(self):
        is_count = self.password.count(self.letter)
        return self.min_count <= is_count <= self.max_count


with open('../input') as input_file:
    entries = tuple(PasswordEntry.from_entry(e) for e in input_file)

print(f'The number of valid password entries is {sum(e.is_valid() for e in entries)}.')
