from dataclasses import dataclass

TARGET_BAG_COLOR = 'shiny gold'

 
@dataclass
class BagEntry:
    evaluated: bool
    count_factor: int
    count: int
    color: str


def parse_input_line(line: str):
    line = line.strip('.\n')
    outer_bag_color, contents = line.split(' bags contain ')
    contents = contents.replace(' bags', '').replace(' bag', '').split(', ')
    inner_bags = []
    for inner_bag in contents:
        data = inner_bag.split(' ')
        if data[0] == 'no':
            continue
        inner_bags.append((int(data[0]), ' '.join(data[1:])))
    return {outer_bag_color: inner_bags}


def get_bag_count(rules):
    inner_bags = [BagEntry(False, 1, count, color) for count, color in rules.get(TARGET_BAG_COLOR)]
    bag_count = 0

    while True:
        prev_bag_count = len(inner_bags)

        for inner_bag in inner_bags:
            if inner_bag.evaluated:
                continue
            inner_bag_count = inner_bag.count_factor * inner_bag.count
            bag_count += inner_bag_count
            inner_bag.evaluated = True
            inner_bags += [BagEntry(False, inner_bag_count, bag[0], bag[1]) for bag in rules.get(inner_bag.color)]

        if len(inner_bags) == prev_bag_count:  # no more entries left to evaluate
            return bag_count


def main():
    rules = {}
    with open('../input') as input_file:
        for line in input_file:
            rules.update(parse_input_line(line))

    print(f'The number of bags a {TARGET_BAG_COLOR} bag must contain is {get_bag_count(rules)}.')


if __name__ == '__main__':
    main()
