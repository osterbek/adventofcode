def determine_size(key):
    value = 1
    size = 0
    while True:
        size += 1
        value = (value * 7) % 20201227
        if value == key:
            break
    return size


def create_key(initial_subject_number, loop_size):
    value = 1
    for i in range(0, loop_size):
        value = (value * initial_subject_number) % 20201227
    return value


if __name__ == '__main__':
    keys = [335121, 363891]
    loop_size_card = determine_size(keys[0])
    loop_size_door = determine_size(keys[1])
    encryption_key = create_key(create_key(7, loop_size_card), loop_size_door)
    print('Answer part 1 = {:d} '.format(encryption_key), encryption_key == 9420461)
    print('Answer part 2 = {:d} '.format(50), 50 == 50)
