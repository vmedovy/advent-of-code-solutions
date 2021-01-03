from dataclasses import dataclass
from copy import deepcopy

accumulator = 0


@dataclass
class Command:
    cmd: str
    arg: int
    already_executed: bool = False


def parse_input_line(line: str):
    cmd, arg = line.split()
    return Command(cmd, int(arg))


def execute_program_until_loop(program):
    global accumulator
    current_program_position = 0
    while True:
        if current_program_position == len(program):
            return True  # no loop detected -> boot successful

        current_instruction = program[current_program_position]
        if current_instruction.already_executed:
            return False  # loop detected -> failure to boot due to infinite loop
        elif current_instruction.cmd == 'nop':
            current_program_position += 1
        elif current_instruction.cmd == 'jmp':
            current_program_position += current_instruction.arg
        elif current_instruction.cmd == 'acc':
            accumulator += current_instruction.arg
            current_program_position += 1

        current_instruction.already_executed = True


def main():
    with open('../input') as input_file:
        original_program = list(map(parse_input_line, input_file))

    changed_command_position = 0
    while True:
        global accumulator
        accumulator = 0

        # copying every time makes the code simpler even if it probably is a performance nightmare
        program = deepcopy(original_program)

        current_instruction = program[changed_command_position]
        if current_instruction.cmd == 'acc':
            changed_command_position += 1
            continue
        else:
            current_instruction.cmd = 'jmp' if current_instruction.cmd == 'nop' else 'nop'
            changed_command_position += 1

        if execute_program_until_loop(program):
            break  # program terminated without an endless loop
        if changed_command_position == len(original_program):
            raise IndexError('Endless loop could not be fixed by changing only one `nop` or `jmp` instruction.')

    print(f'The accumulator value when the program terminates correctly after changing only one `nop` or `jmp`'
          f' instruction is {accumulator}.')


if __name__ == '__main__':
    main()
