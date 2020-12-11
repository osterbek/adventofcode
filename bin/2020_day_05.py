from pathlib import Path


def get_id(boardingpass):
    minimum = 0
    maximum = 127
    for i in range(0, 8):
        if boardingpass[i] == 'F':
            maximum -= ((maximum - minimum + 1) // 2)
        else:
            minimum += ((maximum - minimum + 1) // 2)
    row = maximum
    minimum = 0
    maximum = 7
    for i in range(0, 3):
        if boardingpass[7 + i] == 'L':
            maximum -= ((maximum - minimum + 1) // 2)
        else:
            minimum += ((maximum - minimum + 1) // 2)
    column = maximum
    return row * 8 + column


def part1(ds):
    answer = 0
    for i in range(0, len(ds)):
        seat_id = get_id(ds[i])
        if seat_id > answer:
            answer = seat_id
    return answer


def part2(ds):
    seats = []
    for i in range(0, len(ds)):
        seats.append(get_id(ds[i]))
    seats = sorted(seats)
    answer = 0
    for i in range(1, len(ds)-1):
        if seats[i] > seats[i-1] + 1:
            answer = seats[i-1] + 1
    return answer


if __name__ == '__main__':
    dataset = Path('../input/input_2020_05.txt').read_text().split('\n')
    print('Answer part 1 = {:d} '.format(part1(dataset)))
    print('Answer part 2 = {:d} '.format(part2(dataset)))
