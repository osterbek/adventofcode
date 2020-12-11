from pathlib import Path


if __name__ == '__main__':
    ds = [int(i) for i in Path('../input/input_2020_10.txt').read_text().split('\n')]
    ds.append(0)
    ds.sort()
    ds.append(ds[-1] + 3)

    difference = [0 for i in range(0, 4)]
    for adapter in range(1, len(ds)):
        difference[ds[adapter] - ds[adapter - 1]] += 1
    print('Answer part 1 = {:d} '.format(difference[1] * difference[3]))

    answer_2 = 1
    counter = 0
    for adapter in range(1, len(ds) - 1):
        if ((ds[adapter] - ds[adapter - 1]) == 1) and ((ds[adapter + 1] - ds[adapter]) == 1):
            counter += 1
        else:
            answer_2 = answer_2 * [1, 2, 4, 7][counter]
            counter = 0
    print('Answer part 2 = {:d} '.format(answer_2))
