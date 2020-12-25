def determine_loop_size(initial_subject_number, reference):
    key, loop_size = 1, 0
    while key != reference:
        loop_size += 1
        key = (key * initial_subject_number) % 20201227
    return loop_size


def create_key(initial_subject_number, loop_size):
    key = 1
    for i in range(0, loop_size):
        key = (key * initial_subject_number) % 20201227
    return key


if __name__ == '__main__':
    keys = [335121, 363891]
    encryption_key = create_key(create_key(7, determine_loop_size(7, keys[0])), determine_loop_size(7, keys[1]))
    print('Answer part 1 = {:d} '.format(encryption_key), encryption_key == 9420461)
    print('Answer part 2 = {:d} '.format(50), 50 == 50)
