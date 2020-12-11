from pathlib import Path


def year2020_day02_part1(ds):
    answer = 0
    for i in range(0, len(ds)):
        minimum = int(ds[i][0].split('-')[0])
        maximum = int(ds[i][0].split('-')[1])
        char = ds[i][1][0]
        password = ds[i][2]
        counter = 0
        for j in range(0, len(password)):
            if password[j] == char:
                counter += 1
        if maximum >= counter >= minimum:
            answer += 1
    return answer


def year2020_day02_part2(ds):
    answer = 0
    for i in range(0, len(ds)):
        first = int(ds[i][0].split('-')[0]) - 1
        second = int(ds[i][0].split('-')[1]) - 1
        char = ds[i][1][0]
        password = ds[i][2]
        if bool(password[first] == char) + bool(password[second] == char) == 1:
            answer += 1
    return answer


if __name__ == '__main__':
    temp = Path('../input/input_2020_02.txt').read_text().split('\n')

    dataset = []
    for i in range(0, len(temp)):
        dataset.append(temp[i].split(' '))

    print('Answer part 1 = {:d} '.format(year2020_day02_part1(dataset)))
    print('Answer part 2 = {:d} '.format(year2020_day02_part2(dataset)))
