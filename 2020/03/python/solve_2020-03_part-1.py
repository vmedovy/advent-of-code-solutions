class TreeMap:
    __TREE_CHAR = '#'

    def __init__(self, input_file):
        self.__map = [line.replace('\n', '') for line in input_file.readlines()]

    def is_tree(self, x: int, y: int):
        if y >= len(self.__map):
            raise ValueError(f'y coordinate of {y} to high (max: {len(self.__map) - 1}')
        x = x % len(self.__map[0])
        return self.__map[y][x] == self.__TREE_CHAR

    def get_max_y(self):
        return len(self.__map) - 1


with open('../input') as input_file:
    tree_map = TreeMap(input_file)

count = 0
current_x = 0
current_y = 0
while current_y <= tree_map.get_max_y():
    if tree_map.is_tree(current_x, current_y):
        count += 1
    current_x += 3
    current_y += 1

print(f'The toboggan hit {count} trees on the current slope.')
