import itertools


def get_first_invalid_number(number_sequence):
    for current_position in range(25, len(number_sequence)):
        current_window = number_sequence[current_position - 25:current_position]
        possible_combinations = tuple(itertools.combinations(current_window, 2))
        current_number = number_sequence[current_position]
        if current_number not in (sum(e) for e in possible_combinations):
            return current_number


def get_encryption_weakness(number_sequence, target_number):
    for current_position in range(1, len(number_sequence)):
        offset = 1
        while True:
            current_sequence = number_sequence[current_position - 1:current_position + offset]
            current_sum = sum(current_sequence)
            if current_sum == target_number:
                return min(current_sequence) + max(current_sequence)
            elif current_sum > target_number:
                break
            else:
                offset += 1


def main():
    with open('../input') as input_file:
        number_sequence = tuple(map(int, input_file))

    target_number = get_first_invalid_number(number_sequence)
    encryption_weakness = get_encryption_weakness(number_sequence, target_number)

    print(f'The encryption weakness is {encryption_weakness}.')


if __name__ == '__main__':
    main()
