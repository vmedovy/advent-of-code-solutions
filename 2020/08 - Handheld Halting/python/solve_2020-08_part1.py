from dataclasses import dataclass

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
        current_instruction = program[current_program_position]
        if current_instruction.already_executed:
            return
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
        program = list(map(parse_input_line, input_file))
    execute_program_until_loop(program)
    print(f'The value in the accumulator right before any instruction is executed a second time is {accumulator}.')


if __name__ == '__main__':
    main()
