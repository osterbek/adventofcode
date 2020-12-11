from pathlib import Path


def get_accumulator(ds):
    pointer = 0
    accumulator = 0
    used_lines = []
    exitcode = 0
    while exitcode == 0:
        argument = ds[pointer][4:]
        command = ds[pointer][:3]
        value = int(argument[1:])
        if argument[0] == '-':
            value = - value
        used_lines.append(pointer)
        if command == 'acc':
            accumulator += value
            pointer += 1
        elif command == 'jmp':
            pointer += value
        elif command == 'nop':
            pointer += 1
        if pointer >= len(ds):
            exitcode = 1
        elif pointer in used_lines:
            exitcode = 2
    return [exitcode, accumulator]


if __name__ == '__main__':
    dataset = Path('../input/input_2020_08.txt').read_text().split('\n')

    solution_2 = 0
    for i in range(0, len(dataset)):
        temp = dataset[i]
        if dataset[i][:3] == 'jmp':
            temp = 'nop' + dataset[i][3:]
        elif dataset[i][:3] == 'nop':
            temp = 'jmp' + dataset[i][3:]
        answer = get_accumulator(dataset[:i] + [temp] + dataset[i+1:])
        if answer[0] == 1:
            solution_2 = answer[1]

    print('Answer part 1 = {:d} '.format(get_accumulator(dataset)[1]))       # => 1553
    print('Answer part 2 = {:d} '.format(solution_2))                        # => 1877


