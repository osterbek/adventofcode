from pathlib import Path


if __name__ == '__main__':
    dataset = [i for i in Path('../input/input_2020_13.txt').read_text().split('\n')]

    best = [-1, -1]
    a = []
    counter = 0
    for bus in [i for i in dataset[1].split(',')]:
        if 'x' not in bus:
            depart = (int(dataset[0])//int(bus) + 1) * int(bus) - int(dataset[0])
            if (depart < best[1]) or (best[1] < 0):
                best = [int(bus), depart]
            a.append([int(bus), counter])
        counter += 1
    print('Answer part 1 = {:d} '.format(best[0] * best[1]))

    answer_2 = 0
    increment = 1
    for i in range(0, len(a)):
        while True:
            answer_2 += increment
            if ((answer_2 + a[i][1]) % a[i][0]) == 0:
                break
        increment = increment * a[i][0]
    print('Answer part 2 = {:d} '.format(answer_2))
