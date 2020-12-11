from pathlib import Path


def part1(dataset):
    level = 0
    bag = [[level, 'shiny gold']]
    found = True
    while found:
        level += 1
        found = False
        for i in range(0, len(dataset)):
            for j in range(0, len(bag)):
                if (dataset[i][1].find(bag[j][1]) > 0) and (bag[j][0] == level-1):
                    bag.append([level, dataset[i][0]])
                    found = True
    solution = []
    for i in range(1, len(bag)):
        if bag[i][1] not in solution:
            solution.append(bag[i][1])
    return len(solution)


def part2(dataset):
    bulk = [['shiny gold', 1, True]]
    solution = 0
    anymore = True
    while anymore:
        anymore = False
        for i in range(0, len(bulk)):
            if bulk[i][2]:
                anymore = True
                bulk[i][2] = False
                for j in range(0, len(dataset)):
                    if dataset[j][0] == bulk[i][0]:
                        for k in range(0, len(dataset[j][1])):
                            count = dataset[j][1][k][0] * bulk[i][1]
                            bulk.append([dataset[j][1][k][1], count, True])
                            solution += count
    return solution


if __name__ == '__main__':
    data = Path('../input/input_2020_07.txt').read_text()
    data = data.replace(' bags', '').replace(' bag', '').replace('.', '')
    data = data.split('\n')

    dataset1 = []
    for i in range(0, len(data)):
        dataset1.append(data[i].split(' contain '))
    dataset2 = []

    for i in range(0, len(data)):
        a = dataset1[i][1].split(', ')
        temp = []
        for j in range(0, len(a)):
            if a[j][0] in '123456789':
                temp.append([int(a[j][0]), a[j][2:]])
        dataset2.append([dataset1[i][0], temp])

    print('Answer part 1 = {:d} '.format(part1(dataset1)))
    print('Answer part 2 = {:d} '.format(part2(dataset2)))
