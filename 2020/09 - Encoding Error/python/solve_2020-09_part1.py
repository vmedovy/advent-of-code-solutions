import itertools


def main():
    with open('../input') as input_file:
        number_sequence = tuple(map(int, input_file))

    for current_position in range(25, len(number_sequence)):
        current_window = number_sequence[current_position - 25:current_position]
        possible_combinations = tuple(itertools.combinations(current_window, 2))
        current_number = number_sequence[current_position]
        if current_number not in (sum(e) for e in possible_combinations):
            print(f'The first number that does not have the required property is {current_number} at position'
                  f' {current_position}.')
            break


if __name__ == '__main__':
    main()
