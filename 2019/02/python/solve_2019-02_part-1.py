from typing import List


def add(command_sequence: List[int], src_id_1: int, src_id_2: int, target_id: int):
    command_sequence[target_id] = command_sequence[src_id_1] + command_sequence[src_id_2]


def multiply(command_sequence: List[int], src_id_1: int, src_id_2: int, target_id: int):
    command_sequence[target_id] = command_sequence[src_id_1] * command_sequence[src_id_2]


def run_intcode(cmd_sequence: List[int]) -> List[int]:
    curr_pos = 0
    while cmd_sequence[curr_pos] != 99:
        curr_op = cmd_sequence[curr_pos]
        if curr_op == 1:
            add(cmd_sequence, cmd_sequence[curr_pos + 1], cmd_sequence[curr_pos + 2], cmd_sequence[curr_pos + 3])
        elif curr_op == 2:
            multiply(cmd_sequence, cmd_sequence[curr_pos + 1], cmd_sequence[curr_pos + 2], cmd_sequence[curr_pos + 3])
        else:
            raise ValueError(f"Invalid operation! (code {curr_op})")
        curr_pos += 4
    return cmd_sequence


with open('../input') as input_file:
    application = list(int(e) for e in input_file.readline().strip().split(','))

# repair application as described
application[1] = 12
application[2] = 2

print(f'The solution is {run_intcode(application)[0]}.')
