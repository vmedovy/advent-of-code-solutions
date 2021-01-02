TARGET_BAG_COLOR = 'shiny gold'


def parse_input_line(line: str):
    line = line.strip('.\n')
    outer_bag_color, contents = line.split(' bags contain ')
    contents = contents.replace(' bags', '').replace(' bag', '').split(', ')
    inner_bag_colors = tuple(' '.join(inner_bag.split(' ')[1:]) for inner_bag in contents)
    return {outer_bag_color: inner_bag_colors}


rules = {}
with open('../input') as input_file:
    for line in input_file:
        rules.update(parse_input_line(line))

outer_colors = set(k for k, v in rules.items() if TARGET_BAG_COLOR in v)  # hold target bag color directly

while True:
    prev_color_count = len(outer_colors)

    additional_colors = set()
    for color in outer_colors:
        additional_colors.update(k for k, v in rules.items() if color in v)
    outer_colors.update(additional_colors)

    if len(outer_colors) == prev_color_count:
        break

print(f'The number of outermost bag colors that contain at least one {TARGET_BAG_COLOR} bag is {len(outer_colors)}.')
