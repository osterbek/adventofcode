from pathlib import Path


if __name__ == '__main__':
    ds = Path('../input/input_2020_01.txt').read_text().split('\n')

    answer1 = 0
    answer2 = 0
    for i in range(0, len(ds)):
        for j in range(0, len(ds)):
            if int(ds[i]) + int(ds[j]) == 2020:
                answer1 = int(ds[i]) * int(ds[j])
            for k in range(0, len(ds)):
                if int(ds[i]) + int(ds[j]) + int(ds[k]) == 2020:
                    answer2 = int(ds[i]) * int(ds[j]) * int(ds[k])

    print('Answer part 1 = {:d} '.format(answer1))
    print('Answer part 2 = {:d} '.format(answer2))

