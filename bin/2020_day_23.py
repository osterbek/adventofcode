def initial_setup(dataset):
    successors = {}
    for i in range(0, len(dataset) - 1):
        successors[int(dataset[i])] = int(dataset[i + 1])
    successors[int(dataset[len(dataset) - 1])] = int(dataset[0])
    current = int(dataset[0])
    return [successors, current]


def execute_moves(successors, current, count):
    for r in range(0, count):
        pick_up_1 = successors.get(current)
        pick_up_2 = successors.get(pick_up_1)
        pick_up_3 = successors.get(pick_up_2)
        destination = current - 1
        while (destination in [pick_up_1, pick_up_2, pick_up_3]) or (destination <= 0):
            destination -= 1
            if destination <= 0:
                destination = key_count
        successors[current] = successors.get(pick_up_3)
        successors[pick_up_3] = successors.get(destination)
        successors[destination] = pick_up_1
        current = successors.get(current)
    return successors


if __name__ == '__main__':
    dataset = '614752839'
    [successors_part_1, current_part_1] = initial_setup(dataset)
    key_count = max(successors_part_1.keys())
    successors_part_1 = execute_moves(successors_part_1, current_part_1, 100)
    answer_1 = ''
    ptr = successors_part_1.get(1)
    for i in range(0, key_count - 1):
        answer_1 += str(ptr)
        ptr = successors_part_1.get(ptr)
    print('Answer part 1 = {:d} '.format(int(answer_1)), int(answer_1) == 89372645)
    [successors_part_2, current_part_2] = initial_setup(dataset)
    key_count = max(successors_part_2.keys())
    for i in range(key_count + 1, 1000000):
        successors_part_2[i] = i + 1
    successors_part_2[1000000] = successors_part_2[key_count]
    successors_part_2[key_count] = key_count + 1
    key_count = max(successors_part_2.keys())
    successors_part_2 = execute_moves(successors_part_2, current_part_2, 10000000)
    answer_2 = successors_part_2.get(1) * successors_part_2.get(successors_part_2.get(1))
    print('Answer part 2 = {:d} '.format(answer_2), answer_2 == 21273394210)
